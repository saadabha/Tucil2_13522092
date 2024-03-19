from midpointbezier import *
from bruteforcebezier import *
import time

# jumlahpoint = int(input("Masukkan jumlah point: "))
# while jumlahpoint < 3:
#     jumlahpoint = int(input("Masukkan jumlah point(minimal 3): "))

pointlist = createallinitialpoint()

iteration = int(input("Masukkan jumlah iterasi: "))
while iteration < 1:
    print("Jumlah iterasi minimal 1")
    iteration = int(input("Masukkan jumlah iterasi(minimal 1): "))

plt.subplot(1, 2, 1)

initcoorx = [point[0] for point in pointlist]
initcoory = [point[1] for point in pointlist]

plt.plot(initcoorx, initcoory, marker='o', linestyle='-', label='Initial Point', markersize=8)

drawalliteration(pointlist, iteration)
startmidpoint = time.perf_counter()
midpointbeziercurve = createbezier(pointlist, iteration)
endmidpoint = time.perf_counter()
decimal_places = 4
# exectimemidpoint = f"{endmidpoint-startmidpoint:.{decimal_places}f}"
exectimemidpoint = endmidpoint-startmidpoint

finalcoorx = [point[0] for point in midpointbeziercurve]
finalcoory = [point[1] for point in midpointbeziercurve]

plt.plot(finalcoorx, finalcoory, marker='o', linestyle='-', label='Final Bezier Curve')

titlemidpoint = "Midpoint Algorithm (Execution Time: "+str(exectimemidpoint)+" s)"
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(titlemidpoint)
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)

plt.plot(initcoorx, initcoory, marker='o', linestyle='-', label='Initial Point', markersize=8)

startbruteforce = time.perf_counter()
bruteforcebeziercurve = bruteforcebezier(pointlist, iteration)
endbruteforce = time.perf_counter()
# exectimebruteforce = f"{endbruteforce-startbruteforce:.{decimal_places}f}"
exectimebruteforce = endbruteforce-startbruteforce

coorx = [point[0] for point in bruteforcebeziercurve]
coory = [point[1] for point in bruteforcebeziercurve]

plt.plot(coorx, coory, marker='o', linestyle='-', label='Final Bezier Curve')

titlebruteforce = "Bruteforce Algorithm (Execution Time: "+str(exectimebruteforce)+" s)"
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(titlebruteforce)
plt.legend()
plt.grid()

plt.suptitle('Bezier Curve')

print(exectimemidpoint)
print(exectimebruteforce)
plt.show()