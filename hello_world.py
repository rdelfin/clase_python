print("Dame una temperatura en Celcius:")
temperatura = float(input())
temperatura_farenheit = (temperatura * 1.8) + 32
if temperatura >= 35:
    print("hace mucho calor")
elif temperatura > 4:
    print("estas vivo")
else:
    print("necesitas ayuda?")

for index in range(10):
    print(f"Index: {index}")
    for index_2 in range(10):
        print(f"Index 2: {index_2}")


# Mario Pyramid
# 
# Dame una altura: 3
# *
# **
# ***


   *
  **
 ***
****

#   *
#  ***
# *****