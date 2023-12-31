import os
import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")#window size
        self.root.title("Store Management System | ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING")
        self.root.config(bg="white")
        self.root.focus_force()
        self.var_invoice=StringVar()
        self.bill_list=[]

        ##title
        lbl_title=Label(self.root,text="--CUSTOMER BILLING--",font=("ALGERIAN",30),bg="pink",fg="blue").pack(side=TOP,fill = X,padx=10,pady=10)
        lbl_invoice=Label(self.root,text="Invoice no.",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)
        
        btn_search=Button(self.root,text="search",command=self.search,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)        
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",fg="white",cursor="hand2").place(x=490,y=100,width=120,height=28)
        ##====BILL LIST
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=20,y=140,width=200,height=330)

        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_List=Listbox(sales_Frame,font=("comic sans ms",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)
        ###======BILL AREA
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=330)
       

        lbl_title2=Label(bill_Frame,text="Bill Area",font=("ALGERIAN",20),bg="orange",fg="white").pack(side=TOP,fill = X)
        
        scrolly2=Scrollbar(sales_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,font=("comic sans ms",15),bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)


        ## image=========
        self.bill_photo=Image.open("IMAGES/billing.png")
        self.bill_photo=self.bill_photo.resize((450,300),Image.ANTIALIAS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root,image=self.bill_photo)
        lbl_image.place(x=700,y=160,width=395)

        self.show()
        #####################3
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)
            #print(os.listdir('bill'))
        for i in os.listdir('bill'):
                if i.split('.')[-1]== 'txt':
                    self.Sales_List.insert(END,i)
                    self.bill_list.append(i.split('.')[0])        
    
    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no required!",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Iṇvāl̥īḍ īnvoice",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)


if __name__=="__main__":        
    root=Tk()
    obj=salesClass(root)
    root.mainloop()         