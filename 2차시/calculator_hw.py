import tkinter as tkt

def is_int(number):
    if int(number) == float(number):
        return int(number)
    else:
        return float(number)

def on_click(number):
    entry.insert(tkt.END, number)

def on_clear():
    entry.delete(0, tkt.END)

def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = int(entry.get())
    entry.delete(0, tkt.END)

def on_equal():
    second_num = int(entry.get())
    entry.delete(0, tkt.END)

    if 연산자 == "+":
        entry.insert(0, first_num + second_num)
    elif 연산자 == "-":
        entry.insert(0, first_num - second_num)
    elif 연산자 == "*":
        entry.insert(0, first_num * second_num)
    elif 연산자 == "/":
        entry.insert(0, first_num / second_num)
    elif 연산자 == "%":
        entry.insert(0, first_num % second_num)

# 윈도우 생성
root = tkt.Tk()
root.title("계산기")

# 아이콘 설정
#photo = tkt.PhotoImage(file="./윈도우계산기아이콘.png")
#root.iconphoto(False, photo)

# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)


def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
    button = tkt.Button(root, text=text, padx=width, pady=height, command=command, bg=bg, font=('Helvetica',14, 'bold'))
    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')


for number in range(9):
    create_button(number + 1, 4-number//3, number%3, lambda n=number+1: on_click(n), bg='gainsboro')
create_button(0, 5, 0, lambda: on_click(0), columnspan=1, bg='gainsboro')

create_button("C", 1, 0, on_clear, bg='gray70')
create_button("%", 1, 3, lambda: operate("%"), bg='gray70')
create_button("/", 5, 3, lambda: operate("/"), bg='gray70')
create_button("*", 4, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 2, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 1, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 2, on_equal, bg='orange')

root.mainloop()