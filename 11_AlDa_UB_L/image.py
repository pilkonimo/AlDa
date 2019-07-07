from pgm import readPGM, writePGM

#### TASK A

def createMask(width, height, data, threshold):
    #mask array holds the values of pixels
    mask = [-1] * width*height
    i = 0

    #decision whether pixel is smaller or larger than threshold
    for pixel in data:
        if pixel < threshold:
            mask[i] = 0
        else:
            mask[i] = 255
        i += 1

    return mask


#### TASK B

def createGraph(width, height, mask):
    '''creates a graph in adjacency matrix format'''
    graph = [[] for i in range(width*height)]


    for i in range(len(mask)):
        edgecount = 0

        #check left pixel
        if i % width > 0 and mask[i-1] is mask[i]:
            graph[i].append(i-1)
            edgecount += 1

        #check right pixel
        if i % width < (width - 1) and mask[i+1] is mask[i]:
            graph[i].append(i+1)
            edgecount += 1

        #check pixel in row above
        if i // width > 0 and mask[i-width] is mask[i]:
            graph[i].append(i-width)
            edgecount += 1

        #check pixel in row below
        if i // width < (height - 1):
            if mask[i+width] is mask[i]:
                graph[i].append(i+width)
                edgecount += 1

        # if i < 350 and i > 320:
        #     print(graph[i])
        #     print('added ', edgecount, ' edges for pixel', i, 'mask: ', mask[i])

    return graph


#### TASK C


def findAnchor(anchors, node):
    '''returns parent anchor (with a self-referencing anchor)'''
    start = node
    while node != anchors[node]:
        node = anchors[node]
    anchors[start] = node
    return node


def unionFindConnectedComponents(graph):
    '''Code for Union find algorithm from lecture'''
    anchors = list(range(len(graph)))

    # create anchor array
    for node in range(len(graph)):
        for neighbor in graph[node]:
            if neighbor < node:
                continue
            a1 = findAnchor(anchors, node)
            a2 = findAnchor(anchors, neighbor)
            if a1 < a2:
                anchors[a2] = a1
            elif a2 < a1:
                anchors[a1] = a2

    #labeling array
    labels = [None] * len(graph)
    current_label = 0
    for node in range(len(graph)):
        a = findAnchor(anchors, node)
        if a == node:
            labels[a] = current_label
            current_label += 1
        else:
            labels[node] = labels[a]

    return anchors, labels

def connectedComponents(graph):
    '''depth-first search version of finding connected Components'''
    anchors = [None] * len(graph)
    labels = [None] * len(graph)

    #recursive search of anchors
    def visit(node, anchor):
        if anchors[node] is None:
            anchors[node] = anchor
            labels[node] = labels[anchor]
            for neighbor in graph[node]:
                visit(neighbor, anchor)

    #labeling array
    current_label = 0
    for node in range(len(graph)):
        if anchors[node] == None:
            labels[node] = current_label
            visit(node, node)
            current_label += 1

    return anchors, labels


def assignLabel0toBackground(mask, anchors, labels):
    '''Not necessary for the given data, but could be a handy method for other pictures'''
    ...
    return anchors, labels


#### TASK D

def getSize(labeling):
    #create  labeling array (+1 because 0 and max value included)
    size = [None] * (max(labeling)+1)
    for label in range(len(size)):
        #count numbers of pixels with label
        size[label] = labeling.count(label)
    return size

def getMaxIntensity(data, labeling):
    # create  intensity array (+1 because 0 and max value included)
    intensity = [-1] * (max(labeling)+1)

    for pixel in range(len(data)):
        label = labeling[pixel]
        if intensity[label] < data[pixel]:
            intensity[label] = data[pixel]

    return intensity

def createOutput(labeling, size, intensity):
    width, height, data = readPGM('cells.pgm')
    output = [-1] * width * height

    for pixel in range(len(data)):
        label = labeling[pixel]
        print(label)
        #only one of the characteristics applies to every single pixel -> elif
        if label is 0:
            output[pixel] = 0
        elif size[label] < 30:
            output[pixel] = 255
        elif intensity[label] > 220:
            output[pixel] = 160
        else:
            output[pixel] = 80

    writePGM(width, height, output, 'output.pgm')

    return output




#######################################################

def task_a():
    width, height, data = readPGM('cells.pgm')
    mask = createMask(width, height, data, 60)
    writePGM(width, height, mask, 'mask.pgm')

    return data

def task_b():
    width, height, mask = readPGM('mask.pgm')
    graph = createGraph(width, height, mask)
    return width, height, graph

def task_c():
    width, height, graph = task_b()
    anchors, labeling = unionFindConnectedComponents(graph)
    #anchors, labeling = connectedComponents(graph)


    writePGM(width, height, labeling, 'labeling.pgm')
    print('labels count: ', max(labeling))

    return labeling

def task_d():
    width, height, data = readPGM('cells.pgm')
    labeling = task_c()

    size = getSize(labeling)
    intensity = getMaxIntensity(data, labeling)

    # for i in range(len(size)):
    #     print(i, size[i], intensity[i])

    percent_bg = size[0] / (width * height) * 100

    regions_u30px = 0
    for region in size:
        if region < 30:
            regions_u30px += 1

    regions_nuclei = 0
    for region in intensity:
        if region > 220:
            regions_nuclei += 1

    print('Background: {:.2f} %'.format(percent_bg))
    print('Regions under 30 px count:', regions_u30px)
    print('Regions over 220 Intensity: ', regions_nuclei)

    output = createOutput(labeling, size, intensity)




if __name__ == '__main__':
    #task_a()
    #task_b()
    #task_c()
    task_d()