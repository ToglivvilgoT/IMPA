#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

struct Node {
    int id;
    vector<Node*> neighbours = {};
    int color = 0;
    Node(int index) {
        id = index;
    }
    Node(){};
};

bool isBicolorable(Node* node) {
    queue<Node*> que;
    set<int> visited;
    node->color = 1;
    que.push(node);
    visited.insert(node->id);

    while (!que.empty()) {
        Node* curr = que.back();
        int currColor = curr->color;
        que.pop();
        for (Node* neighbour : curr->neighbours) {
            if (neighbour->color == currColor) {
                return false;
            }
            if (!visited.count(neighbour->id)) {
                neighbour->color = ~currColor;
                visited.insert(neighbour->id);
                que.push(neighbour);
            }
        }
    }

    return true;
}

int main() {
    int nodesAmount, edges;
    while (cin >> nodesAmount >> edges) {
        const int nodess = nodesAmount;
        Node* nodes = new Node[nodess];
        for (int i = 0; i < nodesAmount; i++) {
            *(nodes + i) = Node(i);
        }
        for (; edges > 0; edges--) {
            int from, to;
            cin >> from >> to;
            nodes[from].neighbours.push_back(&nodes[to]);
            nodes[to].neighbours.push_back(&nodes[from]);
        }
        if (isBicolorable(nodes)) {
            cout << "BICOLORABLE." << endl;
        }
        else {
            cout << "NOT BICOLORABLE." << endl;
        }
        Node* end = nodes + nodesAmount;
        delete[] nodes;
    }
    return 0;
}