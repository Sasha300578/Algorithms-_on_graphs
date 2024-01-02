from __future__ import annotations
from typing import Iterator


class Graph:
    matrix: list[list[int]] # Матрица смежности
    vertexes: list[str] # Список вершин
    marks: list[str] # Список меток для вершин: индекс вершины совпадает с индексом метки для вершины


    def __init__(self):
        self.matrix= []
        self.vertexes= []
        self.marks = [None]*len(self.vertexes)


    def get_vertex_index(self, v: str) -> int:
        for index, vertex in enumerate(self.vertexes):
            if vertex == v:
                return index

        raise Exception(f'Вершина {v} не найдена')


    def first(self, v: str) -> str:
        neighbors = [neighbor for neighbor in self.next(v)]
        if not len(neighbors):
            raise Exception('Граф пустой')

        return neighbors[0]


    def next(self, v: str) -> Iterator[str]:
        idx_v = self.get_vertex_index(v)

        for idx, way in enumerate(self.matrix[idx_v]):
            if way:
                yield self.vertexes[idx]


    def vertex_f(self, v: str, i: int) -> str:
        neighbors = [neighbor for neighbor in self.next(v)]

        if 0 <= i < len(neighbors):
            return neighbors[i]
        else:
            raise Exception('Вершина не найдена')


    def add_v(self, v: str):
        if v in self.vertexes:
            raise Exception(f'Vertex {v} already exists')

        for row in self.matrix:
            row.append(0)

        new_size = len(self.matrix) + 1
        self.matrix.append([0]*new_size)

        self.vertexes.append(v)
        self.marks.append(None)


    def add_e(self, src: str, dst: str):
        idx_src = self.get_vertex_index(src)
        idx_dst = self.get_vertex_index(dst)

        self.matrix[idx_src][idx_dst] = 1


    def del_v(self, v: str):
        if v not in self.vertexes:
            raise Exception(f'Vertex {v} not found')

        idx_v = self.get_vertex_index(v)
        del self.vertexes[idx_v]
        del self.matrix[idx_v]
        del self.marks[idx_v]

        for row in self.matrix:
            del row[idx_v]



    def del_e(self, v: str, w: str):
        idx_v = self.get_vertex_index(v)
        idx_w = self.get_vertex_index(w)

        if 0 <= idx_v < len(self.matrix) and 0 <= idx_w < len(self.matrix):
            self.matrix[idx_v][idx_w] = 0


    def edit_v(self, v: str, label: str):
        idx_v = self.get_vertex_index(v)
        self.marks[idx_v] = label


    def edit_e(self, v: str, w: str, weight: int):
        idx_v = self.get_vertex_index(v)
        idx_w = self.get_vertex_index(w)

        if 0 <= idx_v < len(self.matrix) and 0 <= idx_w < len(self.matrix):
            self.matrix[idx_v][idx_w] = weight


    def output_graph(self):
        print('Граф:')
        for i, vertex in enumerate(self.vertexes):
            print(f"{vertex} -> {', '.join(self.vertexes[j] for j in range(len(self.matrix[i])) if self.matrix[i][j])}")
        print(' ')


    def print_matrix(self):
        print('Матрица смежности:')
        print(" ", end="\t")
        for vertex in self.vertexes:
            print(vertex, end="\t")
        print()
        for i in range(len(self.matrix)):
            print(self.vertexes[i], end="\t")
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end="\t")
            print()


    def print_marks(self):
        print('Метки вершин:')
        for vertex in self.vertexes:
            print(vertex, '-',  self.marks[self.get_vertex_index(vertex)])


    def print_graph(self):
        self.output_graph()
        self.print_matrix()


    def dfs(self, start_vertex: str, kol_edges: int, visited, stack, path):
        if stack is None:
            # Стэк из начального узла и итератора на его соседях - дуга
            stack = [(start_vertex, self.next(start_vertex))]

        this_vertex, neighbors = stack[-1]
        # Список соседей, дуги к которым ещё не посещены
        unvisited_neighbors = [neighbor for neighbor in neighbors if (this_vertex, neighbor) not in visited]

        for neighbor in unvisited_neighbors:
            visited.add((this_vertex, neighbor))
            path.append((this_vertex, neighbor))
            new_stack = [(neighbor, iter(self.next(neighbor)))]

            result = self.dfs(neighbor, kol_edges, visited, new_stack, path)
            if result:
                return result
            else:
                visited.remove((this_vertex, neighbor))
                path.pop()

        # Когда все дуги из текущего узла посещены, то убираем последний элемент
        stack.pop()

        # Если длина пути из дуг == количеству дуг, то возвращаем путь
        if len(path) == kol_edges:
            return path

        return []




