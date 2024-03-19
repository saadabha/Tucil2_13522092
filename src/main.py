from midpointbezier import *
from bruteforcebezier import *
import time

# jumlahpoint = int(input("Masukkan jumlah point: "))
# while jumlahpoint < 3:
#     jumlahpoint = int(input("Masukkan jumlah point(minimal 3): "))

print("Silahkan pilih cara input:")
print("1. Input manual")
print("2. Input file")
masukkan = int(input("Pilihan: "))

if masukkan == 1:
    pointlist = createallinitialpoint()

    iteration = int(input("Masukkan jumlah iterasi: "))
    while iteration < 1:
        print("Jumlah iterasi minimal 1")
        iteration = int(input("Masukkan jumlah iterasi(minimal 1): "))
elif masukkan == 2:
    filename = input("Masukkan nama file: ")
    filename = "../test/"+filename
    with open(filename, "r") as file:
        pointlist = []
        
        for i in range(3):
            line = file.readline()
            numbers = line.split()
            numbers_tuple = tuple(float(num) for num in numbers)
            pointlist.append(numbers_tuple)
        val = file.readline()
        iteration = int(val)
else:
    print("Input tidak valid")
    exit()

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
exectimemidpoint = (endmidpoint-startmidpoint)*1000

finalcoorx = [point[0] for point in midpointbeziercurve]
finalcoory = [point[1] for point in midpointbeziercurve]

plt.plot(finalcoorx, finalcoory, marker='o', linestyle='-', label='Final Bezier Curve')

titlemidpoint = "Midpoint Algorithm (Execution Time: "+str(exectimemidpoint)+" ms)"
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
exectimebruteforce = (endbruteforce-startbruteforce)*1000

coorx = [point[0] for point in bruteforcebeziercurve]
coory = [point[1] for point in bruteforcebeziercurve]

plt.plot(coorx, coory, marker='o', linestyle='-', label='Final Bezier Curve')

titlebruteforce = "Bruteforce Algorithm (Execution Time: "+str(exectimebruteforce)+" ms)"
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(titlebruteforce)
plt.legend()
plt.grid()

plt.suptitle('Bezier Curve')

plt.show()