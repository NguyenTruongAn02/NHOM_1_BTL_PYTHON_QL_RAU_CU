from tkinter import *
from PIL import ImageTk

def flayppy_bird():
    import flappy_brid

def gamexephinh():
    import xephinh

def dangnhap():
    window.destroy()
    import dangnhap

window = Tk()

window.geometry('950x540+0+0')

window.resizable(False, False)

backgroud = ImageTk.PhotoImage(file ='bg_raucu.jpg')

bgLable = Label(window, image=backgroud)
bgLable.place(x=0, y=0)
loginFrame = Frame(window, bg='white')
loginFrame.place(x=330, y=100)

#Tạo nút chuyển form FLAPPY BIRD
loinButton = Button(loginFrame, text='FLAPPY BIRD',
                    font=('times new roman', 20, 'bold'),
                    width=15, fg='white', bg='cornflowerblue',
                    activebackground='cornflowerblue',
                    activeforeground='white', cursor='hand2',
                    command=flayppy_bird)
loinButton.grid(row=0, column=1, pady=20, padx=20)

#Tạo nút chuyển form GAME XẾP HÌNH
loinButton = Button(loginFrame, text='GAME XẾP HÌNH',
                    font=('times new roman', 20, 'bold'),
                    width=15, fg='white', bg='cornflowerblue',
                    activebackground='cornflowerblue',
                    activeforeground='white', cursor='hand2',
                    command=gamexephinh)
loinButton.grid(row=1, column=1, pady=20, padx=20)

#Tạo nút chuyển form ĐĂNG NHẬP
loinButton = Button(loginFrame, text='ĐĂNG NHẬP',
                    font=('times new roman', 20, 'bold'),
                    width=15, fg='white', bg='cornflowerblue',
                    activebackground='cornflowerblue',
                    activeforeground='white', cursor='hand2',
                    command=dangnhap)
loinButton.grid(row=2, column=1, pady=20, padx=20)

window.mainloop()