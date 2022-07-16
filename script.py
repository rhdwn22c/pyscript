import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://i.com/" # https:// 꼭 붙여야 연결됩니다!
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
colors = ["#000000", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이원준")
write("description", "대소고 2학년")
write("button", "인스타그램")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "대소고 다니는 사람": "meronajoa0",
  "인스타 아이디": "e_1jun_22_",
  "대소고 찐따 공식": "so._.in",
  "두카미 얼굴천재222222": "yr0118kim"
}
information(informations)
