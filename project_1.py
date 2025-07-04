from tkinter import Tk,Label,Button,Entry,ttk,Frame,messagebox,simpledialog
from tkintertable import TableCanvas, TableModel
import time
import webbrowser
from PIL import Image,ImageTk
import random
import autotable_creation
import sqlite3
import gmail
import re

win = Tk()
win.title('My Project')
win.state('zoomed')
win.config(bg = 'sky blue')
win.resizable(width= False, height= False)


# importing image of 'header'
img1=Image.open('d:/Ducat/PROJECT/bank_project/used_images/back.jpg').resize((1290,125))
bitmap_1=ImageTk.PhotoImage(img1,win)

# importing image of 'admin user'
img2=Image.open('d:/Ducat/PROJECT/bank_project/used_images/admin_logo.jpeg').resize((160,43))
bitmap_2=ImageTk.PhotoImage(img2,win)

# importing image of 'user'
img3=Image.open('d:/Ducat/PROJECT/bank_project/used_images/user_logo.jpeg').resize((160,45))
bitmap_3=ImageTk.PhotoImage(img3,win)

#importing image in background of main screen
img4=Image.open('d:/Ducat/PROJECT/bank_project/used_images/bg2_image.jpg').resize((1300,550))
bitmap_4=ImageTk.PhotoImage(img4,win)

#importing image on main screen of email icon
img5=Image.open('d:/Ducat/PROJECT/bank_project/used_images/mail2.png').resize((35,28))
bitmap_5=ImageTk.PhotoImage(img5,win)

#importing image on main screen of phone icon
img6=Image.open('d:/Ducat/PROJECT/bank_project/used_images/phone.png').resize((35,28))
bitmap_6=ImageTk.PhotoImage(img6,win)

#importing image on main screen of complain icon
img7=Image.open('d:/Ducat/PROJECT/bank_project/used_images/complain.png').resize((35,28))
bitmap_7=ImageTk.PhotoImage(img7,win)


image_1_label=Label(win,image=bitmap_1)
image_1_label.place(x=0, y=0, relwidth=1, height=110)

image_2_label = Label(win,image=bitmap_2)
image_2_label.place(x= 525, y= 115 )

image_3_label = Label(win,image=bitmap_3)
image_3_label.place(x= 525, y= 115 )

image_4_label = Label(win,image=bitmap_4)
image_4_label.place(relx= 0, rely= .15,relwidth=1,relheight= 0.78)

image_5_label = Label(win,image=bitmap_5)
image_5_label.place(x=32, y=657)

image_6_label = Label(win,image=bitmap_6)
image_6_label.place(x= 560, y= 657 )

image_7_label = Label(win,image=bitmap_7)
image_7_label.place(x= 930, y= 657 )


# creating header
header_title = Label(win, text = 'Banking Automation', font = ('algebrain',28,'bold'),fg= 'black', bg="#a2dcde")
header_title.place(x = 445, y = 36)

# importing time in header
cur_time = time.ctime()

header_time = Label(win,text=f'Today: {cur_time}',font= ('veranda',10,'bold'),fg= 'black',bg= '#a2dcde')
header_time.place(x= 518,y= 83)


# creating hyperlinks for the complain footer
def on_complain_click():
    webbrowser.open('https://services.india.gov.in/service/detail/lodge-complaint-with-banking-ombudsman-of-rbi')

def on_mail_click():
    webbrowser.open('https://rbi.org.in/Scripts/helpdesk.aspx')

def on_phone_click():
    webbrowser.open('https://paisaboltahai.rbi.org.in/contact_us.aspx')

# creating footer
footer_1_detail = Label(win,text= ': bankingautomation@gmail.com',font= ('veranda',14,'bold','underline'),height= 2,fg= 'red',bg= 'sky blue')
footer_1_detail.place(x = 73,y = 649)#,fill= 'x')
footer_1_detail.bind('<Button-1>', lambda e: on_mail_click())

# creating footer
footer_2_detail = Label(win,text= ': +021-5328790',font= ('veranda',14,'bold','underline'),height= 2,fg= 'red',bg= 'sky blue')
footer_2_detail.place(x = 600,y = 649)#,fill= 'x')
footer_2_detail.bind('<Button-1>', lambda e: on_phone_click())

# creating footer
footer_3_detail = Label(win,text= ': bankings@complaint.com',font= ('veranda',14,'bold','underline'),height= 2,fg= 'red',bg= 'sky blue')
footer_3_detail.place(x= 970,y= 649)#,fill= 'x')
footer_3_detail.bind('<Button-1>', lambda e: on_complain_click())



# creating main screen
def main_screen():

    # creating frame of main screen
    frm = Frame(win,highlightbackground='black', highlightthickness= .5)
    frm.config(bg= 'sky blue')
    frm.place(relx= 0, rely= .15,relwidth=1,relheight= 0.78)

    # placing image in the backgorund of the main screen
    image_4_label = Label(win,image=bitmap_4)
    image_4_label.place(relx= 0, rely= .15,relwidth=1,relheight= 0.78)

    def on_reset_click():
        acn_entry.delete(0,'end')
        pass_entry.delete(0,'end')
        acn_entry.focus()

    # creating action for command of 'login' button
    def login_click():

        # making inout of account as global variable
        global input_acn
        # taking user entries from entry of 'account' , 'password' and 'role entry'
        input_acn = acn_entry.get()
        input_pass = pass_entry.get()
        input_role = roll_button.get()

        if len(input_acn) == 0 and len(input_pass) == 0:
            messagebox.showerror('Login','Account No. or Password cannot be empty !')
            return
        
        input_acn = int(input_acn)
        # creating conditions for 'Admin' login
        if input_acn == 0 and input_pass == 'admin' and input_role == 'Admin':
            frm.destroy()
            welcome_admin_screen()
        elif input_role == 'User':
            # connecting connection with sqlite file
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            # creating a query for fetching all chechking of the details for logging in
            cur_obj.execute('select * from users where user_acno = ? and user_pass = ?',(input_acn, input_pass))

            # creating a varibale 'tup' to store and fetch the data of the user of accunt number and password to login
            tup = cur_obj.fetchone()
            if tup == None:
                messagebox.showerror('Login','Invalid User')
            else:
                frm.destroy()
                welcome_user_screen()
        else:
            messagebox.showerror('Login','Invalid Role')


     # creating action for command of 'exit' button
    def on_exit():
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
        if response:
            win.quit()

    #  creating label in the main screen of 'Account'
    acn_label = Label(win, text= 'Account      ->>',font= ('veranda',14,'bold','underline'),bg= '#ace7fa')
    acn_label.place(x = 350,y = 150)  

    # creating entry in the main screen of the 'Account label'
    acn_entry = Entry(win,font= ('veranda',14,'bold'),bd=4)
    acn_entry.place(x=545, y= 150)
    acn_entry.focus()


    # creating label in main screen of 'Role'
    role_label = Label(win, text= 'Role             ->>',font= ('veranda',14,'bold','underline'),bg= 'sky blue')
    role_label.place(x = 350,y = 225)

    # creating 'roll back' in main screen
    options = ['User', 'Admin']
    roll_button = ttk.Combobox(win,values= options,state= 'readonly',font= ('veranda',13,'bold'),width=22,height= 18)
    roll_button.set('select an option')
    roll_button.place(x= 545, y= 225)


    # creating label in the main screen of 'Password'
    pass_label = Label(win, text= 'Password   ->>',font= ('veranda',14,'bold','underline'),bg= 'sky blue')
    pass_label.place(x = 350,y = 290)

    # creating entry in main screen of the 'Password label'
    pass_entry = Entry(win,font= ('veranda',14,'bold'),show= '*',bd=4)
    pass_entry.place(x=545, y= 290)


    # creating button in main screen of 'Forget Password'
    forgotpass_button = Button(win,text= 'Forgot Password ?',font= ('veranda',8,'bold','underline'),bg= '#e695b9',command= forgot_password_screen,bd=4)
    forgotpass_button.place(x=655, y= 324)

    # creating button in main screen of 'Login button'
    login_button = Button(win,text= 'Login',font= ('veranda',13,'bold'),bg= '#e695b9',command= login_click,width= 8,bd=4)
    login_button.place(x=545, y= 390)

    # creating button in main screen of 'Reset button'
    reset_button = Button(win,text= 'Reset',font= ('veranda',13,'bold'),bg= '#e695b9',width= 8,bd=4,command= on_reset_click)
    reset_button.place(x=653, y= 390)

    # creating button on main screen of 'exit'
    exit_button = Button(win,text= 'Exit',font= ('veranda',12,'bold','underline'),bg= 'red',fg= 'white',command= on_exit,width= 8,bd=4)
    exit_button.place(x=1176, y= 110)



# creating screen for the 'admin login'
def welcome_admin_screen():

    # creating frame for the 'admin screen'
    frm = Frame(win,highlightbackground='black', highlightthickness= .5)
    frm.config(bg= 'sky blue')
    frm.place(relx= 0, rely= .15,relwidth=1,relheight= 0.78)

    # creating action for command of 'logout' button
    def on_logout_click():
        response = messagebox.askyesno('Log out', 'Are you sure you want to logout?')
        if response:
            frm.destroy()
            main_screen()

    # creating screen for 'create user'
    def create_user_click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= '#9cf0b5')
        ifrm.place(x = 200, rely= .14,relwidth=.73,relheight= .73)

        # creating aciton on button 'open account' in crate user screen
        def on_open_acn_click():

            # getting all the entries from the entries in the create user screen
            uname = name_entry.get()
            umob = mobile_entry.get()
            uemail = email_entry.get()
            uaadhar = aadhar_entry.get()
            ubal = 0
            upass = str(random.randint(100000,999999))
            uacntype = acnroll_button.get()
            current_time = cur_time

            # creating checks and warnings for data validation

            if len(uname) == 0 or len(umob) == 0 or len(uemail) == 0 or len(uaadhar) == 0 :
                messagebox.showerror('Warning','Fields cannot be empty !')
                return
            
            if not re.fullmatch('[a-zA-Z ]+',uname):
                messagebox.showerror('Warning','Kindly enter a valid Name !')
                return

            if not re.fullmatch('[6-9][0-9]{9}',umob):
                messagebox.showerror('Warning','Kindly enter a valid Mobile No. !')
                return
            
            if not re.fullmatch('[a-z0-9_.]+@[a-z]+[.][a-z]+',uemail):
                messagebox.showerror('Warning','Kindly enter a valid Email !')
                return
            
            if not re.fullmatch('[0-9]{12}',uaadhar):
                messagebox.showerror('Warning','Kindly enter a valid Aadhar !')
                return

            # creating connectio and inserting values in the table of the new user
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('insert into users(user_pass,user_name,user_mob,user_email,user_bal,user_aadhar,user_opendate,user_acn_type) values (?,?,?,?,?,?,?,?)', (upass,uname,umob,uemail,ubal,uaadhar,current_time,uacntype))
            con_obj.commit()
            con_obj.close()

            # fetching the account number of latest user for sending the email
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('select max(user_acno) from users')
            tup = cur_obj.fetchone()
            uacn = tup[0]
            con_obj.close()

            # sending the mail to the new user of their details
            try:
                mail_con = gmail.GMail('chaubey5439@gmail.com','fhav iukf alal qjni')
                umsg = f'''Dear {uname},

            Welcome to XYZ Bank!

            We are excited to have you on board. Your account has been successfully created. Here are the details:
            
            Account No. : {uacn}
            Password : {upass}
            Account Type: {uacntype}

            Kindly change your Password after logging in.

            You can now access your account and explore our services by logging in using your Account No. and Password.

            Best regards,
            XYZ Bank'''
                msg = gmail.Message(to = uemail,subject= 'Account Successfully Created!',text= umsg)
                mail_con.send(msg)
                messagebox.showinfo('Open Account','Account created !\nCheck your Email for details')

            except:
                messagebox.showerror('Open Account','Something went Wrong !')

        # creating title in create user
        create_user_title = Label(frm, text= 'This is Create User Screen',font= ('veranda',13,'bold'),bg= '#9cf0b5',fg='red')
        create_user_title.place(x= 498, y= 88)

        # creating label in create user screen of 'name'
        name_label = Label(frm, text= 'Name  : ',font= ('veranda',12,'bold'),bg= '#9cf0b5',fg='red')
        name_label.place(x = 246,y = 135)

        # creating entry for label 'name'
        name_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        name_entry.place(x=246, y= 162)
        
        # creating label in create user screen of 'mobile no.'
        mobile_label = Label(frm, text= 'Mobile No. : ',font= ('veranda',12,'bold'),bg= '#9cf0b5',fg='red')
        mobile_label.place(x = 740,y = 135)

        # creating entry for label 'mobile no.'
        mobile_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        mobile_entry.place(x=740, y= 162)
        
        # creating label in create user screen of 'email'
        email_label = Label(frm, text= 'Email  : ',font= ('veranda',12,'bold'),bg= '#9cf0b5',fg='red')
        email_label.place(x = 246,y = 205)

        # creating entry for label 'email'
        email_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        email_entry.place(x=246, y= 232)  

        # creating label in create user screen of 'aadhar no.'
        aadhar_label = Label(frm, text= 'Aadhar No. : ',font= ('veranda',12,'bold'),bg= '#9cf0b5',fg='red')
        aadhar_label.place(x = 740,y = 205)

        # creating entry for label 'aadhar no.'
        aadhar_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        aadhar_entry.place(x=740, y= 232)

        # creating label in create user screen of 'account type'
        acntype_label = Label(frm, text= 'Account Type : ',font= ('veranda',12,'bold'),bg= '#9cf0b5',fg='red')
        acntype_label.place(x = 246,y = 292)

        # creating roll back button for label 'account type'
        options = ['Savings', 'Current']
        acnroll_button = ttk.Combobox(frm,values= options,state= 'readonly',font= ('veranda',12,'bold'),width=22,height= 18)
        acnroll_button.set('select an option',)
        acnroll_button.place(x= 246, y= 319)

        # creating button in create user screen of 'open account'
        acn_open_button = Button(frm,text= 'Open Account',font= ('veranda',13,'bold'),bg= '#e695b9',width= 12,bd=4,command= on_open_acn_click)
        acn_open_button.place(x=915, y= 360)

        # creating button in create user screen of 'reset'
        reset_button = Button(frm,text= 'Reset',font= ('veranda',12,'bold'),bg= '#e695b9',width= 12,bd=4)
        reset_button.place(x=915, y= 405)


    # creating screen for 'view user'
    def view_user_click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= '#e7f09c')
        ifrm.place(x = 200, rely= .14,relwidth=.73,relheight= .73)
        
        # creating title in view user screen
        view_user_title = Label(frm, text= '    This is View User Screen',font= ('veranda',13,'bold'),bg= '#e7f09c',fg= 'red')
        view_user_title.place(x= 485, y= 87 )

        # Create a Frame (Fix for NoneType error)
        frame = Frame(ifrm)
        frame.place(relx=.06,rely=.15,relwidth=.88)

        data={}
        i=1
        con_obj=sqlite3.connect(database='bank.sqlite')
        cur_obj=con_obj.cursor()
        cur_obj.execute("select * from users")

        for tup in cur_obj:
            data[f"{i}"]= {"Acn No.": tup[0], "Name ":tup[2], "Mobile No.": tup[3],"Email ":tup[4],"Balance ":tup[5],"Aadhar No. ":tup[6],"Acn Opendate ":tup[7],"Acn Type ":tup[8]}
            i+=1

        con_obj.close()

        # Create Table Model
        model = TableModel()
        model.importDict(data)  # Load data into the model

        # Create Table Canvas inside Frame (Important Fix)
        table = TableCanvas(frame, model=model, editable=False)
        table.show()

        

    # creating screen for 'delete user'
    def delete_user_click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= '#f09c9c')
        ifrm.place(x = 200, rely= .14,relwidth=.73,relheight= .73)

        # creating title of the delete user screen
        delete_user_title = Label(frm, text= ' This is Delete User Screen',font= ('veranda',13,'bold'),bg= '#f09c9c',fg= 'blue')
        delete_user_title.place(x= 485, y= 87 )

        def on_delete_click():
            uacn = acn_entry.get()

            # doing data validation:
            if len(uacn) == 0:
                messagebox.showerror('Delete User','Account feild cannot be empty !')
                return
            
            if not re.fullmatch('[0-9]+',uacn):
                messagebox.showerror('Warning','Kindly enter a valid Account No. !')
                return

            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('delete from users where user_acno = ?',(uacn,))
            cur_obj.execute('delete from txn where txn_acno = ?',(uacn,))
            con_obj.commit()
            con_obj.close()
            messagebox.showinfo('Delete Account',f'Account with Acn No. {uacn} deleted successfully !')

        # creating label in delete user screen of 'account no.'
        acn_label = Label(frm, text= 'Account No. : ',font= ('veranda',14,'bold'),bg= '#f09c9c',fg='blue')
        acn_label.place(x = 246,y = 180)

        # creating entry of label 'account no.'
        acn_entry = Entry(frm,font= ('veranda',14,'bold'),bd=4)
        acn_entry.place(x=246, y= 205)

        # creating button in delete user screen of 'delete account'
        delete_button = Button(frm,text= 'Delete Account',font= ('veranda',13,'bold'),bg= '#e695b9',width= 12,bd=4,command= on_delete_click)
        delete_button.place(x=915, y= 360)

        # creating button in the delete user screen of 'reset'
        reset_button = Button(frm,text= 'Reset',font= ('veranda',12,'bold'),bg= '#e695b9',width= 12,bd=4)
        reset_button.place(x=915, y= 405)


    # placing image in admin screen of 'welcome admin'
    image_2_label = Label(win,image=bitmap_2)
    image_2_label.place(x= 533, y= 115 )

    # creating button in admin screen of 'logout'
    logout_button = Button(win,text= 'Log Out',font= ('veranda',13,'bold'),bg= '#e695b9',width= 11,bd=4,command= on_logout_click)
    logout_button.place(x=1150, y= 116)

    # creating button in admin screen of 'create user button'
    create_user_button = Button(win,text= 'Create User',font= ('veranda',13,'bold'),bg= '#57f29d',bd=4,command= create_user_click, width = 11)
    create_user_button.place(x=12, y= 180)

    # creating button in admin screen of 'view user button'
    view_user_button = Button(win,text= 'View User',font= ('veranda',13,'bold'),bg= '#e3f257',bd=4, width = 11,command= view_user_click)
    view_user_button.place(x= 12, y= 255)

    # creating button in admin screen of 'delete user button'
    delete_user_button = Button(win,text= 'Delete User',font= ('veranda',13,'bold'),bg= '#f25757',bd=4, width = 11,command= delete_user_click)
    delete_user_button.place(x=12, y= 330)



# creating screen for the 'Forgot Password'
def forgot_password_screen():

    # creating frame for the forgot password screen
    frm = Frame(win,highlightbackground='black', highlightthickness= .5)
    frm.config(bg= 'sky blue')
    frm.place(relx= 0, rely= .15,relwidth=1,relheight= 0.78)

    # placing image in the backgorund of the forgot password screen
    image_4_label = Label(win,image=bitmap_4)
    image_4_label.place(relx= 0, rely= .15,relwidth=1,relheight= 0.78)

    # creating action for the 'back' button of forgot password screen
    def on_back_click():
        main_screen()


    # creating action for the 'submit ' button 
    def on_submit_click():

        # getting all information from the entries
        uacn = acn_entry.get()
        uemail = email_entry.get()
        umob = mobile_entry.get()

        # doing data validation:
        if len(uacn) == 0 or len(uemail) == 0 or len(umob) == 0:
            messagebox.showerror('Forgot Password','Feilds cannot be empty !')
            return
        
        if not re.fullmatch('[0-9]+',uacn):
            messagebox.showerror('Warning','Kindly enter a valid Account No. !')
            return
        
        if not re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',uemail):
            messagebox.showerror('Warning','Kindly enter a valid Email !')
            return
        
        if not re.fullmatch('[6-9][0-9]{9}',umob):
            messagebox.showerror('Warning','Kindly enter a valid Mobile No. !')
            return
            

        # creating a sqlite connection for fetching the password 
        con_obj = sqlite3.connect(database= 'bank.sqlite')
        cur_obj = con_obj.cursor()
        cur_obj.execute('select user_name,user_pass from users where user_acno = ? and user_email = ? and user_mob = ?',(uacn,uemail,umob))
        tup = cur_obj.fetchone()
        con_obj.close()

        if tup == None:
            messagebox.showerror('Forgot Password','Invalid Details !')
        else:
            # using try and except for sending the mail after passowrd recovery
            try:
                mail_con = gmail.GMail('chaubey5439@gmail.com','fhav iukf alal qjni')
                umsg = f'''Dear {tup[0]},

            Your password has been Successfully recovered.

            Password :  {tup[1]}

            You can now access your account and explore our services by logging in using your Account no. and Password.

            Best regards,
            XYZ Bank'''
                msg = gmail.Message(to = uemail,subject= 'Password Successfully Recovered!',text= umsg)
                mail_con.send(msg)
                messagebox.showinfo('Forgot Password','Check your email !')

            except:
                messagebox.showerror('Forgot Password','Something went Wrong!')


    # creating button in the forgot pass screen of 'Back Button'
    back_button = Button(win,text= 'Back',font= ('veranda',13,'bold'),bg= '#e695b9',width= 11,bd=4,command= on_back_click)
    back_button.place(x=15, y= 116)


    # creating label in forgot pass screen of 'Account'
    acn_label = Label(win, text= 'Account      ->>',font= ('veranda',14,'bold','underline'),bg= '#ace7fa')
    acn_label.place(x = 350,y = 150)  

    # creating entry in forgot pass screen for the 'Account label'
    acn_entry = Entry(win,font= ('veranda',14,'bold'),bd=4)
    acn_entry.place(x=545, y= 150)
    acn_entry.focus()

    
    # creating label in forgot pass screen 'Email'
    email_label = Label(win, text= 'Email           ->>',font= ('veranda',14,'bold','underline'),bg= 'sky blue')
    email_label.place(x = 350,y = 225)

    # creating entry in forgot pass screen for the 'Email label'
    email_entry = Entry(win,font= ('veranda',14,'bold'),bd=4)
    email_entry.place(x= 545, y= 225)


    # creating label in forgot pass screen 'Mobile No.'
    mobile_label = Label(win, text= 'Mobile No.  ->>',font= ('veranda',14,'bold','underline'),bg= 'sky blue')
    mobile_label.place(x = 350,y = 290)

    # creating entry in the forgot pass screen for the 'Mobile No. label'
    mobile_entry = Entry(win,font= ('veranda',14,'bold'),bd=4)
    mobile_entry.place(x=545, y= 290)
    

    # creating button in forgot pass screen for 'Submit'
    submit_button = Button(win,text= 'Submit',font= ('veranda',13,'bold'),bg= '#e695b9',width= 10,bd=4,command= on_submit_click)
    submit_button.place(x=705, y= 370)



def welcome_user_screen():

    # creating frame for the 'admin screen'
    frm = Frame(win,highlightbackground='black', highlightthickness= .5)
    frm.config(bg= 'sky blue')
    frm.place(relx= 0, rely= .15,relwidth=1,relheight= 0.78)

    # creating action for command of 'logout' button
    def on_logout_click():
        response = messagebox.askyesno('Log out', 'Are you sure you want to logout?')
        if response:
            frm.destroy()
            main_screen()

    # placing image in admin screen of 'welcome admin'
    image_3_label = Label(win,image=bitmap_3)
    image_3_label.place(x= 533, y= 115 )

    # creating button in user screen of 'logout'
    logout_button = Button(win,text= 'Log Out',font= ('veranda',13,'bold'),bg= '#e695b9',width= 11,bd=4,command= on_logout_click)
    logout_button.place(x=1150, y= 116)


    # creating ifrm / screen for 'check balance'
    def account_details__click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= '#57f29d')
        ifrm.place(x = 200, rely= .17,relwidth=.73,relheight= .75)

        acn_details_title = Label(frm, text= ' This is Account Details Screen',font= ('veranda',12,'bold'),bg= '#57f29d',fg= 'red')
        acn_details_title.place(x= 495, y= 97 )

        # creating connection to fetch the account details
        con_obj = sqlite3.connect(database= 'bank.sqlite')
        cur_obj = con_obj.cursor()
        cur_obj.execute('select user_bal,user_aadhar,user_opendate,user_acn_type from users where user_acno = ?',(input_acn,))
        tup = cur_obj.fetchone()
        con_obj.close()

        # creating labels for the details along with the details in account details screen

        bal_label = Label(ifrm, text= f'Account Balance    : \t {tup[0]}',font= ('veranda',12,'bold'),bg= '#57f29d',fg= 'red')
        bal_label.place(x = 246,y = 115)

        aadhar_label = Label(ifrm, text= f'Aadhar Number      : \t {tup[1]}',font= ('veranda',12,'bold'),bg= '#57f29d',fg= 'red')
        aadhar_label.place(x = 246,y = 165)

        opendate_label = Label(ifrm, text= f'Account Opendate : \t {tup[2]}',font= ('veranda',12,'bold'),bg= '#57f29d',fg= 'red')
        opendate_label.place(x = 246,y = 215)

        acntype_label = Label(ifrm, text= f'Account Type        : \t {tup[3]}',font= ('veranda',12,'bold'),bg= '#57f29d',fg= 'red')
        acntype_label.place(x = 246,y = 265)


    # creating ifrm / screen for 'update details'
    def update_details__click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= 'white')
        ifrm.place(x = 200, rely= .17,relwidth=.73,relheight= .75)

        update_details_title = Label(frm, text= ' This is Update Details Screen',font= ('veranda',12,'bold'),bg= 'white',fg= 'red')
        update_details_title.place(x= 495, y= 97 )

        def on_update_click():

            uname = name_entry.get()
            uemail = email_entry.get()
            umob = mobile_entry.get()
            upass = password_entry.get()
            uacntype = acntype_button.get()

            # creating checks and warnings for data validation

            if len(uname) == 0 or len(umob) == 0 or len(uemail) == 0 or len(upass) == 0 :
                messagebox.showerror('Warning','Fields cannot be empty !')
                return
            
            if not re.fullmatch('[a-zA-Z ]+',uname):
                messagebox.showerror('Warning','Kindly enter a valid Name !')
                return

            if not re.fullmatch('[6-9][0-9]{9}',umob):
                messagebox.showerror('Warning','Kindly enter a valid Mobile No. !')
                return
            
            if not re.fullmatch('[a-z0-9_.]+@[a-z]+[.][a-z]+',uemail):
                messagebox.showerror('Warning','Kindly enter a valid Email !')
                return
            
            if not re.fullmatch('[0-9a-zA-Z_-.$@]+',upass):
                messagebox.showerror('Warning','Kindly enter a valid Password !')
                return

            # connection to update the details of the user
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('update users set user_email = ?,user_pass = ? ,user_acn_type = ? ,user_name = ?, user_mob = ? where user_acno = ?',(uemail,upass,uacntype,uname,umob,input_acn))
            con_obj.commit()
            con_obj.close()
            messagebox.showinfo('Update Details','Details Updated Successfully !')
            main_screen()

            # sending mail afte the updatation completes
            try:
                mail_con = gmail.GMail('chaubey5439@gmail.com','fhav iukf alal qjni')
                umsg = f'''Hi {uname}!

                Your bank deatils are successfully updated.

                Here are your details:
                Password : {upass}
                Email : {uemail}
                Mobile No. : {umob}
                Account Type: '{uacntype}'

                Best Regards
                XYZ Bank'''
                msg = gmail.Message(to = uemail,subject= 'Details Updated Successfully !',text= umsg)
                mail_con.send(msg)

            except:
                messagebox.showerror('Open Account','Something went Wrong!')

        # to select the details of the logged in user
        con_obj = sqlite3.connect(database= 'bank.sqlite')
        cur_obj = con_obj.cursor()
        cur_obj.execute('select * from users where user_acno = ?',(input_acn,))
        tup = cur_obj.fetchone()
        con_obj.close()


        # creating label in update details screen of 'name'
        name_label = Label(frm, text= 'Name  : ',font= ('veranda',12,'bold'),bg= 'white',fg='blue')
        name_label.place(x = 246,y = 155)

        # creating entry for label 'name'
        name_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        name_entry.place(x=246, y= 182)
        name_entry.insert(0,tup[2])
        name_entry.focus()
        
        # creating label in update details screen of 'mobile no.'
        mobile_label = Label(frm, text= 'Mobile No. : ',font= ('veranda',12,'bold'),bg= 'white',fg='blue')
        mobile_label.place(x = 740,y = 155)

        # creating entry for label 'mobile no.'
        mobile_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        mobile_entry.place(x=740, y= 182)
        mobile_entry.insert(0,tup[3])
        
        # creating label in update details screen of 'email'
        email_label = Label(frm, text= 'Email  : ',font= ('veranda',12,'bold'),bg= 'white',fg='blue')
        email_label.place(x = 246,y = 225)

        # creating entry for label 'email'
        email_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        email_entry.place(x=246, y= 252)  
        email_entry.insert(0,tup[4])

        # creating label in update details screen of 'password'
        password_label = Label(frm, text= 'Password : ',font= ('veranda',12,'bold'),bg= 'white',fg='blue')
        password_label.place(x = 740,y = 225)

        # creating entry for label 'password'
        password_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        password_entry.place(x=740, y= 252)
        password_entry.insert(0,tup[1])

        # creating label in update details screen of 'address'
        acntype_label = Label(frm, text= 'Account Type : ',font= ('veranda',12,'bold'),bg= 'white',fg='blue')
        acntype_label.place(x = 246,y = 300)

        # creating entry for label 'address'
        options = ['Savings', 'Current']
        acntype_button = ttk.Combobox(frm,values= options,state= 'readonly',font= ('veranda',12,'bold'),width=22,height= 18)
        acntype_button.set('Savings')
        acntype_button.insert(0,tup[8])
        acntype_button.place(x= 246, y= 327)

        # creating button in update details screen of 'update'
        update_button = Button(frm,text= 'Update',font= ('veranda',13,'bold'),bg= '#e695b9',width= 12,bd=4,command= on_update_click)
        update_button.place(x=915, y= 390)


    # creating ifrm / screen for 'deposit'
    def deposit__click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= '#f09c9c')
        ifrm.place(x = 200, rely= .17,relwidth=.73,relheight= .75)

        deposit_title = Label(frm, text= ' This is Deposit Screen',font= ('veranda',12,'bold'),bg= '#f09c9c',fg= 'black')
        deposit_title.place(x= 520, y= 97 )

        # creating action for the 'deposit button'
        def on_deposit_click():
            uamt = amount_entry.get()

            # doing data validation:
            if len(uamt) == 0:
                messagebox.showerror('Deposit','Amount feild cannot be empty !')
                return
            
            if not re.fullmatch('[0-9]+',uamt):
                messagebox.showerror('Warning','Kindly enter a valid Amount !')
                return
            
            uamt = int(uamt)

            # connection to fetch account no. of user
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('select user_bal,user_email from users where user_acno = ?',(input_acn,))
            tup = cur_obj.fetchone()
            con_obj.close()

            # connection to update balamnce after the deposit
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('update users set user_bal = user_bal + ? where user_acno = ?',(uamt,input_acn))
            con_obj.commit()
            con_obj.close()

            # connection to insert details in txn table of txn 
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('insert into txn(txn_acno,txn_type,txn_date,txn_amt,txn_updated_bal) values (?,?,?,?,?)',(input_acn,'Credit',cur_time,uamt,uamt+tup[0]))
            con_obj.commit()
            con_obj.close()

            messagebox.showinfo('Deposit',f'Amount {uamt} deposited \n Updated balance {tup[0]+uamt}')

            # sending mail after deposit completes
            try:
                mail_con = gmail.GMail('chaubey5439@gmail.com','fhav iukf alal qjni')
                umsg = f'''Hi !

                Your Transaction of {uamt} has been Successfull.

                Here are your details:
                Credit Amount : {uamt}
                New Balance : {tup[0]+uamt}

                Best Regards
                XYZ Bank'''
                msg = gmail.Message(to = tup[1],subject= f'Transaction Successfull !',text= umsg)
                mail_con.send(msg)

            except:
                messagebox.showerror('Deposit Amount','Something went Wrong!')

        # creating label in deposit user screen of 'amount'
        amount_label = Label(frm, text= 'Deposit Amount : ',font= ('veranda',12,'bold'),bg= '#f09c9c',fg='black')
        amount_label.place(x = 246,y = 200)

        # creating entry of label 'amount'
        amount_entry = Entry(frm,font= ('veranda',14,'bold'),bd=4)
        amount_entry.place(x=246, y= 225)
        amount_entry.focus()

        # creating button in deposit screen of 'deposit'
        deposit_button = Button(frm,text= 'Deposit',font= ('veranda',13,'bold'),bg= '#e695b9',width= 12,bd=4,command= on_deposit_click)
        deposit_button.place(x=915, y= 390)


    # creating ifrm / screen for 'withdrawl'
    def withdrawl__click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= '#e3f257')
        ifrm.place(x = 200, rely= .17,relwidth=.73,relheight= .75)

        withdrawl_title = Label(frm, text= ' This is Withdrawl Screen',font= ('veranda',12,'bold'),bg= '#e3f257',fg= 'red')
        withdrawl_title.place(x= 505, y= 97 )

        # creating action for the button 'withdraw'
        def on_withdrwal_click():
            uamt = amount_entry.get()

            # doing data validation:
            if len(uamt) == 0:
                messagebox.showerror('Withdrawl','Amount feild cannot be empty !')
                return
            
            if not re.fullmatch('[0-9]+',uamt):
                messagebox.showerror('Warning','Kindly enter a valid Amount !')
                return
            
            uamt = int(uamt)

            # connection to fetch balance and email of the login user
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('select user_bal,user_email from users where user_acno = ?',(input_acn,))
            tup = cur_obj.fetchone()
            con_obj.close()

            if tup[0] >= uamt:
                # connection to update balanace of the user after withdrawl
                con_obj = sqlite3.connect(database= 'bank.sqlite')
                cur_obj = con_obj.cursor()
                cur_obj.execute('update users set user_bal = user_bal - ? where user_acno = ?',(uamt,input_acn))
                con_obj.commit()
                con_obj.close()

                # connection to insert details in the txn table of the txn
                con_obj = sqlite3.connect(database= 'bank.sqlite')
                cur_obj = con_obj.cursor()
                cur_obj.execute('insert into txn(txn_acno,txn_type,txn_date,txn_amt,txn_updated_bal) values (?,?,?,?,?)',(input_acn,'Debit',cur_time,uamt,tup[0]-uamt))
                con_obj.commit()
                con_obj.close()

                messagebox.showinfo('Withdrwal',f'Amount {uamt} Withdrawn \n Updated balance {tup[0]-uamt}')

                # sending mail after withdrawl completes
                try:
                    mail_con = gmail.GMail('chaubey5439@gmail.com','fhav iukf alal qjni')
                    umsg = f'''Hi !

                    Your Transaction of {uamt} has been Successfull.

                    Here are your details:
                    Debit Amount : {uamt}
                    New Balance : {tup[0]-uamt}

                    Best Regards
                    XYZ Bank'''
                    msg = gmail.Message(to = tup[1],subject= f'Transaction Successfull !',text= umsg)
                    mail_con.send(msg)

                except:
                    messagebox.showerror('Withdrawl Amount','Something went Wrong!')

            else:
                messagebox.showinfo('Withdrwal',f'Insufficient Balance {tup[0]}')


        # creating label in withdrawl screen of 'account no.'
        amount_label = Label(frm, text= 'Withdrawl Amount : ',font= ('veranda',12,'bold'),bg= '#e3f257',fg='red')
        amount_label.place(x = 246,y = 200)

        # creating entry of label 'account no.'
        amount_entry = Entry(frm,font= ('veranda',14,'bold'),bd=4)
        amount_entry.place(x=246, y= 225)
        amount_entry.focus()

        # creating button in withdrawl screen of 'withdrawl'
        withdrawl_button = Button(frm,text= 'Withdrawl',font= ('veranda',13,'bold'),bg= '#e695b9',width= 12,bd=4,command= on_withdrwal_click)
        withdrawl_button.place(x=915, y= 390)


    # creating ifrm / screen for 'transfer'
    def transfer__click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= 'light pink')
        ifrm.place(x = 200, rely= .17,relwidth=.73,relheight= .75)    

        # creating title for the transfer screen
        transfer_title = Label(frm, text= ' This is Transfer Screen',font= ('veranda',12,'bold'),bg= 'light pink',fg= 'black')
        transfer_title.place(x= 510, y= 97 )

        # creating action command for teh button 'transfer'
        def on_transfer_click():
            toacn = to_acn_entry.get()
            uamt = amount_entry.get()

            # applying data validation
            if len(uamt) == 0 or len(toacn) == 0:
                messagebox.showerror('Transfer','Feilds cannot be empty !')
                return
            
            if not re.fullmatch('[0-9]+',toacn):
                messagebox.showerror('Warning','Kindly enter a valid Account !')
                return
            
            if not re.fullmatch('[0-9]+',uamt):
                messagebox.showerror('Warning','Kindly enter a valid Amount !')
                return

            toacn = int(toacn)
            uamt = float(uamt)

            # connection to fetch user balance and email of login user
            con_obj = sqlite3.connect(database= 'bank.sqlite')
            cur_obj = con_obj.cursor()
            cur_obj.execute('select user_bal,user_email from users where user_acno = ?',(input_acn,))
            tup = cur_obj.fetchone()
            con_obj.close()

            # creating logic to check captcha before the transfer
            if captcha_entry.get() != cap:
                messagebox.showerror('Captcha','Invalid captcha !')
                return

            # creating condition 'executing code only if the user balance is greater than the transferring balance'
            if tup[0] >= uamt:

                # connection to fetch account no. of the recieving user 
                con_obj = sqlite3.connect(database= 'bank.sqlite')
                cur_obj = con_obj.cursor()
                cur_obj.execute('select * from users where user_acno = ?',(toacn,))
                tupp = cur_obj.fetchone()
                con_obj.close()

                if tup[0] == None:
                    messagebox.showerror('Trnasfer','Transfer Account does not exist')

                else:

                    # creating code for the otp (while transferring the money)
                    otp = random.randint(1000,9999)

                    # sending mail for the otp
                    try:
                        mail_con = gmail.GMail('chaubey5439@gmail.com','fhav iukf alal qjni')
                        umsg = f'''Hi !

                        OTP has been sent successfully.

                        Here are your details:
                        OTP : {otp}

                        Kindly verify your OTP to complete the transaction.

                        Best Regards
                        XYZ Bank'''
                        msg = gmail.Message(to = tup[1],subject= f'Verify your OTP!',text= umsg)
                        mail_con.send(msg)
                        messagebox.showinfo('Transfer','OTP has been sent successfully on your registered mail !')

                        # using this to create a entry box nd also to verify the otp
                        uotp = simpledialog.askinteger('OTP','Enter OTP')

                        if otp == uotp:     # checking if the entered otp matched with the given otp

                            # connection to update the balance of both the users (to and from)
                            con_obj = sqlite3.connect(database= 'bank.sqlite')
                            cur_obj = con_obj.cursor()
                            cur_obj.execute('update users set user_bal = user_bal - ? where user_acno = ?',(uamt,input_acn))
                            cur_obj.execute('update users set user_bal = user_bal + ? where user_acno = ?',(uamt,toacn))
                            con_obj.commit()
                            con_obj.close()

                            tobal = tupp[5]     # it is to fetch the user balance of the user to whom the amount is being transferred

                            # connection to insert the txn details in the txn table
                            con_obj = sqlite3.connect(database= 'bank.sqlite')
                            cur_obj = con_obj.cursor()
                            cur_obj.execute('insert into txn(txn_acno,txn_type,txn_date,txn_amt,txn_updated_bal) values (?,?,?,?,?)',(input_acn,'Debit',cur_time,uamt,tup[0]-uamt))
                            cur_obj.execute('insert into txn(txn_acno,txn_type,txn_date,txn_amt,txn_updated_bal) values (?,?,?,?,?)',(toacn,'Credit',cur_time,uamt,tobal+uamt))
                            con_obj.commit()
                            con_obj.close()

                            messagebox.showinfo('Transfer',f'Amount {uamt} transfered \n Updated balance {tup[0]-uamt}')

                        else:
                            messagebox.showerror('OTP','Invalid OTP')       # if entered otp does not match with given otp

                    except:
                        messagebox.showerror('Withdrawl Amount','Something went Wrong!')        # if interruption comes during sending mail
            else:
                messagebox.showerror('Transfer',f'Insufficient Amount {tup[0]}')        # if transferring amount is more than balance

        # making cap as global to use the captcha in the code
        global cap
        cap = ''

        # creating function to generate captcha
        def generate_captcha():

            global cap
            cap = ''
            n = str(random.randint(0,9))
            cap = n+cap
            c = chr(random.randint(65,90))   # includes all the capital letters
            cap = cap+c
            s = chr(random.randint(97,122))  # includes all the small letters
            cap = cap+s
            n = str(random.randint(0,9))
            cap = n+cap
            s = chr(random.randint(97,122))
            cap = cap+s
            c = chr(random.randint(65,90))
            cap = cap+c

            return cap


        # creating label in transfer screen of 'to account'
        to_acn_label = Label(frm, text= 'To Account :  ',font= ('veranda',12,'bold'),bg= 'light pink',fg='black')
        to_acn_label.place(x = 246,y = 185)

        # creating entry for label 'to account'
        to_acn_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        to_acn_entry.place(x=246, y= 213)
        to_acn_entry.focus()

        # creating label in transfer screen of 'amount'
        amount_label = Label(frm, text= 'Transfer Amount : ',font= ('veranda',12,'bold'),bg= 'light pink',fg='black')
        amount_label.place(x = 246,y = 275)

        # creating entry of label 'amount'
        amount_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        amount_entry.place(x= 246, y= 302)

        # creating button in transfer screen of 'transfer'
        transfer_button = Button(frm,text= 'Transfer',font= ('veranda',13,'bold'),bg= '#e695b9',width= 12,bd=4,command= on_transfer_click)
        transfer_button.place(x=915, y= 395)

        # creating label in transfer screen of 'captcha'
        captcha_label = Label(frm, text= 'Captcha : ',font= ('veranda',12,'bold'),bg= 'light pink',fg='black')
        captcha_label.place(x = 580,y = 185)

        # creating entry  of label 'captcha'
        captcha_entry = Entry(frm,font= ('veranda',12,'bold'),bd=4)
        captcha_entry.place(x= 580, y= 213)

        # creating label to generate captcha
        gen_captcha_label = Label(frm, text= generate_captcha() ,font= ('veranda',12,'bold'),bg= 'white',fg='black',width= 10)
        gen_captcha_label.place(x = 620,y = 250)


    # creating ifrm / screen for 'txn history'
    def txn_history_click():
        ifrm = Frame(frm, highlightbackground= 'black', highlightthickness= .5)
        ifrm.config(bg= '#5ce0de')
        ifrm.place(x = 200, rely= .17,relwidth=.73,relheight= .75) 

        txn_history_title = Label(frm, text= ' This is Txn History Screen',font= ('veranda',12,'bold'),bg= '#5ce0de',fg= 'black')
        txn_history_title.place(x= 495, y= 97 )

        # Create a Frame (Fix for NoneType error)
        frame = Frame(ifrm)
        frame.place(relx=.14,rely=.16,relwidth=.70)

        data={}
        i=1
        con_obj = sqlite3.connect(database= 'bank.sqlite')
        cur_obj=con_obj.cursor()
        cur_obj.execute("select * from txn where txn_acno=?",(input_acn,))

        for tup in cur_obj:
            data[f"{i}"]= {"Txn Id": tup[0], "Txn Amt":tup[4], "Txn Date": tup[3],"Txn Type":tup[2],"Updated Bal":tup[5]}
            i+=1

        con_obj.close()

        # Create Table Model
        model = TableModel()
        model.importDict(data)  # Load data into the model

        # Create Table Canvas inside Frame (Important Fix)
        table = TableCanvas(frame, model=model, editable=True)
        table.show()


    # creating button in user screen of 'check balance'
    acn_details_button = Button(win,text= 'Account Detail',font= ('veranda',13,'bold'),bg= '#57f29d',bd=4,width = 11,command= account_details__click)
    acn_details_button.place(x=12, y= 195)

    # creating button in user screen of 'update details
    update_details_button = Button(win,text= 'Update Details',font= ('veranda',13,'bold'),bg= 'white',bd=4, width = 11,fg= 'black',command= update_details__click)
    update_details_button.place(x= 12, y= 270)

    # creating button in user screen of 'deposit'
    deposit_button = Button(win,text= 'Deposit',font= ('veranda',13,'bold'),bg= '#f25757',bd=4, width = 11,command= deposit__click)
    deposit_button.place(x=12, y= 345)

    # creating button in user screen of 'withdrwal'
    withdrawl_button = Button(win,text= 'Withdrawl',font= ('veranda',13,'bold'),bg= '#e3f257',bd=4, width = 11,command= withdrawl__click)
    withdrawl_button.place(x=12, y= 420)

    # creating button in user screen of 'transfer'
    transfer_button = Button(win,text= 'Transfer',font= ('veranda',13,'bold'),bg= 'light pink',bd=4, width = 11,command= transfer__click)
    transfer_button.place(x=12, y= 490)

    # creating button in user screen of 'txn history'
    txn_history_button = Button(win,text= 'Txn History',font= ('veranda',13,'bold'),bg= '#5ce0de',bd=4, width = 11,command= txn_history_click)
    txn_history_button.place(x=12, y= 565)


main_screen()
win.mainloop()
