from math import sin, cos, tan, asin, acos, atan, radians, degrees

# 사용자로부터 연산할 함수와 각도/라디안 여부를 입력 받음
operation = input("어떤 함수를 사용하시겠습니까? (sin, cos, tan, arcsin, arccos, arctan): ")
angle_mode = input("입력하실 각도가 '도'인 경우 'd', '라디안'인 경우 'r'을 입력해주세요: ")

# 사용자로부터 각도를 입력 받음
angle = float(input("각도를 입력해주세요: "))

# 입력 받은 각도를 라디안으로 변환
if angle_mode == "d":
    angle = radians(angle)

# 사용자가 선택한 함수를 계산
if operation == "sin":
    result = sin(angle)
elif operation == "cos":
    result = cos(angle)
elif operation == "tan":
    result = tan(angle)
elif operation == "arcsin":
    result = degrees(asin(angle))
elif operation == "arccos":
    result = degrees(acos(angle))
elif operation == "arctan":
    result = degrees(atan(angle))
else:
    result = "잘못된 입력입니다."

# 결과 출력
if type(result) == float:
    print("결과는 {:.4f}입니다.".format(result))
else:
    print(result)