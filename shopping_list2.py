from tkinter import *
import pickle
import webbrowser

# functions

def add_item():
    item = entry.get()
    listbox.insert(END, item)
    entry.delete(0, END)

def remove_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)

def save_item():
    items = list(listbox.get(0,END))
    with open('shopping_list2.pkl', 'wb') as f:
        pickle.dump(items, f)

    with open('shopping_list2.txt','w', encoding='utf-8') as txtfile:
        for item in items:
            print(item, file=txtfile)

def load_list():
    try:
        with open('shopping_list2.pkl', 'rb') as f:
            items = pickle.load(f)
            for item in items:
                listbox.insert(END, item)
    except FileNotFoundError:
        pass

def net():
    webbrowser.open('https://google.com')




root = Tk()
root.title("Shopping list")
root.geometry('500x500')

# Colors
bg_color = '#fcf3cf'
button_color = '#5dade2'

root.configure(bg=bg_color)

# Entry mező
entry = Entry(root)
entry.configure(bg=bg_color,font='Arial 16', width=30)
entry.pack()

# Gombok

add_buton = Button(root, bg=button_color, text='Add', font='Arial 16', command=add_item)
add_buton.pack()

remove_button = Button(root, bg=button_color, text='Remove', font='Arial 16', command=remove_item)
remove_button.pack()

save_button = Button(root, bg=button_color, text='Save', font='Arial 16', command=save_item)
save_button.pack()

browser_button = Button(root, bg=button_color, text='Browser', font='Arial 16', command=net)
browser_button.pack()

# listbox

listbox = Listbox(root, height=50, width=30)
listbox.configure(bg=bg_color, font='Arial 16')
listbox.pack()

load_list()









root.mainloop()