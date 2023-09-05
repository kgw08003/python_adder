num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))
operation = input("수행할 연산 종류를 입력하세요 (+, -, *, /, **, sqrt): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        result = num1 / num2
elif operation == '**':
    result = num1 ** num2
elif operation == 'sqrt':
    import math
    result = math.sqrt(num1)

print("결과: ", result)