import random
answer=random.randint(0,80)
print(answer)
counts=1
while counts<=3:
    temp=input("请输入一个数")
    guess=int(temp)
    if guess==answer:
        print("猜对了游戏结束")
        break
    else:
        counts=counts+1
        print("猜错了")
        if guess>answer:
            print("猜偏大了")
        else:print("猜偏小了")

print("今日体验次数已用完")
