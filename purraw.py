from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 
# from supplier import adminsupplier
# from rawmaterial import adminmaterial



class purchasematerial:
    def __init__(self,root):
        self.root=root
        self.root.title("Jewellery Management System")
        self.root.geometry("1200x550+230+220")
       
 #================== variables ========
        self.var_purchase_id=StringVar()
        self.var_bill_no=StringVar()
        self.var_purchase_date=StringVar()
        self.var_supplier_name=StringVar()
        self.var_material_id=StringVar()
        self.var_material_name=StringVar()
        self.var_weight=StringVar()
        self.var_total_amount=StringVar()


#========================Title========================
        rawpurpurtitle=Label(self.root,text="RAW MATERIAL PURCHASE MANAGEMENT",font=("times new roman",18,"bold"),bg="goldenrod",fg="black",bd=4)
        rawpurpurtitle.place(x=0,y=0,width=1550,height=40)
        
       
#==================Labelframe========================
        labelframepurraw=LabelFrame(self.root,bd=2,relief=RIDGE,text="ADD PURCHASE DETAILS",font=("time new roman",12,"bold"),padx=2)
        labelframepurraw.place(x=5,y=50,width=425,height=520)

 #============== labels and entries============
        
           #Purchase id

        purchaseid = Label(labelframepurraw,font=("arial",12,"bold"),text="Purchase Id",padx=2,pady=6)
        purchaseid.grid(row=0,column=0,sticky=W)
        txtpurchaseid=ttk.Entry(labelframepurraw,textvariable=self.var_purchase_id,font=("arial",12,"bold"),width=29)
        txtpurchaseid.grid(row=0,column=1)

        #Bill no
        
        billno = Label(labelframepurraw,font=("arial",12,"bold"),text="Bill No",padx=2,pady=6)
        billno.grid(row=1,column=0,sticky=W)
        txtbillno=ttk.Entry(labelframepurraw,textvariable=self.var_bill_no,font=("arial",12,"bold"),width=29)
        txtbillno.grid(row=1,column=1)

        
        #Purchase date

        purchasedate = Label(labelframepurraw,font=("arial",12,"bold"),text="Purchase Date",padx=2,pady=6)
        purchasedate.grid(row=2,column=0,sticky=W)
        txtpurchasedate=ttk.Entry(labelframepurraw,textvariable=self.var_purchase_date,font=("arial",12,"bold"),width=29)
        txtpurchasedate.grid(row=2,column=1)

    

         #Supplier name

        suppliername = Label(labelframepurraw,font=("arial",12,"bold"),text="Supplier Name",padx=2,pady=6)
        suppliername.grid(row=3,column=0,sticky=W)
        txtsuppliername=ttk.Entry(labelframepurraw,textvariable=self.var_supplier_name,font=("arial",12,"bold"),width=29)
        txtsuppliername.grid(row=3,column=1)

        #Material id

        materialid = Label(labelframepurraw,font=("arial",12,"bold"),text="Material Id",padx=2,pady=6)
        materialid.grid(row=4,column=0,sticky=W)
        txtmaterialid=ttk.Entry(labelframepurraw,textvariable=self.var_material_id,font=("arial",12,"bold"),width=29)
        txtmaterialid.grid(row=4,column=1)
       

        #Material name

        materialname = Label(labelframepurraw,font=("arial",12,"bold"),text="Material Name",padx=2,pady=6)
        materialname.grid(row=5,column=0,sticky=W)
        combo_material=ttk.Combobox(labelframepurraw,textvariable=self.var_material_name,font=("arial",12,"bold"),width=27)
        combo_material["value"]=("Gold","Silver","Nickel","Copper")
        combo_material.current(0)
        combo_material.grid(row=5,column=1)

          
         
        #Weight

        weight= Label(labelframepurraw,font=("arial",12,"bold"),text="Weight (gm)",padx=2,pady=6)
        weight.grid(row=6,column=0,sticky=W)
        txtweight=ttk.Entry(labelframepurraw,textvariable=self.var_weight,font=("arial",12,"bold"),width=29)
        txtweight.grid(row=6,column=1)

    

        
        #Total amount

        totalamount= Label(labelframepurraw,font=("arial",12,"bold"),text="Total Amount",padx=2,pady=6)
        totalamount.grid(row=7,column=0,sticky=W)
        txttotalamount=ttk.Entry(labelframepurraw,textvariable=self.var_total_amount,font=("arial",12,"bold"),width=29)
        txttotalamount.grid(row=7,column=1)

    

        #========== buttons ===================================

        button_framepurraw=Frame(labelframepurraw,bd=2,relief=RIDGE)
        button_framepurraw.place(x=31,y=370,width=350,height=32)

        button_add = Button(button_framepurraw,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=7)
        button_add.grid(row=0,column=0)

        button_update = Button(button_framepurraw,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        button_update.grid(row=0,column=1)

        button_delete = Button(button_framepurraw,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        button_delete.grid(row=0,column=2)
       
        button_reset = Button(button_framepurraw,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        button_reset.grid(row=0,column=3)

       

        #==================tableframe1========================

        tableframepurraw=LabelFrame(self.root,bd=2,relief=RIDGE,text="EXISTING RAW MATERIAL PURCHASE DETAILS",font=("time new roman",12,"bold"),padx=2)
        tableframepurraw.place(x=435,y=50,width=1000,height=520)

        labelsearchby= Label(tableframepurraw,font=("arial",12,"bold"),text="Search By:",bg="black",fg="goldenrod")
        labelsearchby.grid(row=0,column=0,sticky=W)

        combo_Search=ttk.Combobox(tableframepurraw,font=("arial",12,"bold"),width=28,state="randomly")
        combo_Search["value"]=("Bill No","Material Id","Purchase Date")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        txtSearch=ttk.Entry(tableframepurraw,font=("arial",12,"bold"),width=29)
        txtSearch.grid(row=0,column=2)

        

        button_search = Button(tableframepurraw,text="Search",font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        button_search.grid(row=0,column=3)

        button_showall = Button(tableframepurraw,text="Show All",font=("arial",12,"bold"),bg="black",fg="goldenrod",width=8)
        button_showall.grid(row=0,column=4)
       
         #========================Show Data Table=======================================

       
        details_tablepurraw=Frame(tableframepurraw,bd=2,relief=RIDGE)
        details_tablepurraw.place(x=0,y=50,width=995,height=445)

        scroll_x2=ttk.Scrollbar(details_tablepurraw,orient=HORIZONTAL)
        scroll_y2=ttk.Scrollbar(details_tablepurraw,orient=VERTICAL)

        self.Raw_Material_Purchase_Details_Table=ttk.Treeview(details_tablepurraw,column=("purchase_id","bill_no","purchase_date","supplier_name","material_id","material_name","weight",
                                                                    "total_amount"),xscrollcommand=scroll_x2.set)

        
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)

        scroll_x2.config(command=self.Raw_Material_Purchase_Details_Table.xview)
        scroll_y2.config(command=self.Raw_Material_Purchase_Details_Table.yview)
        
        self.Raw_Material_Purchase_Details_Table.heading("purchase_id",text="Purchase Id")
        self.Raw_Material_Purchase_Details_Table.heading("bill_no",text="Bill No")
        self.Raw_Material_Purchase_Details_Table.heading("purchase_date",text="Purchase Date")
        self.Raw_Material_Purchase_Details_Table.heading("supplier_name",text="Supplier Name")
        self.Raw_Material_Purchase_Details_Table.heading("material_id",text="Material Id")
        self.Raw_Material_Purchase_Details_Table.heading("material_name",text="Material Name")
        self.Raw_Material_Purchase_Details_Table.heading("weight",text="Weight (gm)")
        self.Raw_Material_Purchase_Details_Table.heading("total_amount",text="Total Amount")
    
        

        self.Raw_Material_Purchase_Details_Table["show"]="headings"

        self.Raw_Material_Purchase_Details_Table.column("purchase_id",width=100)
        self.Raw_Material_Purchase_Details_Table.column("bill_no",width=100)
        self.Raw_Material_Purchase_Details_Table.column("purchase_date",width=100)
        self.Raw_Material_Purchase_Details_Table.column("supplier_name",width=100)
        self.Raw_Material_Purchase_Details_Table.column("material_id",width=100)
        self.Raw_Material_Purchase_Details_Table.column("material_name",width=100)
        self.Raw_Material_Purchase_Details_Table.column("weight",width=100)
        self.Raw_Material_Purchase_Details_Table.column("total_amount",width=100)
      
        
         
    

    
        self.Raw_Material_Purchase_Details_Table.pack(fill=BOTH,expand=1)
        self.Raw_Material_Purchase_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        
         #=======================intializing database connection================
        self.initialize_database()

    def initialize_database(self):
        try:
            #===============mysql connector===========
            self.conn=mysql.connector.connect(
                host="localhost",
                user="akhilapottekkatt",
                password="7#M4M04SzV5K",
                database='jeweller'

            )
            self.cursor=self.conn.cursor()
            #=====================create table=====================
            create_table_purchasematerial = """
                                    CREATE TABLE IF NOT EXISTS purchasematerial(
                                       purchase_id INT PRIMARY KEY,
                                       bill_no VARCHAR(255) NOT NULL,
                                       purchase_date VARCHAR(255) NOT NULL,
                                       supplier_name VARCHAR(255) NOT NULL,
                                       material_id VARCHAR(255) NOT NULL,
                                       material_name VARCHAR(255) NOT NULL,
                                       weight VARCHAR(255) NOT NULL,
                                       total_amount VARCHAR(255) NOT NULL
                                      
                                      
                                    )"""   
            self.cursor.execute(create_table_purchasematerial)
            self.conn.commit()
        
        except mysql.connector.Error as e:
            messagebox.showerror("Database initilaization error",f"Error: {e}")

       


        

    def add_data(self):
      if self.var_bill_no.get()==""or self.var_purchase_date.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
           try:
             
              conn=mysql.connector.connect(host="localhost",user="akhilapottekkatt",password="7#M4M04SzV5K",database='jeweller')
              my_cursor=conn.cursor()
              my_cursor.execute("insert into purchasematerial values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                  self.var_purchase_id.get(),
                                                                  self.var_bill_no.get(),
                                                                  self.var_purchase_date.get(),
                                                                  self.var_supplier_name.get(),
                                                                  self.var_material_id.get(),
                                                                  self.var_material_name.get(),
                                                                  self.var_weight.get(),
                                                                  self.var_total_amount.get()
                                                                  
                                                                 ))
              conn.commit()
              self.fetch_data()
              conn.close()

         
              messagebox.showinfo("Success","Purchase has been added",parent=self.root)
           except Exception as es:
              messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    

    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",user="akhilapottekkatt",password="7#M4M04SzV5K",database='jeweller')
       my_cursor=conn.cursor()
       my_cursor.execute("select * from purchasematerial")
       rows=my_cursor.fetchall()

       if len(rows)!=0:
             self.Raw_Material_Purchase_Details_Table.delete(*self.Raw_Material_Purchase_Details_Table.get_children())
             for i in rows:
                 self.Raw_Material_Purchase_Details_Table.insert("",END,values=i)
             conn.commit()
       conn.close()

    def get_cursor(self,event=""):
         cursor_row=self.Raw_Material_Purchase_Details_Table.focus()
         content=self.Raw_Material_Purchase_Details_Table.item(cursor_row)
         row=content["values"]

         self.var_purchase_id.set(row[0]),  
         self.var_bill_no.set(row[1]),                                                       
         self.var_purchase_date.set(row[2]),                                                      
         self.var_supplier_name.set(row[3]),
         self.var_material_id.set(row[4]),                                                   
         self.var_material_name.set(row[5]),                                                                                                                                               
         self.var_weight.set(row[6]),                                                                                             
         self.var_total_amount.set(row[7])
  
    def update(self):
        if self.var_material_name.get()=="":
            messagebox.showerror("Error","please enter number of item",parent=self.root)

        else:
           conn=mysql.connector.connect(host="localhost",user="akhilapottekkatt",password="7#M4M04SzV5K",database='jeweller')
           my_cursor=conn.cursor()
           my_cursor.execute("update purchasematerial set bill_no=%s, purchase_date=%s,supplier_name=%s,material_id=%s,material_name=%s,weight=%s,total_amount=%s where purchase_id=%s",(
                                                                                                                                 
                                                                                                                                 self.var_bill_no.get(),
                                                                                                                                 self.var_purchase_date.get(),
                                                                                                                                 self.var_supplier_name.get(),
                                                                                                                                 self.var_material_id.get(),
                                                                                                                                 self.var_material_name.get(),
                                                                                                                                 self.var_weight.get(),
                                                                                                                                 self.var_total_amount.get(),
                                                                                                                                 self.var_purchase_id.get()
                                                                  
                                                                                                                    ))

           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Update"," purchase details are updated successfully",parent=self.root)     

    def delete(self):
        delete=messagebox.askyesno("Jewellery managemnt system","do you want to delete this purchase details", parent=self.root)
        
        if delete>0:
             conn=mysql.connector.connect(host="localhost",user="akhilapottekkatt",password="7#M4M04SzV5K",database='jeweller')
             my_cursor=conn.cursor()
             query="delete from purchasematerial where purchase_id=%s"
             value=(self.var_purchase_id.get(),)
             my_cursor.execute(query,value)

        else:
             if not delete:
                 return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
         self.var_purchase_id.set(""),
         self.var_bill_no.set(""),                                                       
         self.var_purchase_date.set(""),                                                    
         self.var_supplier_name.set(""),    
         self.var_material_id.set(""),                                                
         self.var_material_name.set(""),                                                                                                                                              
         self.var_weight.set(""),                                                                                             
         self.var_total_amount.set("")                                            
                                              
         



if __name__=="__main__":
    root=Tk()
    obj=purchasematerial(root)

    root.mainloop()