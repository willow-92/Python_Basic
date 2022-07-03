import datetime as dt
import random
random.seed()

now = dt.datetime.now()
# company =['sk.y', 'ss.p', 'ej.y', 'eb.c', 'k.s', 'sj.k', 'jg.i', 'wr.b', 'hy.y']

def select():
    company =['박상선', '최은배', '송경', '강세종', '임정근', '봉우리', '양희영', '서경원']
    day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    num_list = []

    for i in range(len(company)):
        num = random.randint(0,len(company)-1)
        while num in num_list :
            num = random.randint(0,len(company)-1)
        num_list.append(num)
    print(num_list)



    p1 = num_list[0:4]
    p2 = num_list[4:]
    # p3 = num_list[6:9]

    print(company[p1[0]], company[p1[1]], company[p1[2]], company[p1[3]])
    print(company[p2[0]], company[p2[1]], company[p2[2]], company[p2[3]])
    # print(company[p3[0]], company[p3[1]], company[p3[2]])
   


select()

