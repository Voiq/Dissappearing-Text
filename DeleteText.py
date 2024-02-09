from tkinter import *
import time
import threading

class DeleteText(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Writing App")
        self.geometry("500x300")
        self.config(bg="#F1EB9C")


        self.text=Text(self,wrap="word" , bg="#F1EB9C")
        self.text.pack(expand=True,fill="both")

        self.countdown = 10
        self.typing = False

        self.text.bind("<Key>",self.key_pressed)

        self.timer_thread = threading.Thread(target=self.start_writing)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def key_pressed(self,event):
        self.typing = True


    def start_writing(self):
        while self.countdown > 0 :
            time.sleep(1.2)
            self.countdown -= 1
            self.typing = False
        self.delete_text()


    def delete_text(self):
        self.text.delete("1.0",END)
        self.countdown = 10
        self.start_writing()

