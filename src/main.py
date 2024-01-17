import tkinter
from PIL import Image, ImageTk
from dataclasses import dataclass

@dataclass
class box:
   num: int
   pos: int


BOX_R1 = box(1,10)
BOX_R1ACC = box(0,10)

BOX_R2 = box(3,40)
BOX_R2ACC = box(2,40)

BOX_VOUTmin = box(4,100)
BOX_VOUTtyp = box(5,100)
BOX_VOUTmax = box(6,100)

BOX_ERROR = box(7,130)

# クリックイベント
def btn_clear():
   i = 0
   while i <= 6:
      txt[i].delete(0, tkinter.END) # 削除の処理
      i = i + 1
def btn_click():
   # テキスト取得
   R1ACC = float(txt[BOX_R1ACC.num].get())
   R2ACC = float(txt[BOX_R2ACC.num].get())
   R1 = float(txt[BOX_R1.num].get())*1000
   R2 = float(txt[BOX_R2.num].get())*1000


   txt[BOX_ERROR.num].delete(0, tkinter.END)
   if (R2 > 400000):
      txt[BOX_ERROR.num].insert(0,"R2 shouldn't exceed 400kΩ.")


   R1INC = 1.0 + R1ACC/100.0
   R1DEC = 1.0 - R1ACC/100.0

   R2INC = 1.0 + R2ACC/100.0
   R2DEC = 1.0 - R2ACC/100.0

   VOUTtyp = 0.8*(1.0 + (R1)/(R2))
   VOUTmin = 0.8*(1.0 + (R1*R1DEC)/(R2*R2INC))
   VOUTmax = 0.8*(1.0 + (R1*R1INC)/(R2*R2DEC))

   i = BOX_VOUTmin.num
   while i <= BOX_VOUTmax.num:
      txt[i].delete(0, tkinter.END)
      i = i + 1

   txt[BOX_VOUTmin.num].insert(0,VOUTmin)
   txt[BOX_VOUTtyp.num].insert(0,VOUTtyp)
   txt[BOX_VOUTmax.num].insert(0,VOUTmax)

# 画面作成
tki = tkinter.Tk()
tki.geometry('500x200')
tki.title('TPS63070の電圧の計算機')
# ラベル
tkinter.Label(text='精度').place(x=210, y=BOX_R1ACC.pos)
tkinter.Label(text='%').place(x=320, y=BOX_R1ACC.pos)
tkinter.Label(text='精度').place(x=210, y=BOX_R2ACC.pos)
tkinter.Label(text='%').place(x=320, y=BOX_R2ACC.pos)

tkinter.Label(text='R1').place(x=30, y=BOX_R1.pos)
tkinter.Label(text='kΩ').place(x=150, y=BOX_R1.pos)
tkinter.Label(text='R2').place(x=30, y=BOX_R2.pos)
tkinter.Label(text='kΩ').place(x=150, y=BOX_R2.pos)

tkinter.Label(text='Vout').place(x=30, y=BOX_VOUTmin.pos)
#tkinter.Label(text='min').place(x=30, y=BOX_VOUTmin.pos)
#tkinter.Label(text='typ').place(x=30, y=BOX_VOUTtyp.pos)
#tkinter.Label(text='max').place(x=30, y=BOX_VOUTmax.pos)

tkinter.Label(text='Error').place(x=30, y=BOX_ERROR.pos)


tkinter.Label(text='<=').place(x=175, y=BOX_VOUTtyp.pos)
tkinter.Label(text='<=').place(x=295, y=BOX_VOUTtyp.pos)


tkinter.Label(text='V').place(x=420, y=BOX_VOUTtyp.pos)

# テキストボックス
txt = [0]*100

txt[BOX_R1.num] = tkinter.Entry(width=10)
txt[BOX_R1.num].place(x=80, y=BOX_R1.pos)
txt[BOX_R1ACC.num] = tkinter.Entry(width=10)
txt[BOX_R1ACC.num].place(x=250, y=BOX_R1ACC.pos)
txt[BOX_R2.num] = tkinter.Entry(width=10)
txt[BOX_R2.num].place(x=80, y=BOX_R2.pos)
txt[BOX_R2ACC.num] = tkinter.Entry(width=10)
txt[BOX_R2ACC.num].place(x=250, y=BOX_R2ACC.pos)


txt[BOX_VOUTmin.num] = tkinter.Entry(width=15)
txt[BOX_VOUTmin.num].place(x=80, y=BOX_VOUTmin.pos)
txt[BOX_VOUTtyp.num] = tkinter.Entry(width=15)
txt[BOX_VOUTtyp.num].place(x=200, y=BOX_VOUTtyp.pos)
txt[BOX_VOUTmax.num] = tkinter.Entry(width=15)
txt[BOX_VOUTmax.num].place(x=320, y=BOX_VOUTmax.pos)

txt[BOX_ERROR.num] = tkinter.Entry(width=60)
txt[BOX_ERROR.num].place(x=80, y=BOX_ERROR.pos)

# ボタン
btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=100, y=65)

btn = tkinter.Button(tki, text='クリア', command=btn_clear)
btn.place(x=200, y=65) # xが横,yが縦
# 画面をそのまま表示

tki.mainloop()