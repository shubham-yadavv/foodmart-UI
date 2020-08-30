from tkinter import *
from tkinter.ttk import *
from tabulate import tabulate
def restaurant():
    import pymysql
    mydb = pymysql.connect(
      host="localhost",
      user="root",
      passwd="ysystem",
      database="bill"
      )
    mycursor = mydb.cursor()
    mycursor.execute("create table tab3(items varchar(30),amount int)")
    
    def procbill():
        def destroytab3():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()   
            mycursor.execute("drop table tab3")
            
            mydb.commit() 
            
        def showbill():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()   
            mycursor.execute("SELECT * from tab3")
            mybill=mycursor.fetchall()
            print(tabulate(mybill,headers=['items','amount'],tablefmt='psql'))
            
            mycursor.execute("select sum(amount)from tab3")
            mybill=mycursor.fetchall()
            print(tabulate(mybill,headers=['TOTAL AMOUNT'],tablefmt='psql'))
            
            
            mydb.commit()            
       
        root5=Toplevel()
        root5.title("BILL")
        root5.geometry('500x500')
        button=Button(root5, text="SHOW BILL ",command= showbill)
        button.place(x=100,y=60)
        
        lbl=Label(root5,text="METHOD OF PAYMENT",font=("Algerian",16))
        lbl.place(x=100,y=100)
        r1=Radiobutton(root5,text="Cash",value=1)
        r1.place(x=100,y=150)
        r2=Radiobutton(root5,text="Credit card",value=2)
        r2.place(x=100,y=200)
        r3=Radiobutton(root5,text="debit card",value=3)
        r3.place(x=100,y=250)
        r4=Radiobutton(root5,text="Net banking",value=4)
        r4.place(x=100,y=300)
        
        buttonpay=Button(root5, text="proceed to pay ",command=destroytab3 )
        buttonpay.place(x=400,y=400)
        
        style.configure('W.TButton', font =
			('calibri', 10, 'bold', 'underline'), 
				foreground = 'red') 
        buttondestroy=Button(root5, text="Quit ",style='W.TButton',command=root.destroy )
        buttondestroy.place(x=400,y=40)
        
        root5.mainloop()
        
        
        
        
    def pizzahut():
        def insert_vegpizza():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()           
            sql = "INSERT INTO tab3 (items,amount) VALUES (%s, %s)"
            val = ("Veg pizza", 200)
            mycursor.execute(sql, val)
            mydb.commit()
            
        def insert_nonvegpizza():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()           
            sql = "INSERT INTO tab3 (items,amount) VALUES (%s, %s)"
            val = ("Non Veg pizza", 300)
            mycursor.execute(sql, val)
            mydb.commit()
     
     
     
     
     
        root3=Toplevel()
        root3.title("PIZZA HUT")
        root3.geometry('1000x1000')
        photoveg = PhotoImage(file = r"assets/food/Veg_Extravaganz.png")
        photoimageveg = photoveg.subsample(2,2)
        buttonv=Button(root3,text =" Veg Pizza\n\n Rs.200  ",image = photoimageveg,compound=LEFT,command =insert_vegpizza)
        buttonv.place(x=50,y=60)
        photononveg = PhotoImage(file = r"assets/food/Non-Veg_Supreme.png")
        photoimagenonveg = photononveg.subsample(2,2)
        buttonnv=Button(root3,text =" Non Veg Pizza\n\n Rs.300  ",image = photoimagenonveg,compound=LEFT,command =insert_nonvegpizza)
        buttonnv.place(x=50,y=250)
              
        buttonok = Button(root3, text = 'ok', style = 'W.TButton', command = root3.destroy) 
        buttonok.place(x=550,y=550)
        
        root3.mainloop()
        
    def macd():
        def insert_vegburger():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()           
            sql = "INSERT INTO tab3 (items,amount) VALUES (%s, %s)"
            val = ("Veg burger", 100)
            mycursor.execute(sql, val)
            mydb.commit()
            
        def insert_nonvegburger():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()           
            sql = "INSERT INTO tab3 (items,amount) VALUES (%s, %s)"
            val = ("Non Veg burger", 150)
            mycursor.execute(sql, val)
            mydb.commit()
            
            
            
        root4=Toplevel()
        root4.title("MC DONALDS")
        root4.geometry('1000x1000')
        photobveg = PhotoImage(file = r"assets/food/veg burger.png")
        photoimagebveg = photobveg.subsample(2,2)
        buttonbv=Button(root4,text =" Veg burger\n\n Rs.100  ",image = photoimagebveg,compound=LEFT,command =insert_vegburger)
        buttonbv.place(x=50,y=60)
        photobnonveg = PhotoImage(file = r"assets/food/non veg burger.png")
        photoimagebnonveg = photobnonveg.subsample(2,2)
        buttonbnv=Button(root4,text =" Non Veg burger\n\n Rs.150  ",image = photoimagebnonveg,compound=LEFT,command =insert_nonvegburger)
        buttonbnv.place(x=50,y=250)
        
        buttonok = Button(root4, text = 'ok', style = 'W.TButton', command = root4.destroy) 
        buttonok.place(x=550,y=550)
        
        root4.mainloop()
        
        
    def subway():
        def insert_paneersub():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()           
            sql = "INSERT INTO tab3 (items,amount) VALUES (%s, %s)"
            val = ("Paneersub", 110)
            mycursor.execute(sql, val)
            mydb.commit()
        
        def insert_chickensub():
            import pymysql
            mydb = pymysql.connect(
                    host="localhost",
                    user="root",
                    passwd="ysystem",
                    database="bill"
                    )
            mycursor = mydb.cursor()           
            sql = "INSERT INTO tab3 (items,amount) VALUES (%s, %s)"
            val = ("Chicken sub", 140)
            mycursor.execute(sql, val)
            mydb.commit()
            
            
            
        root5=Toplevel()
        root5.title("SUBWAY")
        root5.geometry('1000x1000')
        photopaneersub = PhotoImage(file = r"assets/food/paneersub.png")
        photoimagepaneersub = photopaneersub.subsample(2,2)
        buttonpaneersub=Button(root5,text =" Paneer sub\n\n Rs.110  ",image = photoimagepaneersub,compound=LEFT,command =insert_paneersub)
        buttonpaneersub.place(x=50,y=60)
        photochickensub = PhotoImage(file = r"assets/food/chickensub.png")
        photoimagechickensub = photochickensub.subsample(2,2)
        buttonchickensub=Button(root5,text ="Chicken sub\n\n Rs.140  ",image = photoimagechickensub,compound=LEFT,command =insert_chickensub)
        buttonchickensub.place(x=50,y=200)
        
        buttonok = Button(root5, text = 'ok', style = 'W.TButton', command = root5.destroy) 
        buttonok.place(x=550,y=550)
        
        root5.mainloop()
    
    root2=Toplevel()
    root2.title("RESTAURANTS")
    root2.geometry('1000x1000') 
    
    photoMcD = PhotoImage(file = r"assets/food/McD.png")
    photoimageMcD = photoMcD.subsample(2,2)  
    photoPzH = PhotoImage(file = r"assets/food/PzH.png")
    photoimagePzH= photoPzH.subsample(2,2)
    photosubway = PhotoImage(file = r"assets/food/subway.png")
    photoimagesubway= photosubway.subsample(2,2)
    
    button1=Button(root2, image = photoimageMcD,command =macd)
    button1.place(x=500,y=260)
    button2=Button(root2, image = photoimagePzH,command=pizzahut)
    button2.place(x=700,y=260)
    button3=Button(root2, text="PROCEED TO BILL",command =procbill)
    button3.place(x=800,y=560)    
    button4=Button(root2, image = photoimagesubway,command =subway)
    button4.place(x=500,y=420)    
    
    root2.mainloop()




root = Tk() 
root.title("Y/A FOODMART")
root.geometry('1000x1000') 

 


photoCUS = PhotoImage(file = r"assets/food/food.png")

photoimageCUS = photoCUS.subsample(6,6)  

 
button1=Button(root, image = photoimageCUS,command=restaurant)
button1.place(x=700,y=260)


root.mainloop() 