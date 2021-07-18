# GUI translate
from tkinter import *
# จาก library tkinter ดึงความสามารถหลักออกมาให้หมด
from tkinter import ttk # ttk is theme of tk
### -------Google Translate------
from googletrans import Translator
translator = Translator()
   

GUI = Tk() # 1 สร้างหน้าต่างหลัก
GUI.geometry('500x300')   # กว้าง x สูง
GUI.title('โปรแกรมแปลภาษา by Ben')
# -----config-----------
FONT = ('Angsana New',15)

# -------Label----------

L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()


# ------- Entry(ช่องกรอกข้อความ)-----
v_vocab = StringVar() #กล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)

#--------- Button (ปุ่มแปล)-----
def Translate():
    vocab = v_vocab.get() #.get คือ ให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print( vocab + ':' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ':' + meaning.text)

B1 = ttk.Button(GUI,text='Translate',command=Translate)  # สร้างปุม
B1.pack(ipadx=20, ipady=10)  # show ปุ่มขึ้นมาวางจากบนลงล่าง
# -------Label----------

L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()
# -------Result-----------
v_result = StringVar()   #กล่องเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2, foreground='green')
R1.pack()



GUI.mainloop() # ทำให้โปรแกรมรันตลอดเวลาจนกว่าจะปิด (บรรทัดสุดท้าย)
