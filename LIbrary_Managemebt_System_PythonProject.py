from tkinter import ttk
from tkinter import *
import mysql.connector
import tkinter
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x900+0+0")

        lbltitle = Label(self.root,bd=20,relief=GROOVE,text='Library Management System',bg='powder blue',fg='white',font=('times new roman',50,'bold'))
        lbltitle.pack(side=TOP,fill=X)

        frame = Frame(self.root,bd=12,relief=GROOVE,bg='powder blue')
        frame.place(x=0,y=120,width=1550,height=400)

        # =================================== Variable =======================================================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()





        # =============================== DataFrame for Membership ============================================

        DataFrameLeft = LabelFrame(frame,bd=6,relief=RIDGE,text='Library Membership Details',font=('times new roman',12,'bold'),bg='powder blue',fg='black',padx=2,pady=6)
        DataFrameLeft.place(x=4,y=0,width=900,height=370)

        lblmembertype = Label(DataFrameLeft,text='Member Type',font=('times new roman',12,'bold'),bg='powder blue',fg='black',padx=2,pady=6)
        lblmembertype.grid(row=0,column=0)
        membertype = ttk.Combobox(DataFrameLeft,font=('times new roman',12,'bold'),textvariable=self.member_var,state='readonly',width=25)
        membertype['values'] = ('Admin staff','Student','Lecturer')
        membertype.current(0)
        membertype.grid(row=0,column=1)

        lblprnno = Label(DataFrameLeft,text='PRN No.',bg='powder blue',fg='black',font=('times new roman',12,'bold'))
        lblprnno.grid(row=1,column=0)
        prnno = Entry(DataFrameLeft,textvariable=self.prn_var,font=('arial',12,'bold'),width=24)
        prnno.grid(row=1,column=1)

        lblid = Label(DataFrameLeft, text='ID No.', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'),padx=2,pady=6)
        lblid.grid(row=2, column=0)
        id = Entry(DataFrameLeft,textvariable=self.id_var,font=('arial', 12, 'bold'), width=24)
        id.grid(row=2, column=1)

        lblfirstname = Label(DataFrameLeft, text='First Name', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'),padx=2,pady=6)
        lblfirstname.grid(row=3, column=0)
        firstname = Entry(DataFrameLeft,textvariable=self.firstname_var, font=('arial', 12, 'bold'), width=24)
        firstname.grid(row=3, column=1)

        lbllastname = Label(DataFrameLeft, text='Last Name', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'),padx=2,pady=6)
        lbllastname.grid(row=4, column=0)
        lastname = Entry(DataFrameLeft,textvariable=self.lastname_var, font=('arial', 12, 'bold'), width=24)
        lastname.grid(row=4, column=1)

        lbladdress1 = Label(DataFrameLeft, text='Address1', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'),padx=2,pady=6)
        lbladdress1.grid(row=5, column=0)
        address1 = Entry(DataFrameLeft,textvariable=self.address1_var, font=('arial', 12, 'bold'), width=24)
        address1.grid(row=5, column=1)

        lbladdress2 = Label(DataFrameLeft, text='Address2', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'),padx=2,pady=6)
        lbladdress2.grid(row=6, column=0)
        address2 = Entry(DataFrameLeft,textvariable=self.address2_var, font=('arial', 12, 'bold'), width=24)
        address2.grid(row=6, column=1)

        lblpostcode = Label(DataFrameLeft, text='Post Code', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'),padx=2,pady=6)
        lblpostcode.grid(row=7, column=0)
        postcode = Entry(DataFrameLeft,textvariable=self.postcode_var, font=('arial', 12, 'bold'), width=24)
        postcode.grid(row=7, column=1)

        lblmobile = Label(DataFrameLeft, text='Mobile', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'),padx=2,pady=6)
        lblmobile.grid(row=8, column=0)
        mobile = Entry(DataFrameLeft,textvariable=self.mobile_var, font=('arial', 12, 'bold'), width=24)
        mobile.grid(row=8, column=1)

        lblbookid = Label(DataFrameLeft, text='Book Id.', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lblbookid.grid(row=0, column=2)
        bookid = Entry(DataFrameLeft,textvariable=self.bookid_var, font=('arial', 12, 'bold'), width=24)
        bookid.grid(row=0, column=3)

        lblbooktitle = Label(DataFrameLeft, text='Book Title', bg='powder blue', fg='black',
                          font=('times new roman', 12, 'bold'))
        lblbooktitle.grid(row=1, column=2)
        booktitle = Entry(DataFrameLeft,textvariable=self.booktitle_var,font=('arial', 12, 'bold'), width=24)
        booktitle.grid(row=1, column=3)

        lblauther = Label(DataFrameLeft, text='Auther Name', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lblauther.grid(row=2, column=2)
        auther = Entry(DataFrameLeft,textvariable=self.auther_var, font=('arial', 12, 'bold'), width=24)
        auther.grid(row=2, column=3)

        lbldateborrowed = Label(DataFrameLeft, text='Date Borrowed', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lbldateborrowed.grid(row=3, column=2)
        dateborrowed = Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=('arial', 12, 'bold'), width=24)
        dateborrowed.grid(row=3, column=3)

        lblduedate = Label(DataFrameLeft, text='Due Date', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lblduedate.grid(row=4, column=2)
        duedate = Entry(DataFrameLeft,textvariable=self.datedue_var, font=('arial', 12, 'bold'), width=24)
        duedate.grid(row=4, column=3)

        lbldaysonbook = Label(DataFrameLeft, text='Days On Book', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lbldaysonbook.grid(row=5, column=2)
        daysonbook = Entry(DataFrameLeft,textvariable=self.daysonbook_var, font=('arial', 12, 'bold'), width=24)
        daysonbook.grid(row=5, column=3)

        lbllatereturnfine = Label(DataFrameLeft, text='Late Return Fine', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lbllatereturnfine.grid(row=6, column=2)
        latereturnfine = Entry(DataFrameLeft,textvariable=self.latereturnfine_var, font=('arial', 12, 'bold'), width=24)
        latereturnfine.grid(row=6, column=3)

        lbldateoverdue = Label(DataFrameLeft, text='Date Over Due', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lbldateoverdue.grid(row=7, column=2)
        dateoverdue = Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=('arial', 12, 'bold'), width=24)
        dateoverdue.grid(row=7, column=3)

        lblfinalprice = Label(DataFrameLeft, text='Actual Price', bg='powder blue', fg='black',
                         font=('times new roman', 12, 'bold'))
        lblfinalprice.grid(row=8, column=2)
        finalprice = Entry(DataFrameLeft,textvariable=self.finalprice_var, font=('arial', 12, 'bold'), width=24)
        finalprice.grid(row=8,column=3)





        # ============================= Button Frame =========================================================
        btnframe = Frame(self.root,bd=12,relief=GROOVE,bg='powder blue')
        btnframe.place(x=0,y=520,width=1550,height=80)

        addbtn = Button(btnframe,command=self.add_data,bg='grey',fg='powder blue',text='ADD DATA',font=('times new roman',12,'bold'),width=24)
        addbtn.pack(side=LEFT,padx=20)

        showbtn = Button(btnframe,command=self.showdata, bg='grey', fg='powder blue', text='SHOW DATA', font=('times new roman', 12, 'bold'),width=24)
        showbtn.pack(side=LEFT, padx=20)

        updatebtn = Button(btnframe,command=self.updatedata, bg='grey', fg='powder blue', text='UPDATE DATA',width=24,
                           font=('times new roman', 12, 'bold'))
        updatebtn.pack(side=LEFT, padx=20)

        deletebtn = Button(btnframe,command=self.delete, bg='grey', fg='powder blue', text='DELETE DATA',width=24,
                           font=('times new roman', 12, 'bold'))
        deletebtn.pack(side=LEFT, padx=20)

        resetbtn = Button(btnframe,command=self.resetdata,bg='grey', fg='powder blue', text='RESET DATA',width=24,
                           font=('times new roman', 12, 'bold'))
        resetbtn.pack(side=LEFT, padx=20)

        exitbtn = Button(btnframe,command=self.iExit, bg='grey', fg='powder blue', text='EXIT',width=24,
                           font=('times new roman', 12, 'bold'))
        exitbtn.pack(side=LEFT, padx=20)

        # =============================== DataFrame for Book Deatails ==========================================
        DataFrameRight = LabelFrame(frame,bd=6,relief=RIDGE,text='Book Details',bg='powder blue',fg='black',font=('arial',12,'bold'))
        DataFrameRight.place(x=910,y=0,width=600,height=370)

        self.txtbox = Text(DataFrameRight,font=('arial',12,'bold'),width=32,height=18)
        self.txtbox.grid(row=0,column=2,padx=4)

        booklist = ['Book1','Book2','Book3','Book4','Book5','Book6','Book7','Book8','Book9','Book10','Book11','Book12','Book13','Book14','Book15','Book16','Book17','Book18','Book19','Book20']

        def selectbook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if (x=='Book1'):
                self.bookid_var.set("BKID1111")
                self.booktitle_var.set("Book - 1")
                self.auther_var.set("Auther - 1")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif (x=='Book2'):
                self.bookid_var.set("BKID1112")
                self.booktitle_var.set("Book - 2")
                self.auther_var.set("Auther - 2")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.600")

            elif (x=='Book3'):
                self.bookid_var.set("BKID1113")
                self.booktitle_var.set("Book - 3")
                self.auther_var.set("Auther - 3")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.600")

            elif (x=='Book4'):
                self.bookid_var.set("BKID1114")
                self.booktitle_var.set("Book - 4")
                self.auther_var.set("Auther - 4")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.900")

            elif (x == 'Book5'):
                self.bookid_var.set("BKID1115")
                self.booktitle_var.set("Book - 5")
                self.auther_var.set("Auther - 5")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book6'):
                self.bookid_var.set("BKID1116")
                self.booktitle_var.set("Book - 6")
                self.auther_var.set("Auther - 6")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book7'):
                self.bookid_var.set("BKID1117")
                self.booktitle_var.set("Book - 7")
                self.auther_var.set("Auther - 7")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book8'):
                self.bookid_var.set("BKID1118")
                self.booktitle_var.set("Book - 8")
                self.auther_var.set("Auther - 8")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book9'):
                self.bookid_var.set("BKID1119")
                self.booktitle_var.set("Book - 9")
                self.auther_var.set("Auther - 9")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book10'):
                self.bookid_var.set("BKID1120")
                self.booktitle_var.set("Book - 10")
                self.auther_var.set("Auther - 10")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book11'):
                self.bookid_var.set("BKID1121")
                self.booktitle_var.set("Book - 11")
                self.auther_var.set("Auther - 11")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book12'):
                self.bookid_var.set("BKID1122")
                self.booktitle_var.set("Book -12")
                self.auther_var.set("Auther - 12")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book13'):
                self.bookid_var.set("BKID1123")
                self.booktitle_var.set("Book - 13")
                self.auther_var.set("Auther - 13")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book14'):
                self.bookid_var.set("BKID1124")
                self.booktitle_var.set("Book - 14")
                self.auther_var.set("Auther - 14")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book15'):
                self.bookid_var.set("BKID1125")
                self.booktitle_var.set("Book - 15")
                self.auther_var.set("Auther - 15")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book16'):
                self.bookid_var.set("BKID1126")
                self.booktitle_var.set("Book - 16")
                self.auther_var.set("Auther - 16")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book17'):
                self.bookid_var.set("BKID1127")
                self.booktitle_var.set("Book - 17")
                self.auther_var.set("Auther - 17")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book18'):
                self.bookid_var.set("BKID1128")
                self.booktitle_var.set("Book - 18")
                self.auther_var.set("Auther - 18")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book19'):
                self.bookid_var.set("BKID1129")
                self.booktitle_var.set("Book - 19")
                self.auther_var.set("Auther - 19")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif (x == 'Book20'):
                self.bookid_var.set("BKID1130")
                self.booktitle_var.set("Book - 20")
                self.auther_var.set("Auther - 20")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1.strftime('%d/%m/%y'))
                self.datedue_var.set(d3.strftime('%d/%m/%y'))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

        listscrollbar = Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0, column=1, sticky='ns')



        listbox = Listbox(DataFrameRight,font=('arial',12,'bold'),width=20,height=16)

        listbox.bind("<<ListboxSelect>>",selectbook)
        listbox.grid(row=0,column=0,padx=4)



        listscrollbar.config(command=listbox.yview)

        for item in booklist:
            listbox.insert(END,item)





        # ==================================== Information Frame =============================================
        framedetails = Frame(self.root,bd=12,relief=GROOVE,bg='powder blue')
        framedetails.place(x=0,y=600,width=1540,height=240)

        tableframe = Frame(framedetails,bd=6,relief=GROOVE,bg='powder blue')
        tableframe.place(x=10,y=10,width=1500,height=200)

        xscroll = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(tableframe, orient=VERTICAL)


        self.library_table = ttk.Treeview(tableframe, column=('membertype', 'prnno','id','firstname', 'lastname', 'address1', 'address2', 'postid', 'mobile', 'bookid',
        'booktitle', 'auther', 'dateborrowed', 'datedue', 'days', 'latereturnfine', 'dateoverdue', 'finalprice'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("id", text="ID No.")

        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postid", text="Post Id")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="auther")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.fetch_data()
        self.library_table.bind('<ButtonRelease-1>', self.get_cursor)

        self.library_table.pack(fill=BOTH,expand=1)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



    def add_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Md@mysql444',database='lms')
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get(),
                                                                                                                ))
        conn.commit()

        self.fetch_data()

        conn.close()

        messagebox.showinfo("Successful","Member Has Been Inserted Successfully.")



    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Md@mysql444',database='lms')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows) !=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def updatedata(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Md@mysql444',database='lms')
        my_cursor=conn.cursor()
        my_cursor.execute("update library set member=%s,id=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,postid=%s,mobile=%s,bookid=%s,booktitle=%s,auther=%s,dateborrowed=%s,datedue=%s,days=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where prnno=%s",(
                                                                                                                                                                                                                                                                              self.member_var.get(),
                                                                                                                                                                                                                                                                              self.id_var.get(),
                                                                                                                                                                                                                                                                              self.firstname_var.get(),
                                                                                                                                                                                                                                                                              self.lastname_var.get(),
                                                                                                                                                                                                                                                                              self.address1_var.get(),
                                                                                                                                                                                                                                                                              self.address2_var.get(),
                                                                                                                                                                                                                                                                              self.postcode_var.get(),
                                                                                                                                                                                                                                                                              self.mobile_var.get(),
                                                                                                                                                                                                                                                                              self.bookid_var.get(),
                                                                                                                                                                                                                                                                              self.booktitle_var.get(),
                                                                                                                                                                                                                                                                              self.auther_var.get(),
                                                                                                                                                                                                                                                                              self.dateborrowed_var.get(),
                                                                                                                                                                                                                                                                              self.datedue_var.get(),
                                                                                                                                                                                                                                                                              self.daysonbook_var.get(),
                                                                                                                                                                                                                                                                              self.latereturnfine_var.get(),
                                                                                                                                                                                                                                                                              self.dateoverdue_var.get(),
                                                                                                                                                                                                                                                                              self.finalprice_var.get(),
                                                                                                                                                                                                                                                                              self.prn_var.get(),
                                                                                                                                                                                                                                                                                ))
        conn.commit()
        self.fetch_data()
        self.resetdata()
        conn.close()

        tkinter.messagebox.showinfo("Success","Member Has Been Updated.")



    def get_cursor(self,event=''):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def showdata(self):
        self.txtbox.insert(END,'Member Type :\t\t'+self.member_var.get()+'\n')
        self.txtbox.insert(END, 'PRN No. :\t\t' + self.prn_var.get() + '\n')
        self.txtbox.insert(END, 'ID No. :\t\t' + self.id_var.get() + '\n')
        self.txtbox.insert(END, 'First Name :\t\t' + self.firstname_var.get() + '\n')
        self.txtbox.insert(END, 'Last Name :\t\t' + self.lastname_var.get() + '\n')
        self.txtbox.insert(END, 'Address1 :\t\t' + self.address1_var.get() + '\n')
        self.txtbox.insert(END, 'Address2  :\t\t' + self.address2_var.get() + '\n')
        self.txtbox.insert(END, 'Post Code :\t\t' + self.postcode_var.get() + '\n')
        self.txtbox.insert(END, 'Mobile No :\t\t' + self.mobile_var.get() + '\n')
        self.txtbox.insert(END, 'Book ID. :\t\t' + self.bookid_var.get() + '\n')
        self.txtbox.insert(END, 'Book Title :\t\t' + self.booktitle_var.get() + '\n')
        self.txtbox.insert(END, 'Auther Name :\t\t' + self.auther_var.get() + '\n')
        self.txtbox.insert(END, 'Date Borrowed :\t\t' + self.dateborrowed_var.get() + '\n')
        self.txtbox.insert(END, 'Date Due :\t\t' + self.datedue_var.get() + '\n')
        self.txtbox.insert(END, 'Days On Book :\t\t' + self.daysonbook_var.get() + '\n')
        self.txtbox.insert(END, 'Late Return Fine :\t\t' + self.latereturnfine_var.get() + '\n')
        self.txtbox.insert(END, 'Date Over Due :\t\t' + self.dateoverdue_var.get() + '\n')
        self.txtbox.insert(END, 'Final Price :\t\t' + self.finalprice_var.get() + '\n')

    def resetdata(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.txtbox.delete('1.0',END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System","Do You Really Want To Exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=='' or self.id_var.get()=='':
            messagebox.showerror('Error','First Select The Member')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Md@mysql444',database='lms')
            my_cursor=conn.cursor()
            querry="delete from library where prnno=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(querry,value)
            conn.commit()
            self.fetch_data()
            self.resetdata()
            conn.close()

            messagebox.showinfo("Success","Member Has Been Deleted")





if __name__ == "__main__":
    root = Tk()
    obj =  LibraryManagementSystem(root)

    root.mainloop()
