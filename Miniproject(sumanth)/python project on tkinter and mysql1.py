from tkinter import *
from tkinter import messagebox
from functools import partial
import mysql.connector

def call_result(rollno, name):
    global current_rollno, current_name
    r = rollno.get()
    n = name.get().lower()
    current_rollno=r
    current_name=n

   

    
    if r == "" or n == "":
        messagebox.showinfo("Input Error", "Please enter the all details")
        return

    if (r, n) in [("111", "mani"), ("112", "sumanth"), ("113", "abhi"), ("114", "sravya"), ("115", "akhila")]:
        show_exam_instructions()
    else:
        messagebox.showwarning("Input Error", "you are not eligiable")
    
                # Open new Toplevel window for eligibility
def show_exam_instructions():
    
    
    top = Toplevel()
    top.title("EXAM DETIALS")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 70
    top.geometry(f"{x}x{y}")

    
    top.config(bg="lightgreen")
    Label(top, text="You are eligible to write the exam", fg="blue", bg="lightgreen",font=("Arial",16)).pack(pady=20)
    Label(top,text="-------------------------------------------------------------------------Note---------------------------------------------------------------------------",fg="blue",bg="lightgreen",font=("Arial",16)).pack(pady=21)
    Label(top,text="*In This Examination Contains Three Sections",fg="blue",bg="lightgreen",font=("Arial",16)).pack(pady=22)
    Label(top,text="1)Arithmetic consists 10 Questions",fg="blue",bg="lightgreen",font=("Arial",16)).pack(pady=23)
    Label(top,text="2)Reasoning consists 10 Questions",fg="blue",bg="lightgreen",font=("Arial",16)).pack(pady=24)
    Label(top,text="3)English consists 10 Questions",fg="blue",bg="lightgreen",font=("Arial",16)).pack(pady=23)
    Label(top,text="4)Total Examination consists 30 marks",fg="blue",bg="lightgreen",font=("Arial",16)).pack(pady=23)
    Label(top,text="5)If the answer is correct you award 1 mark else 0 mark",fg="blue",bg="lightgreen",font=("Arial",16)).pack(pady=23)
        
        

    # Define checkbox variables
    checkvar1 = IntVar()
    checkvar2 = IntVar()
    checkvar3 = IntVar()

    # Create checkboxes
    Checkbutton(top, text="Choose only one option", bg="lightgreen", variable=checkvar1).pack(pady=5)
    Checkbutton(top, text="Malpractice not allowed", bg="lightgreen", variable=checkvar2).pack(pady=5)
    Checkbutton(top, text="I agree to these points to start and continue the exam", bg="lightgreen", variable=checkvar3).pack(pady=5)
                




        # Define submit button
    def start_exam():
        if checkvar1.get() == 1 and checkvar2.get() == 1 and checkvar3.get() == 1:
            messagebox.showinfo("Confirmation", "You can write the exam")
            launch_section1()
        else:
            # Open new Toplevel window for ineligibility
            messagebox.showwarning("Input Error","please tick all the checkboxes")
    Button(top, text="START-EXAM", command=start_exam, bg="pink").pack(pady=20)
    
score=0
def launch_section1():
    global score
    def question1():
        global score
        selection1="you selected the option"+str(radio1.get())
        label1.config(text=selection1)
        if radio1.get()==3:
            score +=1
        else:
            score=0
    
    sec1=Toplevel()
    sec1.title("SECTION 1- ARITHEMATIC")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 60
    sec1.geometry(f"{x}x{y}")
    sec1.config(bg="lightgreen")
    Label(sec1,text="--------ARITHEMATIC SECTION--------",bg="lightgreen",fg="blue",font=16).pack(anchor=S)
    Label(sec1,text=("Q1)If one-third of one-fourth of a number is 15,then three-tenth  of that number is:?"),bg="lightgreen").pack(anchor=W)
    radio1=IntVar()
    q1a=Radiobutton(sec1,text="a)35",bg="lightgreen",variable=radio1,value=1,command=question1)
    q1a.pack(anchor=W)
    q1b=Radiobutton(sec1,text="b)36",bg="lightgreen",variable=radio1,value=2,command=question1)
    q1b.pack(anchor=W)
    q1c=Radiobutton(sec1,text="c)45",bg="lightgreen",variable=radio1,value=3,command=question1)
    q1c.pack(anchor=W)
    q1d=Radiobutton(sec1,text="d)54",bg="lightgreen",variable=radio1,value=4,command=question1)
    q1d.pack(anchor=W)
    
    label1=Label(sec1,bg="lightgreen")
    label1.pack()


    def question2():
        global score
        selection2="you selected the option"+str(radio2.get())
        label2.config(text=selection2)
        if radio2.get()==3:
            score +=1
        else:
            score=0
    
                    

    Label(sec1,text="Q2)The H.C.F of two numbers is 23 and the other two factors of their  L.C.M are 13 and 14.The larger of the two numbers is:?",bg="lightgreen").pack(anchor=W)
    radio2=IntVar()
    q2a=Radiobutton(sec1,text="a)276",bg="lightgreen",variable=radio2,value=1,command=question2)
    q2a.pack(anchor=W)
    q2b=Radiobutton(sec1,text="b)299",bg="lightgreen",variable=radio2,value=2,command=question2)
    q2b.pack(anchor=W)
    q2c=Radiobutton(sec1,text="c)322",bg="lightgreen",variable=radio2,value=3,command=question2)
    q2c.pack(anchor=W)
    q2d=Radiobutton(sec1,text="d)345",bg="lightgreen",variable=radio2,value=4,command=question2)
    q2d.pack(anchor=W)

    label2=Label(sec1,bg="lightgreen")
    label2.pack()

    

    def question3():
        global score
        selection3="you selected the option"+str(radio3.get())
        label3.config(text=selection3)
        if radio3.get()==1:
            score +=1
        else:
            score=0
    
                
    Label(sec1,text="Q3)The least perfect square, which is divisible by each  of 21,36 and 66 is:?",bg="lightgreen").pack(anchor=W)
    radio3=IntVar()
    q3a=Radiobutton(sec1,text="a)213444",bg="lightgreen",variable=radio3,value=1,command=question3)
    q3a.pack(anchor=W)
    q3b=Radiobutton(sec1,text="b)214344",bg="lightgreen",variable=radio3,value=2,command=question3)
    q3b.pack(anchor=W)
    q3c=Radiobutton(sec1,text="c)214434",bg="lightgreen",variable=radio3,value=3,command=question3)
    q3c.pack(anchor=W)
    q4d=Radiobutton(sec1,text="d)231444",bg="lightgreen",variable=radio3,value=4,command=question3)
    q4d.pack(anchor=W)

    label3=Label(sec1,bg="lightgreen")
    label3.pack()


    def question4():
        global score
        selection4="you selected the option"+str(radio4.get())
        label4.config(text=selection4)
        if radio4.get()==4:
            score +=1
        else:
            score=0


    
    Label(sec1,text="Q4)The average of 20 numbers is zero. Of them,at the most, how many may be greater than zero?",bg="lightgreen").pack(anchor=W)
    radio4=IntVar()
    q4a=Radiobutton(sec1,text="a)0",bg="lightgreen",variable=radio4,value=1,command=question4)
    q4a.pack(anchor=W)
    q4b=Radiobutton(sec1,text="b)1",bg="lightgreen",variable=radio4,value=2,command=question4)
    q4b.pack(anchor=W)
    q4c=Radiobutton(sec1,text="c)10",bg="lightgreen",variable=radio4,value=3,command=question4)
    q4c.pack(anchor=W)
    q4d=Radiobutton(sec1,text="d)19",bg="lightgreen",variable=radio4,value=4,command=question4)
    q4d.pack(anchor=W)

    label4=Label(sec1,bg="lightgreen")
    label4.pack()

   

    def question5():
        global score
        selection5="you selected the option"+str(radio5.get())
        label5.config(text=selection5)
        if radio5.get()==2:
            score +=1
        else:
            score=0

  

    Label(sec1,text="Q5)The cube root of .000216 is:?",bg="lightgreen").pack(anchor=W)
    radio5=IntVar()
    q5a=Radiobutton(sec1,text="a).6",bg="lightgreen",variable=radio5,value=1,command=question5)
    q5a.pack(anchor=W)
    q5b=Radiobutton(sec1,text="b).06",bg="lightgreen",variable=radio5,value=2,command=question5)
    q5b.pack(anchor=W)
    q5c=Radiobutton(sec1,text="c)77",bg="lightgreen",variable=radio5,value=3,command=question5)
    q5c.pack(anchor=W)
    q5d=Radiobutton(sec1,text="d)87",bg="lightgreen",variable=radio5,value=4,command=question5)
    q5d.pack(anchor=W)

    label5=Label(sec1,bg="lightgreen")
    label5.pack()
                            
                
    button=Button(sec1,text="NEXT ",command=launch_section2)
    button.pack(anchor=S)

    


def launch_section2():
    global score
    def question6():
        global score
        selection6="you selected the option"+str(radio6.get())
        label6.config(text=selection6)
        if radio6.get()==3:
            score +=1
        else:
            score=0

    
    sec2=Toplevel()
    sec2.title("SECTION 1- ARITHEMATIC")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 60
    sec2.geometry(f"{x}x{y}")
    sec2.config(bg="lightgreen")
    Label(sec2,text="--------ARITHEMATIC SECTION--------",bg="lightgreen",fg="blue",font=16).pack(anchor=S)
    Label(sec2,text=("Q6)Look at the series: 22,21,23,22,24,23,.............What number should come next?"),bg="lightgreen").pack(anchor=W)
    radio6=IntVar()
    q6a=Radiobutton(sec2,text="a)22",bg="lightgreen",variable=radio6,value=1,command=question6)
    q6a.pack(anchor=W)
    q6b=Radiobutton(sec2,text="b)24",bg="lightgreen",variable=radio6,value=2,command=question6)
    q6b.pack(anchor=W)
    q6c=Radiobutton(sec2,text="c)25",bg="lightgreen",variable=radio6,value=3,command=question6)
    q6c.pack(anchor=W)
    q6d=Radiobutton(sec2,text="d)26",bg="lightgreen",variable=radio6,value=4,command=question6)
    q6d.pack(anchor=W)
    
    label6=Label(sec2,bg="lightgreen")
    label6.pack()

    def question7():
        global score
        selection7="you selected the option"+str(radio7.get())
        label7.config(text=selection7)
        if radio7.get()==4:
            score +=1
        else:
            score=0
        

   
                
    Label(sec2,text="Q7)If Rs 782 be divided into three parts, proportional to  1/2 : 2/3 : 3/4, then the first part is:?",bg="lightgreen").pack(anchor=W)
    radio7=IntVar()
    q7a=Radiobutton(sec2,text="a)182",bg="lightgreen",variable=radio7,value=1,command=question7)
    q7a.pack(anchor=W)
    q7b=Radiobutton(sec2,text="b)190",bg="lightgreen",variable=radio7,value=2,command=question7)
    q7b.pack(anchor=W)
    q7c=Radiobutton(sec2,text="c)196",bg="lightgreen",variable=radio7,value=3,command=question7)
    q7c.pack(anchor=W)
    q7d=Radiobutton(sec2,text="d)204",bg="lightgreen",variable=radio7,value=4,command=question7)
    q7d.pack(anchor=W)

    label7=Label(sec2,bg="lightgreen")
    label7.pack()

    def question8():
        global score
        selection8="you selected the option"+str(radio8.get())
        label8.config(text=selection8)
        if radio8.get()==1:
            score +=1
        else:
            score=0

    Label(sec2,text="Q8)If 20% of a = b, then b % of 20 is the same as:?",bg="lightgreen").pack(anchor=W)
    radio8=IntVar()
    q8a=Radiobutton(sec2,text="a)4% of a",bg="lightgreen",variable=radio8,value=1,command=question8)
    q8a.pack(anchor=W)
    q8b=Radiobutton(sec2,text="b)5% of a",bg="lightgreen",variable=radio8,value=2,command=question8)
    q8b.pack(anchor=W)
    q8c=Radiobutton(sec2,text="c)20% of a",bg="lightgreen",variable=radio8,value=3,command=question8)
    q8c.pack(anchor=W)
    q8d=Radiobutton(sec2,text="d)none of these",bg="lightgreen",variable=radio8,value=4,command=question8)
    q8d.pack(anchor=W)

    label8=Label(sec2,bg="lightgreen")
    label8.pack()

    def question9():
        global score
        selection9="you selected the option"+str(radio9.get())
        label9.config(text=selection9)
        if radio9.get()==4:
            score +=1
        else:
            score=0

    Label(sec2,text="Q9)The reflex angle betwween the hands of a clock at 10.25 is:?",bg="lightgreen").pack(anchor=W)
    radio9=IntVar()
    q9a=Radiobutton(sec2,text="a)180",bg="lightgreen",variable=radio9,value=1,command=question9)
    q9a.pack(anchor=W)
    q9b=Radiobutton(sec2,text="b)192 1/2",bg="lightgreen",variable=radio9,value=2,command=question9)
    q9b.pack(anchor=W)
    q9c=Radiobutton(sec2,text="c)195",bg="lightgreen",variable=radio9,value=3,command=question9)
    q9c.pack(anchor=W)
    q9d=Radiobutton(sec2,text="d)197 1/2",bg="lightgreen",variable=radio9,value=4,command=question9)
    q9d.pack(anchor=W)

    label9=Label(sec2,bg="lightgreen")
    label9.pack()

    def question10():
        global score
        selection10="you selected the option"+str(radio10.get())
        label10.config(text=selection10)
        if radio10.get()==4:
            score +=1
        else:
            score=0
 

    Label(sec2,text="Q10)At what time between 7 and 8:00 clock will the hands of a  clock be in the same straight line but, not together?",bg="lightgreen").pack(anchor=W)
    radio10=IntVar()
    q10a=Radiobutton(sec2,text="a)5 min. past 7",bg="lightgreen",variable=radio10,value=1,command=question10)
    q10a.pack(anchor=W)
    q10b=Radiobutton(sec2,text="b)5 2/11 min. past 7",bg="lightgreen",variable=radio10,value=2,command=question10)
    q10b.pack(anchor=W)
    q10c=Radiobutton(sec2,text="c)5 3/11 min. past 7",bg="lightgreen",variable=radio10,value=3,command=question10)
    q10c.pack(anchor=W)
    q10d=Radiobutton(sec2,text="d)5 5/11 min. past 7",bg="lightgreen",variable=radio10,value=4,command=question10)
    q10d.pack(anchor=W)

    label10=Label(sec2,bg="lightgreen")
    label10.pack()

    button=Button(sec2,text="NEXT",command=launch_section3)
    button.pack(anchor=S)
    



     
    


def launch_section3():
    global score
    def question11():
        global score
        selection11="you selected the option"+str(radio11.get())
        label11.config(text=selection11)
        if radio11.get()==4:
            score +=1
        else:
            score=0
 
        
    sec3=Toplevel()
    sec3.title("SECTION 2- REASONING")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 60
    sec3.geometry(f"{x}x{y}")
    sec3.config(bg="lightgreen")
    Label(sec3,text="----------------------REASONING SECTION--------------------",bg="lightgreen",fg="blue",font=16).pack(anchor=S)
    Label(sec3,text=("q1)Look at the series: 22,21,23,22,24,21,... What number should come next?"),bg="lightgreen").pack(anchor=W)
    radio11=IntVar()
    q11a=Radiobutton(sec3,text="a)22",bg="lightgreen",variable=radio11,value=1,command=question11)
    q11a.pack(anchor=W)
    q11b=Radiobutton(sec3,text="b)22",bg="lightgreen",variable=radio11,value=2,command=question11)
    q11b.pack(anchor=W)
    q11c=Radiobutton(sec3,text="c)25",bg="lightgreen",variable=radio11,value=3,command=question11)
    q11c.pack(anchor=W)
    q11d=Radiobutton(sec3,text="d)26",bg="lightgreen",variable=radio11,value=4,command=question11)
    q11d.pack(anchor=W)

    label11=Label(sec3,bg="lightgreen")
    label11.pack()

    def question12():
        global score
        selection12="you selected the option"+str(radio12.get())
        label12.config(text=selection12)
        if radio12.get()==2:
            score +=1
        else:
            score=0
 
        
    Label(sec3,text=("q2)Look at this series: 53,53,40,40,27,27,...... what number should come next?"),bg="lightgreen").pack(anchor=W)
    radio12=IntVar()
    q12a=Radiobutton(sec3,text="a)12",bg="lightgreen",variable=radio12,value=1,command=question12)
    q12a.pack(anchor=W)
    q12b=Radiobutton(sec3,text="b)14",bg="lightgreen",variable=radio12,value=2,command=question12)
    q12b.pack(anchor=W)
    q12c=Radiobutton(sec3,text="c)27",bg="lightgreen",variable=radio12,value=3,command=question12)
    q12c.pack(anchor=W)
    q12d=Radiobutton(sec3,text="d)53",bg="lightgreen",variable=radio12,value=4,command=question12)
    q12d.pack(anchor=W)

    label12=Label(sec3,bg="lightgreen")
    label12.pack()

    def question13():
        global score
        selection13="you selected the option"+str(radio13.get())
        label13.config(text=selection13)
        if radio13.get()==4:
            score +=1
        else:
            score=0
 

    Label(sec3,text=("q3)Which word does not being with the others?"),bg="lightgreen").pack(anchor=W)
    radio13=IntVar()
    q13a=Radiobutton(sec3,text="a)inch",bg="lightgreen",variable=radio13,value=1,command=question13)
    q13a.pack(anchor=W)
    q13b=Radiobutton(sec3,text="b)ounce",bg="lightgreen",variable=radio13,value=2,command=question13)
    q13b.pack(anchor=W)
    q13c=Radiobutton(sec3,text="c)centimeter",bg="lightgreen",variable=radio13,value=3,command=question13)
    q13c.pack(anchor=W)
    q13d=Radiobutton(sec3,text="d)yard",bg="lightgreen",variable=radio13,value=4,command=question13)
    q13d.pack(anchor=W)

    label13=Label(sec3,bg="lightgreen")
    label13.pack()

    def question14():
        global score
        selection14="you selected the option"+str(radio14.get())
        label14.config(text=selection14)
        if radio14.get()==2:
            score +=1
        else:
            score=0
 

    Label(sec3,text=("q4)Look at this series:2,1,(1/2),(1/4)....what number should come next?"),bg="lightgreen").pack(anchor=W)
    radio14=IntVar()
    q14a=Radiobutton(sec3,text="a)(1/3)",bg="lightgreen",variable=radio14,value=1,command=question14)
    q14a.pack(anchor=W)
    q14b=Radiobutton(sec3,text="b)(1/8)",bg="lightgreen",variable=radio14,value=2,command=question14)
    q14b.pack(anchor=W)
    q14c=Radiobutton(sec3,text="c)(2/8)",bg="lightgreen",variable=radio14,value=3,command=question14)
    q14c.pack(anchor=W)
    q14d=Radiobutton(sec3,text="d)(1/16)",bg="lightgreen",variable=radio14,value=4,command=question14)
    q14d.pack(anchor=W)

    label14=Label(sec3,bg="lightgreen")
    label14.pack()

    def question15():
        global score
        selection15="you selected the option"+str(radio15.get())
        label15.config(text=selection15)
        if radio15.get()==4:
            score +=1
        else:
            score=0
 

    Label(sec3,text=("q5)If A is the brother of B;B is the sister of C;and C is the father of D,how D is related to A?"),bg="lightgreen").pack(anchor=W)
    radio15=IntVar()
    q15a=Radiobutton(sec3,text="a)Brother",bg="lightgreen",variable=radio15,value=1,command=question15)
    q15a.pack(anchor=W)
    q15b=Radiobutton(sec3,text="b)Sister",bg="lightgreen",variable=radio15,value=2,command=question15)
    q15b.pack(anchor=W)
    q15c=Radiobutton(sec3,text="c)Nephew",bg="lightgreen",variable=radio15,value=3,command=question15)
    q15c.pack(anchor=W)
    q15d=Radiobutton(sec3,text="d)cannot be determined",bg="lightgreen",variable=radio15,value=4,command=question15)
    q15d.pack(anchor=W)

    label15=Label(sec3,bg="lightgreen")
    label15.pack()

    btna=Button(sec3,text="NEXT",command=launch_section4)
    btna.pack(anchor=S)

def launch_section4():
    global score
    def question16():
        global score
        selection16="you selected the option"+str(radio16.get())
        label16.config(text=selection16)
        if radio16.get()==4:
            score +=1
        else:
            score=0
        

    sec4=Toplevel()
    sec4.title("SECTION 2- REASONING")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 60
    sec4.geometry(f"{x}x{y}")
    sec4.config(bg="lightgreen")
    Label(sec4,text="--------REASONING SECTION--------",bg="lightgreen",fg="blue",font=16).pack(anchor=S)
    Label(sec4,text=("q6)Look at this series:201,202,204,207,...What number should come next?"),bg="lightgreen").pack(anchor=W)
    radio16=IntVar()
    q16a=Radiobutton(sec4,text="a)205",bg="lightgreen",variable=radio16,value=1,command=question16)
    q16a.pack(anchor=W)
    q16b=Radiobutton(sec4,text="b)208",bg="lightgreen",variable=radio16,value=2,command=question16)
    q16b.pack(anchor=W)
    q16c=Radiobutton(sec4,text="c)210",bg="lightgreen",variable=radio16,value=3,command=question16)
    q16c.pack(anchor=W)
    q16d=Radiobutton(sec4,text="d)211",bg="lightgreen",variable=radio16,value=4,command=question16)
    q16d.pack(anchor=W)

    label16=Label(sec4,bg="lightgreen")
    label16.pack()

    def question17():
        global score
        selection17="you selected the option"+str(radio17.get())
        label17.config(text=selection17)
        if radio17.get()==4:
            score +=1
        else:
            score=0

    Label(sec4,text=("q7)Which word does not being with the others?"),bg="lightgreen").pack(anchor=W)
    radio17=IntVar()
    q17a=Radiobutton(sec4,text="a)tulip",bg="lightgreen",variable=radio17,value=1,command=question17)
    q17a.pack(anchor=W)
    q17b=Radiobutton(sec4,text="b)rose",bg="lightgreen",variable=radio17,value=2,command=question17)
    q17b.pack(anchor=W)
    q17c=Radiobutton(sec4,text="c)bud",bg="lightgreen",variable=radio17,value=3,command=question17)
    q17c.pack(anchor=W)
    q17d=Radiobutton(sec4,text="d)daisy",bg="lightgreen",variable=radio17,value=4,command=question17)
    q17d.pack(anchor=W)

    label17=Label(sec4,bg="lightgreen")
    label17.pack()

    def question18():
        global score
        selection18="you selected the option"+str(radio18.get())
        label18.config(text=selection18)
        if radio18.get()==4:
            score +=1
        else:
            score=0

    Label(sec4,text=("q8)ELFA,GLHA,ILJA,,MLNA?"),bg="lightgreen").pack(anchor=W)
    radio18=IntVar()
    q18a=Radiobutton(sec4,text="a)OLPA",bg="lightgreen",variable=radio18,value=1,command=question18)
    q18a.pack(anchor=W)
    q18b=Radiobutton(sec4,text="b)KLMA",bg="lightgreen",variable=radio18,value=2,command=question18)
    q18b.pack(anchor=W)
    q18c=Radiobutton(sec4,text="c)LLMA",bg="lightgreen",variable=radio18,value=3,command=question18)
    q18c.pack(anchor=W)
    q18d=Radiobutton(sec4,text="d)KLLA",bg="lightgreen",variable=radio18,value=4,command=question18)
    q18d.pack(anchor=W)

    label18=Label(sec4,bg="lightgreen")
    label18.pack()

    def question19():
        global score
        selection19="you selected the option"+str(radio19.get())
        label19.config(text=selection19)
        if radio19.get()==1:
            score +=1
        else:
            score=0

    Label(sec4,text=("q9)Choose the word which is different from the rest."),bg="lightgreen").pack(anchor=W)
    radio19=IntVar()
    q19a=Radiobutton(sec4,text="a)Chicken",bg="lightgreen",variable=radio19,value=1,command=question19)
    q19a.pack(anchor=W)
    q19b=Radiobutton(sec4,text="b)Snake",bg="lightgreen",variable=radio19,value=2,command=question19)
    q19b.pack(anchor=W)
    q19c=Radiobutton(sec4,text="c)Swan",bg="lightgreen",variable=radio19,value=3,command=question19)
    q19c.pack(anchor=W)
    q19d=Radiobutton(sec4,text="d)Crocodile",bg="lightgreen",variable=radio19,value=4,command=question19)
    q19d.pack(anchor=W)

    label19=Label(sec4,bg="lightgreen")
    label19.pack()

    def question20():
        global score
        selection20="you selected the option"+str(radio20.get())
        label20.config(text=selection20)
        if radio20.get()==3:
            score +=1
        else:
            score=0

    Label(sec4,text=("q10)SCD,TEF,UGH,_,WKL"),bg="lightgreen").pack(anchor=W)
    radio20=IntVar()
    q20a=Radiobutton(sec4,text="a)CMN",bg="lightgreen",variable=radio20,value=1,command=question20)
    q20a.pack(anchor=W)
    q20b=Radiobutton(sec4,text="b)UJI",bg="lightgreen",variable=radio20,value=2,command=question20)
    q20b.pack(anchor=W)
    q20c=Radiobutton(sec4,text="c)VIJ",bg="lightgreen",variable=radio20,value=3,command=question20)
    q20c.pack(anchor=W)
    q20d=Radiobutton(sec4,text="d)IJT",bg="lightgreen",variable=radio20,value=4,command=question20)
    q20d.pack(anchor=W)

    label20=Label(sec4,bg="lightgreen")
    label20.pack()

    btnab=Button(sec4,text="NEXT",command=launch_section5)
    btnab.pack(anchor=S)

def launch_section5():
    global score
    def question21():
        global score
        selection21="you selected the option"+str(radio21.get())
        label21.config(text=selection21)
        if radio21.get()==1:
            score +=1
        else:
            score=0
    sec5=Toplevel()
    sec5.title("SECTION 3- ENGLISH")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 60
    sec5.geometry(f"{x}x{y}")
    sec5.config(bg="lightgreen")
    Label(sec5,text="--------ENGLISH SECTION--------",bg="lightgreen",fg="blue",font=16).pack(anchor=S)
    Label(sec5,text=("q1)VENT"),bg="lightgreen").pack(anchor=W)
    radio21=IntVar()
    q21a=Radiobutton(sec5,text="a)Opening",bg="lightgreen",variable=radio21,value=1,command=question21)
    q21a.pack(anchor=W)
    q21b=Radiobutton(sec5,text="b)Stodge",bg="lightgreen",variable=radio21,value=2,command=question21)
    q21b.pack(anchor=W)
    q21c=Radiobutton(sec5,text="c)End",bg="lightgreen",variable=radio21,value=3,command=question21)
    q21c.pack(anchor=W)
    q21d=Radiobutton(sec5,text="d)Past tense of go",bg="lightgreen",variable=radio21,value=4,command=question21)
    q21d.pack(anchor=W)

    label21=Label(sec5,bg="lightgreen")
    label21.pack()

    def question22():
        global score
        selection22="you selected the option"+str(radio22.get())
        label22.config(text=selection22)
        if radio22.get()==4:
            score +=1
        else:
            score=0

    
    Label(sec5,text=("q2)CORPULENT"),bg="lightgreen").pack(anchor=W)
    radio22=IntVar()
    q22a=Radiobutton(sec5,text="a)Lean",bg="lightgreen",variable=radio22,value=1,command=question22)
    q22a.pack(anchor=W)
    q22b=Radiobutton(sec5,text="b)Gaunt",bg="lightgreen",variable=radio22,value=2,command=question22)
    q22b.pack(anchor=W)
    q22c=Radiobutton(sec5,text="c)Emaciated",bg="lightgreen",variable=radio22,value=3,command=question22)
    q22c.pack(anchor=W)
    q22d=Radiobutton(sec5,text="d)Obeses",bg="lightgreen",variable=radio22,value=4,command=question22)
    q22d.pack(anchor=W)

    label22=Label(sec5,bg="lightgreen")
    label22.pack()

    def question23():
        global score
        selection23="you selected the option"+str(radio23.get())
        label23.config(text=selection23)
        if radio23.get()==1:
            score +=1
        else:
            score=0

    
    Label(sec5,text=("q3)EMBEZZLE"),bg="lightgreen").pack(anchor=W)
    radio23=IntVar()
    q23a=Radiobutton(sec5,text="a)Misappropiate",bg="lightgreen",variable=radio23,value=1,command=question23)
    q23a.pack(anchor=W)
    q23b=Radiobutton(sec5,text="b)Balance",bg="lightgreen",variable=radio23,value=2,command=question23)
    q23b.pack(anchor=W)
    q23c=Radiobutton(sec5,text="c)Remunerate",bg="lightgreen",variable=radio23,value=3,command=question23)
    q23c.pack(anchor=W)
    q23d=Radiobutton(sec5,text="d)Clear",bg="lightgreen",variable=radio23,value=4,command=question23)
    q23d.pack(anchor=W)

    label23=Label(sec5,bg="lightgreen")
    label23.pack()

    def question24():
        global score
        selection24="you selected the option"+str(radio24.get())
        label24.config(text=selection24)
        if radio24.get()==3:
            score +=1
        else:
            score=0

    
    Label(sec5,text=("q4)My uncle decided to take ____and my sister to the market?"),bg="lightgreen").pack(anchor=W)
    radio24=IntVar()
    q24a=Radiobutton(sec5,text="a)I",bg="lightgreen",variable=radio24,value=1,command=question24)
    q24a.pack(anchor=W)
    q24b=Radiobutton(sec5,text="b)mine",bg="lightgreen",variable=radio24,value=2,command=question24)
    q24b.pack(anchor=W)
    q24c=Radiobutton(sec5,text="c)me",bg="lightgreen",variable=radio24,value=3,command=question24)
    q24c.pack(anchor=W)
    q24d=Radiobutton(sec5,text="d)myself",bg="lightgreen",variable=radio24,value=4,command=question24)
    q24d.pack(anchor=W)

    label24=Label(sec5,bg="lightgreen")
    label24.pack()

    def question25():
        global score
        selection25="you selected the option"+str(radio25.get())
        label25.config(text=selection25)
        if radio25.get()==3:
            score +=1
        else:
            score=0

    
    Label(sec5,text=("q5)The grapes are now ____enough to be picked."),bg="lightgreen").pack(anchor=W)
    radio25=IntVar()
    q25a=Radiobutton(sec5,text="a)ready",bg="lightgreen",variable=radio25,value=1,command=question25)
    q25a.pack(anchor=W)
    q25b=Radiobutton(sec5,text="b)mature",bg="lightgreen",variable=radio25,value=2,command=question25)
    q25b.pack(anchor=W)
    q25c=Radiobutton(sec5,text="c)ripe",bg="lightgreen",variable=radio25,value=3,command=question25)
    q25c.pack(anchor=W)
    q25d=Radiobutton(sec5,text="d)advanced",bg="lightgreen",variable=radio25,value=4,command=question25)
    q25d.pack(anchor=W)

    label25=Label(sec5,bg="lightgreen")
    label25.pack()


    btnabcd=Button(sec5,text="NEXT",command=launch_section6)
    btnabcd.pack(anchor=S)


     
#section6
def launch_section6():
    global score
    def question26():
        global score
        selection26="you selected the option"+str(radio26.get())
        label26.config(text=selection26)
        if radio26.get()==2:
            score +=1
        else:
            score=0

    sec6=Toplevel()
    sec6.title("SECTION 3- ENGLISH")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 60
    sec6.geometry(f"{x}x{y}")
    sec6.config(bg="lightgreen")
    Label(sec6,text="--------ENGLISH SECTION--------",bg="lightgreen",fg="blue",font=16).pack(anchor=S)
    Label(sec6,text=("q6)(solve as per the direction given above)"),bg="lightgreen").pack(anchor=W)
    radio26=IntVar()
    q26a=Radiobutton(sec6,text="a)Efficient",bg="lightgreen",variable=radio26,value=1,command=question26)
    q26a.pack(anchor=W)
    q26b=Radiobutton(sec6,text="b)Treatment",bg="lightgreen",variable=radio26,value=2,command=question26)
    q26b.pack(anchor=W)
    q26c=Radiobutton(sec6,text="c)Beterment",bg="lightgreen",variable=radio26,value=3,command=question26)
    q26c.pack(anchor=W)
    q26d=Radiobutton(sec6,text="d)Emloyd",bg="lightgreen",variable=radio26,value=4,command=question26)
    q26d.pack(anchor=W)

    label26=Label(sec6,bg="lightgreen")
    label26.pack()

    def question27():
        global score
        selection27="you selected the option"+str(radio27.get())
        label27.config(text=selection27)
        if radio27.get()==2:
            score +=1
        else:
            score=0

     
    Label(sec6,text=("q7)(solve as per the direction given above)"),bg="lightgreen").pack(anchor=W)
    radio27=IntVar()
    q27a=Radiobutton(sec6,text="a)Foreign",bg="lightgreen",variable=radio27,value=1,command=question27)
    q27a.pack(anchor=W)
    q27b=Radiobutton(sec6,text="b)Foreine",bg="lightgreen",variable=radio27,value=2,command=question27)
    q27b.pack(anchor=W)
    q27c=Radiobutton(sec6,text="c)Fariegn",bg="lightgreen",variable=radio27,value=3,command=question27)
    q27c.pack(anchor=W)
    q27d=Radiobutton(sec6,text="d)Forein",bg="lightgreen",variable=radio27,value=4,command=question27)
    q27d.pack(anchor=W)

    label27=Label(sec6,bg="lightgreen")
    label27.pack()

    def question28():
        global score
        selection28="you selected the option"+str(radio28.get())
        label28.config(text=selection28)
        if radio28.get()==1:
            score +=1
        else:
            score=0

     
    Label(sec6,text=("q8)The miser gazed _____at the pile of gold coins in front of him."),bg="lightgreen").pack(anchor=W)
    radio28=IntVar()
    q28a=Radiobutton(sec6,text="a)avidly",bg="lightgreen",variable=radio28,value=1,command=question28)
    q28a.pack(anchor=W)
    q28b=Radiobutton(sec6,text="b)admiringly",bg="lightgreen",variable=radio28,value=2,command=question28)
    q28b.pack(anchor=W)
    q28c=Radiobutton(sec6,text="c)thoughtfully",bg="lightgreen",variable=radio28,value=3,command=question28)
    q28c.pack(anchor=W)
    q28d=Radiobutton(sec6,text="d)earnestly",bg="lightgreen",variable=radio28,value=4,command=question28)
    q28d.pack(anchor=W)

    label28=Label(sec6,bg="lightgreen")
    label28.pack()

    def question29():
        global score
        selection29="you selected the option"+str(radio29.get())
        label29.config(text=selection29)
        if radio29.get()==1:
            score +=1
        else:
            score=0

     
    Label(sec6,text=("q9)EXODUS"),bg="lightgreen").pack(anchor=W)
    radio29=IntVar()
    q29a=Radiobutton(sec6,text="a)Influx",bg="lightgreen",variable=radio29,value=1,command=question29)
    q29a.pack(anchor=W)
    q29b=Radiobutton(sec6,text="b)Home-coming",bg="lightgreen",variable=radio29,value=2,command=question29)
    q29b.pack(anchor=W)
    q29c=Radiobutton(sec6,text="c)Returning",bg="lightgreen",variable=radio29,value=3,command=question29)
    q29c.pack(anchor=W)
    q29d=Radiobutton(sec6,text="d)Restoration",bg="lightgreen",variable=radio29,value=4,command=question29)
    q29d.pack(anchor=W)

    label29=Label(sec6,bg="lightgreen")
    label29.pack()
  
    def question30():
        global score
        selection30="you selected the option"+str(radio30.get())
        label30.config(text=selection30)
        if radio30.get()==2:
            score +=1
        else:
            score=0

     
    Label(sec6,text=("q10)(I saw a _____of cows in the field.)"),bg="lightgreen").pack(anchor=W)
    radio30=IntVar()
    q30a=Radiobutton(sec6,text="a)group",bg="lightgreen",variable=radio30,value=1,command=question30)
    q30a.pack(anchor=W)
    q30b=Radiobutton(sec6,text="b)herd",bg="lightgreen",variable=radio30,value=2,command=question30)
    q30b.pack(anchor=W)
    q30c=Radiobutton(sec6,text="c)swarm",bg="lightgreen",variable=radio30,value=3,command=question30)
    q30c.pack(anchor=W)
    q30d=Radiobutton(sec6,text="d)Flock",bg="lightgreen",variable=radio30,value=4,command=question30)
    q30d.pack(anchor=W)

    label30=Label(sec6,bg="lightgreen")
    label30.pack()

    btnabcde=Button(sec6,text="SUBMIT",command=show_score)
    btnabcde.pack(anchor=S)

    
    
    
    
def close():
    root.destroy()
    
    
     
def show_score():
    global score
    sec7=Toplevel()
    sec7.title("SUMMARY")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - 90
    y = screen_height - 60
    sec7.geometry(f"{x}x{y}")
    sec7.config(bg="lightgreen")
    
   
    if score <= 15:
       
        message=Label(sec7,text="You are NOT qualified!",bg="lightgreen",fg="blue",font=16)
        message.pack(anchor=S)
    else:
        
        message=Label(sec7,text="You are  qualified!",bg="lightgreen",fg="blue",font=16)
        message.pack(anchor=S)

    score_label=Label(sec7,text=f"your total score:{score}/30",bg="lightgreen",fg="blue",font=16)
    score_label.pack(anchor=S)

    btnc1=Button(sec7,text="close",command=close)
    btnc1.pack(anchor=S)

    import mysql.connector
    global current_rollno, current_name


    mydb = mysql.connector.connect(host="localhost", user="root",password="root123",database="crttext")
    mycursor = mydb.cursor()
    sql1 = "CREATE TABLE IF NOT EXISTS student_scores (hall_ticket_number VARCHAR(20) PRIMARY KEY, name VARCHAR(100),score INT)"
    mycursor.execute(sql1)
    sql = "INSERT INTO student_scores (hall_ticket_number, name,score)VALUES (%s,%s,%s);"
    val= (current_rollno, current_name, score)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "row inserted")
    
    
    

   
    


# Main window
root = Tk()
root.title("LOGIN DETIALS")
root.configure(bg="lightgreen")
root.geometry("8000x6000")

rollno = StringVar()
name = StringVar()

Label(root,text="Enter the HallTicket Number and Name of the Candiate",fg="blue",bg="lightgreen",font=("Arial",16)).grid(row=0,column=0)

# Roll number input
Label(root, text="HALL TICKET NUMBER:", font=("Arial",16), fg="blue", bg="lightgreen").grid(row=1, column=0)
Entry(root, textvariable=rollno).grid(row=1, column=1)

# Name input
Label(root, text="NAME:", font=("Arial",16), fg="blue", bg="lightgreen").grid(row=2, column=0)
Entry(root, textvariable=name).grid(row=2, column=1)

# Button to trigger result check
call_result_func = partial(call_result, rollno, name)
Button(root, text="NEXT",font=("Arial",16), activeforeground="red", activebackground="pink", command=call_result_func).grid(row=7, column=1)

root.mainloop()
