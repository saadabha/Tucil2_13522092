def bruteforcebezier(pointlist, iteration):
    bezier = []

    if iteration == 1:
        x = (0.5**2)*pointlist[0][0]+2*(0.5*0.5)*pointlist[1][0]+(0.5**2)*pointlist[2][0]
        y = (0.5**2)*pointlist[0][1]+2*(0.5*0.5)*pointlist[1][1]+(0.5**2)*pointlist[2][1]
        bezier.append((x, y))

    else:
        temp = 1/iteration

        for i in range(iteration):
            if i == iteration-1:
                x = pointlist[2][0]
                y = pointlist[2][0]
                bezier.append((x, y))

            else:
                t = i*temp
                x = ((1-t)**2)*pointlist[0][0]+2*(1-t)*t*pointlist[1][0]+(t**2)*pointlist[2][0]
                y = ((1-t)**2)*pointlist[0][1]+2*(1-t)*t*pointlist[1][1]+(t**2)*pointlist[2][1]
                bezier.append((x, y))
    
    return bezier