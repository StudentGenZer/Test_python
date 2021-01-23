string = input()
n_1 = 0
arr = string.split(" ")
a_1 = int(arr[0])
a_2 = int(arr[1])
a_3 = int(arr[2])
b_1 = int(arr[3])
b_2 = int(arr[4])
b_3 = int(arr[5])
arr_cost = [a_1,a_2,a_3]
arr_mass = [b_1,b_2,b_3]
for i in range(0,3):
    a = max(arr_cost)
    b = max(arr_mass)
    n_1 += a*b
    arr_cost.remove(a)
    arr_mass.remove(b)
print(n_1)
