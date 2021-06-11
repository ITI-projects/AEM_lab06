from datetime import datetime
from preparedata import *
from draw import *
from evolutionary import *


def calculate_distance(matrix, visited_vertexes):
    sum_of_distance = 0
    for i in range(len(visited_vertexes) - 1):
        sum_of_distance += matrix[visited_vertexes[i]][visited_vertexes[i + 1]]
    sum_of_distance += matrix[visited_vertexes[-1]][visited_vertexes[0]]
    return sum_of_distance


def test(matrix, alg, number_of_tests, path_length):
    all_paths = []
    all_distances = []
    all_times = []
    for i in range(number_of_tests):
        start = datetime.now()
        path_in = alg(matrix, path_length)
        stop = datetime.now()
        current_len = calculate_distance(matrix, path_in)
        all_distances.append(current_len)
        all_paths.append(path_in)
        all_times.append(stop - start)

    print("Distances")
    best, worst, mean = results(np.asarray(all_distances))
    print(all_distances[best])
    print(all_distances[worst])
    print(mean)
    print("Times")
    best_time, worst_time, mean_time = results(np.asarray(all_times))
    print(all_times[best_time])
    print(all_times[worst_time])
    print(mean_time)

    return all_paths[best]


def results(all_distance):
    best = all_distance.argmin(axis=0)
    mean = all_distance.mean(axis=0)
    worst = all_distance.argmax(axis=0)
    return best, worst, mean


def main(path):
    loaded_data = PrepareData(path)
    coordinates = loaded_data.get_coords()
    drawing = DrawPlot(coordinates)
    matrix = loaded_data.calculate_distance_matrix()
    number_of_tests = 10
    path_length = 100

    print("New - Evolutionary steady state")
    min_path = test(matrix, evolutionary, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/evolutionary_" + path + ".png", 'New Evolutionary_' + path)


if __name__ == '__main__':
    print("kroA200")
    main(pathA)
    print("kroB200")
    main(pathB)
