from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")#window size
        self.root.title("Store Management System | ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING")
        self.root.config(bg="white")
        self.root.focus_force()
        ##===VARIABLE==
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        ##=========title
        lbl_title=Label(self.root,text="manage product category",font=("ALGERIAN",30),bg="pink",fg="blue").pack(side=TOP,fill = X,padx=10,pady=10)

        lbl_name=Label(self.root,text="Enter Category Name",font=("comic sans ms",15),bg="white",fg="black").place(x=20,y=62)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("comic sans ms",15),bg="lightyellow",fg="black").place(x=20,y=95,width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("comic sans ms",15),bg="green",fg="black",cursor="hand2").place(x=330,y=95,width=100,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("comic sans ms",15),bg="red",fg="black",cursor="hand2").place(x=435,y=95,width=100,height=30)

        ###===category details
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=580,y=65,relwidth=0.47,height=430)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        
        self.category_table.heading("cid",text="CID")
        self.category_table.heading("name",text="NAME") 
    
        self.category_table["show"]="headings"
        
        self.category_table.column("cid",width=90)
        self.category_table.column("name",width=90) 
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)
        

        ##===images
        ##self.im1=Image.open("IMAGES/app-development.png")
        ##self.im1=self.im1.resize((500,200),Image.ANTIALIAS)
        ##self.im1=ImageTk.PhotoImage(self.im1)

        ##self.lbl_im1=Label(self.root,image=self.im1)
        ##self.lbl_im1.place(x=50,y=220)
        ####=======images=
        self.im1=Image.open("IMAGES/app-development.png")
        self.im1=self.im1.resize((450,350),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1)
        self.lbl_im1.place(x=60,y=135)
        self.show()
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="": 
                messagebox.showerror("STOP!","Category is required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("HALT!","This Category already exists",parent=self.root)
                else:
                    cur.execute("Insert into category(name)values(?)",(
                        self.var_name.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success☺","Category added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)
    
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        ##print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="": 
                    messagebox.showerror("STOP!","Select Item from table",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid.",parent=self.root)
                else:      
                    op=messagebox.askyesno("confirm","This move can not be reversed!",parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Category deleted!",parent=self.root)
                        #self.clear()
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Whoa,Hold on!",f"ERROR DUE TO :{str(ex)}",parent=self.root)
            
if __name__=="__main__":        
    root=Tk()
    obj=categoryClass(root)
    root.mainloop() 