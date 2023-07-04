from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Store Management System | ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING")
        self.root.config(bg="white")
        self.root.focus_force()
        ##
        #all variable===
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        
        ##searchframe
        ##SearchFrame=LabelFrame(self.root,text="search ITEM by invoice",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        ##SearchFrame.place(x=250,y=20,width=600,height=70)


        #------options
        
        lbl_search=Label(self.root,text="Search by invoice no",bg="white",font=("times new roman",15))
        lbl_search.place(x=550,y=450)
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("times new roman",15),bg="lightyellow").place(x=700,y=450,height=31)
        btn_search=Button(self.root,text="search",command=self.search,font=("times new roman",15),bg="green",cursor="hand2").place(x=911,y=450,width=150,height=30)
        ##heading
        title=Label(self.root,text="SUPPLIER DETAILS",font=("times new roman",15),bg="blue",fg="white").place(x=50,y=10,width=1000 )
        ###--content
        ##----ROW1
        lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("times new roman",15),bg="white").place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15),bg="lightyellow").place(x=180,y=80,width=180)
       ##txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15),bg="white").place(x=450,y=150,width=180)
        ##-------------row2
        lbl_name=Label(self.root,text="NAME",font=("times new roman",15),bg="white").place(x=50,y=130)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow").place(x=180,y=130,width=180)
        ##-----row3
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=50,y=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=180,y=180,width=180)
        
        ##txt_utype=Entry(self.root,textvariable=self.var_utype,font=("times new roman",15),bg="lightyellow").place(x=880,y=230,width=180)
        
        ##----ROW4
        lbl_desc=Label(self.root,text="Description",font=("times new roman",15),bg="white").place(x=50,y=230)
        self.txt_desc=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=230,width=300,height=70)
        #txt_salary=Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),bg="lightyellow").place(x=650,y=270,width=180)
        ##====button===
        btn_add=Button(self.root,text="SAVE",command=self.add,font=("times new roman",15),bg="green",cursor="hand2").place(x=100,y=350,width=110,height=28)
        #btn_update=Button(self.root,text="UPDATE",command=self.update,font=("times new roman",15),bg="blue",cursor="hand2").place(x=250,y=400,width=110,height=28)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("times new roman",15),bg="RED",cursor="hand2").place(x=100,y=400,width=110,height=28)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman",15),bg="GRAY",cursor="hand2").place(x=250,y=350,width=110,height=28)
        

        ####=====EMP DETAILS===
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=550,y=40,relwidth=0.5,height=400)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.heading("invoice",text="INVOICE")
        self.supplierTable.heading("name",text="NAME") 
        self.supplierTable.heading("contact",text="CONTACT")
        self.supplierTable.heading("desc",text="DESC")

        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=90) 
        self.supplierTable.column("contact",width=90)
        self.supplierTable.column("desc",width=90)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
########################################################################3
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": 
                messagebox.showerror("STOP!","Invoice is required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:

                    messagebox.showerror("HALT!","This Invoice already exists",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc)values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                        ))
                    con.commit()
                    messagebox.showinfo("Success☺","Supplier added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        ##print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])
                    
    def update(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_sup_invoice.get()=="": 
                    messagebox.showerror("STOP!","Supplier id is required",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("HALT!","This employee ID is INVALID!",parent=self.root)
                    else:
                        cur.execute("update supplier set name=?,contact=?,desc=?, invoice=?",(
                            self.var_name.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0',END),
                            self.var_sup_invoice.get(),
                        ))
                        con.commit()
                        messagebox.showinfo("Success☺"," SUPPLIER Updated Successfully",parent=self.root)
                        self.show()

            except Exception as ex:
                messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": 
                    messagebox.showerror("STOP!","invoice no is required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else:      
                    op=messagebox.askyesno("confirm","This move can not be reversed!",parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Supplier deleted!",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)
    def clear(self):        
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()



    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Enter Invoice to search",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No data found!",parent=self.root) ##replace else------------------------------
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)

if __name__=="__main__":        
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()    