# 1
# 3의 배수의 합
# - 1부터 사용자에게 입력 받은 수 까지의 자연수 주 3의 배수의 합을 구하시오.
# 1. 문제에서 몇 개의 변수가 필요한지 생각
# 2. 반복 조건 생각
# 3. 3배수일 때 더하기 연산을 한다
# 4. 결과 출력

num = int(input("number : "))
answer = 0

for i in range(1, num+1) :
    if i % 3 == 0 :
        answer += i

        
print("answer :", answer)


