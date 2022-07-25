# 데이터 범위 정의
# id = 0~9999 이하의 정수. 
# 투자성향 = 안정지향, 수익지향, 균형지향
# 나이 = 20~99 이하의 정수
# 원하는 투자금액 = 1000 ~ 9999 이하의 정수
# 가계상황 = 맞벌이, 외벌이
# 결과 = SCF, 부동산PF상품, 아파트담보상품

# 필요 라이브러리 불러오기
import random


# 리스트 만들기
Invest_Type = ["안정지향", "수익지향", "균형지향"]
household_situation = ["외벌이", "맞벌이"]
result = ["SCF", "부동산PF상품", "아파트담보상품"]

# const object = {
#     id: i
#     invest : {name: "투자성향", value : Invest_Type[random.randrange(0,2)]}
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
with open ("C:/Users/admin/OneDrive/바탕 화면/reccommendation.csv", "w", encoding='utf-8') as f:
    f.write("id,투자성향,나이,원하는 투자금액,가계상황,결과\n")

    for i in range(10000):
        # Object.keys(object).map((v) => v = object[v])
        # data = "{},{},{},{},{},{}{}".format(object.id, object.invest, object.age, object.price, household, result'\n')
        id = i
        invest = Invest_Type[random.randrange(0,2)]
        age = random.randrange(20,100)
        price = random.randrange(1000, 9999)
        household = household_situation[random.randrange(0,2)]
        result = result[random.randrange(0,3)]
        data = "{},{},{},{},{},{}{}".format(id, invest, age, price, household, result'\n')
        # f.write(data)
        # print(data)
print("done!")


# 숙제!