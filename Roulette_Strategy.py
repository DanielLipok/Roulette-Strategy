import random


count = 0
bankroll = 250
largest = 0

while bankroll > 0:
    count += 1
    if bankroll > largest:
        largest = bankroll
    ball = random.randint(0, 38)
    print("The number is " + str(ball))
    bankroll -= 5
    if ball in range(0,12):
        bankroll += 15
        print(bankroll)
        ball = random.randint(0, 38)
        if ball in range(13,24):
            bankroll += 30
            print(bankroll)
            ball = random.randint(0, 38)
            if ball in range(25,36):
                bankroll += 90
                print(str(bankroll) + " We have a Winner" )
            else:
                bankroll -= 30
        else:
            bankroll -= 20
    else:
        print(bankroll)

print("Final Bankroll " + str(bankroll))
print("Balls spun " + (str(count)))
print("Maximum Bankroll was " + str(largest))