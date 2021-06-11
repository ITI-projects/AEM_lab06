from greedy_algorithm import *
import time
from random import randint
from greedy_cycle_algorithm import *


def generate_random_path(length, dataset_size):
    points = np.arange(dataset_size)
    np.random.shuffle(points)
    return points[:length], points[length:]


def calculate_distance(matrix, visited_vertexes):
    sum_of_distance = 0
    for i in range(len(visited_vertexes) - 1):
        sum_of_distance += matrix[visited_vertexes[i]][visited_vertexes[i + 1]]
    sum_of_distance += matrix[visited_vertexes[-1]][visited_vertexes[0]]
    return sum_of_distance


def generate_population(matrix, path_length):
    population = []
    distances = []
    for i in range(0, 10):
        print(i)
        path_in, out = generate_random_path(path_length, len(matrix[0]))
        path_out = GreedyEdgesAlgorithm(path_in, out, matrix)
        if calculate_distance(matrix, path_out) not in distances:
            population.append(path_out)
            distances.append(calculate_distance(matrix, path_out))
        else:
            i -= 1
    return population, distances


def recombination(path, another_path, n):
    children_path = list(set(path).intersection(another_path))

    if len(children_path) < n:
        ver_diff = np.setxor1d(path, another_path)
        np.random.shuffle(ver_diff)
        ver_diff = ver_diff.tolist()
        diff_num = n - len(children_path)
        children_path = children_path + ver_diff[:diff_num]

    return np.array(children_path)


def recombination_v2(path_1, path_2, matrix):
    beg_1 = randint(0, len(path_1) - 1)
    beg_2 = randint(0, len(path_1) - 1)

    new_list = [path_1[(beg_1 + i) % len(path_1)] for i in range(len(path_1) // 2)]

    for i in range(0, len(path_1)):
        if len(new_list) >= len(path_1):
            break
        index = (beg_2 + i) % len(path_1)
        if path_2[index] not in new_list:
            new_list.append(path_2[index])

    # ---------------------------------------
    counter = 20
    while counter > 0:
        if randint(0, 1) == 0:
            rand_elem = randint(0, len(new_list) - 1)
            new_list = np.delete(new_list, rand_elem)
            counter -= 1
        else:
            rand_elem = randint(0, len(new_list) - 1)
            new_list = np.delete(new_list, [rand_elem, (rand_elem + 1) % len(new_list)])
            counter -= 2

    greed = GreedyCycleAlgorithm(distance_matrix=matrix)
    new_list = greed.run(new_list, len(path_1) - len(new_list))

    # ---------------------------------------

    return new_list


def evolutionary(matrix, path_length):
    population, distances = generate_population(matrix, path_length)
    timeout = time.time() + 700
    print(distances)
    while time.time() < timeout:
        print("iterating")
        print(distances)
        picked_keys = np.random.choice(np.arange(len(population)), 2, replace=False)
        pop1 = population[picked_keys[0]]
        pop2 = population[picked_keys[1]]
        recombined_path = recombination_v2(pop1, pop2, matrix)
        outside_y = [e for e in range(0, len(matrix[0])) if e not in recombined_path]
        path_out = GreedyEdgesAlgorithm(recombined_path, outside_y, matrix)
        new_distance = calculate_distance(matrix, path_out)
        print(new_distance)
        if new_distance not in distances and new_distance<max(distances):
            index = distances.index(max(distances))
            distances.pop(index)
            population.pop(index)
            distances.append(new_distance)
            population.append(path_out)
            print("changing")

    best = np.asarray(distances).argmin(axis=0)
    return population[best]
