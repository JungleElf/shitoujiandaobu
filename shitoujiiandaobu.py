import random
time = 1
win = 0
while win < 3:
    user = input("请输入对应数字，石头(1)/剪刀(2)/布(3)：")
    computer = random.randint(1,3)
    print("当前是第"+str(time)+"局")
    print("您出的是:",user)
    print("电脑出的是:",computer)
    print("您已获胜"+str(win)+"局")
    if ((user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1)):
        print('你赢了')
        win += 1
    elif user == computer:
        print("平局")
    else:
        print("电脑胜出")
time += 1