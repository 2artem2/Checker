import urllib.request
import ssl
from tkinter import Tk, Label, Button, Entry

window = Tk()
window.geometry("700x350")
window.title("Connectivity Checker")

head = Label(window, text="Введите URL сайта", font=('Calibri 15'))
head.pack(pady=20)

result_label = Label(window, font=('Calibri 15'))
result_label.place(x=200, y=200)


def check():
    web = url.get()
    try:
        context = ssl._create_unverified_context()
        status_code = urllib.request.urlopen(web, context=context).getcode()
        if status_code in range(200, 300):
            result_label.config(text="Website Available")
        else:
            result_label.config(text="Website Not Available")
    except Exception as e:
        result_label.config(text=f"Error: {e}")


url = Entry(window)
url.place(x=200, y=80, height=30, width=280)

Button(window, text="Check", command=check).place(x=320, y=160)

window.mainloop()
