import json
from scipy import stats
import matplotlib.pyplot as plot

def vertex_similarity(path_1, path_2):
    x = len((set(path_1) & set(path_2)))
    y = (len(path_1) - 1)
    return x / y


def edges_similarity(path_1, path_2):
    similarity = 0
    edges_path_1 = [(path_1[e], path_1[e + 1]) for e in range(len(path_1) - 1)]
    edges_path_2 = [(path_2[e], path_2[e + 1]) for e in range(len(path_1) - 1)]

    for e in edges_path_1:
        if e in edges_path_2 or e[::-1] in edges_path_2:
            similarity += 1

    return similarity / (len(path_1) - 1)


def main():
    with open('kroA100.tspstats.json', 'r') as json_file:
        js = json.load(json_file)

        # -------------------------------------- VERTICES TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(vertex_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA100 - Vertices similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA100 - Vertices similarity to best.png')
        plot.show()

        # -------------------------------------- EDGE TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(edges_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA100 - Edges similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA100 - Edges similarity to best.png')
        plot.show()

        # -------------------------------------- VERTICES TO MEDIUM
        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += vertex_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med/(len(js["distances"])-1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA100 - Vertices similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA100 - Vertices similarity to mean.png')
        plot.show()

        # -------------------------------------- EDGE TO MEDIUM

        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += edges_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med / (len(js["distances"]) - 1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA100 - Edges similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA100 - Edges similarity to mean.png')
        plot.show()

    with open('kroB100.tspstats.json', 'r') as json_file:
        js = json.load(json_file)

        # -------------------------------------- VERTICES TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(vertex_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB100 - Vertices similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB100 - Vertices similarity to best.png')
        plot.show()

        # -------------------------------------- EDGE TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(edges_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB100 - Edges similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB100 - Edges similarity to best.png')
        plot.show()

        # -------------------------------------- VERTICES TO MEDIUM
        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += vertex_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med / (len(js["distances"]) - 1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB100 - Vertices similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB100 - Vertices similarity to mean.png')
        plot.show()

        # -------------------------------------- EDGE TO MEDIUM

        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += edges_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med / (len(js["distances"]) - 1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB100 - Edges similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB100 - Edges similarity to mean.png')
        plot.show()

    with open('kroA200.tspstats.json', 'r') as json_file:
        js = json.load(json_file)

        # -------------------------------------- VERTICES TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(vertex_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA200 - Vertices similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA200 - Vertices similarity to best.png')
        plot.show()

        # -------------------------------------- EDGE TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(edges_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA200 - Edges similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA200 - Edges similarity to best.png')
        plot.show()

        # -------------------------------------- VERTICES TO MEDIUM
        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += vertex_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med/(len(js["distances"])-1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA200 - Vertices similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA200 - Vertices similarity to mean.png')
        plot.show()

        # -------------------------------------- EDGE TO MEDIUM

        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += edges_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med / (len(js["distances"]) - 1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROA200 - Edges similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROA200 - Edges similarity to mean.png')
        plot.show()

    with open('kroB200.tspstats.json', 'r') as json_file:
        js = json.load(json_file)

        # -------------------------------------- VERTICES TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(vertex_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB200 - Vertices similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB200 - Vertices similarity to best.png')
        plot.show()

        # -------------------------------------- EDGE TO BEST
        list_target = []
        list_similarity = []
        best_dist = js["best_distance"]
        best_path = js["best_path"]
        for i in range(0, len(js["distances"])):
            if js["paths"][i] != best_path:
                list_target.append(js["distances"][i])
                list_similarity.append(edges_similarity(js["paths"][i], best_path))
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB200 - Edges similarity to best, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB200 - Edges similarity to best.png')
        plot.show()

        # -------------------------------------- VERTICES TO MEDIUM
        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += vertex_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med / (len(js["distances"]) - 1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB200 - Vertices similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB200 - Vertices similarity to mean.png')
        plot.show()

        # -------------------------------------- EDGE TO MEDIUM

        list_target = []
        list_similarity = []
        for i in range(0, len(js["distances"])):
            med = 0
            for j in range(0, len(js["distances"])):
                if i != j:
                    med += edges_similarity(js["paths"][i], js["paths"][j])
            list_similarity.append(med / (len(js["distances"]) - 1))
            list_target.append(js["distances"][i])
        print(list_similarity)
        print(list_target)

        corel, _ = stats.pearsonr(list_target, list_similarity)
        print(corel)
        plot.title("KROB200 - Edges similarity to mean, corel: " + str(corel))
        plot.scatter(list_target, list_similarity)

        plot.savefig('images/KROB200 - Edges similarity to mean.png')
        plot.show()

if __name__ == '__main__':
    main()
