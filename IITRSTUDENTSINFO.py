from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("871x764+590+143")
root.title("IITR STUDENTS INFO")

frame0 = Frame(root, borderwidth= "2", width= 845, relief=GROOVE)
frame0.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.97)
lbl0 = Label(frame0, text= "Students Info", font=('Arial Rounded MT Bold',19,'bold','underline'),width=812,anchor=CENTER)
lbl0.place(relx=0.01, rely=0.13, height=56, width=812)

frame1 = Frame(root, borderwidth="2", width=845, relief=GROOVE)
frame1.place(relx=0.01, rely=0.12, relheight=0.14, relwidth=0.97)

EnrollmentNo = Label(frame1, font=('Arial Rounded MT Bold',12,'bold'),text= "ENTER YOUR ENROLLMENT NO :- ",width=372)
EnrollmentNo.place(relx=0.01, rely=0.29, height=36, width=372)

Enroll = StringVar()
txtEnroll = Entry(frame1, width=244, textvariable=Enroll, justify='left',font=('Arial Rounded MT Bold',14,'bold'))
txtEnroll.place(relx=0.5, rely=0.19,height=54, relwidth=0.29)

frame2 = Frame(root, borderwidth= "2", width= 845, relief=GROOVE)
frame2.place(relx=0.01, rely=0.26, relheight=0.73, relwidth=0.97)

Name = Label(frame2, text=" ", relief=GROOVE, anchor=W,width=822,font=('Arial Rounded MT Bold',12,'bold','italic'))
Name.place(relx=0.01, rely=0.04, height=66, width=822)

RoomNo = Label(frame2, text=" ", relief=GROOVE, anchor=W,width=822,font=('Arial Rounded MT Bold',12,'bold','italic'))
RoomNo.place(relx=0.01, rely=0.18, height=66, width=822)

EmailID = Label(frame2, text=" ", relief=GROOVE, anchor=W,width=822,font=('Arial Rounded MT Bold',12,'bold','italic'))
EmailID.place(relx=0.01, rely=0.32, height=66, width=822)

Branch =  Label(frame2, text=" ", relief=GROOVE, anchor=NW, width=822,font=('Arial Rounded MT Bold',12,'bold','italic'))
Branch.place(relx=0.01, rely=0.47, height=246, width=822)


Copyrightsymbol = Label(frame2,text="© Akash Gajare", font=('segoe UI',9),foreground="#3a3a3a",width=122)
Copyrightsymbol.place(relx=0.84, rely=0.92, height=36, width=122)

def studentsInfo():
    EnrollNo = Enroll.get()
    url = "http://students.iitr.ac.in/" + EnrollNo

    r = requests.get(url)
    r_text = r.text
    soup = BeautifulSoup(r_text, "html.parser", )

    EnrollName = soup.find('a', {'class': 'name'})
    EnrollBranch = soup.find('a', {'class': 'branch'})
    EnrollRoomNo = soup.find('a', {'class': 'address'})
    EnrollEmail = soup.find('a', {'class': 'email'})


    Name.configure(text= "Name : " + EnrollName.text)
    RoomNo.configure(text="Room No : " + EnrollRoomNo.text)
    EmailID.configure(text="Email ID : " + EnrollEmail.text)
    Branch.configure(text="Branch : " + EnrollBranch.text)

button1 = Button(frame1, text="SEARCH", width=116,command=studentsInfo)
button1.place(relx=0.83, rely=0.19, height=53, width=116)


root.mainloop()