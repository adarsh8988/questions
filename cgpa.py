import tkinter as tk
import joblib
import sklearn
# 
modl = joblib.load('package_checker.joblib')

def checkpkg():
    cgpa=en.get()
    cgpa=float(cgpa)
    
    m=modl.coef_
    b=modl.intercept_
    # print(m[0])
    # print(cgpa,"")
    

    
    pkg=m[0] * cgpa +b
    pkg=str(pkg)[0:4]
    lbl5.config(text=f"{pkg} Lakh.")
    
    
    


data=tk.Tk()
data.geometry("500x400")
data.title("Salary Prediction")
data.config(bg="skyblue")

frame1=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue")
frame1.pack()
lbl1=tk.Label(frame1,text="Check Your Package",font=("robort",10,"bold"),bg="skyblue")
lbl1.grid(row=1,column=3)
# lbl1.pack()
frame2=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue",width=50)
frame2.pack(padx=5,pady=10)

lbl2=tk.Label(frame2,text="Enter CGPA",font=("robort",10,"bold"),bg="skyblue")
lbl2.grid(row=2,column=2,pady=10)

lbl3=tk.Label(frame2,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl3.grid(row=2,column=3,pady=10)


en=tk.Entry(frame2,font=("robort",10,"bold"),width=20)
en.grid(padx=10,row=2,column=4,pady=10)
# en.pack()

lbl=tk.Button(frame2,text="Check",font=("robort",10,"bold"),bg="red",command=checkpkg)
lbl.grid(row=3,column=4,pady=10)
# lbl.pack()

frame3=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue")
frame3.pack(pady=10)

lbl4=tk.Label(frame3,text="Your package is ",font=("robort",10,"bold"),bg="skyblue")
lbl4.grid(row=4,column=1,padx=5,pady=10)
# lbl4.pack()

lbl4=tk.Label(frame3,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl4.grid(row=4,column=2,padx=5,pady=10)
# lbl4.pack()
lbl5=tk.Label(frame3,text=" ",font=("robort",10,"bold"),bg="skyblue")
lbl5.grid(row=4,column=3,padx=5,pady=10)


# en1=tk.Entry(data,font=("robort",10,"bold"),width=20)
# en1.grid(row=4,column=3,padx=10)
# en1.pack()











data.mainloop()

