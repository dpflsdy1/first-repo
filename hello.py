#과제 1부터 10까지 반복하는 과정에서 3의 배수일경우, year 출력 나머지는 그대로 출력

for i in range(1,20+1):
    if i % 15 == 0:
        print('yeardream')
    elif i % 3 == 0:
        print('year')
    elif i % 5 == 0:
        print('dream')
    else:
        print(i)
