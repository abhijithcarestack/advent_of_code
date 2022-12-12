from abc import ABC, abstractmethod
file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()


class Graph:
    def __init__(self, gdict=None) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        try:
            self.gdict[vertex].append(edge)
        except:
            self.gdict[vertex] = [edge]

    def BFS_SP(self, start, goal):
        explored = []
        queue = [[start]]
        if start == goal:
            print("Same Node")
            return

        while queue:
            path = queue.pop(0)
            node = path[-1]

            # current node is not visited
            if node not in explored:
                neighbours = self.gdict[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        print("Shortest path = ", len(new_path)-1)
                        return
                explored.append(node)

        # Condition when the nodes
        # are not connected
        print("So sorry, but a connecting"
              "path doesn't exist :(")
        return


graph = Graph()

for i in range(len(inputvalues)):
    for j in range(len(inputvalues[i])):

        try:
            left = inputvalues[i+1][j]
            right = inputvalues[i][j]
            if inputvalues[i+1][j] == 'S':
                left = 'a'
            if inputvalues[i+1][j] == 'E':
                left = 'z'
            if inputvalues[i][j] == 'S':
                right = 'a'
            if inputvalues[i][j] == 'E':
                right = 'z'

            if ord(left)-ord(right) < 2:
                graph.addEdge(inputvalues[i][j]+str(i) + ',' +
                              str(j), inputvalues[i+1][j]+str(i+1)+','+str(j))
        except:
            pass
        try:
            left = inputvalues[i-1][j]
            right = inputvalues[i][j]
            if inputvalues[i-1][j] == 'S':
                left = 'a'
            if inputvalues[i-1][j] == 'E':
                left = 'z'
            if inputvalues[i][j] == 'S':
                right = 'a'
            if inputvalues[i][j] == 'E':
                right = 'z'
            if ord(left)-ord(right) < 2 and i != 0:
                graph.addEdge(inputvalues[i][j]+str(i) + ',' +
                              str(j), inputvalues[i-1][j]+str(i-1)+','+str(j))
        except:
            pass
        try:
            left = inputvalues[i][j+1]
            right = inputvalues[i][j]
            if inputvalues[i][j+1] == 'S':
                left = 'a'
            if inputvalues[i][j+1] == 'E':
                left = 'z'
            if inputvalues[i][j] == 'S':
                right = 'a'
            if inputvalues[i][j] == 'E':
                right = 'z'
            if ord(left)-ord(right) < 2:
                graph.addEdge(inputvalues[i][j]+str(i) + ',' +
                              str(j), inputvalues[i][j+1]+str(i)+','+str(j+1))
        except:
            pass
        try:
            left = inputvalues[i][j-1]
            right = inputvalues[i][j]
            if inputvalues[i][j-1] == 'S':
                left = 'a'
            if inputvalues[i][j-1] == 'E':
                left = 'z'
            if inputvalues[i][j] == 'S':
                right = 'a'
            if inputvalues[i][j] == 'E':
                right = 'z'
            if ord(left)-ord(right) < 2 and j != 0:
                graph.addEdge(inputvalues[i][j]+str(i) + ',' +
                              str(j), inputvalues[i][j-1]+str(i)+','+str(j-1))
        except:
            pass

shortest = []

for i in range(len(inputvalues)):
    for j in range(len(inputvalues[i])):
        if inputvalues[i][j] == 'S':
            short = graph.BFS_SP('S20,0', 'E20,119')
            shortest.append(short)
        elif inputvalues[i][j] == 'a':
            short = graph.BFS_SP('a'+str(i)+','+str(j), 'E20,119')
            shortest.append(short)

print(min(shortest))

# print(graph.BFS_SP('S20,0', 'E20,119'))
