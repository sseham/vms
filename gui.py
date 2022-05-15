#imports
import tkinter as tk
from tkinter import *

#window initializing
window=tk.Tk()
window.title('Vehicle Maintenance System')
window.geometry("1920x1080")
window.configure(bg="#E62727")

#vms backgrounds and labels
#capital vms label
vms = tk.Label(window, text= "VMS", font = ("Bold", 75), fg="white", bg="#E62727").place(x=570,y=50)
#full vms acronym
vms_full= tk.Label(window, text = "Vehical Maintenance System", font = ("Arial", 25), bg = "#E62727", fg="white").place(x=470,y=155)
#second half of the screen bg
bg_color_sec = tk.Label(window, bg = "white", width = 1920, height = 1080).place(y=250)

#image importing
menu_image = tk.PhotoImage(file = r"C:\Users\wahid\Downloads\menu_icon.png")
howto_image = tk.PhotoImage(file = r"C:\Users\wahid\Downloads\howto.png")
mycar_image = tk.PhotoImage(file = r"C:\Users\wahid\Downloads\mycars.png")

#create functions label for buttons
#command prompt after home-icon button is pushed
def menu_command():
    #menu text and bg labels
    menu_slide_label = tk.Label(window, bg = "#1e1b1b", width = 30, height = 500).place(x=0,y=0)
    menu_slide_text = tk.Label(window, text = "MENU", font = ("Arial", 25), fg = "white", bg = "#1e1b1b").place(x=55,y=50)
    #navigation text
    home_menu_text = tk.Button(window, text = "Home", font = ("Arial", 20), bg = "#1e1b1b", fg = "#E62727").place(x=20,y= 120)
    mycar_menu_text = tk.Button(window, text = "My Car", font = ("Arial", 20), bg = "#1e1b1b", fg = "#E62727").place(x=20,y= 190)
    howto_menu_text = tk.Button(window, text = "How To", font = ("Arial", 20), bg = "#1e1b1b", fg = "#E62727").place(x=20,y=260)
    
    #exit button command
    def exit_command():
        #add to this
        menu_button = tk.Button(window, image =menu_image, command = menu_command, borderwidth =0,).place(x=50,y=50)
        return
    #button to exit menu
    exit_button = tk.Button(window, text = ">", font = ("Arial", 15), bg = "#1e1b1b", fg = "white", width = 3,height=1, command = exit_command).place(x=160,y=5)
    return

#command after my cars button is pushed
def mycar_command():
    return

#command after how-to button is pushed
def howto_command(): 
    #fill in command
    return

#creating labels for the images
menu_label = tk.Label(image = menu_image, relief="groove")
menu_bg_label = tk.Label(window, bg = "white", width = 15, height = 7).place(x=45,y=45)
mycar_label = tk.Label(image = mycar_image, relief="groove")
howto_label = tk.Label(image = howto_image, relief="groove")

#creating text labels for the images
menu_text_label = tk.Label(window, text = "Menu", font = ("Arial", 15), fg = "white", bg ="#E62727").place(x=75, y=160)
mycar_text_label =  tk.Label(window, text = "My Car", font = ("Arial", 15), fg = "#E62727", bg ="white").place(x=410, y=565)
howto_text_label = tk.Label(window, text = "How To", font = ("Arial", 15), fg = "#E62727", bg ="white").place(x=1100, y=565)

#creating buttons for the image labels
menu_button = tk.Button(window, image =menu_image, command =menu_command, borderwidth =0,).place(x=50,y=50)
mycar_button = tk.Button(window, image =mycar_image, command =mycar_command, borderwidth =0).place(x=325, y=300)
howto_button = tk.Button(window, image =howto_image, command =howto_command, borderwidth =0).place(x=1000,y=300)


window.mainloop()
