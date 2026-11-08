a = 114514
if (int(input("请输入第一次猜想的数字： "))) == a:
    print("恭喜你，猜对啦")
else :
    if (int(input("不对，再猜一次： ")) == a):
        print("恭喜你，猜对啦")
    else:
        if(int(input("不对，再猜最后一次： ")) == a):
            print("恭喜你，猜对啦")
        else:
            print(f"Sorry，全部猜错啦，我想的是： {a}")