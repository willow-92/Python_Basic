#section 03-3
# Daum 주식 정보 가져오기

# 데이터를 가져오는 방법도 중요하지만, 어떻게 다음이나 네이버, 페이스북 유튜브 같은 사이트들이 우리가 요청하는 클라이언트를 구분하는지
# 파이썬 코드로 요청을 하면 규모가 작은 사이트들은 그냥 데이터를 주지만, 포털 사이트들은 데이터가 넘어오지 않음. 제한이 걸려 있음
# 403 에러가 쓰면서= 제한이 되어 있기 때문에,
# 우리 컴퓨터로 실제로 브라우저를 통해서 사용자가 요청을 했는지, 아니면 코드로 요청을 했는지를 구분을 할 수가 있다. 
# 그렇기 떄문에 코드에서 최대한 클라이언트 브라우저에서 실을 수 있는 헤더 파이썬 코드로 직접 만들어서 보내야 원하는 데이터를 수신할 수 있다. 

# 주식 인기검색어 1위 부터 10위까지 회사명, 주가, 상승률, 하락률 등 3가지 정보를 가져오기
# 클라이언트의 정보를 다음 사이트에 요청하는 것에 포커스를 맞춰서 들을 것. 

# 다음 사이트의 URL로 요청을 하면 브라우저에서 엔터를 치면 원하는 정보가 화면에 렌더링이 되어서 나타남. 
# 개발자 도구의 네트워크 탭에서 정보를 보면 첫 번쨰로 요청된 것이 주소창에서 요청한 finance.daum.net
# 그럼 여기의 request url을 보면 주소창에 요청한 finance.daum.net이 나옴
# 하지만 파이썬에서 이 URL로 요청을 해서 리스폰스를 받아서 read로 읽으면 이 데이터가, 또는 이런 데이터가 없다. 
# 이런 것들을 에이잡스라고 하는데, 비동기로, 처음에 렌더링이 될 때는 특정 부분이 없이 렌더링이 되고,
# 그 부분이 렌더링이 완료가 되면 추가적으로 네트워크에서 또 요청을 해서,
# 남은 부분을 부가적으로 후에 그려넣는 작업을 한다. 이런 것들을 비동기 통신이라고 부름. 
# 포커스는 여기에서 URL 정보를 잘 봐야 한다는 것.
# get으로 요청했는데 304가 왔다. 그 다음에 좀 가면 ranks?limit=10 이라는 부분이 요청이 됨.
# 그러면 https://finance.daum.net/api/search/ranks?limit=10 왠지 우리가 원하는 순위에서 10개니까, 
# 추측을 해보면 이 URL로 요청했다 라는것을 추측할 수 있음
# 원하는 정보를 요청했을 때, 원하는 데이터가 없다? 이 URL로 요청을 했는데? 
# 그럴 때는 네트워크탭에서 다른 URL을 살펴봐야 한다. 

# 그 다음에 확인해야 할 2번 째, 다른 별도의 요청이 있고 그 요청을 클릭해보고 request url 원문이 나오니까. 
# 여기 response 정보를 한번 봐라. 없으면 f5
# 순서를 보면 finance daum.net이 렌더링이 되었는데, 여기를 살펴보면 html에는 순위 정보가 없음. 
# 좀 내려보다가 ranklimit의 response를 보면 데이터에 10개가 넘어와있음.
# 그래서 우리가 원하는 정보는 finance.daum.net의 정보가 아니라 ranklimit에 들어있는 정보.
# https://finance.daum.net/api/search/ranks?limit=10 근데 이 url을 그냥 포털사이트에서 입력하면 막아놨음
# 직접 접근을 막아놓음. 그래서 이 header 정보를 직접 편집해줘야 함. 
# 첫 번쨰로 요청한 것이 finance.daum.net 정보에 request header에 보면 user agent 브라우저가 뭔지, 크롬인지, 윈도우인지 맥인지
# 이런 정보를 유저 에이전트로 싣고, 잘 보면 referrer 이전에 어떤 사이트에서 넘어왔는지. 
# 네이버에 있다가 바로 직접 접근을 하면 이전에 거쳐서 온 사이트에 네이버가 나온다. 
# 다음 사이트는 심플하게 분석한 결과, user agent를 가지고 있어야 하고.
# 기본 코드를 작성해서 요청을 하면 파이썬 엔진으로 나오기 때문에, 다음 서버에서는 브라우저가 아니기 때문에 403 에러를 내려줌
# 그럼 우리가 원하는 데이터를 절대 수신할 수가 없음.
# 그래서 user agent와 referrer의 header 정보를 직접 만들어서 넘겨 줘야 함.

# finance.daum.net에 접근한 사람이 조금 뒤에 limit=10 이걸 수신하는건데, 
# 처음에 인기검색은 없이 수신했다가 두 번쨰로 https://finance.daum.net/api/search/ranks?limit=10 이게 요청이 된 다음에
# 만들어지는 구조인데, 이때 referrer은 당연히 첫 번째로 요청한 finance.daum.net이 referrer가 되고. 
# 두 번째로 https://finance.daum.net/api/search/ranks?limit=10가 요청되어서 만들어 지는 형태. 