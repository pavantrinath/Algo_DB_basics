graph = {'foo':['bar','main'],'bar':['lib'],'lib':[],'main':[]}

def getOrder(graph,start,path=[]):
    path = path+[start]
    for node in graph[start]:
        if node not in path:
            path = getOrder(graph,node, path)
    return path

print getOrder(graph,'foo')
