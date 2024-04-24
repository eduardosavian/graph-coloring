def read(file: str):
    with open('test.txt') as f:
        content = f.read().splitlines()
    
    graph =[[]]
    for vertice in content:
        firstLetter = vertice[0]
        secondLetter = vertice[1]
        print(firstLetter)
        print(secondLetter)
    print(content)
