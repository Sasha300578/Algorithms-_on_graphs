from graph import Graph


VERTEXES_NAMES = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
GRAPH_EDGES: list[dict[str, str]] = [
    # Вариант 1 (Нет пути)
    {"src": "A", "dst": "B"},  # A -> B
    {"src": "B", "dst": "C"},  # B -> C
    {"src": "C", "dst": "H"},  # C -> H
    {"src": "H", "dst": "D"},  # H -> D
    {"src": "D", "dst": "C"},  # D -> C
    {"src": "D", "dst": "E"},  # D -> E
    {"src": "E", "dst": "F"},  # E -> F
    {"src": "F", "dst": "G"},  # F -> G
    {"src": "G", "dst": "A"},  # G -> A
    # Вариант 2 (Есть путь проходящий через все дуги)
    # {"src": "A", "dst": "B"},  # A -> B
    # {"src": "B", "dst": "C"},  # B -> C
    # {"src": "B", "dst": "G"},  # B -> G
    # {"src": "C", "dst": "D"},  # C -> D
    # {"src": "D", "dst": "E"},  # D -> E
    # {"src": "E", "dst": "F"},  # E -> F
    # {"src": "F", "dst": "G"},  # F -> G
    # {"src": "G", "dst": "H"},  # G -> H
    # {"src": "G", "dst": "F"},  # G -> F
    # {"src": "H", "dst": "A"},  # H -> A
    # {"src": "H", "dst": "B"},  # H -> B
]

# Инициализация графа
def _init_graph() -> Graph:
    result = Graph()

    for vertex in VERTEXES_NAMES:
        result.add_v(vertex)

    for params in GRAPH_EDGES:
        result.add_e(**params)

    return result

# Поиск пути через все дуги
def find_path(graph: Graph) -> list[str]:
    kol_edges = len(GRAPH_EDGES)
    visited = set()
    stack = None
    path = list()
    for vertex in VERTEXES_NAMES:
        path = graph.dfs(start_vertex=vertex, kol_edges=kol_edges, visited=visited, stack=stack, path=path)
        if path:
            return path
    return []


if __name__ == '__main__':
    graph = _init_graph()

    graph.print_graph()

    print(' ')
    print(f'Количество связей = {len(GRAPH_EDGES)}')
    print(' ')

    path = find_path(graph)

    if path:
        # print(f'path[0][0] {path[0][0]}')
        # print(f'path[-1][1] {path[-1][1]}')
        # print(f'graph.next(path[0][0]) {next(graph.next(path[0][0]))}')
        if ((path[-1][1] == (next(graph.next(path[0][0])))) or (path[0][0] == (next(graph.next(path[-1][1]))))):
            print('Путь, проходящий через все дуги, найден, но начальная и конечная вершины смежны!')
        else:
            print('Путь через все дуги: ')
            print('    Начало дуги, конец дуги')
            for edge in path:
                print(f'           {edge}')
    else:
        print('Путь, проходящий через все дуги, не найден')

    # # Проверка методов
    # print(f'vertex(H, 1): {graph.vertex_f('H', 1)}')
    # print(f'first(H): {graph.first('H')}')
    # # Удаление вершины
    # graph.del_v('A')
    # # Удаление дуги
    # graph.del_e('C', 'D')
    # # Изменение метки узла
    # graph.edit_v('G', 'G1')
    # graph.print_marks()
    # # Изменение веса дуги
    # graph.edit_e('E', 'F', 2)
    # graph.print_graph()









