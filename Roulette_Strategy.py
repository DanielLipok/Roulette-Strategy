# Just a fun project where I tested a roulette betting strategy to see how successfull it can be

import random

#For keeping track of values
count = 0
bankroll = 250
largest = 0

#While loop to repeat the roll
while bankroll > 0:
    count += 1
#To keep track of the highest amount of money earned    
    if bankroll > largest:
        largest = bankroll
#Rolling the ball        
    ball = random.randint(0, 38)
    print("The number is " + str(ball))
#5 dollar first bet    
    bankroll -= 5
    if ball in range(0,12):
        bankroll += 15
        print(bankroll)
        ball = random.randint(0, 38)
#Parley 2nd bet        
        if ball in range(13,24):
            bankroll += 30
            print(bankroll)
            ball = random.randint(0, 38)
#Parley 3rd bet            
            if ball in range(25,36):
                bankroll += 90
                print(str(bankroll) + " We have a Winner" )
            else:
                bankroll -= 30
        else:
            bankroll -= 20
    else:
        print(bankroll)
#The odds are against you so eventually you will hit 0 so that is why I don't implement a max cap 
print("Final Bankroll " + str(bankroll))
print("Balls spun " + (str(count)))
print("Maximum Bankroll was " + str(largest))
