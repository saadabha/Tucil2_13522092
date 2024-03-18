from midpointbezier import *
from bruteforcebezier import *

# jumlahpoint = int(input("Masukkan jumlah point: "))
# while jumlahpoint < 3:
#     jumlahpoint = int(input("Masukkan jumlah point(minimal 3): "))

pointlist = createallinitialpoint()

iteration = int(input("Masukkan jumlah iterasi: "))

plt.subplot(1, 2, 1)

initcoorx = [point[0] for point in pointlist]
initcoory = [point[1] for point in pointlist]

plt.plot(initcoorx, initcoory, marker='o', linestyle='-', label='Initial Point', markersize=8)

drawalliteration(pointlist, iteration)
midpointbeziercurve = createbezier(pointlist, iteration)

finalcoorx = [point[0] for point in midpointbeziercurve]
finalcoory = [point[1] for point in midpointbeziercurve]

plt.plot(finalcoorx, finalcoory, marker='o', linestyle='-', label='Final Bezier Curve')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Midpoint Algorithm')
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)

plt.plot(initcoorx, initcoory, marker='o', linestyle='-', label='Initial Point', markersize=8)

bruteforcebeziercurve = bruteforcebezier(pointlist, iteration)

coorx = [point[0] for point in bruteforcebeziercurve]
coory = [point[1] for point in bruteforcebeziercurve]

plt.plot(finalcoorx, finalcoory, marker='o', linestyle='-', label='Final Bezier Curve')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bruteforce Algorithm')
plt.legend()
plt.grid()

plt.suptitle('Bezier Curve')

plt.show()