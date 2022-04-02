import pyperclip
import pyshorteners
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Making 'Paste with mouse'menu
def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Paste")


# Showing 'Paste with mouse'menu
def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


# =====The URl-shortening function======
def shortener():
    srv = choose_shortener.get()
    try:
        s = pyshorteners.Shortener()
        long_url_adr = long_url.get()
        if srv == 'Chilp.it':
            short_url_adr = s.chilpit.short(long_url_adr)
        elif srv == 'Clck.ru':
            short_url_adr = s.clckru.short(long_url_adr)
        elif srv == 'Da.gd':
            short_url_adr = s.dagd.short(long_url_adr)
        elif srv == 'Is.gd':
            short_url_adr = s.isgd.short(long_url_adr)
        elif srv == 'NullPointer':
            short_url_adr = s.nullpointer.short(long_url_adr)
        elif srv == 'Os.db':
            short_url_adr = s.osdb.short(long_url_adr)
        else:
            short_url_adr = s.tinyurl.short(long_url_adr)
        short_url.delete(0, END)
        short_url.insert(0, short_url_adr)
    except:
        messagebox.showerror('URL-address shortening error',
                             'Wrong URL-address or\nNo internet connection!')  


# Copy short URL-address into clipboard
def copy_to_clipboard():
    url = short_url.get()
    pyperclip.copy(url)


# Clear all entries
def clear_all():
    long_url.delete(0, END)
    short_url.delete(0, END)


# =====VARIABLES=====
bg_color = '#EEE8AA'  # Pale Goldenrod
fg_color = '#0D0E0E'  # Black Pearl
app_font = 'Tahoma 11 bold'
shortener_list = ['Chilp.it',
                  'Clck.ru',
                  'Da.gd',
                  'Is.gd',
                  'NullPointer',
                  'Os.db',
                  'TinyURL.com']  # list of URL-shortening services


# =====INTERFACE=====
root = Tk()
root.title("URL Shortener")
root.iconbitmap('icon.ico')
root.geometry('549x225+300+200')
root.resizable(0, 0)
root['bg'] = bg_color
make_menu(root)

Label(root, text = 'Choose a shortening service:', font = app_font,
      bg = bg_color, fg = fg_color).grid(row = 0, column = 0,
                                         columnspan = 2, pady = 15)

# Choose a URL-address shortening service
srv = StringVar()
choose_shortener = ttk.Combobox(root, width = 22, textvariable = srv)
choose_shortener['values'] = shortener_list
choose_shortener.grid(row = 0, column = 2, pady = 10)
choose_shortener.current(6)

# Frame for a long URL-address
insert_url_frame = LabelFrame(root, text = 'Paste a URL-address',
                              height = 100, bg = bg_color, relief = RIDGE,
                              fg = fg_color)
insert_url_frame.grid(row = 1, columnspan = 3, padx = 5)

# Entry window for a long URL-address
long_url = Entry(insert_url_frame, width = 85)
long_url.grid(row = 2, columnspan = 3, padx = 10, pady = 5)
long_url.focus_set()  # focus on the entry window on the program start
long_url.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

# Frame for a short URL-address
short_url_frame = LabelFrame(root, text = 'Shortened URL-address',
                             height = 100, bg = bg_color, relief = RIDGE)
short_url_frame.grid(row = 4, columnspan = 3, padx = 5, pady = 10)

# Window for a short URL-address
short_url = Entry(short_url_frame, width = 85)
short_url.grid(row=5, columnspan = 3, padx = 10, pady = 5)

# Buttons
btn_short = ttk.Button(root, width = 19, text = 'Shorten URL-address',
                       command = shortener)
btn_short.grid(row=6, column=0, padx = 10, pady = 10)

btn_copy = ttk.Button(root, width = 19, text = 'Copy URL-address',
                      command = copy_to_clipboard)
btn_copy.grid(row=6, column=1, padx = 10, pady = 10)

btn_clear = ttk.Button(root, width = 19, text = 'Clear all',
                       command = clear_all)
btn_clear.grid(row=6, column=2, padx = 10, pady = 10)

root.mainloop()
