from queue import SimpleQueue

class Graph:
    def __init__(self, directed = True):
        self.label_map: list[str] = []
        self.connections: list[list[int]] = []
        self.directed = directed

    def __getitem__(self, p: tuple[str, str]):
        ai = self.label_map.index(p[0])
        bi = self.label_map.index(p[1])
        return self.connections[ai][bi]

    def __setitem__(self, p: tuple[str, str], val: int):
        ai = self.label_map.index(p[0])
        bi = self.label_map.index(p[1])
        self.connections[ai][bi] = val
        if not self.directed:
            self.connections[bi][ai] = val

    def __repr__(self) -> str:
        header = ''
        s = ''

        col_widths = []
        for l in self.label_map:
            col_widths.append(len(l))

        widest = max(col_widths)
        s += ' ' * (widest + 1)
        for i, label in enumerate(self.label_map):
            s += label + ' ' * (widest - len(label) + 1)
        s += '\n'

        for i, row in enumerate(self.connections):
            label = self.label_map[i]
            s += label + ' ' * (widest - len(label) + 1)
            for conn in row:
                pad = (widest - len(str(conn)) + 1) * ' '
                s += f'{conn}{pad}'
            s += '\n'
        return s

    def add(self, label: str | list[str]):
        if label in self.label_map or len(label) < 1:
            return

        if type(label) is list:
            for e in label:
                self.add(e)
        else:
            self.label_map.append(str(label))
            new_row = [0 for _ in range(0, len(self.connections))]
            self.connections.append(new_row)

            for i, _ in enumerate(self.connections):
                self.connections[i].append(0)

    def remove(self, label: str):
        if label not in self.label_map:
            return

        idx = self.label_map.index(label)
        self.connections.pop(idx)
        for i, _ in enumerate(self.connections):
            self.connections[i].pop(idx)

    def transitive_closure(self, starting_node: str):
        visited = [False for _ in range(0, len(self.connections))]
        levels = [-1 for _ in range(0, len(self.connections))]

        queue = SimpleQueue()
        start = self.label_map.index(starting_node)

        queue.put(start)
        levels[start] = 0

        while not queue.empty():
            cur = queue.get()

            if visited[cur]: continue

            visited[cur] = True
            for adj in range(0, len(self.connections)):
                if self.connections[cur][adj] > 0 and not visited[adj]:
                    queue.put(adj)
                    levels[adj] = levels[cur] + 1

        res = []
        for i in range(0, len(self.connections)):
            res.append((self.label_map[i], levels[i]))

        return res
