"""
GROUP 07: 
Member : 
 1/ Dang Thanh Tuyen - 20110412
 2/ Danh Truong Son - 20110394
 3/ Dang Phuoc Truong Tai - 20110396
"""
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
import os

from DataCollect import datacollet




class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Group 7 __ Member: Danh Truong Son - 20110394 / Dang Phuoc Truong Tai - 20110396 / Dang Thanh Tuyen - 20110412")
        self.root.geometry("1366x768+0+0")

        # first header image  
        img=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

         #title section
        title_lb1 = Label(bg_img,text="Ứng Dụng Hỗ Trợ Quản Lý Học Sinh Thông Qua Nhận Diện Khuôn Mặt",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Button 1: Student List
        std_img_btn=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=370,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        std_b1_1.place(x=370,y=280,width=180,height=45)
        # Button 2: Emotion Detector
        det_img_btn=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=600,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Emotion Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        det_b1_1.place(x=600,y=280,width=180,height=45)
        # Button 3: Attendance
        att_img_btn=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=830,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        att_b1_1.place(x=830,y=280,width=180,height=45)
        # Button 4: Photo
        pho_img_btn=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/photo.jpg")
        pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=600,y=350,width=180,height=180)

        pho_b1_1 = Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        pho_b1_1.place(x=600,y=510,width=180,height=45)
        # Button 5: Help
        hlp_img_btn=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=370,y=350,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="Help Support",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        hlp_b1_1.place(x=370,y=510,width=180,height=45)
        # Button 6: Exit
        exi_img_btn=Image.open(r"C:/Users/Administrator/Downloads/TAILIEU/DIGITALIMAGE/HomeWork/Project/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=830,y=350,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        exi_b1_1.place(x=830,y=510,width=180,height=45)
        
#==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=datacollet(self.new_window)
    def Close(self):
        root.destroy()

if __name__== "__main__":
    root = Tk()
    obj=Login(root)
    root.mainloop()
       