from collections import defaultdict


def calculate_longest_path(graph_list):
    edges = {item for sublist in graph_list for item in sublist}

    def calculate_path(dict1, start_point, path=None):
        if not path:
            path = start_point
        main_path = path
        pathes = []
        for item in dict1[start_point]:
            if item not in path:
                path = main_path + '-' + item
                pathes.append(path)
                pathes.extend(calculate_path(dict1, item, path))
        return pathes

    dict1 = defaultdict(list)
    for i, j in graph_list:
        dict1[i].append(j)
        dict1[j].append(i)

    longest_path = []
    for item in edges:
        result = calculate_path(dict(dict1), item)
        max_len = max(len(p) for p in result)
        max_paths = [p for p in result if len(p) == max_len]
        longest_path.extend(max_paths)
    max_len = max(len(p) for p in longest_path)
    longest_path = [p for p in longest_path if len(p) == max_len]
    print(f'Longest path:{longest_path} Length:{len(longest_path[0]) // 2}')
    return (longest_path, len(longest_path[0]) // 2)


if __name__ == '__main__':
    inp = input("Please send a list of tuples for graph \n")
    inp = inp.replace(' ', '').replace('[', '').replace(']', '').replace('(', '').replace("'", "")

    graph_list = [item.replace(')', '').split(',') for item in inp.split('),')]
    if len(graph_list[0]) != 2:
        raise Exception("Please Enter your graph nodes in this format (a,b),(b,e),(e,f),(b,c),(c,d)")

    calculate_longest_path(graph_list)
