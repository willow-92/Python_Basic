# 3의 배수는 통과
# 정수 1개를 입력받는다.
# (1 ~ 100)
# 1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
# 3의 배수는 출력하지 않는다.

# 입력예시: 10
# 출력 예시: 1 2 4 5 7 8 10

num = float(input("숫자를 입력하세요 : "))
i = 1
while i <= num:
  if i%3 == 0:
    i+=1
  else:
    print(i)
    i+=1

print("===========================")

for i in range(1, int(num)+1):
  if i % 3 == 0:
    continue
  print(i)
