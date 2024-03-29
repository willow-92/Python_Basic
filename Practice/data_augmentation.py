# 데이터 범위 정의
# id = 0~9999 이하의 정수. 
# 투자성향 = 안정지향, 수익지향, 균형지향
# 나이 = 20~99 이하의 정수
# 원하는 투자금액 = 1000 ~ 9999 이하의 정수
# 가계상황 = 맞벌이, 외벌이
# 결과 = SCF, 부동산PF상품, 아파트담보상품

# 필요 라이브러리 불러오기
import random
import re

# 리스트 만들기
Invest_Type = ["안정지향", "수익지향", "균형지향"]
household_situation = ["외벌이", "맞벌이"]
recommend_result = ["SCF", "부동산PF상품", "아파트담보상품"]

# i 값 지정
i = 0

# 딕셔너리 리스트 생성
dct_arr = []

# 칼럼명 지정
labels =['id', 'invest', 'age', 'price', 'household', 'result']



# 딕셔너리 형태로 데이터 저장하여 CSV로 만들기
with open ('c://Python_Projects/Python_Basic/Practice/data_aumentation.csv', 'w', encoding='utf-8') as f: 
    f.write(re.sub("[\[\]']", '', str(labels)))
    for i in range(10):
        recommend_dict = {
            labels[0] : int(i),
            labels[1] : Invest_Type[random.randrange(0, 2)],
            labels[2] : random.randrange(20,100),
            labels[3] : random.randrange(1000, 9999),
            labels[4] : household_situation[random.randrange(0,2)],
            labels[5] : recommend_result[random.randrange(0,3)]  
        }
        # print(recommend_dict)
        data = re.sub("[\[\]']", '', str(list(recommend_dict.values()))) + '\n'
        # f.write(data)
        print(data)
print('done')

# 후처리 추가할 것

# pprint.pprint(dct_arr)





# with open('csv_dct.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=labels)
#     writer.writeheader()


# print(str(recommend_dict.values()))







# ======= 참고자료 ==================
# const object = {
#     id: i
#     invest :Invest_Type[random.randrange(0,2)]}
#     age : random.randrange(20,100)
#     price : random.randrange(1000, 9999)
#     household : household_situation[random.randrange(0,2)]
#     result : result[random.randrange(0,3)]
#     dd : ddd,
#     djkfwkwr
# }

# let format = ""
# function makeForm () {
#     const objectLen = object.keys(object).length;

#      for i in range(0, objectLen):
#         format += i,i === 0 || i === objectLen - 1 ? "{}" : ",{}";
# }

# 랜덤값 도출 후 CSV에 쓰기
# with open ("C:/Users/admin/OneDrive/바탕 화면/reccommendation.csv", "w", encoding='utf-8') as f:
#     f.write("id,투자성향,나이,원하는 투자금액,가계상황,결과\n")

#     for i in range(10000):
#         # Object.keys(object).map((v) => v = object[v])
#         # data = "{},{},{},{},{},{}{}".format(object.id, object.invest, object.age, object.price, household, result'\n')
#         id = i
#         invest = Invest_Type[random.randrange(0,2)]
#         age = random.randrange(20,100)
#         price = random.randrange(1000, 9999)
#         household = household_situation[random.randrange(0,2)]
#         result = result[random.randrange(0,3)]
#         data = "{},{},{},{},{},{}{}".format(id, invest, age, price, household, result'\n')
#         # f.write(data)
#         # print(data)
# print("done!")


# 숙제!
# 유지보수가 용이한 형태로 코드를 짤 것. 
# 기존에 짰던 코드는 매번 변수가 추가되면 하드코딩으로 매번 바꿔줘야 하는 불편함이 있음
# 딕셔너리 형태로 데이터를 저장하고, 해당 데이터에서 가져다가 변수를 사용하는 형태로 바꿔볼 것.
