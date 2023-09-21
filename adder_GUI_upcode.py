import tkinter as tk

class Calculator:
    def __init__(self, master): # __init__ 메소드 (생성자)
        self.master = master
        master.title("Calculator") # master를 저장하고, title을 "Calculator"로 설정

        # 계산기 화면 생성
        self.screen = tk.Entry(master, width=20, font=('Arial', 16))
        self.screen.grid(row=0, column=0, columnspan=4, pady=5)
        # tk.Entry() 함수를 이용하여 Entry(입력창) 위젯을 생성하고, width와 font를 설정
        # 생성한 Entry(입력창) 위젯을 grid() 메소드로 행(row) 0, 열(column) 0 위치에 위치시키고, columnspan으로 4칸을 차지하게 함
        # pady를 통해 위젯과 위젯 사이의 간격을 설정
        
        # 버튼 생성
        button_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_index = 1
        col_index = 0

        # 반복문을 이용하여 버튼들을 생성함
        # tk.Button() 함수를 이용하여 Button(버튼) 위젯을 생성하고, text, width, height, font, command를 설정
        # 생성한 Button(버튼) 위젯을 grid() 메소드로 row_index와 col_index 위치에 위치시키고, padx와 pady를 통해 위젯과 위젯 사이의 간격을 설정함
        # lambda 함수를 이용하여 각 버튼을 클릭할 때마다 button_click 메소드가 실행되도록 함
        for button_text in button_list:
            button = tk.Button(master, text=button_text, width=5, height=2,
                               font=('Arial', 12), command=lambda text=button_text: self.button_click(text))
            button.grid(row=row_index, column=col_index, padx=5, pady=5)
            col_index += 1
            # col_index가 4와 같아지면 다음 행으로 이동
            if col_index == 4:
                col_index = 0
                row_index += 1
                
    # button_click 메소드
    def button_click(self, text):
        # 버튼 클릭 시 동작하는 함수
        if text == '=':
            # '=' 버튼을 눌렀을 때, 계산식을 계산하고 결과 값을 출력함
            # try-except 구문을 이용하여 계산식이 올바르지 않을 때 "Error"를 출력함
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, 'Error')
        else:
            # '=' 버튼이 아닌 다른 버튼을 눌렀을 때, 해당 버튼의 텍스트를 입력창에 추가함
            self.screen.insert(tk.END, text)

# GUI 프로그램 실행
root = tk.Tk()          # tkinter 모듈의 Tk 클래스를 이용하여 루트 윈도우를 생성합니다. 이 윈도우는 계산기의 전체 프레임이 됩니다.
calculator = Calculator(root)       # Calculator 클래스의 객체 calculator를 생성하고, 이 객체를 root 윈도우에 연결합니다.
root.mainloop()     # mainloop() 메서드를 이용하여 계산기 프로그램을 실행합니다. 이 메서드는 계산기 윈도우가 종료될 때까지 계속 실행되며, 
                    #이벤트를 처리합니다. 계산기 윈도우를 닫기 전까지는 계산기 프로그램이 종료되지 않습니다.
  
