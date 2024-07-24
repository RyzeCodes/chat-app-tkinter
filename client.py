import socket
from threading import Thread
from tkinter import *

nickname = input("Enter nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address, port))

print("connected with the server")







class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width = False, height = False)
        self.login.configure(width = 400, height = 300)
        self.pls = Label(self.login, text="Please login to continue...", justify = CENTER, font="helvetica 14 bold")
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)
        
        self.labelName = Label(self.login, text="Name: ", font="helvetica 12")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        self.entryName = Entry(self.login, font="helvetica 14")
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        self.go = Button(self.login, text="Continue", font = "helvetica 14 bold", command=self.goahead(self.entryName.get()))
        self.go.place(relheight=0.1, relx=0.4, rely=0.4)


        self.window.mainloop()

    def goahead(self, name):
        self.login.destroy()
        self.name = name
        recv = Thread(target=self.recieve)
        recv.start()
    
    def recieve(self):
        while True:
            try:
                message = client.recv(2048).decode("utf-8")
                if message == "NICKNAME":
                    client.send(nickname.encode("utf-8"))
                else:
                    print(message)
            except:
                print("connection closed by the server")
                client.close()
                break

g = Gui()



# def recieve():
#     while True:
#         try:
#             message = client.recv(2048).decode("utf-8")
#             if message == "NICKNAME":
#                 client.send(nickname.encode("utf-8"))
#             else:
#                 print(message)
#         except:
#             print("connection closed by the server")
#             client.close()
#             break

# recv_thread = Thread(target=recieve)
# recv_thread.start()

