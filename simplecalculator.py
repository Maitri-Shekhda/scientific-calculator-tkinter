import tkinter as tk
from math import *
from tkinter import messagebox
from winsound import *

convert_constant=1
inverse_convert_constant=1

def fsin(arg):
    return sin(arg*convert_constant)

def fcos(arg):
    return cos(arg*convert_constant)

def ftan(arg):
    return tan(arg*convert_constant)

def arcsin(arg):
    return sin(arg*convert_constant)

def arccos(arg):
    return cos(arg*convert_constant)

def arctan(arg):
    return tan(arg*convert_constant)

btn_p={'padx':16,'pady':1,'bd':4,'fg':'BLACK','bg':'#FFDBA4','font':('arial',18),'width':2,'height':2,'relief':'flat','activebackground':'black'}
class Calculator:
    def __init__(self,master):
        self.exp=''
        #self.recall=''
        self.sum_up=''
        self.text_input=tk.StringVar()
        #self.answ=''
        self.master=master
        top_frame=tk.Frame(root,width=600,height=15,bd=10,relief='flat',bg='#ffb3b3')
        top_frame.pack(side=tk.TOP)
        top_frame1=tk.Frame(root,width=600,height=15,bd=10,relief='flat',bg='#ffb3b3')
        top_frame1.pack()
        global txt_display1
        txt_display1=tk.Entry(top_frame1,font=('arial',36),relief='flat',bg='white',fg='black',width=60,bd=12,justify='right')
        txt_display1.pack()
        txt_display1.insert(2,self.sum_up)
        
        
        bottom_frame=tk.Frame(root,width=600,height=600,bd=2,relief='flat',bg='#c1efff')
        bottom_frame.pack(side=tk.BOTTOM)

        txt_display=tk.Entry(top_frame,font=('arial',36),relief='flat',bg='white',fg='black',textvariable=self.text_input,width=60,bd=12,justify='left')
        txt_display.pack()
        top_frame.bind_all("<Delete>", self.btn_clear_all, add= '+')
        top_frame.bind_all("<Return>", self.btn_total, add= '+')
        top_frame.bind_all("<KP_1>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_2>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_3>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_4>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_5>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_6>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_7>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_8>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_9>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_0>", self.btn_click, add= '+')
        top_frame.bind_all("<KP_Decimal>", self.btn_click, add= '+')
        top_frame.bind_all("<Control-Alt-8>", self.btn_click, add= '+')
        top_frame.bind_all("+",self.btn_click, add = '+')
        # top_frame.bind_all("<KP_Add>",self.btn_append, add= '+')
        self.btn_lb=tk.Button(bottom_frame,**btn_p,text="(" ,command=lambda :self.btn_click('('))
        self.btn_lb.grid(row=0,column=0)
        self.btn_rb=tk.Button(bottom_frame,**btn_p,text=")" ,command=lambda :self.btn_click(')'))
        self.btn_rb.grid(row=0,column=1)
        self.btn_exp=tk.Button(bottom_frame,**btn_p,text="e" ,command=lambda :self.btn_click('2.718281828459045'))
        self.btn_exp.grid(row=0,column=2)
        self.btn_pi=tk.Button(bottom_frame,**btn_p,text="π" ,command=lambda :self.btn_click('3.14159265'))
        self.btn_pi.grid(row=0,column=3)
        self.btn_sqrt=tk.Button(bottom_frame,**btn_p,text="sqrt" ,command=lambda :self.btn_click('sqrt('))
        self.btn_sqrt.grid(row=0,column=4)
        self.btn_ac=tk.Button(bottom_frame,**btn_p,text="AC" ,command=self.btn_clear_all,)
        self.btn_ac.grid(row=0,column=5)
        self.btn_c=tk.Button(bottom_frame,**btn_p,text="C" ,command=self.btn_clear )
        self.btn_c.grid(row=0,column=6)
        self.cube = tk.Button(bottom_frame, **btn_p, text=u"x\u00B3", command=lambda: self.btn_click('**3') )
        self.cube.grid(row=1, column=1)
        self.square = tk.Button(bottom_frame, **btn_p, text=u"x\u00B2", command=lambda: self.btn_click('**2') )
        self.square.grid(row=1, column=2)
        self.btn_abs = tk.Button(bottom_frame, **btn_p, text="abs", command=lambda: self.btn_click('abs(') )
        self.btn_abs.grid(row=1, column=3)
        self.btn_7 = tk.Button(bottom_frame, **btn_p, text="7", command=lambda: self.btn_click(7) )
        self.btn_7.configure(activebackground="black", bg='#FFDBA4')
        self.btn_7.grid(row=1, column=4)
        self.btn_8 = tk.Button(bottom_frame, **btn_p, text="8", command=lambda: self.btn_click(8) )
        self.btn_8.configure(activebackground="black", bg='#FFDBA4')
        #top_frame.bind_all("Num-8", self.btn_click("8"), add= '+')
        self.btn_8.grid(row=1, column=5)
        self.btn_9 = tk.Button(bottom_frame, **btn_p, text="9", command=lambda: self.btn_click(9) )
        self.btn_9.configure(activebackground="black", bg='#FFDBA4')
        self.btn_9.grid(row=1, column=6)
        self.btn_4 = tk.Button(bottom_frame, **btn_p, text="4", command=lambda: self.btn_click(4) )
        self.btn_4.configure(activebackground="black", bg='#FFDBA4')
        self.btn_4.grid(row=2, column=4)
        self.btn_5 = tk.Button(bottom_frame, **btn_p, text="5", command=lambda: self.btn_click(5) )
        self.btn_5.configure(activebackground="black", bg='#FFDBA4')
        self.btn_5.grid(row=2, column=5)
        self.btn_6 = tk.Button(bottom_frame, **btn_p, text="6", command=lambda: self.btn_click(6) )
        self.btn_6.configure(activebackground="black", bg='#FFDBA4')
        self.btn_6.grid(row=2, column=6)
        self.btn_1 = tk.Button(bottom_frame, **btn_p, text="1", command=lambda: self.btn_click(1) )
        self.btn_1.configure(activebackground="black", bg='#FFDBA4')
        self.btn_1.grid(row=3, column=4)
        self.btn_2 = tk.Button(bottom_frame, **btn_p, text="2", command=lambda: self.btn_click(2) )
        self.btn_2.configure(activebackground="black", bg='#FFDBA4')
        self.btn_2.grid(row=3, column=5)
        self.btn_3 = tk.Button(bottom_frame, **btn_p, text="3", command=lambda: self.btn_click(3) )
        self.btn_3.configure(activebackground="black", bg='#FFDBA4')
        self.btn_3.grid(row=3, column=6)
        self.btn_div=tk.Button(bottom_frame,**btn_p,text="/",command=lambda :self.btn_click('/') )
        self.btn_div.grid(row=0,column=7)
        self.btn_mult = tk.Button(bottom_frame,**btn_p, text="x", command=lambda: self.btn_click('*') )
        self.btn_mult.grid(row=1, column=7)
        self.btnSub = tk.Button(bottom_frame, **btn_p, text="-", command=lambda: self.btn_click('-') )
        self.btnSub.grid(row=2, column=7)
        self.btn_add = tk.Button(bottom_frame, **btn_p, text="+", command=lambda: self.btn_click('+') )
        self.btn_add.grid(row=3, column=7)
        self.btn_sin = tk.Button(bottom_frame, **btn_p, text="sin", command=lambda: self.btn_click('fsin(') )
        self.btn_sin.grid(row=2, column=0)
        self.btn_cos = tk.Button(bottom_frame, **btn_p, text="cos", command=lambda: self.btn_click('fcos(') )
        self.btn_cos.grid(row=2, column=1)
        self.btn_tan = tk.Button(bottom_frame, **btn_p, text="tan", command=lambda: self.btn_click('ftan(') )
        self.btn_tan.grid(row=2, column=2)
        self.btn_log = tk.Button(bottom_frame, **btn_p, text="log", command=lambda: self.btn_click('log(') )
        self.btn_log.grid(row=2, column=3)
        self.btn_sini = tk.Button(bottom_frame, **btn_p, text=u"sin-\u00B9", command=lambda: self.btn_click('arcsin(') )
        self.btn_sini.grid(row=3, column=0)
        self.btn_cosi = tk.Button(bottom_frame, **btn_p, text=u"cos-\u00B9", command=lambda: self.btn_click('arccos(') )
        self.btn_cosi.grid(row=3, column=1)
        self.btn_tani = tk.Button(bottom_frame, **btn_p, text=u"tan-\u00B9", command=lambda: self.btn_click('arctan(') )
        self.btn_tani.grid(row=3, column=2)
        self.btn_ln = tk.Button(bottom_frame, **btn_p, text="ln", command=lambda: self.btn_click('log1p(') )
        self.btn_ln.grid(row=3, column=3)
        self.btn_fact = tk.Button(bottom_frame, **btn_p, text="n!", command=lambda: self.btn_click('factorial(') )
        self.btn_fact.grid(row=4, column=0)
        self.btn_pow = tk.Button(bottom_frame, **btn_p, text="x^y", command=lambda: self.btn_click('**') )
        self.btn_pow.grid(row=1, column=0)
        self.btn_deg = tk.Button(bottom_frame, **btn_p, text="Deg", command=self.convert_deg )
        self.btn_deg.grid(row=4, column=1)
        self.btn_rad = tk.Button(bottom_frame, **btn_p, text="Rad", command=self.convert_rad )
        self.btn_rad.grid(row=4, column=2)
        self.btn_ans = tk.Button(bottom_frame, **btn_p, text="Ans", command=self.answer )
        self.btn_ans.grid(row=4, column=3)
        self.btn_comma = tk.Button(bottom_frame, **btn_p, text=",", command=lambda: self.btn_click(',') )
        self.btn_comma.grid(row=4, column=4)
        self.btn_0 = tk.Button(bottom_frame, **btn_p, text="0", command=lambda: self.btn_click('0') )
        self.btn_0.grid(row=4, column=5)
        self.btn_dot = tk.Button(bottom_frame, **btn_p, text=".", command=lambda: self.btn_click('.') )
        self.btn_dot.grid(row=4, column=6)
        self.btn_equals = tk.Button(bottom_frame, **btn_p, text="=", command=self.btn_total )
        self.btn_equals.grid(row=4, column=7)
        #txt_display.bind("s", self.btn_click('fsin('))
        #self.btn_1.bind("1", self.btn_click(1))
        #self.btn_2.bind("2", self.btn_click(1))
        


    def btn_click(self,exp_v):
        if len(self.exp)>=100:
            self.exp=self.exp
            self.text_input.set(self.exp)
        else:
            self.exp=self.exp+str(exp_v)
            self.text_input.set(self.exp)

    def btn_clear(self):
        self.exp=self.exp[:-1]
        self.text_input.set(self.exp)

    def change_signs(self):
        self.exp=self.exp+'-'
        self.text_input.set(self.exp)


    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_rad["foreground"] = 'white'
        self.btn_deg["foreground"] = 'red'
 
    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        self.btn_rad["foreground"] = 'red'
        self.btn_deg["foreground"] = 'white'

    def answer(self, *args):
        self.answer=self.sum_up
        self.exp=self.exp + self.answer
        self.text_input.set(self.exp)

    def btn_total(self,*args):
        self.sum_up = str(eval(self.exp))
        #self.text_input.set(self.sum_up)
        global ans
        ans=round(float(self.sum_up),4)
        #print(type(ans))
        txt_display1.insert(2, ans)
        self.exp = self.sum_up


    def btn_clear_all(self, *args):
        PlaySound('Metal Gear Solid Alert - Sound Effect (HD) (128 kbps).wav', SND_FILENAME)

        if messagebox.askyesno("Confirm","Do you want to clear?"):

            self.exp=''
            #print(self.exp)
            self.text_input.set('')
            txt_display1.delete(0,'end')
            txt_display1.delete(0)
            

ans = 0
root=tk.Tk()
b=Calculator(root)
root.title("Scienctific calculator")
root.geometry("580x580+50+50")

root.resizable(False,False)
root.mainloop()