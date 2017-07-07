# Power Ball Lottery Code
#This program tells whether you have won the lottery or not

from random import randrange

#This module generates the lucky no. for the lottery winner.
#The lucky no. has 5 distinct random no.s between [1,60) clubbed together and a powerball no. between [1,36)

def lottery_no():
    lucky_no = []
    n = 1
    while(n < 6):
        flag = 1
        random_no = randrange(1,60)
        for number in lucky_no:
            if random_no == number:
                flag = 0
        if flag == 1:
            lucky_no.append(random_no)
        n += 1
    powerball_no = randrange(1,36)
    flag = 1
    for no in lucky_no:
        if no == powerball_no:
            flag = 0
    lucky_no.append(powerball_no)
    return lucky_no

# Take the input of ticket no. of the user

lottery_ticket_no = []
n=1
while (n < 7):
    lottery_ticket_no.append(int(input()))
    n += 1

# Checking whether user wins

lucky_no = lottery_no()

print("The lottery no. is:", lucky_no) 
    
if(lucky_no == lottery_ticket_no):
    print("You win the jackpot")

elif(lucky_no[len(lucky_no)-1] == lottery_ticket_no[len(lottery_ticket_no)-1]):
    print("You win the power ball no.")

else:
    print("You lost")
