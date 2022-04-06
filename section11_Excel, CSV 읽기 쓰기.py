#section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제 1
with open('./Python_Basic/resource/sample1.csv', 'r', ) as f:
    reader = csv.reader(f)
  #   next(reader) Hearder 스팁
    next(reader)
    next(reader)
    # 확인
    # print(reader)
    # print(type(reader))
    # print(dir(reader))
    # print()

    # for c in reader:
        # print(c)

# 예제 2
with open('./Python_Basic/resource/sample2.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')
  #   next(reader) Hearder 스팁
    next(reader)
    # 확인
    # print(reader)
    # print(type(reader))
    # print(dir(reader))
    # print()

# 예제3 (Dict변환)
with open('./Python_Basic/resource/sample1.csv', 'r', ) as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('----------------')
