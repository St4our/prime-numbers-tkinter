from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from openpyxl import Workbook #reading/loading workbooks
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows #appending dataframes to rows
from tkinter import Tk, Canvas, Frame, BOTH

window = Tk()  
window.title("01-02-2022-ПЗ")  
window.geometry('700x800')  

def kliner1():
    txt_pole.delete('1.0', END)

def prost():
    a= int(txt_a.get())
    b= int(txt_b.get())
    k=[]
    for n in range(a,b):
        if all(n%i!=0 for i in range(2,n)):
            k.append(n)
    txt_pole.insert("1.0",k)
    txt_pole.insert("2.0","\n")


def save_file():
    file = filedialog.asksaveasfilename(initialdir='/', title='Select file',
                                             filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))
    if file:
        f = open(file, 'w')
        text_save = str(txt_pole.get(1.0, END))
        f.write(text_save+'\n')
        f.close()




#1
#текст
lbl_1 = Label(window, text="Задание 1.", font=("Arial Bold", 14))  
lbl_1.grid(column=0, row=0)

lbl_1 = Label(window, text="Вывести все простые числа", font=("Arial Bold", 14))  
lbl_1.grid(column=0, row=2)
#______начало интервала______

lbl_a = Label(window, text="Число а", font=("Arial Bold", 12))  
lbl_a.grid(column=1, row=0)

txt_a=Entry(window,width=30)  
txt_a.grid(column=2, row=0)
#______конец интервала______

lbl_b = Label(window, text="Цисло b", font=("Arial Bold", 12))  
lbl_b.grid(column=1, row=1)

txt_b=Entry(window,width=30)  
txt_b.grid(column=2, row=1)

#поле
txt_pole=scrolledtext.ScrolledText(window, width=50,height=8)
txt_pole.grid(column=0, row=3) 

#кнопки

knopka1 = Button(window, text="Посчитать!", command=prost)  
knopka1.grid(column=1, row=3) 

knopka2 = Button(window, text="Очистить!", command=kliner1)  
knopka2.grid(column=2, row=3) 

knopka2 = Button(window, text="Сохранить!", command=save_file)  
knopka2.grid(column=0, row=4) 





window.mainloop()
