#@ayuboid - Salahuddin[@]protonmail.ch/com
from tkinter import * #import all from tkinter
import subprocess

window=Tk()#window.geometry("400x200")#command mai function k saat () nahi dalni
window.title("Wifi")#title

class wifi:

    def user(self):
        x_1=subprocess.Popen("netsh wlan show profiles",shell=True,stdout=subprocess.PIPE) #run IDE as admin
        stdout=x_1.communicate()[0]
        return stdout

    def password_1(self,name):
        r='1'
        for pswd in name:
            #remove spaces from both sides [pswd[1].strip()]
            CREATE_NO_WINDOW= 0x08000000
            x_1=subprocess.Popen(r'netsh wlan show profiles name="%s" key=clear' %pswd[1].strip(),shell=True,stdout=subprocess.PIPE) #run IDE as admin
            #-----> Important NOTe:if there are spaces between the values then send raw strings FORMAT[r'"<type>"' %<variable>]
            #----->Make sure remove unwanted space in names
            
            #communicate() method is used to get the output from pipe
            stdout=x_1.communicate()[0]
            stdout=stdout.decode().splitlines()
            U="u"+r #use can use loop through list also
            for line in stdout:
                if "Key Content" in line:
                    #print("Username : %s\nPassword : %s " % (pswd[1],line.split(":")[1])) 
                    self.labels(U,r,pswd[1],line)
            r=str(int(r)+1)
        U1=Label(window,text="@ayuboid - Salahuddin@pm.me")
        U1.grid(row=int(r),columnspan=2)

    def labels(self,U,r,pswd,line):
        U=Label(window,text=pswd)
        U.grid(row=int(r),column=0)
        U=Text(window,height=1,width=20)
        U.grid(row=int(r),column=1)
        U.insert(END,line.split(":")[1])

class wifi_1(wifi):

    def username(self):
        x_1=self.user()
        name_list=[]
        #Decode (binary to utf8) and then split it by lines
        x_1=x_1.decode().splitlines()
        #Extract the string from list
        for l in x_1:
        #Check For the string in given line
            if "All User Profile" in l:
                #Split the current line from : e-g test : OK -----> ['test','OK'] and append to list
                name_list.append(l.split(":"))
        return name_list

    def password(self):
        name_list=self.username()
        name=self.password_1(name_list)

b=wifi_1()
#Defaults
U1=Label(window,text="< Wifi >")
U1.grid(row=0,column=0)
U1=Label(window,text="< Password >")
U1.grid(row=0,column=1)
#print(b.username()) GET USERNAMES
#You can also use os.system
b1=Button(window ,text="Show", command=b.password,borderwidth=4,foreground="Green")
b1.grid(row=0,column=3)
window.mainloop()
