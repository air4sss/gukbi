# 1
# 좀비가 몇 마리인지 사용자입력 받기
# 좀비가 20마리 이상이면 문자 출력
# 20마리 미만이면 poor zombies 출력
# 0을 입력하였을 경우에 문구 출력

zombies = int(input("How many zombies : "))
if zombies >= 20 :
    print("That's a lot of zombies")
elif zombies <= 20 and zombies != 0 :
    print("poor zombies")
else :
    print("No zombies here!")


# 2
# 비밀번호 입력 받기
# 입력 값이 같으면 성공 출력
#

pw = "python"
attempt = input("Password : ")
if pw == attempt :
    print("Login Success")
else :
    print("Wrong Password")
print("Login Program Finish")



# 3.
# 나이에 따라 지하철 교통요금 출력하는 프로그램을 만드시오.
# - 8세 미만의 어린이의 지하철 교통요금은 450원이다.
# - 8세 이상 19세 이하의 청소년 지하철 교통요금은 720원이다
# - 20세 이상의 성인 지하철 교통요금은 1250원이다.

# 조건
# 1. 나이를 입력 받아 변수에 저장
# 2. 문제에서 조건이 몇 개 필요한지 생각
# 3.  조건식 생각
# 4. 각 조건에 따라 수행할 문장 생각

# 요금을 부과하는 함수 작성
def charge_system(ages) :
    charge = 0
    if ages < 8 :
        charge = 450
    elif ages >= 8 and ages <= 19 :
        charge = 720
    elif ages >= 20 :
        charge = 1250
        
    return charge

# 나이 입력
age = int(input("age : "))
print(charge_system(age))



# 4
# 성적에 따라 학점을 출력하는 프로그램을 만드시오.
# - 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D

# 조건
# 1. 성적을 입력 받아 변수에 저장
# 2. 조건이 몇 개 필요한지 생각
# 3. 조건식 생각
# 4. 각 조건에 따라 수행할 문장 생각

# 학점을 부과하는 함수 작성
def give_grade(point) :
    grade = ''
    if point >= 90 :
        grade = "A"
    elif point >= 80 :
        grade = "B"
    elif point >= 70 :
        grade = "C"
    elif point >= 60 :
        grade = "D"
    else :
        grade = "F"
        
    return grade

# 성적을 입력 받음
point = int(input("점수 : "))
grade = give_grade(point)
print(grade)



# 5
# 터널 통과하기
# 어떤 차의 높이가 170cm이다. 이 차는 3개의 터널을 통과하게 된다.
# 터널의 높이가 차의 높이보다 같거나 낮다면 충돌하여 사고가 날 것이다.
# 터널의 높이 3개를 차례대로 사용자 입력하여 모두 통과하면 PASS를, 사고가 난다면 CRASH를 출력
# 이 문제를 2가지 이상의 방법으로 해결하라

# 터널 통과 함수 작성
def tunnel(length1, length2, length3) :
    if length1 >= 170 and length2 >= 170 and length3 >= 170 :
        return "PASS!!"
    else :
        return "CRUSH!!"

"""
# 터널 통과 함수 작성 (제한 높이를 변수 처리)
def tunnel(length1, length2, length3) :
    limit = 170
    if length1 >= limit and length2 >= limit and length3 >= limit :
        return "PASS!"
    else :
        return "CRUSH!"
"""

# 길이 값 입력
length1 = int(input("첫번째 높이 입력 : "))
length2 = int(input("두번째 높이 입력 : "))
length3 = int(input("세번째 높이 입력 : "))

print(tunnel(length1, length2, length3))

