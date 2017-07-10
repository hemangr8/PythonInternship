from tkinter import *
from random import randrange

#For keeping score
countCPU = 0 
countPlayer = 0

#Allot number to user's selection
def convertToNumber(userInput):
    if userInput == "Rock":
        return 0
    elif userInput == "Spock":
        return 1
    elif userInput == "Paper":
        return 2
    elif userInput == "Lizard":
        return 3
    else:
        return 4

#Determine CPU's random selection
def cpuSelection(selectionNo):
    if selectionNo == 0:
        return "Rock"
    elif selectionNo == 1:
        return "Spock"
    elif selectionNo == 2:
        return "Paper"
    elif selectionNo == 3:
        return "Lizard"
    else:
        return "Scissors"

#Determine the result
#Uses the concept that the user's selection beats the CPU's selection if the
#CPU's selection lies at one of the previous 2 counterclockwise positions
#and user's selection loses to the CPU's selection if the
#CPU's selection lies at one of the next 2 clockwise positions
def result (player, cpu):
    global countPlayer
    global countCPU
    if player == cpu:
        return "Draw"
    elif player == 0 and cpu+2 < 5:
        countCPU += 1
        return "Player lost"
    elif player == 0 and cpu+2 >= 5:
        countPlayer += 1
        return "Player won"
    elif (player-((cpu+2)%5))<=0:
        countPlayer += 1
        return "Player won"
    else:
        countCPU += 1
        return "Player lost"


#Bound to the Play button as callback to execute command
def cbc(textResult):
    return lambda : callback(textResult)

#Actions on button click
def callback(textResult):
    global countCPU
    global countPlayer
    userInput = entry.get()
    player = convertToNumber(userInput)
    cpu = randrange(0,5)
    ans = result(player, cpu)
    text = "CPU's Selection is {} Result:  {}\n".format(cpuSelection(cpu), ans)
    score = "CPU: {} Player: {}".format(countCPU, countPlayer)
    entryScore.delete(0, END)
    entryScore.insert(0, score)
    textResult.insert(END, text)
    #To allow scrolling
    textResult.see(END)             

def cbcRock(entry):
    return lambda : setRock(entry)

def cbcPaper(entry):
    return lambda : setPaper(entry)

def cbcScissors(entry):
    return lambda : setScissors(entry)

def cbcLizard(entry):
    return lambda : setLizard(entry)

def cbcSpock(entry):
    return lambda : setSpock(entry)

def setRock(entry):
    entry.delete(0, END)
    entry.insert(0, "Rock")

def setPaper(entry):
    entry.delete(0, END)
    entry.insert(0, "Paper")

def setScissors(entry):
    entry.delete(0, END)
    entry.insert(0, "Scissors")

def setLizard(entry):
    entry.delete(0, END)
    entry.insert(0, "Lizard")

def setSpock(entry):
    entry.delete(0, END)
    entry.insert(0, "Spock")

top = Tk()
textResult = Text(master = top)
textResult.grid(column = 1)
entry = Entry(master = top)
entry.grid(row = 0)
entry.insert(0, "Press choice button")
entryScore = Entry(master = top)
entryScore.grid(column = 1)
entryScore.insert(0, "CPU: 0 Player: 0")
btn = Button(top, text="Play", command = cbc(textResult))
btn.grid(row = 1)
btnRock = Button(top, text="Rock", command = cbcRock(entry))
btnRock.grid(row = 1, column = 2)
btnPaper = Button(top, text="Paper", command = cbcPaper(entry))
btnPaper.grid(row = 2, column = 2)
btnScissors = Button(top, text="Scissors", command = cbcScissors(entry))
btnScissors.grid(row = 3, column = 2)
btnLizard = Button(top, text="Lizard", command = cbcLizard(entry))
btnLizard.grid(row = 4, column = 2)
btnSpock = Button(top, text="Spock", command = cbcSpock(entry))
btnSpock.grid(row = 5, column = 2)
Button(top, text='Exit', command = top.destroy).grid(row = 2)
top.mainloop()
