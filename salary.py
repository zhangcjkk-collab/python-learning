import random

salary_sum = 10000

for i in range(20):
    performance = random.randint(1,10)
    if salary_sum == 0:
        print("工资发完了，下个月领取吧")
        break
    
    else:
        if performance < 5:
            print(f"员工{i}，绩效分{performance}，低于5，不发工资，下一位")
            continue
        else:
            salary_sum -= 1000
            print(f"给员工{i}发放工资1000元，账户余额还剩{salary_sum}")