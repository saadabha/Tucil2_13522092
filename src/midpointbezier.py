import matplotlib.pyplot as plt

def createpoint():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    return (x, y)

def createallinitialpoint():
    pointlist = []

    for i in range(0,3):
        print("input point P"+str(i))
        pointlist.append(createpoint())

    return pointlist

def titiktengah(point0, point1):
    x = (point0[0] + point1[0]) / 2
    y = (point0[1] + point1[1]) / 2

    return (x, y)

def computebezier(point0, point1, point2, bezierlist, currentIteration, iteration):
    if currentIteration <= iteration:
        titiktengah1 = titiktengah(point0, point1)
        titiktengah2 = titiktengah(point1, point2)
        titiktengah3 = titiktengah(titiktengah1, titiktengah2) 
        currentIteration += 1
        computebezier(point0, titiktengah1, titiktengah3, bezierlist, currentIteration, iteration)
        bezierlist.append(titiktengah3)
        computebezier(titiktengah3, titiktengah2, point2, bezierlist, currentIteration, iteration)

def createbezier(pointlist, iteration):
    bezier = []
    bezier.append(pointlist[0])
    computebezier(pointlist[0], pointlist[1], pointlist[2], bezier, 1, iteration)
    bezier.append(pointlist[len(pointlist)-1])

    return bezier

def plotter(pointlist, iterate):
    coorx = [point[0] for point in pointlist]
    coory = [point[1] for point in pointlist]
    title = "Iteration "+str(iterate)
    plt.plot(coorx, coory, marker='o', linestyle='-', label=title, markersize=3)

def drawalliteration(pointlist, iteration):
    for i in range(1, iteration):
        beziercurve = createbezier(pointlist, i)
        plotter(beziercurve, i)