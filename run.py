from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import threading
import subprocess

class Widget:
    def __init__(self):
        self.root = CTk()
        set_appearance_mode("system")

        self.root.title('Neo')
        self.root.geometry('800x600') 

        self.on = True
        self.terminate_flag = False
        self.stop_main_flag = threading.Event()
        self.thread = None

        def toggle_mode():
            current_bg = self.root.cget("bg")
            set_appearance_mode("light" if current_bg == "gray14" else "dark")

        def click_handler():
            self.on = False
            self.button.config(state=DISABLED, relief=SUNKEN) 
            self.terminate_flag = False
            if self.thread and self.thread.is_alive():
                self.terminate_flag = True
                self.stop_main_flag.set()
                self.thread.join()
                self.thread = None
            self.terminal_text.delete(1.0, END)
            self.thread = threading.Thread(target=self.run_in_thread)
            self.thread.start()

        photo = ImageTk.PhotoImage(file='Data//Nemo_logo.png')
        self.button = Button(self.root, image=photo, command=click_handler, relief=RAISED)
        self.button.pack(pady=100)  

        night_btn = ImageTk.PhotoImage(Image.open('Data//Dark_Light.png'))
        Button(self.root, image=night_btn, command=toggle_mode, borderwidth=0).pack(side='right')

        
        self.terminal_text = Text(self.root, wrap=WORD, height=20, width=80, font=("Helvetica", 14), state=NORMAL)
        self.terminal_text.pack(pady=30)

        scrollbar = Scrollbar(self.root, command=self.terminal_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.terminal_text.config(yscrollcommand=scrollbar.set)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.root.mainloop()

    def run_in_thread(self):
        import sys
        sys.stdout = self.TerminalRedirector(self.terminal_text)

        print("Process Started...")

        self.stop_main_flag.clear()
        process = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        while not self.terminate_flag:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.terminal_text.config(state=NORMAL)
                self.terminal_text.insert(END, output.strip() + '\n')
                self.terminal_text.see(END)
                self.terminal_text.update_idletasks()

        print("Process finished")

        process.terminate()
        process.wait()

        self.root.after(0, self.enable_button)

    def enable_button(self):
        self.button.config(state=NORMAL, relief=RAISED)
        self.on = True  

    def on_close(self):
        self.on = True
        self.terminate_flag = False
        if self.thread and self.thread.is_alive():
            self.terminate_flag = True
            self.stop_main_flag.set()
            self.thread.join()
        self.root.destroy()

    class TerminalRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, text):
            self.text_widget.insert(END, text + '\n')
            self.text_widget.see(END)

if __name__ == '__main__':
    widget = Widget()
