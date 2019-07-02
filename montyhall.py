import random

#need a function that takes in how many times to run it

randomnum = random.randint(0,2)

doordict = {
    'door1':0,
    'door2':0,
    'door3':0
}

doorlist = ['door1','door2','door3']
door_prize = doorlist[random.randint(0,2)]
door_picked = doorlist[random.randint(0,2)]

print door_picked


# list[randn]
# list[randnum] = 1
# random.randint()
# door_picked = list[randnum]

# if door_picked == 1
# else
#     for a in doorlist   
#         if a in doorlist == 0 & a=/= door_picked
