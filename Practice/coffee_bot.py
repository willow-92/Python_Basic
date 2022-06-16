import datetime as dt
import random
random.seed()

now = dt.datetime.now()
company =['sk.y', 'ss.p', 'ej.y', 'eb.c', 'k.s', 'sj.k', 'jg.i', 'wr.b', '양희영']
day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
num_list = []
# print(now.weekday())
random.seed()
for i in range(9):
    num = random.randint(0,8)
    while num in num_list :
        num = random.randint(0,8)
    num_list.append(num)
    print(i)

# print(num_list)

p1 = num_list[0:3]
p2 = num_list[3:6]
p3 = num_list[6:9]

print(p1)
print(p2)
print(p3)

print([company[p1[0]]], print([company[p1[1]]]), print([company[p1[2]]]))
# print([p1[1]])
# print([p1[2]])

# print(company[p1][1])
# print(company[p1][2])