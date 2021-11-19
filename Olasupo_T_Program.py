import tkinter as tk
import random
import time
from PIL import Image, ImageTk #PIL required
from datetime import datetime

title_font=("Microsoft Jhenghei UI Light",35)
text=("Microsoft Jhenghei UI Light",10)
#creates the window for the tkinter program
class MathsApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame=None
        self.switch_frame(StartPage)#sets Startpage as the first page
        self.title("Maths Revision App")#gets window a title
        self.geometry("800x500")#sets the window size
        self.configure(bg="white")#sets the window colour
        

    def switch_frame(self, frame_class):
        #Destroys current frame and replaces it with a new one.
        new_frame=frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame=new_frame
        self._frame.pack(fill="both",expand=True)

        
#the first page class
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Welcome!", font=title_font, bg="white", fg="#004d99")#creates label widget called "welcome"
        lbl.place(x=30, y=20)#places widget onto window        
        btn=tk.Button(self, text="Revise Topic", height=15, width=25, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevPMS))
        btn.place(x=100, y=125)#when button is pressed, switch to "RevPMS"
        btn2=tk.Button(self, text="Practice Test", height=6, width=50, fg="white", bg="#004d99", command=lambda:master.switch_frame(TestPMS))
        btn2.place(x=325, y=125)
        btn3=tk.Button(self, text="Test History", height=6, width=50, fg="white", bg="#004d99", command=lambda:master.switch_frame(HistPMS))
        btn3.place(x=325, y=260)
        exit=tk.Button(self, text="Exit", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.destroy())
        exit.place(x=650, y=400)
#the revision menu
class RevPMS(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Revise?", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        btn=tk.Button(self, text="Pure | Algebra, Inequalities etc", height=3, width=85, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevPure))
        btn.place(x=100, y=125)
        btn2=tk.Button(self, text="Mechanics | Forces, Motion etc", height=3, width=85, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevMech))
        btn2.place(x=100, y=210)
        btn3=tk.Button(self, text="Statistics | Probability, Hypothesis Testing etc", height=3, width=85, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevStats))
        btn3.place(x=100, y=295)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(StartPage))
        back.place(x=650, y=400)
#the test menu
class TestPMS(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Test?", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        btn=tk.Button(self, text="Pure | Algebra, Inequalities etc", height=3, width=85, fg="white", bg="#004d99", command=lambda:master.switch_frame(startPure))
        btn.place(x=100, y=125)
        btn2=tk.Button(self, text="Mechanics | Forces, Motion etc", height=3, width=85, fg="white", bg="#004d99", command=lambda:master.switch_frame(startMech))
        btn2.place(x=100, y=210)
        btn3=tk.Button(self, text="Statistics | Probability, Hypothesis Testing etc", height=3, width=85, fg="white", bg="#004d99", command=lambda:master.switch_frame(startStats))
        btn3.place(x=100, y=295)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(StartPage))
        back.place(x=650, y=400)

#test history menu
class HistPMS(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Review?", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        lbl2=tk.Label(self, text="Find test history in the 'testhistory' text file.", font=("Microsoft Jhenghei UI Light", 15), bg="white", fg="black")
        lbl2.place(x=30, y=100)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(StartPage))
        back.place(x=650, y=400)
        
#the pure maths revision menu
class RevPure(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self,text="Pure Maths",font=title_font,bg="white",fg="#004d99")
        lbl.place(x=30, y=20)
        btn=tk.Button(self,text="Chapter 1 | Algebra", height=1,width=85,fg="white",bg="#004d99",command=lambda:[loadImages(1),master.switch_frame(page1)]) 
        btn.place(x=100, y=150)
        btn2=tk.Button(self,text="Chapter 2 | Polynomials & Binary Theorem",height=1,width=85,fg="white",bg="#004d99",command=lambda:[loadImages(2),master.switch_frame(page1)])
        btn2.place(x=100, y=200)
        btn3=tk.Button(self, text="Chapter 3 | Trigonometry", height=1, width=85,fg="white", bg="#004d99", command=lambda:[loadImages(3), master.switch_frame(page1)])
        btn3.place(x=100, y=250)
        btn4=tk.Button(self, text="Chapter 4 | Differentiation & Intergration", height=1, width=85, fg="white", bg="#004d99", command=lambda:[loadImages(4), master.switch_frame(page1)])
        btn4.place(x=100, y=300)
        btn5=tk.Button(self, text="Chapter 5 | Exponentials & Logarithms", height=1, width=85, fg="white", bg="#004d99", command=lambda:[loadImages(5), master.switch_frame(page1)])
        btn5.place(x=100, y=350)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevPMS))
        back.place(x=650, y=400)
#the mechanics revision menu
class RevMech(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Mechanics", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        btn=tk.Button(self, text="Chapter 6 | Vectors", height=1, width=85,fg="white", bg="#004d99", command=lambda:[loadImages(6), master.switch_frame(page1)])
        btn.place(x=100, y=150)
        btn2=tk.Button(self, text="Chapter 7 | Units and Kinematics", height=1, width=85,fg="white", bg="#004d99", command=lambda:[loadImages(7), master.switch_frame(page1)])
        btn2.place(x=100, y=200)
        btn3=tk.Button(self, text="Chapter 8 | Forces & Newtons Laws", height=1, width=85,fg="white", bg="#004d99", command=lambda:[loadImages(8), master.switch_frame(page1)])
        btn3.place(x=100, y=250)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevPMS))
        back.place(x=650, y=400)
#the statistics revision menu
class RevStats(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Statistics", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        btn=tk.Button(self, text="Chapter 9 | Collect, Representing & Interpret Data", height=1, width=85,fg="white", bg="#004d99", command=lambda:[loadImages(9), master.switch_frame(page1)])
        btn.place(x=100, y=150)
        btn2=tk.Button(self, text="Chapter 10 | Probability & Discrete Random Variables", height=1, width=85,fg="white", bg="#004d99", command=lambda:[loadImages(10), master.switch_frame(page1)])
        btn2.place(x=100, y=200)
        btn3=tk.Button(self, text="Chapter 11 | Hypothesis Testing", height=1, width=85,fg="white", bg="#004d99", command=lambda:[loadImages(11), master.switch_frame(page1)])
        btn3.place(x=100, y=250)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevPMS))
        back.place(x=650, y=400)
#the pure maths test start page
class startPure(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="white")
        lbl=tk.Label(self, text="Test your knowledge: Pure", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=90)
        txt.config(state="normal")
        txt.insert(tk.INSERT,"The questions in this test will be taken from all chapters of the Pure Maths section. If you have  not already, you may want to briefly read the contents of the Pure section. This test will be timed any you will be able to see how long it has taken for you to complete the test. Make sure that your answers do not have spaces in them (ie 'x+3' instead of       'x + 3'). Make sure to give your answer in the for the question asks, if it does ask.")
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        btn=tk.Button(self, text="Start", height=3, width=15, fg="white", bg="#004d99", command=lambda:[getQuestions(1),startTime(),master.switch_frame(q1)])
        btn.place(x=350, y=400)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(TestPMS))
        back.place(x=650, y=400)
#the mechanics test start page
class startMech(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="white")
        lbl=tk.Label(self, text="Test your knowledge: Mechanics", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=90)
        txt.config(state="normal")
        txt.insert(tk.INSERT,"The questions in this test will be taken from all chapters of the Mechanics section. If you have  not already, you may want to briefly read the contents of the Mechanics section. This test will be timed any you will be able to see how long it has taken for you to complete the test. Make sure that your answers do not have spaces in them (ie 'x+3' instead of       'x + 3'). Make sure to give your answer in the for the question asks, if it does ask.")
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        btn=tk.Button(self, text="Start", height=3, width=15, fg="white", bg="#004d99", command=lambda:[getQuestions(2),startTime(),master.switch_frame(q1)])
        btn.place(x=350, y=400)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(TestPMS))
        back.place(x=650, y=400)
#the statistics test start page
class startStats(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="white")
        lbl=tk.Label(self, text="Test your knowledge: Statistics", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=90)
        txt.config(state="normal")
        txt.insert(tk.INSERT,"The questions in this test will be taken from all chapters of the Statistics section. If you have  not already, you may want to briefly read the contents of the Statistics section. This test will be timed any you will be able to see how long it has taken for you to complete the test. Make sure that your answers do not have spaces in them (ie 'x+3' instead of  'x + 3'). Make sure to give your answer in the for the question asks, if it does ask.")
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        btn=tk.Button(self, text="Start", height=3, width=15, fg="white", bg="#004d99", command=lambda:[getQuestions(3),startTime(),master.switch_frame(q1)])
        btn.place(x=350, y=400)
        back=tk.Button(self, text="Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(TestPMS))
        back.place(x=650, y=400)
        
#question 1
class q1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 1", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)#the text box that displays the question
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[0][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)#the entry box the user writes in
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self, master,ans.get()))
        btn.place(x=650, y=400)
#question 2
class q2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 2", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[1][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 3
class q3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 3", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[2][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 4
class q4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 4", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[3][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 5
class q5(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 5", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[4][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 6
class q6(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 6", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[5][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 7
class q7(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 7", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[6][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 8
class q8(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 8", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[7][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 9
class q9(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 9", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[8][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#question 10
class q10(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Question 10", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        txt=tk.Text(self, height=7, width=70)
        txt.config(state="normal")
        txt.insert(tk.INSERT,qlist[9][0])
        txt.config(state="disabled")
        txt.place(x=35,y=125)
        ans=tk.Entry(self)
        ans.place(x=650, y=350,height=25)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:validateAns(self,master,ans.get()))
        btn.place(x=650, y=400)
#the page that displays the users results
class ResultPage(tk.Frame):
    def __init__(self, master):
        global totalTime
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Results", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        mins=round(((totalTime)/60), 3)
        lbl2=tk.Label(self, text=("You answered "+str(correct)+" out of 10 questions correctly."), font=("Microsoft Jhenghei UI Light", 15), bg="white", fg="black")
        lbl2.place(x=30, y=100)
        lbla=tk.Label(self, text=("Completed in "+str(mins)+" minutes, or "+str(totalTime)+" seconds."), font=("Microsoft Jhenghei UI Light", 15), bg="white", fg="black")
        lbla.place(x=30, y=140)#following lines display the results for each question
        lbl3=tk.Label(self, text=("Question 1s answer was "+str(results[0])+". Completed in "+str(times[0])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=180)
        lbl4=tk.Label(self, text=("Question 2s answer was "+str(results[1])+". Completed in "+str(times[1])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=200)
        lbl5=tk.Label(self, text=("Question 3s answer was "+str(results[2])+". Completed in "+str(times[2])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=220)
        lbl6=tk.Label(self, text=("Question 4s answer was "+str(results[3])+". Completed in "+str(times[3])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=240)
        lbl7=tk.Label(self, text=("Question 5s answer was "+str(results[4])+". Completed in "+str(times[4])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=260)
        lbl8=tk.Label(self, text=("Question 6s answer was "+str(results[5])+". Completed in "+str(times[5])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=280)
        lbl9=tk.Label(self, text=("Question 7s answer was "+str(results[6])+". Completed in "+str(times[6])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=300)
        lbla=tk.Label(self, text=("Question 8s answer was "+str(results[7])+". Completed in "+str(times[7])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=320)
        lblb=tk.Label(self, text=("Question 9s answer was "+str(results[8])+". Completed in "+str(times[8])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=340)
        lblc=tk.Label(self, text=("Question 10s answer was "+str(results[9])+". Completed in "+str(times[9])+" seconds."), font=text, bg="white", fg="black").place(x=30, y=360)
        btn=tk.Button(self, text="Back to Main Menu", height=3, width=15, fg="white", bg="#004d99", command=lambda:[refresh(),master.switch_frame(StartPage)])
        btn.place(x=650, y=400)
        btn2=tk.Button(self, text="Save Result", height=3, width=15, fg="white", bg="#004d99", command=lambda:save())#saves results
        btn2.place(x=650, y=200)

class page1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        load=Image.open(images[0])#calls the first image onto the page
        render=ImageTk.PhotoImage(load)
        img=tk.Label(self, image=render)
        img.image=render
        img.place(x=50,y=30)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page2))
        btn.place(x=650, y=420)
        btn2=tk.Button(self, text="Back to Revise", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(RevPMS))
        btn2.place(x=40, y=420)

class page2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        load=Image.open(images[1])#calls the second image onto the page
        render=ImageTk.PhotoImage(load)
        img=tk.Label(self, image=render)
        img.image=render
        img.place(x=50,y=30)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page3))
        btn.place(x=650, y=420)
        btn2=tk.Button(self, text="Previous", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page1))
        btn2.place(x=40, y=420)

class page3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        load=Image.open(images[2])#calls the third image onto the page
        render=ImageTk.PhotoImage(load)
        img=tk.Label(self, image=render)
        img.image=render
        img.place(x=50,y=30)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page4))
        btn.place(x=650, y=420)
        btn2=tk.Button(self, text="Previous", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page2))
        btn2.place(x=40, y=420)

class page4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        load=Image.open(images[3])#calls the fourth image onto the page
        render=ImageTk.PhotoImage(load)
        img=tk.Label(self, image=render)
        img.image=render
        img.place(x=50,y=30)
        btn=tk.Button(self, text="Next", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page5))
        btn.place(x=650, y=420)
        btn2=tk.Button(self, text="Previous", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page3))
        btn2.place(x=40, y=420)

class page5(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        load=Image.open(images[4])#calls the fifth image onto the page
        render=ImageTk.PhotoImage(load)
        img=tk.Label(self, image=render)
        img.image=render
        img.place(x=50,y=30)
        btn=tk.Button(self, text="Previous", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(page4))
        btn.place(x=40, y=420)

class errorPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="white")
        lbl=tk.Label(self, text="Please answer the question", font=title_font, bg="white", fg="#004d99")
        lbl.place(x=30, y=20)
        lbl2=tk.Label(self, text="You have not typed in an answer. Please give an answer", font=("Microsoft Jhenghei UI Light", 15), bg="white", fg="black")
        lbl2.place(x=30, y=100)
        lbl3=tk.Label(self, text="for every single question.", font=("Microsoft Jhenghei UI Light", 15), bg="white", fg="black")
        lbl3.place(x=30, y=125)
        btn2=tk.Button(self, text="Go Back", height=3, width=15, fg="white", bg="#004d99", command=lambda:master.switch_frame(questionpages[currentQ]))
        btn2.place(x=40, y=400)

questionpages=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
currentQ=0

def validateAns(self, master, ans):
    global questionpages,currentQ
    if ans=="" or ans==" ":
        self.master.switch_frame(errorPage)
    else:
        if currentQ==9:
            checkAns(ans, currentQ)
            getTimes()
            self.master.switch_frame(ResultPage)
        else:
            checkAns(ans, currentQ)
            getTimes()
            currentQ=currentQ+1
            self.master.switch_frame(questionpages[currentQ])


then=0
def startTime():
    global then
    then = time.time() #collects the current time, in this case the time the test begins.

times=[]
totalTime=0
def getTimes():
    global times, then, totalTime
    now= time.time() #collects time that the current question has been finished
    qtime=(now-then)//1 #calculates the time spent on the question
    times.append(qtime) #adds to list
    totalTime=totalTime+qtime #adds to tally
    then=now
    
    
           
qlist=0
subject=0
def getQuestions(x):
    global qlist, subject
    qlist=[0,0,0,0,0,0,0,0,0,0]#creates empty question list
    noschosen=[]
    if x==1:
        with open("purequestions.txt","r") as f:
            lines=f.read().strip().split("\n")#takes from pure file if the test is pure
        subject=1
    elif x==2:
        with open("mechanicsquestions.txt","r") as f:
            lines=f.read().strip().split("\n")#takes from mechanics file if the test is mechanics
        subject=2
    elif x==3:
        with open("statisticsquestions.txt","r") as f:
            lines=f.read().strip().split("\n")#takes from statistics file if the test is statistics
        subject=3
    i=0
    while i<len(qlist):
        chosen=False
        n=random.randint(1,50)#chooses random n from 1 to 50
        while n in noschosen:
            n=random.randint(1,50)#chooses again if the number has already been chosen
        qline=2*n-1#makes number odd
        noschosen.append(n)#adds number to the list of chosen ones
        qlist[i]=(lines[qline],lines[qline+1])#retrieves the line of the random odd number, and also the line below it
        i=i+1#increment

results=[]
correct=0
def checkAns(ans, questionAns):
    global results, correct
    if ans == qlist[questionAns][1]:
        results.append("right")#adds right to the array in the question order
        correct=correct+1
    else:
        results.append("wrong")#adds wrong to the array in the question order


def refresh():
    global qlist,results, correct, times, totalTime, currentQ
    qlist=0
    results=[]
    correct=0
    times=[]
    totalTime=0
    currentQ=0

images=[]
def loadImages(x):
    global images
    if x==1:
        images=["ch1p1.png","ch1p2.png","ch1p3.png","ch1p4.png","ch1p5.png"]#ch1 images
    elif x==2:
        images=["ch2p1.png","ch2p2.png","ch2p3.png","null.png","null.png"]#ch2 images
    elif x==3:
        images=["ch3p1.png","ch3p2.png","null.png","null.png","null.png"]#ch3 images
    elif x==4:
        images=["ch4p1.png","ch4p2.png","ch4p3.png","null.png","null.png"]#ch4 images
    elif x==5:
        images=["ch5p1.png","ch5p2.png","null.png","null.png","null.png"]#ch5 images
    elif x==6:
        images=["ch6p1.png","ch6p2.png","null.png","null.png","null.png"]#ch6 images
    elif x==7:
        images=["ch7p1.png","ch7p2.png","ch7p3.png","null.png","null.png"]#ch7 images
    elif x==8:
        images=["ch8p1.png","ch8p2.png","null.png","null.png","null.png"]#ch8 images
    elif x==9:
        images=["ch9p1.png","ch9p2.png","ch9p3.png","null.png","null.png"]#ch9 images
    elif x==10:
        images=["ch10p1.png","ch10p2.png","null.png","null.png","null.png"]#ch10 images
    elif x==11:
        images=["ch11p1.png","ch11p2.png","null.png","null.png","null.png"]#ch11 images


def save():
    global correct, totalTime, subject
    date=(str(datetime.now())) #collect current date
    if subject==1:
        testType="Pure" #recognise the test to be on pure maths
    elif subject==2:
        testType="Mechanics" #recognise the test to be on mechanics
    elif subject==3:
        testType="Statistics" #recognise the test to be on statistics
    appendFile=open('testhistory.txt','a') #open test history file, to add to it
    appendFile.write('\n') #\n means new line
    appendFile.write(date) #write date
    appendFile.write('\n')
    appendFile.write('Test on topic: '+testType+".") #write the test type
    appendFile.write('\n')
    appendFile.write('Score: '+str(correct)+'/10') #write the score
    appendFile.write('\n')
    appendFile.write('Time to complete: '+str(totalTime)+' seconds.') #write the time taken
    appendFile.write('\n')
    appendFile.write('------------------')
            
        
if __name__ == "__main__":
    app = MathsApp()
    app.mainloop()
        
