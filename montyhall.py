import random

doordict = {
    'door1':0,
    'door2':0,
    'door3':0
}

doorlist = ['door1','door2','door3']

change_wins = []
same_wins = []


def run(iterations):
#choose the other door
    for a in range(1,iterations,1):
        door_prize = doorlist[random.randint(0,2)]
        door_picked = doorlist[random.randint(0,2)]
        

#if you switch
#if you pick the door with the car - you lose
        if door_picked == door_prize:
            change_wins.append(0)
            same_wins.append(1)
        
        else:
            change_wins.append(1)
            same_wins.append(0)
        

run(1001)

# print len(change_wins)
# print len(same_wins)
# print change_wins.count(1)

change_win_percentage = (float(change_wins.count(1))/len(change_wins)) * 100
same_win_percentage = (float(same_wins.count(1))/len(same_wins)) * 100


print('The number of times you win by changing the doors is %f percent' % change_win_percentage)
print('The number of times you win by keeping your original door is %f percent' % same_win_percentage)
#if you pick the door without the car, then win


#if you keep the same door



# def switch_door(iterations)
#     door_prize = doorlist[random.randint(0,2)]
#     doordict[door_prize]
#     door_picked = doorlist[random.randint(0,2)]


# def keep_door(iteration)

# list[randn]
# list[randnum] = 1
# random.randint()
# door_picked = list[randnum]

# if door_picked == 1
# else
#     for a in doorlist   
#         if a in doorlist == 0 & a=/= door_picked
