import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://instargram.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["white", "black"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이원준")
write("description", "Until make the best game of the world")
write("button", "벝흔")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "좋아하는 것": "먹을거, 놀기",
  "싫어하는 것": "푸팟퐁커리",
  "취미": "사감 몰래 폰하기, 소설 보기",
  "진로": "Game Developer"
}
information(informations)