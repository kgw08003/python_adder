import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # 계산기 화면 생성
        self.screen = tk.Entry(master, width=20, font=('Arial', 16))
        self.screen.grid(row=0, column=0, columnspan=4, pady=5)
        
        # 버튼 생성
        button_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_index = 1
        col_index = 0

        for button_text in button_list:
            button = tk.Button(master, text=button_text, width=5, height=2,
            font=('Arial', 12), command=lambda text=button_text: self.button_click(text))
            button.grid(row=row_index, column=col_index, padx=5, pady=5)
            col_index += 1

            if col_index == 4:
                col_index = 0
                row_index += 1
                
    # button_click 메소드
    def button_click(self, text):

        # 버튼 클릭 시 동작하는 함수
        if text == '=':
            
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, 'Error')
        else:
            
            self.screen.insert(tk.END, text)

# GUI 프로그램 실행
root = tk.Tk()          
calculator = Calculator(root)       
root.mainloop()     
