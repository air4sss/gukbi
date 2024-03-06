# a란 변수에 들어있는 문자열을 슬라이싱하여 아래와 같은 결과가 나오도록 year, date, weather 변수 선언
# a = "20240305 Sunny" >>> 2024 >>>> 0305 >>>> Sunny
a = "20240305 Sunny"
year = a[:4]
date = a[4:8]
weather = a[-5:]
a = ">>>"
print(year, a, date, a, weather)

# 'Pithon' 이라는 문자열을 넣은 b라는 변수를 사용하여 'Python'이라는 문자열을 출력해보자
b = "Pithon"
print(b[:1] + "y" + b[2:])
