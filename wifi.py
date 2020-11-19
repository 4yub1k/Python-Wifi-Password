#@ayuboid --- salahuddin[@]protonmail.ch/com
import subprocess
class t:
    def user(self):
        x_1=subprocess.Popen("netsh wlan show profiles",stdout=subprocess.PIPE) #run IDE as admin
        stdout,stdin=x_1.communicate()
        return stdout

    def password_1(self,name):
        for pswd in name:
            #remove spaces from both sides [pswd[1].strip()]
            x_1=subprocess.Popen(r'netsh wlan show profiles name="%s" key=clear' %pswd[1].strip(),stdout=subprocess.PIPE) #run IDE as admin
            #-----> Important NOTe:if there are spaces between the values then send raw strings FORMAT[r'"<type>"' %<variable>]
            #----->Make sure remove unwanted space in names
            
            #communicate() method is used to get the output from pipe
            stdout=x_1.communicate()[0]
            stdout=stdout.decode().splitlines()
            for line in stdout:
                if "Key Content" in line:
                    print("Username : %s\nPassword : %s " % (pswd[1],line.split(":")[1]))
class t1(t):
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

b=t1()
b.password()
#print(b.username()) GET USERNAMES
#You can also use os.system
