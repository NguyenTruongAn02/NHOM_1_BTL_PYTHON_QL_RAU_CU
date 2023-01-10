from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    #Tài khoản là python, mật khẩu python
    if usernameEntry.get() == '' and passwordEntry.get() =='':
        messagebox.showerror('Lỗi đăng nhập',
                             'Tài khoản hoặc mật khẩu sai chưa được nhập. Vui lòng kiểm tra lại!')
    elif usernameEntry.get() == 'python' and passwordEntry.get() == 'python':
        messagebox.showinfo('Thông báo', 'Đăng nhập thành công!')
        window.destroy()
        import quanly_raucu
    else: messagebox.showerror('Lỗi đăng nhập',
                               'Tài khoản hoặc mật khẩu sai. Vui lòng kiểm tra lại!')

def giaitri():
    window.destroy()
    import main

window = Tk()

window.geometry('950x540+0+0')

window.resizable(False, False)

backgroud = ImageTk.PhotoImage(file ='bg_raucu.jpg')

bgLable = Label(window, image=backgroud)
bgLable.place(x=0, y=0)
loginFrame = Frame(window, bg='white')
loginFrame.place(x=150, y=100)

#Tạo icon trên đăng nhập
logoImage = PhotoImage(file='boy.png ')
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

#Tạo icon tài khoản
userImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame,
                      image=userImage, text='Tài khoản',
                      compound=LEFT,
                      font=('times new roman', 20, 'bold'))
usernameLabel.grid(row=1, column=0, pady=10)

#Tạo input nhập vào tài khoản
usernameEntry = Entry(loginFrame,
                      font=('times new roman', 20, 'bold'), bd=5)
usernameEntry.grid(row=1,column=1, pady= 10, padx=20)

#Tạo input nhập mật khẩu
passwordImage = PhotoImage(file='padlock.png')
passwordLable = Label(loginFrame,
                      image=passwordImage, text='Mật khẩu',
                      compound=LEFT,
                      font=('times new roman', 20, 'bold'))
passwordLable.grid(row=2, column=0, pady=10)

#Tạo input nhập vào
passwordEntry = Entry(loginFrame,
                      font=('times new roman', 20, 'bold'), bd=5)
passwordEntry.grid(row=2,column=1, pady= 10, padx=20)

#Tạo nút đăng nhập
loinButton = Button(loginFrame, text='ĐĂNG NHẬP',
                    font=('times new roman', 20, 'bold'),
                    width=15, fg='white', bg='cornflowerblue',
                    activebackground='cornflowerblue',
                    activeforeground='white', cursor='hand2',
                    command=login)
loinButton.grid(row=3, column=1, pady=20, padx=20)

#Tạo nút giải trí
loinButton = Button(loginFrame, text='GIẢI TRÍ',
                    font=('times new roman', 20, 'bold'),
                    width=15, fg='white', bg='cornflowerblue',
                    activebackground='cornflowerblue',
                    activeforeground='white', cursor='hand2',
                    command=giaitri)
loinButton.grid(row=3, column=0, pady=20, padx=20)


window.mainloop()