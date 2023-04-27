n,x = map(int, input("두 개의 숫자를 입력하세요: ").split())
num = list(map(int, input("첫 번째 숫자 개수만큼의 숫자를 입력하세요: ").split()))
for i in range(n):
    if num[i] > x:
        print(num[i])