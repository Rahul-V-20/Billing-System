import tkinter as tk
from tkinter import messagebox
import random
import pickle

class LoginOrSignupPage(tk.Tk):

    try:
        
        data_file = open("data.dat","rb")
        
    except:
        
        data_file = open("data.dat","wb")
        pickle.dump({},data_file)
        data_file.close()
        data_file=open("data.dat","rb")

    DATA = pickle.load(data_file)
    print("LOG IN STARTUP",DATA)
    data_file.close()

    def __init__(self):
        super().__init__()
        self.refresh()
        

    def refresh(self):
        try:
            
            self.clear_screen(self)
        except:
            pass

        

        
        
        self.frame = tk.Frame(master = self, width =300,height = 250)
        self.frame.pack()        

        self.button_login = tk.Button(master = self.frame,text = "Login",font = 20,width = 20,height = 2,
                                      command = self.login_button_clicked)
        self.button_login.place(x=60,y=60)
        self.button_signup = tk.Button(master = self.frame,text = "Signup",font = 20,width = 20,height = 2,
                                       command = self.signup_button_clicked)
        self.button_signup.place(x=60,y=120)
        

    def signup_button_clicked(self):

        self.clear_screen(self.frame)
        self.text1 = tk.Entry(self, width =20)
        self.text_Username = tk.Label(master = self.frame, text = "Username")
        self.text_password = tk.Label(master = self.frame, text = "Password")
        self.text2 = tk.Entry(self, width =20,show = "*")
        self.button_signupcontinue = tk.Button(master = self.frame,text = "continue",font = 20,
                                               width = 10,height = 1,command= self.post_signup)
        self.text_cnfrmpass = tk.Label(master = self.frame, text = "Confirm Password")
        self.text3 = tk.Entry(self, width =20,show = "*")
        self.text_signupheader = tk.Label(master = self.frame, text = "SIGN UP")
        self.back = tk.Button(master = self.frame,text = "back",font = 20,width = 10,height = 1,
                              command= self.backbuttonclicked)
       
        
        
        self.text1.place(x=105,y=65)
        self.text_Username.place(x=25,y=65)
        self.text_password.place(x=25,y=100)
        self.text2.place(x=105,y=100)
        self.button_signupcontinue.place(x=50,y=180)
        self.text3.place(x=105,y=135)
        self.text_cnfrmpass.place(x=3,y=135)
        self.back.place(x=160,y=180)
        
        self.text_signupheader.place(x=125,y=25)

        
        

    def clear_screen(self,frame):

        for child in frame.winfo_children():
    
            child.destroy()
    def post_signup(self):
        
        if len(self.text1.get())== 0:
            messagebox.showerror("Invalid","username should not have 0 characters")
            return
        if self.text2.get() != self.text3.get():
            messagebox.showerror("Invalid","the confirmed  password does not match the password try again")
            return
        if len(self.text2.get()) <= 3:
            messagebox.showerror("invalid","passsword must have more than 3 characters")
            return
        try:
            f=eval(open("psst.txt","r").read())
            f[self.text1.get()]= self.text2.get()
        
            
            a=open("psst.txt","w")
            a.write(repr(f))
            a.close()
        except:
            a=open("psst.txt","w")
            f={}
            f[self.text1.get()]= self.text2.get()
            a.write(repr(f))
            a.close()


        messagebox.showinfo("Success","You are signed up and read to go")


    def backbuttonclicked(self):
        
        self.refresh()

    def login_button_clicked(self):
 
        self.clear_screen(self.frame)

        
        #self.frame['width'],self.frame['height'] = 350,300

        self.frame_login = tk.Frame(master = self.frame)
        

        #entries
        self.entry_name = tk.Entry(self.frame_login,font = 18)
        self.entry_password = tk.Entry(self.frame_login, show = "*",font = 18)
        self.login_continue_button = tk.Button(master = self.frame,text = "Continue",font = 20,width = 20,
                                               height = 2,command = self.post_login)
        #labels
        self.text_Username = tk.Label(master = self.frame_login, text = "Username",font=20).grid(row = 1,column = 1)
        self.text_Password = tk.Label(master = self.frame_login, text = "Password",font=20).grid(row = 2,column = 1)

        self.text_login_text = tk.Label(master = self.frame, text = "LOGIN",font = 50).place(x=120,y=30)

        self.text_blank = tk.Label(master = self.frame_login,text  = "  ").grid(row=1,column=2)
        self.entry_name.grid(row=1,column=3)
        self.entry_password.grid(row=2,column=3)
        self.frame_login.place(relx=0.5,rely=0.5,anchor = "center",relwidth = 0.8,relheight=0.5)
        self.login_continue_button.place(x = 50,y=120)
        self.enter_pressed_btn = False


    def post_login(self,add=0):

        try:

            file_pass = eval(open("psst.txt","r").read())

        except:
            print("LOG IN POST LOGIN error")
            return

        username = self.entry_name.get()
        password = self.entry_password.get()
        
        if username in file_pass :
            if file_pass[username] == password:
                
                try:
                    self.entries = len(self.DATA[username].keys())
                    #print(1)
                    #print(self.DATA[username][self.entries])
                    self.parse = len(self.DATA[username][self.entries].keys())
                    print(self.parse)
                    #print(2)
                    #print(self.DATA[username],self.DATA[username][self.entries])
                    #print(3)
                except Exception as e:
                    self.entries = 1
                    self.parse = 0
                    self.DATA[username]={self.entries:{}}
                    print(e,"ERROR SAN")
                    
                
                self.user=username

                self.post_login_screen()
            else:
                messagebox.showerror("UnU", "Invalid username or password")

        else:
            messagebox.showerror("UnU", "Invalid username or password")
    def post_login_screen(self):
        self.current_screen = "billing"
        self.clear_screen(self.frame)
        #self.DATA[self.user][self.parse]={}

        self.frame['width'] = 670
        self.frame['height'] = 500

        self.frame_top = tk.Frame(master = self.frame, width = 705, height = 50)
        self.frame_middle_billing = tk.Frame(master = self.frame, width = 705, height = 400)
        self.frame_middle_history = tk.Frame(master = self.frame, width = 705, height = 400)
        self.frame_bottom = tk.Frame(master = self.frame, width = 705, height = 50)

        self.frame_top.pack()
        self.frame_middle_billing.pack()
        self.frame_bottom.pack()

        self.optionmenu()

        self.misc = misc(self)

        tk.Label(master = self.frame_middle_billing,text = "Code").place(x = 10, y = 0)
        tk.Label(master = self.frame_middle_billing,text = "Product Name").place(x = 200, y = 0)
        tk.Label(master = self.frame_middle_billing,text = "Quantity").place(x = 420, y = 0)
        tk.Label(master = self.frame_middle_billing,text = "Rate").place(x = 540, y = 0)
        tk.Label(master = self.frame_middle_billing,text = "Price").place(x = 660, y = 0)

        for i in range(1,20):

            var1 = "self.text_"+str(i)+"_1 = tk.Text(master = self.frame_middle_billing,width = 15,height = 1,state = \"disabled\")"
            var2 = "self.text_"+str(i)+"_1.place(y = " + str((i)*20) + ",x = 10)"
            exec(var1)
            exec(var2)

            var1 = "self.entry_"+str(i)+"_2 = tk.Entry(master = self.frame_middle_billing,width = 50,state = \"disabled\")"
            var2 = "self.entry_"+str(i)+"_2.place(y = " + str((i)*20) + ",x = 105)"
            exec(var1)
            exec(var2)

            var1 = "self.entry_"+str(i)+"_3 = tk.Entry(master = self.frame_middle_billing,width = 15,state = \"disabled\")"
            var2 = "self.entry_"+str(i)+"_3.place(y = " + str((i)*20) + ",x = 410)"
            exec(var1)
            exec(var2)

            var1 = "self.entry_"+str(i)+"_4 = tk.Entry(master = self.frame_middle_billing,width = 15,state = \"disabled\")"
            var2 = "self.entry_"+str(i)+"_4.place(y = " + str((i)*20) + ",x = 505)"
            exec(var1)
            exec(var2)

            var1 = "self.text_"+str(i)+"_5 = tk.Text(master = self.frame_middle_billing,width = 15,height = 1,state = \"disabled\")"
            var2 = "self.text_"+str(i)+"_5.place(y = " + str((i)*20) + ",x = 600)"
            exec(var1)
            exec(var2)
        self.latest_billing_row = 1
        self.billing_entry_enabler()
        self.enter_pressed()

                
                
                    

  


    def billing_entry_enabler(self):
        #latest = "self.entry_"+str(self.latest_billing_row)+ "_
        for i in range(2,5):
            latest = "self.entry_"+str(self.latest_billing_row)+ "_"+str(i)+".configure(state = 'normal')"
            exec(latest)

    def verifier_billing(self,add=0):
        if not add:
            aa = "self.product_name = self.entry_"+str(self.latest_billing_row)+"_2.get() \nself.quantity = self.entry_"+str(self.latest_billing_row)+"_3.get() \nself.rate = self.entry_"+str(self.latest_billing_row)+"_4.get() "
            exec(aa)
        else:
            aa = "self.product_name = self.entry_1_2.get() \nself.quantity = self.entry_1_3.get() \nself.rate = self.entry_1_4.get() "
            exec(aa)
        try:
            if type(self.product_name) and type(eval(self.quantity))==int and type(eval(self.rate))==int:
                return 1
            return 0
        except:
            if add:
                return 0
            messagebox.showerror("ERROR baka >:(","Values not satisfactory \n ERROR 301.")
            return 0
        

    def clear_screen(self,frame):

        for child in frame.winfo_children():
            child.destroy()
            
    def optionmenu(self):
        
        variable = tk.StringVar(self)
        variable.set("billing") # default value
        

        self.option= tk.OptionMenu(self.frame_top, variable,"billing","history",command = self.option_function)
        self.option.config(width = 30,height=1)
        self.option.place(x=1,y=1)
    def next_entry(self,event):
        #print("name = self.entry_"+str(self.latest_billing_row)+"_2.get() \nquantity = self.entry_"+str(self.latest_billing_row)+"_3.get() \nrate = self.entry_"+str(self.latest_billing_row)+"_4.get()")
        
        ret = self.verifier_billing()
        if ret:
            self.latest_billing_row+=1
            self.pricencode()
            self.billing_entry_enabler()
            self.enter_pressed()
            self.enter_pressed_btn = True
            
    def enter_pressed(self):
        try:
            var1 = "self.entry_"+str(self.latest_billing_row)+"_2.bind(\"<Return>\",self.next_entry)"
            exec(var1)
            var1 = "self.entry_"+str(self.latest_billing_row)+"_3.bind(\"<Return>\",self.next_entry)"
            exec(var1)
            var1 = "self.entry_"+str(self.latest_billing_row)+"_4.bind(\"<Return>\",self.next_entry)"
            exec(var1)
            
            
        except:
            messagebox.showerror("ERROR baka >:(","Values not satisfactory.")
    def pricencode(self):

        randcode = ''
        alphabets = []
        for i in range(97,97+27):
            alphabets.append(chr(i))       
        
        for i in range(1,6):
            
            randcode+= alphabets[random.randint(0,25)]
            
        var1 = "self.text_"+str(self.latest_billing_row-1)+"_1.configure(state = 'normal')"
        exec(var1)
        var1 = "self.text_"+str(self.latest_billing_row-1)+"_1.insert(tk.END,randcode)"
        exec(var1)
        var1 = "self.text_"+str(self.latest_billing_row-1)+"_1.configure(state = 'disabled')"
        exec(var1)
        var1 = "self.text_"+str(self.latest_billing_row-1)+"_5.configure(state = 'normal')"
        exec(var1)
        exec("self.price = eval(self.entry_"+str(self.latest_billing_row-1)+"_3.get())*eval(self.entry_"+str(self.latest_billing_row-1)+"_4.get())")
        var1 = "self.text_"+str(self.latest_billing_row-1)+"_5.insert(tk.END,self.price)"
        exec(var1)
        var1 = "self.text_"+str(self.latest_billing_row-1)+"_5.configure(state = 'disabled')"
        exec(var1)

        self.misc.totalprice.configure(state = "normal")
        var1= (self.misc.totalprice.get("1.0",tk.END))
        #print(repr(var1),self.parse)
        
        if var1 == None or var1 == '\n':
            var1 = 0
        else:
            var1 = eval(var1)
        self.misc.totalprice.delete("1.0",tk.END)
        self.misc.totalprice.insert(tk.END,str(self.price+var1))
        self.misc.totalprice.configure(state = "disabled")
        
        #self.DATA[self.user][self.parse][self.latest_billing_row-1] = [randcode,self.product_name,self.quantity,self.rate,self.price]
        '''
        try:
            print(self.DATA[self.user][self.entries][self.parse])
        except:
            pass
        '''
        #print(self.DATA)
        #self.entries+=1
        self.parse+=1
        self.DATA[self.user][self.entries][self.parse] = [randcode,self.product_name,self.quantity,self.rate,self.price]
        
        #self.DATA[self.user][self.entries] = {}
    def option_function(self,event):

        if event == "history":
            if self.current_screen == "history":
                return
            #self.clear_screen(self.frame_bottom)
            #self.clear_screen(self.frame_middle_billing)
            self.misc.addbutton.place_forget()
            self.frame_middle_billing.pack_forget()
            self.frame_bottom.pack_forget()
            
            self.current_screen = "history"

            self.frame_middle_history.pack()
            self.frame_bottom.pack()
            '''
            try:
                self.history_text.insert(tk.END,'')
            except:
            '''
            try:
                self.history_text.destroy()
            except:
                pass
            self.history_text = tk.Text(master = self.frame_middle_history,height = 30,width = 80)
            self.history_text.pack()
            a = True
            #if not a:
                
            #print(self.DATA)
            self.history_text.delete('1.0', "end")
            
            self.insert_history_text("HISTORY!!!")
            for i in self.DATA[self.user]:
                self.insert_history_text("=======================")
                self.insert_history_text("Bill "+str(i))
                self.insert_history_text("=======================")
                for j in self.DATA[self.user][i]:
                    
                    self.insert_history_text("Item "+str(j))
                    var3 = 1
                    for k in self.DATA[self.user][i][j]:
                        self.insert_history_text(str(var3)+". "+str(k))
                        var3+=1 
                    
        else:
            if self.current_screen == "billing":
                return
            #self.clear_screen(self.frame_bottom)
            #self.clear_screen(self.frame_middle_billing)
            self.misc.addbutton.place(x=550,y=4)
            self.frame_middle_history.pack_forget()
            self.frame_bottom.pack_forget()
            self.frame_middle_billing.pack()
            self.frame_bottom.pack()
            self.current_screen = "billing"
    def insert_history_text(self,text):
        if self.current_screen != "history":
            return
        self.history_text.configure(state = "normal")
        self.history_text.insert(tk.END,text+"\n")
        self.history_text.configure(state="disabled")
      

class misc():

    def __init__(self,master):
        self.master=master
        self.addbutton=tk.Button(master = self.master.frame,text = "add",font = 20,width = 10,
                                               height = 1,command = self.addcmd)
        self.totalbox()
        
        self.addbutton.place(x=550,y=4)
    def totalbox(self):
        self.totalprice= tk.Text(master=self.master.frame_bottom,width=10, height=1,state="disabled")
        self.totalprice.place(x=600,y=0)
        self.totaltext=tk.Label(master = self.master.frame_bottom, text = "Total",font=20)
        self.totaltext.place(x=550,y=0)
        
    def addcmd(self):
        if self.master.verifier_billing(add=1) and self.master.enter_pressed_btn :
            self.master.latest_billing_row = 1
            self.master.post_login_screen()
            with open("data.dat","wb") as data_file:
                pickle.dump(self.master.DATA,data_file)
            messagebox.showinfo("SUCCESS :D", "Data billed successfully!")
            self.master.entries+=1
            self.master.DATA[self.master.user][self.master.entries]={}
            self.master.parse=0
        else:
            messagebox.showerror("Values not valid :<","The values you entered arent satisfactory or empty. Please input the right values >:(")
            
if __name__ == "__main__":

    a = LoginOrSignupPage()
    a.mainloop()
