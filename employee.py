from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

import sqlite3
class employeeClass:
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
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        
        ##searchframe
        SearchFrame=LabelFrame(self.root,text="search employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)


        #------options
        
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("select","email","name","contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("times new roman",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search",command=self.search,font=("times new roman",15),bg="green",cursor="hand2").place(x=410,y=8,width=150,height=30)
        ##heading
        title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",15),bg="blue",fg="white").place(x=50,y=100,width=1000 )
        ###--content
        ##----ROW1
        lbl_empid=Label(self.root,text="EMP ID",font=("times new roman",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="GENDER",font=("times new roman",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="CONTACT",font=("times new roman",15),bg="white").place(x=750,y=150)
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15),bg="lightyellow").place(x=130,y=150,width=180)
       ##txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15),bg="white").place(x=450,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","MALE","FEMALE","OTHER"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=480,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=880,y=150,width=180)
        ##-------------row2
        lbl_name=Label(self.root,text="NAME",font=("times new roman",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="DOB",font=("times new roman",15),bg="white").place(x=350,y=190)
        lbl_doj=Label(self.root,text="DOJ",font=("times new roman",15),bg="white").place(x=750,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow").place(x=130,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="lightyellow").place(x=480,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),bg="lightyellow").place(x=880,y=190,width=180)
        ##-----row3
        lbl_email=Label(self.root,text="EMAIL",font=("times new roman",15),bg="white").place(x=50,y=230)
        lbl_pass=Label(self.root,text="PASSWORD",font=("times new roman",15),bg="white").place(x=350,y=230)
        lbl_utype=Label(self.root,text="UTYPE",font=("times new roman",15),bg="white").place(x=750,y=230)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="lightyellow").place(x=130,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("times new roman",15),bg="lightyellow").place(x=480,y=230,width=180)
        ##txt_utype=Entry(self.root,textvariable=self.var_utype,font=("times new roman",15),bg="lightyellow").place(x=880,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("ADMIN","EMPLOYEE"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=880,y=230,width=180)
        cmb_utype.current(0)
        ##----ROW4
        lbl_address=Label(self.root,text="ADD",font=("times new roman",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="SALARY",font=("times new roman",15),bg="white").place(x=550,y=270)
        self.txt_address=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_address.place(x=130,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),bg="lightyellow").place(x=650,y=270,width=180)
        ##====button===
        btn_add=Button(self.root,text="SAVE",command=self.add,font=("times new roman",15),bg="BLUE",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="UPDATE",command=self.update,font=("times new roman",15),bg="GREEN",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("times new roman",15),bg="RED",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman",15),bg="GRAY",cursor="hand2").place(x=860,y=305,width=110,height=28)
        

        ####=====EMP DETAILS===
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=340,relwidth=0.999,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="NAME") 
        self.EmployeeTable.heading("email",text="EMAIL ID")
        self.EmployeeTable.heading("gender",text="GENDER")
        self.EmployeeTable.heading("contact",text="CONTACT")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="PASSWORD")
        self.EmployeeTable.heading("utype",text="U TYPE")
        self.EmployeeTable.heading("address",text="ADDRESS")
        self.EmployeeTable.heading("salary",text="SALARY")

        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=90) 
        self.EmployeeTable.column("email",width=90)
        self.EmployeeTable.column("contact",width=90)
        self.EmployeeTable.column("gender",width=90)
        self.EmployeeTable.column("contact",width=90)
        self.EmployeeTable.column("dob",width=90)
        self.EmployeeTable.column("doj",width=90)
        self.EmployeeTable.column("pass",width=90)
        self.EmployeeTable.column("utype",width=90)
        self.EmployeeTable.column("address",width=90)
        self.EmployeeTable.column("salary",width=90)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
########################################################################3
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="": 
                messagebox.showerror("STOP!","Employee id is required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:

                    messagebox.showerror("HALT!","This employee ID already exists",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success☺","Employee added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        ##print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])
                    
    def update(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_emp_id.get()=="": 
                    messagebox.showerror("STOP!","Employee id is required",parent=self.root)
                else:
                    cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("HALT!","This employee ID is INVALID!",parent=self.root)
                    else:
                        cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0',END),
                            self.var_salary.get(),
                            self.var_emp_id.get(),
                        ))
                        con.commit()
                        messagebox.showinfo("Success☺","Employee Updated Successfully",parent=self.root)
                        self.show()

            except Exception as ex:
                messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="": 
                    messagebox.showerror("STOP!","Employee id is required",parent=self.root)
            else:
                    cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("HALT!","This employee ID is INVALID!",parent=self.root)
                    else:
                        op=messagebox.askyesno("CONFIRM?","This move is irreversible!",parent=self.root)
                        if op ==True:
                            cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),)) 
                            con.commit()
                            messagebox.showinfo("delete","Deleted successfully",parent=self.root)      
                            self.show()
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)
    def clear(self):        
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("ADMIN")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()



    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Enter parameter to search",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                     messagebox.showerror("Error","No data found!",parent=self.root) ##replace else------------------------------
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)

if __name__=="__main__":        
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()    