import tkinter
from tkinter.ttk import *
tk = tkinter.Tk()
frame = Frame(tk)
frame.grid()
combobox = Combobox(frame,values = [u"ОДИН",u"ДВА",u"ТРИ"],height=3)
#frame - задает родительский виджет, на его территории будет располагаться Combobox
#values - задает набор значений, которые будут содержаться в Combobox изначально
#height - задает высоту выпадающего списка. Если число элементов списка меньше 11, то можно не задавать.
#Если не задано при колличестве элементов больше 10, то с правой стороны появится полоса прокрутки.
#Если в нашем примере задать значение height меньше трех, то с правой стороны появится полоса прокрутки,
#но она будет недоступна, а все элементы будут отображаться одновременно.
combobox.set(u"ОДИН")#спомощью этой строчки мы установим Combobox в значение ОДИН изначально
combobox.grid(column=0,row=0)#Позиционируем Combobox на форме
tk.mainloop()