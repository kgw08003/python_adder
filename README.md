# 파이썬 계산기

## adder_GUI_upcode.py 사진

![계산기](https://github.com/kgw08003/python_adder/assets/109195054/131d1943-969e-4ee9-9d29-c82c6ca8b22d)

## 코드 설명

### Tkinter 라이브러리 불러오기:

import tkinter as tk: Tkinter 라이브러리를 불러와서 tk 별칭으로 사용

### Calculator 클래스 정의:

Calculator 클래스를 정의하고, 초기화 메서드 __init__를 포함
초기화 메서드는 주요 GUI 요소를 생성하고 설정

### 계산기 화면 생성:

self.screen은 Tkinter의 Entry 위젯을 사용하여 계산기 화면을 생성
화면의 초기 설정(폭, 글꼴, 등)을 지정하고, grid를 사용하여 화면을 배치

### 버튼 생성:

계산기 버튼에 해당하는 문자열을 포함하는 button_list를 정의
for 루프를 사용하여 각 버튼을 생성하고, 텍스트, 폭, 높이, 글꼴 및 클릭 이벤트 핸들러를 설정
버튼은 grid를 사용하여 행과 열에 배치되며, lambda 함수를 사용하여 각 버튼의 클릭 이벤트를 처리

### 버튼 클릭 메서드 (button_click) 정의:

버튼을 클릭했을 때 동작하는 함수로, 눌린 버튼의 텍스트를 받아옴
= 버튼을 클릭하면, 입력된 계산식을 계산하고 결과를 화면에 표시합니다. 오류가 발생하면 "Error"를 표시
다른 버튼을 클릭하면 해당 버튼의 텍스트를 화면에 추가

### GUI 프로그램 실행:

tk.Tk()를 사용하여 Tkinter의 Tk 클래스를 이용하여 루트 윈도우를 생성
Calculator 클래스의 객체 calculator를 생성하고 이를 루트 윈도우에 연결
mainloop()를 호출하여 GUI 프로그램을 실행합니다. 이 메서드는 계산기 윈도우가 종료될 때까지 이벤트를 처리

## adder.py , adder_GUI.py 결과 사진

![adder](https://github.com/kgw08003/python_adder/assets/109195054/32ee1bb1-1c94-46e2-ae95-fb871b494eb5)

## adder_up 결과사진

![adder_up](https://github.com/kgw08003/python_adder/assets/109195054/6cd73073-364c-48f3-b4b3-f2a7a63b7977)

## adder_upup 결과 사진

![adder_upup](https://github.com/kgw08003/python_adder/assets/109195054/7a9506b5-6128-4849-bcff-4e24073fdc27)
