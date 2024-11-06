from tkinter import *
from tkinter filedialog as fd
from tkinter import ttk
import requests
from bottle import response
from django.utils.encoding import filepath_to_uri


def upload():
    filepath = fd.askopenfilnamee()
    if filepath:
        files = {'file': open(filepath, 'rb')}
        response = requests.post('http://file.io', files=files)
        if response.status_code == 200:
            link = response.json()['link']
            entry.insert(0, link)

window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop()