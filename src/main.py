from graph import Graph

def main():
    g = Graph(directed=False)

    g.add([
        'RS',
        'SC',
        'PR',
        'SP',
    ])

    g['SC', 'RS'] = 1
    g['SC', 'PR'] = 1
    g['PR', 'SP'] = 1
    g['RS', 'SC'] = 1

    print(g)

if __name__ == "__main__":
    main()