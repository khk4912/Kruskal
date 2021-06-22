from __future__ import annotations

from typing import List
from dataclasses import dataclass
from pprint import pprint


# 간선 모델
@dataclass
class Node:
    weight: int  # 가중치
    v: str  # 시작점
    u: str  # 끝점


# 그래프 모델
class Kruskal:
    def __init__(self, vertices: List[str], nodes: List[Node]) -> None:
        self.vertices = vertices
        self.nodes = sorted(nodes, key=lambda x: x.weight)
        # 간선은 cost값을 기준으로 작은 것부터 정렬한다.

        self._parent = {}
        self._rank = {}

        self.result: List[Node] = []

        for i in self.vertices:
            self._parent[i] = i
            self._rank[i] = 0
        # 경로 압축 전 간선 자기 자신을 간선의 대표로 설정한다.

    def _union(self, v: str, u: str):  # union-by-rank 기법
        v1 = self._comp(v)
        u1 = self._comp(u)

        if self._rank[v1] > self._rank[u1]:
            self._parent[u1] = v1  # 더 높은 트리 밑에 낮은 트리를 둔다.
        else:
            self._parent[v1] = u1
            if self._rank[v1] == self._rank[u1]:
                self._rank[u1] += 1  # 만약 두 트리의 높이가 같으면 상위 트리에 높이를 1+

    def _comp(self, vertex: str):  # 경로 압축, 맨 위의 정점을 찾는다.
        if self._parent[vertex] != vertex:
            self._parent[vertex] = self._comp(
                self._parent[vertex]
            )  # 맨 위가 아니라면 재귀호출
        return self._parent[vertex]

    def do(self):  # 실행 메소드
        for node in self.nodes:
            if self._comp(node.v) != self._comp(node.u):  # 순환 구조가 아니면
                self._union(node.v, node.u)
                self.result.append(node)

        return (self.result, sum([x.weight for x in self.result]))


graph = Kruskal(
    vertices=["A", "B", "C", "D", "E", "F"],
    nodes=[
        Node(16, "A", "B"),
        Node(9, "A", "C"),
        Node(7, "A", "D"),
        Node(50, "A", "E"),
        Node(12, "B", "D"),
        Node(25, "B", "E"),
        Node(15, "B", "F"),
        Node(12, "C", "D"),
        Node(40, "C", "E"),
        Node(32, "C", "F"),
        Node(25, "D", "F"),
        Node(9, "E", "F"),
    ],
)
pprint(graph.do())