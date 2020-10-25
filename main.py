from tkinter import *
import tkinter

app=Tk()
app.geometry('218x320')
app.configure(background="black")
app.title("Amshen's Calc")

#Variuble Declaration
screen_font = ('Verdana',25)

#FUNCTIONS
def btn_press(num):
    str=screen.get()
    screen.delete(0,END)
    screen.insert(0,str+num)

def clear():
    screen.delete(0,END)

def equal():
    eq=screen.get()
    eq=str(eval(eq))
    screen.delete(0,END)
    screen.insert(0,eq)


#screen
screen=tkinter.StringVar()
screen=Entry(app,font=screen_font,width=10, textvariable = screen)
screen.grid(row=0,column=0,columnspan=5)

#first row
clear_btn=Button(text='C', height=3,width=6,command=lambda:clear())
btn_one=Button(text='1', height=3,width=6,command=lambda:btn_press("1"))
btn_two=Button(text='2', height=3,width=6,command=lambda:btn_press('2'))
btn_three=Button(text='3', height=3,width=6,command=lambda:btn_press('3'))
AC_btn=Button(text='AC',height=3,width=6, command=lambda:clear())
clear_btn.grid(row=1,column=0)
btn_one.grid(row=2,column=0)
btn_two.grid(row=3,column=0)
btn_three.grid(row=4,column=0)
AC_btn.grid(row=5,column=0)

#Second row
mode_btn=Button(text='M', height=3,width=6)
btn_four=Button(text='4', height=3,width=6, command=lambda:btn_press('4'))
btn_five=Button(text='5', height=3,width=6, command=lambda:btn_press('5'))
btn_six=Button(text='6', height=3,width=6, command=lambda:btn_press('6'))
btn_dot=Button(text='.', height=3,width=6, command=lambda:btn_press('.'))
mode_btn.grid(row=1,column=1)
btn_four.grid(row=2,column=1)
btn_five.grid(row=3,column=1)
btn_six.grid(row=4,column=1)
btn_dot.grid(row=5,column=1)

#Third row
btn_per=Button(text='%', height=3,width=6, command=lambda:btn_press('%'))
btn_seven=Button(text='7', height=3,width=6, command=lambda:btn_press('7'))
btn_eight=Button(text='8', height=3,width=6, command=lambda:btn_press('8'))
btn_nine=Button(text='9', height=3,width=6, command=lambda:btn_press('9'))
equal_btn=Button(text='=', height=3,width=6, command=equal)
btn_per.grid(row=1,column=2)
btn_seven.grid(row=2,column=2)
btn_eight.grid(row=3,column=2)
btn_nine.grid(row=4,column=2)
equal_btn.grid(row=5,column=2)

#Forth row
divide_btn=Button(text='/', height=3,width=6, command=lambda:btn_press('/'))
multiply_btn=Button(text='X', height=3,width=6, command=lambda:btn_press('*'))
sub_btn=Button(text='-', height=3,width=6, command=lambda:btn_press('-'))
pluse_btn=Button(text='+', height=7,width=6, command=lambda:btn_press('+'))
divide_btn.grid(row=1,column=3)
multiply_btn.grid(row=2,column=3)
sub_btn.grid(row=3,column=3)
pluse_btn.grid(row=4,column=3,rowspan=2)


app.mainloop()