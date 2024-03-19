def bruteforcebezier(pointlist, iteration):
    bezier = []
    temp = 1/(2**iteration)

    for i in range((2**iteration)+1):
        if i == 2**iteration:
            x = pointlist[2][0]
            y = pointlist[2][1]
            bezier.append((x, y))

        else:
            t = i*temp
            x = ((1-t)**2)*pointlist[0][0]+2*(1-t)*t*pointlist[1][0]+(t**2)*pointlist[2][0]
            y = ((1-t)**2)*pointlist[0][1]+2*(1-t)*t*pointlist[1][1]+(t**2)*pointlist[2][1]
            bezier.append((x, y))
    
    return bezier