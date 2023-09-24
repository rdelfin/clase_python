num_valores = int(input("Cuantos valores quieres poner?"))
nums = []

for i in range(num_valores):
    new_num = int(input("Dame un número (o sufre las consequencias)"))
    nums.append(new_num)

result_sum = 0
for val in nums:
    result_sum += val

promedio = result_sum / num_valores