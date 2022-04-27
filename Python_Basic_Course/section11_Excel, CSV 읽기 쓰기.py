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
  #   next(reader) Hearder 스탑
    next(reader)
    # 확인
    # print(reader)
    # print(type(reader))
    # print(dir(reader))
    # print()

# 예제3 (Dict변환)
with open('./Python_Basic/resource/sample1.csv', 'r', ) as f:
    reader = csv.DictReader(f)

    # for c in reader:
    #     for k, v in c.items():
    #         print(k, v)
    #     print('----------------')

# 예제4
w = [[1,2,3],[4,5,6,],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
with open('./Python_Basic/resource/sample3.csv', 'w', newline='') as f:
  wt = csv.writer(f)

  for v in w:
    wt.writerow(v)

# newline 옵션은 기억해 놔야 함. 데이터 수가 적으면 개행을 해도 상관 없을 수 있지만, 10만개, 20만개라고 한다면 개행 된 라인이 2배로 늘어나기 때문에 리소스 관리 차원에서 주의해야 함

# 예제 5 (for 문을 사용하지 않고 한 번에 쓸 때)
with open('./Python_Basic/resource/sample4.csv', 'w', newline='') as f:
  wt = csv.writer(f)
  wt.writerows(w) # 리스트 안에 있는 것들을 한 번에 씀


# Parsing이란?
# 설명 1
# 파싱은 구문분석이라고 함
# 문장이 이루고 있는 구성 성분을 분해하고 분해된 성분의 위계 관계를 분석하여 구조를 결정하는 것
# 데이터를 분해 분석하여 원하는 형태로 조립하고 다시 빼내는 프로그램을 말함
# 웹 상에서 주어진 정보를 내가 원하는 형태로 가공하여 서버에서 불러들이는 것
# 이러한 parsing 기법은 XML parsing과 Json parsing이 있음.

# 설명 2
# 파싱은 하나의 프로그램을 런타임환경 (예를 들면, 브라우저 내 자바스크립트 엔진)이 실제로 행할 수 있는 내부 포맷으로 분석하고 변환하는 것을 의미한다.
# 즉 파싱은 문서의 내용을 토큰(token)으로 분석하고, 문법적 의미와 구조를 반영한 파스트리(parse tree)를 생성하는 과정이다.

# *토큰이란? 언어가 사용하는 기본 '단어'를 말함
# 토큰은 구문적으로 의미를 갖는 최소의 단위이며, 우리가 작성하는 프로그램은 모두 이러한 토큰으로 이루어진다.

# 설명 3
# 기존 데이터를 다른 형태(패턴)으로 가공하는 것
# 자료형변환도 파싱의 일종이다.
# 예)
# JSON.stringify();
# Java의 list를 Json으로 바꾸기,
# Json을 스트링으로 바꾸기,
# int를 String 형으로 바꾸기

# 설명 4
# 파싱은 쉽게 말해 문장이나 데이터문자열 (html, json 등)에서 원하는 데이터를 분석하여 추출하는 기술을 말함
# 특정한 패턴과 규칙, 순서를 이용하여 자신이 필요로 하는 데이터를 추출해내는 작업
# 엄격히 말해서 크롤링은 웹데이터를 가져오는 행위 자체를 의미하며, 파싱은 크롤링으로 가져온 데이터에서 필요한 정보를 추출하는 것을 말함
# 국내에서는 크롤링과 파싱을 구분하지 않고 일반적으로 파싱이라고 칭하는 경우가 많음
# 활용 예시
# 기상청의 날씨 정보를 가져와 저장하여 자신에게 맞는 형태로 자동으로 가공 또는 저장함
# 지도 정보 및 데이터를 수집하여 자신에게 맞는 형태로 자동으로 가공 저장함

# 이러한 형태는 자신이 필요한 정보가 있는 웹사이트에 자신이 필요한 정보 및 데이터를 수집하여 저장하고 가공하여 다시 활용할 수 있음
# 파싱의 형태는 사용하는 언어에 따라 다양하게 개발이 되고 있고 사이트의 환경에 따라 데이터를 수집하는 기술이 다양하게 바뀌고 있음
# 아주 많은 각기 다른 환경의 웹사이트에서 자신에게 필요한 데이터를 수집하기 위해서 파싱의 기술도 다양하고 폭넓게 개발되고 있음



# Parser란?
# 파서는 complier의 일부로서 원시 프로그램의 명령문이나 온라인 명령문, HTML 문서 등에서 Markup Tag 등을 입력으로 받아들여서 구문을 해석할 수 있는 단위로
# 여러 부분으로 해석해 주는 역할을 한다. 즉 Complier나 Interpreter에서 원시 프로그램을 읽어 들여, 그 문장이 구조를 알아내는 Parsing을 행하여 주는 프로그램이다.



  # 순회하면서 쓸 때와, 한 번에 리스트 안에 있는 것들을 쓸 때는 다 그 역할이 있음
  # 만약 어떤 회원 목록을 쓸 것인데, 회원번호가 20으로 시작하는 사람, 만약에 92년생 이하 미성년자들은 리스트를 빼고 달라는 부탁을 받았다면?
  # if문으로 가져온 데이터를 조회를 해서, 생년월일을 파싱해서 92년생 이하는, 이상은 안 쓰게 해 놓으면, 그 이상만 나이를 필터링 해서 쓸 수 있다.
  # 하나 하나 검수해서 쓸 때는 writerow로 사용하는 것이고.
  # 어차피 이걸 다 쓴다, 이미 검증이 끝난 데이터다 하면 writerows를 사용하면 된다. 
  # 다 역할이 있는 메소드. 경우에 따라, 프로그램 흐름과 로직에 따라서 구분해서 사용하면 된다. 




# XSL, XLSX
# 엑셀을 처리하는 오픈소스들은 파이썬에 굉장히 많음
# openpyxl, xlswriter, xlrd, xlwt, xlutilis
# pandas를 주로 사용
# 판다스는 데이터과학이나 분석을 하기 위한 전 단계에서 열과 행의 데이터셋, 프레임셋을 만들어서
# 통계를 추출하기 위한 셋을 만든다. 
# 그래서 이 판다스를 설치하게 되면 넘파이라는 것도 설치가 되고. 
# 엑셀 데이터를 다룰 때 판다스를 주로 사용. 왜냐하면 가장 많이 사용하는 openpyxl과 xlrd라는 랭킹 2위인 xlrd를 판다스가 내부적으로 사용함.
# openpyxl과 xlrd를 설치하고 pandas까지 설치하면 csv, XSL등 판다스 하나로 만능으로 사용할 수 있음. 
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd
# sheetname = '시트명' 또는 숫자, header=3, skiprow=숫자
# 시트가 엑셀로 따지면 하나인데, 여러개 있으면 이름을 지정할 수 있고.
# 여러개 시트가 있을 경우 어떤 것을 가져올거냐, 할 수 있고. 
# 한글로 되어 있으면 왼쪽 부터 1번, 2번, 3번 이런 식으로 갈 수 도 있고.
# 여러개 시트일 경우 숫자로 가져오는게 좋음

# header
# 몇 번쨰 열을 해더로 지정할 것인지

# skiprow
# 몇 번 행은 가져오지 않을 것인지. 

# 판다스는 이것 말고도 많은 메소드를 제공함. 기초과정이 판다스 과정이 아니기 때문에, 구글에서 판다스 엑셀이라고 치면 레퍼런스페이지가 나옴
# 여기에 여러가지 옵션들이 있음.
# 사용법도 잘 나와 있음. 

# 해
xlsx = pd.read_excel('./Python_Basic/resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head()) #첫 번째 부터 5개만 보여줌
# 이걸 가지고 와서 스트링 형태로 원하는 대로 파싱할 수 있음.
print()

# 데이터 확인
print(xlsx.tail()) # 끝에 5개를 보여줌

# 데이터 확인
print(xlsx.shape) # 행, 열
# 행과 열을 출력해주는.

# 엑셀 or CSV 다시 쓰기

xlsx.to_excel('./Python_Basic/resource/result.xlsx', index=False)
# 인덱스는 0,1,2,3,4 이렇게 숫자를 붙여줌

xlsx.to_csv('./Python_Basic/resource/result.csv', index=False)

