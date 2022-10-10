# ДЗ 1

# задача 1

#num1 = int(input("Введите число "))
#if num1 == 6 or num1 == 7:
#    print("выходной")
#else:
#    print("рабочий")

#задача 2

# num1 = int(input("Введите координату X "))
# num2 = int(input("Введите координату Y "))
# if num1 > 0 and num2 > 0:
#     print("вторая четверть")
# elif num1 > 0 and num2 < 0:
#     print("третья четверть")
# elif num1 < 0 and num2 < 0:
#     print("четвертая четверть")
# elif num1 < 0 and num2 > 0:
#     print("первая четверть")
# else:
#     print("центр координат")

# задача 3
# num1 = int(input("Введите номер четверти "))

# задача 4

numAX = float(input("Введите координату X точки А "))
numAY = float(input("Введите координату Y точки А "))
numBX = float(input("Введите координату X точки B "))
numBY = float(input("Введите координату Y точки B "))
dista = ((numAX - numBX)**2 + (numAY - numBY)**2)**0.5
print(dista)