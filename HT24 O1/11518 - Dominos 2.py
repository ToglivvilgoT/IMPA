

def solve(chains: int, pushes: int):
    domino_chains: dict[int, list[int]] = {}
    dominos_fallen: set[int] = set()    

    for _ in range(chains):
        source, destin = map(lambda x: int(x), input().split())

        if source in domino_chains.keys():
            domino_chains[source].append(destin)
        else:
            domino_chains[source] = [destin]

    def push_domino(domino: int):
        if domino in dominos_fallen:
            return
        
        dominos_fallen.add(domino)

        if domino in domino_chains.keys():
            for next_domino in domino_chains[domino]:
                push_domino(next_domino)
    
    for _ in range(pushes):
        pushed_domino = int(input())

        push_domino(pushed_domino)

    print(len(dominos_fallen))




if __name__ == '__main__':
    test_cases = int(input())

    for test_case in range(test_cases):
        _, chains, pushes = map(lambda x: int(x), input().split())

        solve(chains, pushes)