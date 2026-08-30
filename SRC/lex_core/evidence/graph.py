from dataclasses import dataclass

@dataclass(frozen=True)
class Edge:
    source: str
    relation: str
    target: str

class EvidenceGraph:
    def __init__(self):
        self.edges: list[Edge] = []

    def link(self, source: str, relation: str, target: str) -> None:
        self.edges.append(Edge(source, relation, target))

    def outgoing(self, source: str) -> list[Edge]:
        return [e for e in self.edges if e.source == source]

    def trace_from(self, source: str, max_depth: int = 8) -> list[Edge]:
        result: list[Edge] = []
        frontier = [(source, 0)]
        seen = set()
        while frontier:
            node, depth = frontier.pop(0)
            if depth >= max_depth:
                continue
            for edge in self.outgoing(node):
                key = (edge.source, edge.relation, edge.target)
                if key in seen:
                    continue
                seen.add(key)
                result.append(edge)
                frontier.append((edge.target, depth + 1))
        return result
      
