string = input()
arr = string.split(" ")
x = int(arr[0])
x_1 = int(arr[1])
x_2 = int(arr[2])
x_3 = int(arr[3])
n = int(arr[4])
mass_2 = n*2*x
if mass_2 > x_2/2:
    k_2 = int((x_2/2)/x)
else:
    k_2 = int(mass_2/x)
mass_3 = mass_2*2
if mass_3 > x_3/2:
    k_3 = int((x_3/2)/x)
else:
    k_3 = int(mass_3/x)
k = n+k_2+k_3
print(k)
