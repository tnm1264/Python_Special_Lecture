#20103323 김태욱 Day05(0828) - homework2 : 도서관리 프로그램을 tkinter와 sqlite3를 이용하여 만들기
from tkinter import *
import sqlite3

#UI class
class BookManageUI:
    #Constructor에서 DB파일을 만들고 manageStart로 UI 시작
    def __init__(self, master):
        #Open db
        self.con = sqlite3.connect('bookDB.db')
        self.cur = self.con.cursor()
        try:
            self.cur.execute("CREATE TABLE BookTable(Name text, Author text, Price text);")
            self.manageStart(master)
        except sqlite3.OperationalError:
            self.manageStart(master)
    
    # manageStart = UI, 추가하고 싶은 책에 대한 정보를 적고, Add를 누르면 DB에 추가된다. 끝내려면 Quit
    def manageStart(self,master):
        frame = Frame(master) 
        frame.pack()

        frame2 = Frame(frame)
        text = Label(frame2, text='BookName')
        text.pack(side=LEFT)
        self.input2 = Entry(frame2)
        self.input2.pack(side=LEFT)
        frame2.pack()

        frame3 = Frame(frame)
        text = Label(frame3, text='Author', padx=12)
        text.pack(side=LEFT)
        self.input3 = Entry(frame3)
        self.input3.pack(side=LEFT)
        frame3.pack()

        frame4 = Frame(frame)
        text = Label(frame4, text='Price', padx=17)
        text.pack(side=LEFT)
        self.input4 = Entry(frame4)
        self.input4.pack(side=LEFT)
        frame4.pack()

        frame6 = Frame(frame)
        self.button = Button(frame6, text="Quit", command=self.close)
        self.button.pack(side=BOTTOM)
        frame6.pack(side=RIGHT)

        frame5 = Frame(frame)
        self.button = Button(frame5, text="Add", command=self.all_output)
        self.button.pack(side=BOTTOM)
        frame5.pack(side=RIGHT)
        
    def output(self):
        return self.input2.get()

    def output2(self):
        return self.input3.get()

    def output3(self):
        return self.input4.get()

    #각 field에 입력된 값을 하나로 합쳐서 DB에 넣는 all_output함수
    def all_output(self):
        inputName = self.output()
        inputAuthor = self.output2()
        inputPrice = self.output3()
        query = "INSERT INTO BookTable VALUES('"+inputName+"','"+inputAuthor+"','"+inputPrice+"');"
        #print(query)
        self.cur.execute(query)
        self.con.commit()
        self.show_db()
        
    #db에 정확히 들어갔는지 확인하기 위한 show_db
    def show_db(self):
        self.cur.execute("SELECT * FROM BookTable;")
        #self.cur.execute("SELECT * FROM sqlite_master WHERE type='table'")
        print(self.cur.fetchall())

    def close(self):
        print('quit')
        self.cur.close()
        self.con.close()
        exit()

def main():
    root = Tk()
    app = BookManageUI(root)
    root.mainloop() 

if __name__ == '__main__': 
    main()
