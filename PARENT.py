from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from sales import salesClass
import time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Store Managemant System | ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING")
        self.root.config(bg="white")
        #title
        self.icon_title=PhotoImage(file="IMAGES/shopping.png")
        title=Label(self.root,text="Store Management System",image=self.icon_title,compound=RIGHT,font=("agency fb",40,"bold"),bg="black",fg="white",anchor="e",padx=10).place(x=0,y=0,relwidth=1,height=70)
        #btn_logout=Button(self.root,text="Employee",command=self.employee,font=("bell mt",15,"bold"),bg="yellow",cursor = "hand2").place(x=300,y=120,height=130,width=300)## new button
       
        #btn lgt
        #btn_logout=Button(self.root,text="Employee",font=("bell mt",15,"bold"),bg="yellow",cursor = "hand2").place(x=20,y=10,height=50,width=150)
       
        #clk
        self.lbl_clock=Label(self.root,text="AIML\t\t Date:03-02-2023 \t\t TIME: 12:10",font=("agency fb",15,"bold"),bg="black",fg="white")
        self.lbl_clock.place(x=0,y=75,relwidth=1,height=20)

        
        
        self.MenuLogo=Image.open("IMAGES/CONTACT.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RAISED,bg="#FFC30F")
        LeftMenu.place(x=0,y=102,width=200,height=580)##height - 565

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        lbl_menu=Label(LeftMenu,text="=MENU=",font=("bell mt",20),bg="yellow").pack(side=TOP,fill=X)
        
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("bell mt",20,"bold"),bg="#C147E9",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("bell mt",20,"bold"),bg="#C147E9",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,font=("bell mt",20,"bold"),bg="#C147E9",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("bell mt",20,"bold"),bg="#C147E9",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        #btn_product=Button(LeftMenu,text="Product",font=("bell mt",20,"bold"),bg="#C147E9",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        #btn_exit=Button(LeftMenu,text="Exit",font=("bell mt",20,"bold"),bg="#C147E9",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        ##---EMP
        #self.lbl_employee=Label(self.root,text="EMPLOYEE\[0]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        #self.lbl_employee.place(x=300,y=120,height=150,width=300)
        ##---SUPP
        #self.lbl_supplier=Label(self.root,text="SUPPLIES\[0]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        #self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        ##---CATE
        #self.lbl_category=Label(self.root,text="CATEGORY\[0]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        #self.lbl_category.place(x=1000,y=120,height=150,width=300)
        ##---PRODU
        #self.lbl_product=Label(self.root,text="PRODUCT\[0]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        #self.lbl_product.place(x=300,y=300,height=150,width=300)
        ##---SALES
        #self.lbl_sales=Label(self.root,text="SALES\[0]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        #self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        #====new image
        self.im1=Image.open("snowimage2.png")
        self.im1=self.im1.resize((1145,620),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1)
        self.lbl_im1.place(x=200,y=95)
        lbl_footer=Label(self.root,text="STORE MANAGEMENT SYSTEM|DEVELOPERS 20AI050,051,053\n ISSUES IN SOFTWARE CONTACT SUBRAMANYA.K,SOORAJ ,SRIPADA  ",font=("calibri",10,"bold"),bg="black",fg="white").pack(side=BOTTOM,fill=X)
##--------------------------------- 
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
            
                   
        



if __name__=="__main__":        
    root=Tk()
    obj=IMS(root)
    root.mainloop()    
