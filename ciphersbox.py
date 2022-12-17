
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
import tkinter.font
import math
from datetime import datetime
#from matdeck.tkinter.COMWidget import COM_Widget
#from matdeck.tkinter.TCPWidget import TCP_Widget
import numpy as np
import string





class textciher():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('700x490')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 700, height = 490)
        self.var = IntVar()
        self.message_var = StringVar()
        self.input_text = Text(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.input_text.place(x = 40, y = 130, width = 280, height = 40)
        self.label2 = Label(self.w1, text = "Input:", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
        self.label2.place(x = 40, y = 100, width = 90, height = 22)
        self.label2_copy = Label(self.w1, text = "output:", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
        self.label2_copy.place(x = 40, y = 180, width = 90, height = 22)
        self.cipher_combo = Combobox(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.cipher_combo.place(x = 510, y = 130, width = 120, height = 42)
        self.cipher_combo['values'] = ("Cesar", "Monoalphabetic", "Polyalphabetic", "Playfair")
        self.cipher_combo.current(0)
        self.cipher_combo.bind("<<ComboboxSelected>>", self.cipher_type)
        self.label2_copy_copy = Label(self.w1, text = "Cipher:", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
        self.label2_copy_copy.place(x = 510, y = 100, width = 90, height = 22)
        self.key_text = Text(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.key_text.place(x = 510, y = 280, width = 160, height = 40)
        self.label2_copy_copy_copy = Label(self.w1, text = "Key", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
        self.label2_copy_copy_copy.place(x = 510, y = 250, width = 90, height = 22)
        self.encrypt_radio = Radiobutton(self.w1, text = "Encryption", value = 1,variable = self.var, anchor='w', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
        self.encrypt_radio.place(x = 140, y = 370, width = 130, height = 32)
        self.encrypt_radio['command'] = self.enc_rad
        self.decrypy_radio = Radiobutton(self.w1, text = "Decryption", value = 2,variable = self.var, anchor='w', font = tkinter.font.Font(family = "Calibri", size = 14), cursor = "arrow", state = "normal")
        self.decrypy_radio.place(x = 140, y = 400, width = 130, height = 32)
        self.decrypy_radio['command'] = self.dec_rad
        self.button1 = Button(self.w1, text = "Convert", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.button1.place(x = 510, y = 380, width = 150, height = 52)
        self.button1['command'] = self.convert
        # self.output_label = Label(self.w1, text = "", anchor='w', fg = "#aa0000", font = tkinter.font.Font(family = "Calibri", size = 16), cursor = "arrow", state = "normal")
        # self.output_label.place(x = 40, y = 210, width = 400, height = 152)
        self.output_message = Message(self.w1 ,width= 400 ,textvariable= self.message_var, fg = "#aa0000", font = tkinter.font.Font(family = "Calibri", size = 16),justify=LEFT,  anchor='w')
        self.output_message.place(x = 40, y = 210, width = 400, height = 152)
        self.button2 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.button2.place(x = 40, y = 40, width = 90, height = 42)
        self.button2['command'] = self.go_home

    def cipher_type(self, e):
        cipher = self.cipher_combo.get()

    def convert(self):
        input = str(self.input_text.get("1.0",'end-1c')).lower()
        print(input)
        cipher = self.cipher_combo.get()
        
        
        alphabet = string.ascii_lowercase
        
        
        
        if cipher == "Cesar":
            key = int(self.key_text.get("1.0",'end-1c'))
            if self.var.get() == 1:
                shift = key % 26
            else:
                shift = (26-key) % 26
            
            
            print(self.var.get())
            shifted = alphabet[shift:] + alphabet[:shift]
            table = str.maketrans(alphabet, shifted)
            print(alphabet)
            print(input.translate(table))
            #self.output_label["text"] = input.translate(table)
            self.message_var.set(input.translate(table))
            
        elif cipher == "Monoalphabetic":
            output=""
            key = str(self.key_text.get("1.0",'end-1c')).lower()
            for c in range(len(input)):
                if input[c] in alphabet:
                    if self.var.get() ==1:
                        i = alphabet.index(input[c])
                        output = output + key[i]
                    else :
                        i = key.index(input[c])
                        output = output + alphabet[i]
                else:
                    output = output + input[c] 
            # self.output_label["text"] = output
            self.message_var.set(output)
            
        
        elif cipher == "Polyalphabetic":
            key = int(self.key_text.get("1.0",'end-1c'))
            output=""
            for c in range(len(input)):
                if input[c] in alphabet:
                    i = alphabet.index(input[c])
                    if self.var.get() == 1:
                        m = (i+key) % 26
                        key = alphabet.index(input[c])
                    else:
                        m = (i - key) % 26
                        key = m
                    
                    
                    output = output + alphabet[m]
                else:
                    output = output + input[c] 
            #self.output_label["text"] = output
            self.message_var.set(output)
        
        elif cipher == "Playfair":
            key = str(self.key_text.get("1.0",'end-1c')).lower()
            output=""

            plaintextpairs = []
            ciphertextpairs = []
            
            for c in range(len(input)):
                if input[c] == "j":
                    input[c] = "i"
                if c != 0:
                    if input[c] == input[c-1]:
                        input = input[:c] + "x" + input[c:]
                        
            
            

            if len(input) % 2 != 0:
                input = input + "z"
            
            z=0
            while z < len(input):
                plaintextpairs.append(input[z]+input[z+1])
                z += 2
            
            print(plaintextpairs)

            
            atoz = string.ascii_lowercase.replace('j','.')
            key_matrix = ['' for i in range(5)]

            i = 0
            j = 0

            for c in key:
                if c in atoz:
                    key_matrix[i] += c
                    atoz = atoz.replace(c,'.')

                    j += 1
                    if j > 4:
                        i += 1
                        j = 0

            for c in atoz:
                if c != '.':
                    key_matrix[i] += c

                    j += 1
                    if j > 4:
                        i += 1
                        j = 0
            
            print(key_matrix)

            for pair in plaintextpairs:
                applied_rule = False

                for row in key_matrix:
                    if pair[0] in row and pair[1] in row:
                        i0 = row.find(pair[0])
                        i1 = row.find(pair[1])
                        if self.var.get() ==1:
                            cipherpair = row[(i0 + 1) % 5] + row[(i1 + 1) % 5]
                        else:
                            cipherpair = row[(i0 - 1) % 5] + row[(i1 - 1) % 5]
                        
                        ciphertextpairs.append(cipherpair)
                        print("rule 1")
                        applied_rule = True
                
                if applied_rule:
                    continue

                for j in range(5):
                    col = "".join([key_matrix[i][j] for i in range(5)])
                    if pair[0] in col and pair[1] in col:
                        j0 = col.find(pair[0])
                        j1 = col.find(pair[1])
                        if self.var.get() == 1:
                            cipherpair = col[(j0 + 1) % 5] + col[(j1 + 1) % 5]
                        else:
                            cipherpair = col[(j0 - 1) % 5] + col[(j1 - 1) % 5]
                        ciphertextpairs.append(cipherpair)
                        print("rule 2")
                        applied_rule = True
                
                if applied_rule:
                    continue


                i0 = 0
                i1 = 0
                j0 = 0
                j1 = 0
                for i in range(5):
                    row = key_matrix[i]
                    if pair[0] in row:
                        i0 = i
                        j0 = row.find(pair[0])

                    if pair[1] in row:
                        i1 = i
                        j1 = row.find(pair[1])
                        
                    
                cipherpair = key_matrix[i0][j1] + key_matrix[i1][j0]
                ciphertextpairs.append(cipherpair)



            print(ciphertextpairs)
            output = "".join(ciphertextpairs)
            print(input)
            #self.output_label["text"] = output
            self.message_var.set(output)


    def enc_rad(self):
        self.r = 1

    def dec_rad(self):
        self.r = 2

    def go_home(self):
        self.w1.destroy()
        a = Home(0)
        a.w1.mainloop()

class Home():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#e3e3e3')
            self.w1.geometry('680x510')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#e3e3e3')
            self.w1.place(x = 0, y = 0, width = 680, height = 510)
        self.widget1 = Frame(self.w1)
        self.widget1.configure(bg = '#393939')
        self.widget1.place(x = -10, y = -10, width = 690, height = 90)
        self.label1 = Label(self.widget1, text = "Ciphers Box", bg = '#393939', anchor='w', fg = "#ffffff", font = tkinter.font.Font(family = "Call Of Ops Duty", size = 26), cursor = "arrow", state = "normal")
        self.label1.place(x = 240, y = 10, width = 240, height = 72)
        self.label2 = Label(self.w1, text = "choose your input", bg = '#e3e3e3', anchor='w', fg = "#000000", font = tkinter.font.Font(family = "Calibri", size = 24), cursor = "arrow", state = "normal")
        self.label2.place(x = 190, y = 150, width = 330, height = 92)
        self.button1 = Button(self.w1, text = "Text", font = tkinter.font.Font(family = "Charlesworth", size = 16), cursor = "arrow", state = "normal")
        self.button1.place(x = 460, y = 310, width = 120, height = 82)
        self.button1['command'] = self.textcipher
        self.button1_copy = Button(self.w1, text = "Image", font = tkinter.font.Font(family = "Charlesworth", size = 16), cursor = "arrow", state = "normal")
        self.button1_copy.place(x = 110, y = 310, width = 120, height = 82)
        self.button1_copy['command'] = self.Image_cipher

    def textcipher(self):
        self.w1.destroy()
        a = textciher(0)
        a.w1.mainloop()

    def Image_cipher(self):
        self.w1.destroy()
        a = Widget3(0)
        a.w1.mainloop()
        






class Widget3():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('930x610')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 930, height = 610)
        self.imagename =""
        self.imagebox = Label(self.w1)
        self.imagebox.place(x = 20, y = 140, width = 440, height = 300)
        
        self.image2 = Label(self.w1)
        self.image2.place(x = 480, y = 140, width = 420, height = 300)
        self.button1 = Button(self.w1, text = "convert", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.button1.place(x = 750, y = 520, width = 140, height = 52)
        self.button1['command'] = self.convert
        self.key_text = Text(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.key_text.place(x = 750, y = 460, width = 130, height = 40)

        self.label1 = Label(self.w1, text = "Image Encryption or Decryption", anchor='w', fg = "#000000", font = tkinter.font.Font(family = "Coolvetica Rg", size = 16), cursor = "arrow", state = "normal")
        self.label1.place(x = 20, y = 60, width = 890, height = 62)
        self.button2 = Button(self.w1, text = "Choose Image", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.button2.place(x = 160, y = 460, width = 100, height = 32)
        self.button2['command'] = self.pick_image
        self.warning_label = Label(self.w1, text = "", anchor='w', fg = "#aa0000", font = tkinter.font.Font(family = "Calibri", size = 16), cursor = "arrow", state = "normal")
        self.warning_label.place(x = 130, y = 500, width = 400, height = 152)
        self.label2 = Label(self.w1, text = "Key:", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 12), cursor = "arrow", state = "normal")
        self.label2.place(x = 710, y = 460, width = 30, height = 52)
        self.button3 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.button3.place(x = 30, y = 30, width = 120, height = 42)
        self.button3['command'] = self.go_home

    def go_home(self):
        self.w1.destroy()
        a = Home(0)
        a.w1.mainloop()

    def convert(self):
        im = Image.open(self.imagename, "r")
        arr = im.load() #pixel data stored in this 2D array

        dimentioms = list(np.array(im).shape)
        def rot(A, n, x1, y1): #this is the function which rotates a given block
            temple = []
            for i in range(n):
                temple.append([])
                for j in range(n):
                    temple[i].append(arr[x1+i, y1+j])
            for i in range(n):
                for j in range(n):
                    arr[x1+i,y1+j] = temple[n-1-i][n-1-j]


        xres = dimentioms[1]
        yres = dimentioms[0]
        alphabet = string.ascii_lowercase
        password = str(self.key_text.get("1.0",'end-1c')).lower()
        if len(password) > 10:
            self.warning_label['text'] = "password maxlength is 10"

        keys = []
        for c in password:
            try:
                keys.append(int(c))
            except:
                if c in alphabet:
                    key = alphabet.index(c) + 1
                    
                    print(datetime.now().ctime())
                    keys.append(key)
                else:
                    pass
            
        BLKSZ = sum(keys) % 27
        
        for i in range(2, BLKSZ+1):
            for j in range(int(math.floor(float(xres)/float(i)))):
                for k in range(int(math.floor(float(yres)/float(i)))):
                    rot(arr, i, j*i, k*i)
        for i in range(3, BLKSZ+1):
            for j in range(int(math.floor(float(xres)/float(BLKSZ+2-i)))):
                for k in range(int(math.floor(float(yres)/float(BLKSZ+2-i)))):
                    rot(arr, BLKSZ+2-i, j*(BLKSZ+2-i), k*(BLKSZ+2-i))
        save_path = "D:/security/images/"
        nameing = str(datetime.now().timestamp())+".png"
        im.save(save_path+nameing)
        image = Image.open(save_path +nameing)
        resized_image = image.resize((440,300))
        img = ImageTk.PhotoImage(resized_image)
        
        self.image2.config(image = img)
        self.image2.image = img
        

    def pick_image(self):
        file1 = filedialog.askopenfile(mode='r',filetypes =[("all files", "*"),('jpg file','*.jpg'),('png file','*.png')])
        if file1 is not None:
            print(file1.name)
            self.imagename = file1.name
            image = Image.open(file1.name)
            resized_image = image.resize((440,300))
            img = ImageTk.PhotoImage(resized_image)
            print(datetime.now().ctime())
            self.imagebox.config(image = img)
            self.imagebox.image = img
if __name__ == '__main__':
    a = Home(0)
    a.w1.mainloop()
