import random

lotteryNumber = []

for i in range(0,6): # 6 numbers
    number = random.randint(1,50) # picking up six numbers from range 1,50

    while number in lotteryNumber:
        number = random.randint(1,50)



    lotteryNumber.append(number)


lotteryNumber.sort()

# printing sorted numbeer appended in lotteryNumbers Dictionary
print(lotteryNumber)

# eg. result -> [12, 20, 23, 24, 40, 44]