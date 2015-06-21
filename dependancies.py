graph = {'foo':['bar','main'],'bar':['lib'],'lib':[],'main':[]}

def getPathdfs(graph,start,path=[]):

    path = path+[start]
    for node in graph[start]:
        if node not in path:
            path = getPath(graph,node,path)
        return path



def find_path(graph, start, end, path=[]):
    path = path+[start]

    for node in graph[start]:
        if node not in path:
            findnewpath = find_path(graph,node,end,path)
            if findnewpath:
                return findnewpath

    return None


def bfspath(graph,start,path=[]):
        queue = [start]

        while queue:
            node = queue.pop(0"\n")

            if node not in path:
                path += [node]
                queue += graph[node]
        return path

print bfspath(graph,"foo",path=[])










def getOrder(graph,start,path=[]):
    path = path+[start]
    for node in graph[start]:
        if node not in path:
            path = getOrder(graph,node, path)
    return path

print getOrder(graph,'foo')
