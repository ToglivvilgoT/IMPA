

class Network:
    def __init__(self):
        self.nodes: dict[any, 'Network.Node'] = {}

    class Node:
        def __init__(self):
            self.connections: set['Network.Node'] = set()
            self.checked = False

        def add_connection(self, node: 'Network.Node'):
            self.connections.add(node)

        def get_connections(self):
            return self.connections
        
        def explore_node(self) -> set['Network.Node']:
            if self.checked:
                return set()
            else:
                self.checked = True
                return self.get_connections()

    def _add_node(self, node_id):
        self.nodes[node_id] = Network.Node()

    def _get_node(self, node_id):
        return self.nodes[node_id]

    def _node_exists(self, node_id):
        return True if node_id in self.nodes.keys() else False

    def add_connection(self, from_id, to_id):
        if not self._node_exists(from_id):
            self._add_node(from_id)

        if not self._node_exists(to_id):
            self._add_node(to_id)

        from_node = self._get_node(from_id)
        to_node = self._get_node(to_id)

        from_node.add_connection(to_node)
        to_node.add_connection(from_node)

    def get_unexplored(self):
        unexplored = 0

        for node in self.nodes.values():
            if not node.checked:
                unexplored += 1

        return unexplored

    def explore(self, start_id, ttl: int):
        next_nodes = {self._get_node(start_id)}

        for _ in range(ttl + 1):
            current_nodes = next_nodes
            next_nodes = set()

            for current_node in current_nodes:
                connected_nodes = current_node.explore_node()

                for connected_node in connected_nodes:
                    next_nodes.add(connected_node)

        return self.get_unexplored()
    
    def unexplore(self):
        for node in self.nodes.values():
            node.checked = False


def get_input(connections: int):
    network = Network()
    searches: list[tuple[any, int]] = []

    done = False
    while not done:
        row = list(map(lambda x: int(x), input().split()))

        while row:
            input_pair = row.pop(0), row.pop(0)
            
            if input_pair == (0, 0):
                done = True
                break

            elif connections:
                connections -= 1
                network.add_connection(*input_pair)

            else:
                searches.append(input_pair)

    return network, searches


def solve(network: Network, seaches: list[tuple[any, int]], test_case: int):
    for start_id, ttl in seaches:
        unexplored = network.explore(start_id, ttl)

        print(f'Case {test_case}: {unexplored} nodes not reachable from node {start_id} with TTL = {ttl}.')

        test_case += 1

        network.unexplore()

    return test_case


if __name__ == '__main__':
    test_case = 1

    while True:
        connections = int(input())

        if connections == 0:
            break

        inp = get_input(connections)

        test_case = solve(*inp, test_case)
