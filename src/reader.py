def read(file: str):
    with open('test.txt') as f:
        content = f.read().splitlines()
    
    structure = []
    for vertice in content:
        firstLetter = vertice[0]
        secondLetter = vertice[1]
        
        structure.append(firstLetter)
        structure.append(secondLetter)
    
    set_structure = set(structure)

    graph = []
    for set_vertice in set_structure:
        for vertice in content:
            if set_vertice == vertice:
                firstLetter = vertice[0]
                secondLetter = vertice[1]

                graph.append(firstLetter)
                graph.append(secondLetter)
                
        

    
    print(graph)
