import time
from tkinter import *
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas

#Các hàm
#Hàm xuất dữ liệu ra exel
def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = vg_table.get_children()
    newlist=[]
    for index in indexing:
        content=vg_table.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table = pandas.DataFrame(newlist, columns=['ma', 'ten',
                                               'gia','xuatxu',
                                               'nxs', 'hsd'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Thông báo','Đã xuất dữ liệu thành công')



#hàm cập nhật
def update_button():
    def update_data():
        query = 'update raucu set ten=%s, gia=%s, xuatxu=%s,' \
                'nxs=%s, hsd=%s where ma=%s'
        mycusor.execute(query,(nameEntry.get(),priceEntry.get(),
                               makeinEntry.get(),nsxEntry.get(),
                               hsdEntry.get(), idEntry.get()))
        con.commit()
        messagebox.showinfo('Thông báo',f'Mã {idEntry.get()}'
                                        f' đã được cập nhật')
        update_window.destroy()
        show_button()

    update_window = Toplevel()
    update_window.grab_set()
    update_window.resizable(False, False)
    update_window.title('CẬP NHẬT')

    # Mã
    idLabel = Label(update_window, text='Mã',
                    font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=20)
    idEntry = Entry(update_window,
                    font=('times new roman', 15, 'bold'),
                    width=24)
    idEntry.grid(row=0, column=1, padx=20, pady=20)

    # tên
    nameLabel = Label(update_window, text='Tên',
                      font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=20)
    nameEntry = Entry(update_window,
                      font=('times new roman', 15, 'bold'),
                      width=24)
    nameEntry.grid(row=1, column=1, padx=20, pady=20)

    # Giá
    priceLabel = Label(update_window, text='Giá',
                       font=('times new roman', 15, 'bold'))
    priceLabel.grid(row=2, column=0, padx=20, pady=20)
    priceEntry = Entry(update_window,
                       font=('times new roman', 15, 'bold'),
                       width=24)
    priceEntry.grid(row=2, column=1, padx=20, pady=20)

    # Xuâất xứ
    makeinLabel = Label(update_window, text='Xuất xứ',
                        font=('times new roman', 15, 'bold'))
    makeinLabel.grid(row=3, column=0, padx=20, pady=20)
    makeinEntry = Entry(update_window,
                        font=('times new roman', 15, 'bold'),
                        width=24)
    makeinEntry.grid(row=3, column=1, padx=20, pady=20)

    # Ngày sản xuất
    nsxLabel = Label(update_window, text='NSX',
                     font=('times new roman', 15, 'bold'))
    nsxLabel.grid(row=4, column=0, padx=20, pady=20)
    nsxEntry = Entry(update_window,
                     font=('times new roman', 15, 'bold'),
                     width=24)
    nsxEntry.grid(row=4, column=1, padx=20, pady=20)

    # hạn sử dụng
    hsdLabel = Label(update_window, text='HSD',
                     font=('times new roman', 15, 'bold'))
    hsdLabel.grid(row=5, column=0, padx=20, pady=20)
    hsdEntry = Entry(update_window,
                     font=('times new roman', 15, 'bold'),
                     width=24)
    hsdEntry.grid(row=5, column=1, padx=20, pady=20)

    # nút thêm
    update_vg_button = ttk.Button(update_window, text='CẬP NHẬT',
                                  command=update_data)
    update_vg_button.grid(row=6, column=1, pady=5, padx=5)

    indexing=vg_table.focus()
    content=vg_table.item(indexing)
    listdata=content['values']
    idEntry.insert(0, listdata[0])
    nameEntry.insert(0,listdata[1])
    priceEntry.insert(0,listdata[2])
    makeinEntry.insert(0,listdata[3])
    nsxEntry.insert(0,listdata[4])
    hsdEntry.insert(0,listdata[5])


#hàm hiện bảng
def show_button():
    query = 'select * from raucu'
    mycusor.execute(query)
    fetched_data = mycusor.fetchall()
    vg_table.delete(*vg_table.get_children())
    for data in fetched_data:
        vg_table.insert('', END, values=data)


#Hàm xóa
def delete_button():
    indexing = vg_table.focus()
    content = vg_table.item(indexing)
    content_id=content['values'][0]
    query = 'delete from raucu where ma = %s'
    mycusor.execute(query, (content_id))
    con.commit()
    messagebox.showinfo('Xóa',
                        f'Sản phẩm có mã  {content_id} đã được xóa')
    query = 'select * from raucu'
    mycusor.execute(query)
    fetched_data = mycusor.fetchall()
    vg_table.delete(*vg_table.get_children())
    for data in fetched_data:
        vg_table.insert('',END, values=data)



#Hàm tìm kiếm
def search_vg():
    def search_data():
        query = 'select * from raucu where ma = %s or ten=%s or gia=%s or xuatxu=%s or nxs=%s or hsd=%s'
        mycusor.execute(query, (idEntry.get(), nameEntry.get(),
                        priceEntry.get(), makeinEntry.get(),
                        nsxEntry.get(), hsdEntry.get()))
        vg_table.delete(*vg_table.get_children())
        fetched_data= mycusor.fetchall()
        for data in fetched_data:
            vg_table.insert('', END, values=data)

    search_window = Toplevel()
    search_window.grab_set()
    search_window.resizable(False, False)
    search_window.title('TÌM KIẾM')

    # Mã
    idLabel = Label(search_window, text='Mã',
                    font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=20)
    idEntry = Entry(search_window,
                    font=('times new roman', 15, 'bold'),
                    width=24)
    idEntry.grid(row=0, column=1, padx=20, pady=20)

    # tên
    nameLabel = Label(search_window, text='Tên',
                      font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=20)
    nameEntry = Entry(search_window,
                      font=('times new roman', 15, 'bold'),
                      width=24)
    nameEntry.grid(row=1, column=1, padx=20, pady=20)

    # Giá
    priceLabel = Label(search_window, text='Giá',
                       font=('times new roman', 15, 'bold'))
    priceLabel.grid(row=2, column=0, padx=20, pady=20)
    priceEntry = Entry(search_window,
                       font=('times new roman', 15, 'bold'),
                       width=24)
    priceEntry.grid(row=2, column=1, padx=20, pady=20)

    # Xuâất xứ
    makeinLabel = Label(search_window, text='Xuất xứ',
                        font=('times new roman', 15, 'bold'))
    makeinLabel.grid(row=3, column=0, padx=20, pady=20)
    makeinEntry = Entry(search_window,
                        font=('times new roman', 15, 'bold'),
                        width=24)
    makeinEntry.grid(row=3, column=1, padx=20, pady=20)

    # Ngày sản xuất
    nsxLabel = Label(search_window, text='NSX',
                     font=('times new roman', 15, 'bold'))
    nsxLabel.grid(row=4, column=0, padx=20, pady=20)
    nsxEntry = Entry(search_window,
                     font=('times new roman', 15, 'bold'),
                     width=24)
    nsxEntry.grid(row=4, column=1, padx=20, pady=20)

    # hạn sử dụng
    hsdLabel = Label(search_window, text='HSD',
                     font=('times new roman', 15, 'bold'))
    hsdLabel.grid(row=5, column=0, padx=20, pady=20)
    hsdEntry = Entry(search_window,
                     font=('times new roman', 15, 'bold'),
                     width=24)
    hsdEntry.grid(row=5, column=1, padx=20, pady=20)

    # nút thêm
    search_vg_button = ttk.Button(search_window, text='TÌM KIẾM',
                               command=search_data)
    search_vg_button.grid(row=6, column=1, pady=5, padx=5)


#Hàm tạo thời gian thực
def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    dateTimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    dateTimeLabel.after(1000, clock)

#Biến count sẽ đếm kí tự của chuỗi và
#Cho xuất hiện từ kí tự trên label
count = 0
text = ''
#Hàm chuyển slide
def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)

#Hàm kết nối cơ sở dữ liệu
def connect_database():
    #Hàm keets nối với mysql

    def connect():
        global mycusor, con
        try:
            con = pymysql.connect(host=hostnameEntry.get(),
                                  user=usernameEntry.get(),
                                  password=passwordEntry.get())
            mycusor = con.cursor()

        except:
            messagebox.showerror('Lỗi kết nối',
                                 'Không thể kết nối với cơ sở dữ liệu',
                                 parent=connectWindow)
            return
        try:
            #Tạo database nếu chưa có
            query = 'create database ql_raucu'
            mycusor.execute(query)
            query = 'use ql_raucu'
            mycusor.execute(query)
            query = 'create table raucu(ma varchar(50) not null primary key,' \
                    'ten varchar(50) not null, gia varchar(50) not null,' \
                    'xuatxu varchar(50), nxs varchar(50) not null,' \
                    'hsd varchar(50) not null)'
            mycusor.execute(query)

        except:
            #Sử dụng database đã có
            query = 'use ql_raucu'
            mycusor.execute(query)
        messagebox.showinfo('Thông báo',
                            'Kết nối thành công.',parent=connectWindow)
        connectWindow.destroy()
        addButton.config(state=NORMAL)
        deleteButton.config(state=NORMAL)
        updateButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
        showButton.config(state=NORMAL)
        searchButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('KẾT NỐI CƠ SỞ DỮ LIỆU')
    connectWindow.resizable(0,0)

    #Tạo các sự kiện
    hostnameLabel = Label(connectWindow,
                          text='Host Name',
                          font=('arial', 15, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)

    hostnameEntry = Entry(connectWindow,
                          font=('roman', 15, 'bold'), bd=2)
    hostnameEntry.grid(row=0, column=1, pady= 20, padx= 40)

    usernameLabel = Label(connectWindow,
                          text='User Name',
                          font=('arial', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow,
                          font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, pady=20, padx=40)

    passwordLabel = Label(connectWindow,
                          text='Password',
                          font=('arial', 15, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWindow,
                          font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, pady=20, padx=40)

    connectButton = ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, columnspan=2)

#Hàm thêm rau củ mới
def add_raucu():
    # Hàm lấy thêm data vào database
    def add_data():
        if idEntry.get() == '' or nameEntry.get()=='' or priceEntry.get()=='' or makeinEntry.get()=='' or nsxEntry.get()==''or hsdEntry.get()=='':
            messagebox.showerror('Lỗi nhập',
                                 'Thông tin nhập vào chưa đầy đủ',
                                 parent=add_window)
        else:
            try:
                query = 'insert into raucu values(%s,%s,%s,%s,%s,%s)'
                mycusor.execute(query,(idEntry.get(), nameEntry.get(),
                                       priceEntry.get(), makeinEntry.get(),
                                       nsxEntry.get(), hsdEntry.get()))
                con.commit()
                result=messagebox.askyesno('Xác nhận','Dữ liệu đã được thêm vào. '
                                    'Bạn có muốn xóa form?',
                                           parent= add_window)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    priceEntry.delete(0, END)
                    makeinEntry.delete(0, END)
                    nsxEntry.delete(0, END)
                    hsdEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Lỗi thêm dữ liệu',
                                     'Mã rau củ bị trùng',
                                     parent=add_window)
                return
            query = 'select * from raucu'
            mycusor.execute(query)
            fetched_data = mycusor.fetchall()
            vg_table.delete(*vg_table.get_children())

            for data in fetched_data:
                datalist = list(data)
                vg_table.insert('',END, values=datalist)


    add_window = Toplevel()
    add_window.grab_set()
    add_window.resizable(False, False)

    #Mã
    idLabel = Label(add_window, text='Mã',
                    font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20,pady=20)
    idEntry = Entry(add_window,
                    font=('times new roman', 15, 'bold'),
                    width=24)
    idEntry.grid(row=0, column=1, padx=20,pady=20)

    # tên
    nameLabel = Label(add_window, text='Tên',
                    font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=20)
    nameEntry = Entry(add_window,
                    font=('times new roman', 15, 'bold'),
                    width=24)
    nameEntry.grid(row=1, column=1, padx=20, pady=20)

    # Giá
    priceLabel = Label(add_window, text='Giá',
                      font=('times new roman', 15, 'bold'))
    priceLabel.grid(row=2, column=0, padx=20, pady=20)
    priceEntry = Entry(add_window,
                      font=('times new roman', 15, 'bold'),
                      width=24)
    priceEntry.grid(row=2, column=1, padx=20, pady=20)

    # Xuâất xứ
    makeinLabel = Label(add_window, text='Xuất xứ',
                       font=('times new roman', 15, 'bold'))
    makeinLabel.grid(row=3, column=0, padx=20, pady=20)
    makeinEntry = Entry(add_window,
                       font=('times new roman', 15, 'bold'),
                       width=24)
    makeinEntry.grid(row=3, column=1, padx=20, pady=20)

    # Ngày sản xuất
    nsxLabel = Label(add_window, text='NSX',
                       font=('times new roman', 15, 'bold'))
    nsxLabel.grid(row=4, column=0, padx=20, pady=20)
    nsxEntry = Entry(add_window,
                       font=('times new roman', 15, 'bold'),
                       width=24)
    nsxEntry.grid(row=4, column=1, padx=20, pady=20)

    # hạn sử dụng
    hsdLabel = Label(add_window, text='HSD',
                     font=('times new roman', 15, 'bold'))
    hsdLabel.grid(row=5, column=0, padx=20, pady=20)
    hsdEntry = Entry(add_window,
                     font=('times new roman', 15, 'bold'),
                     width=24)
    hsdEntry.grid(row=5, column=1, padx=20, pady=20)

    #nút thêm
    add_vg_button=ttk.Button(add_window, text = 'THÊM RAU CỦ',
                             command=add_data)
    add_vg_button.grid(row=6, column=1, pady=5, padx=5)



#Tạo khung chương trình
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('breeze')
root.geometry('1174x500+50+20')
root.title('QUẢN LÝ RAU CỦ')

#Tạo thời gian thực
dateTimeLabel = Label(root,
                      font=('times new roman', 18, 'bold'))
dateTimeLabel.place(x=5, y=5)
clock()

#Tạo slide chuyển động
s = 'CHƯƠNG TRÌNH QUẢN LÝ RAU CỦ'
sliderLabel = Label(root,
                    font=('arial', 28, 'bold'),
                    width=30, fg='blue')
sliderLabel.place(x=280, y=6)
slider()

#Tạo nút connect đến database
connectButton = ttk.Button(root, text='Kết nối dữ liệu',
                           command=connect_database)
connectButton.place(x=1000, y=20)

#Tạo frame các nút xử lý
leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=500)

#Tạo icon
logo_image = PhotoImage(file='iconraucu.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row= 0, column=0)

#Tạo nút thêm rau củ
addButton = ttk.Button(leftFrame, text= 'Thêm rau củ mới',
                       width=25, command=add_raucu)
addButton.grid(row=1, column=0, pady= 20)

#Tạo nút tìm kiếm rau củ
searchButton = ttk.Button(leftFrame, text= 'Tìm kiếm rau củ ',
                          width=25,command=search_vg)
searchButton.grid(row=2, column=0, pady= 20)

#Tạo nút cập nhật rau củ
updateButton = ttk.Button(leftFrame, text= 'Cập nhật rau củ '
                          ,width=25, command=update_button)
updateButton.grid(row=3, column=0, pady= 20)

#Tạo nút xóa rau củ
deleteButton = ttk.Button(leftFrame, text= 'Xóa rau củ ',
                          width=25, command=delete_button)
deleteButton.grid(row=4, column=0, pady= 20)


#Tạo nút xe, rau củ
showButton = ttk.Button(leftFrame, text= 'Xem rau củ ',
                        width=25, command=show_button)
showButton.grid(row=5, column=0, pady= 20)

#Tạo nút xuất exel rau củ
exportButton = ttk.Button(leftFrame, text= 'Xuất exel',
                          width=25, command=export_data)
exportButton.grid(row=6, column=0, pady= 20)

#Tạo frame hiển thị
rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=500)

#Tạo bảng hiển thị
scollBarX= Scrollbar(rightFrame, orient=HORIZONTAL)
scollBarY= Scrollbar(rightFrame, orient=VERTICAL)

vg_table = ttk.Treeview(rightFrame, columns=('ma', 'ten',
                                  'gia', 'xuatxu','NSX', 'HSD'),
                        xscrollcommand=scollBarX.set,
                        yscrollcommand=scollBarY.set)
scollBarX.config(command=vg_table.xview)
scollBarY.config(command=vg_table.yview)
scollBarX.pack(side=BOTTOM, fill=X)
scollBarY.pack(side=RIGHT, fill=Y)
vg_table.pack(fill=BOTH, expand=1)

#Tạo heading cho bảng
vg_table.heading('ma', text='Mã rau củ')
vg_table.heading('ten', text='Tên rau củ')
vg_table.heading('gia', text='Giá rau củ')
vg_table.heading('xuatxu', text='Xuất xứ rau củ')
vg_table.heading('NSX', text='NXS')
vg_table.heading('HSD', text='HSD')
vg_table.config(show='headings')



root.mainloop()