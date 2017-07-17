#!/usr/bin/python3

from tkinter import font
from tkinter import *

window = Tk()
window.title("GCryptor")
window.geometry("1250x500+70+110")

img = Image("photo", file="encrypt.gif")
window.tk.call("wm","iconphoto",window._w,img)

def encrypt(filename): 
    encrypted = ""

    with open(str(filename.get())) as file:
        for line in file:
            for letter in line:
                encrypted += chr(ord(letter) + 5)

    final_encryption = encrypted * 3

    file = open(str(filename.get()),"w")
    file.write(final_encryption)
    file.close()


def decrypt(filename): 
    decrypted = ""

    with open(str(filename.get())) as file:
        for line in file:
            for letter in line:
                decrypted += chr(ord(letter) - 5)

    final_decryption = decrypted[0:int(len(decrypted) / 3)]

    file = open(str(filename.get()),"w")
    file.write(final_decryption)
    file.close()


def main_menu():
    main = Frame(window)
    main.pack()

    def destroy_main():
        main.destroy()

    i11 = font.Font(family="impact", size=11)
    i12 = font.Font(family="impact", size=12)
    i12bold = font.Font(family="impact", size=12, weight=font.BOLD)
    i15 = font.Font(family="impact", size=15)
    

    def encrypt_menu():
        encrypt_frame = Frame()
        encrypt_frame.pack(side=TOP, anchor=W)

        def destroy_encrypt():
            encrypt_frame.destroy()

        back = Button(encrypt_frame, height=4, width=10, bg="#a7a7a7", font=i12 , text="Back", command=lambda:[destroy_encrypt(), main_menu()]).grid(row=0, column=0)

        spacer = Frame(encrypt_frame, width=270).grid(row=0, column=1)

        filename = StringVar()

        entry_box = Entry(encrypt_frame, font=i15, textvariable=filename)
        entry_box.grid(row=0, column=2)

        do_encryption = Button(encrypt_frame, bg="#e49400", height=2, width=10, font=i12bold, text="Encrypt", command=lambda:encrypt(filename))
        do_encryption.grid(row=0, column=3)

    def decrypt_menu():
        decrypt_frame = Frame()
        decrypt_frame.pack(side=TOP, anchor=W)

        def destroy_decrypt():
            decrypt_frame.destroy()

        back = Button(decrypt_frame, height=4, width=10, bg="#a7a7a7", font=i12 , text="Back", command=lambda:[destroy_decrypt(), main_menu()]).grid(row=0, column=0)

        spacer = Frame(decrypt_frame, width=270).grid(row=0, column=1)

        filename = StringVar()

        entry_box = Entry(decrypt_frame, font=i15, textvariable=filename)
        entry_box.grid(row=0, column=2)

        do_decryption = Button(decrypt_frame, bg="#e49400", height=2, width=10, font=i12bold, text="Decrypt", command=lambda:decrypt(filename))
        do_decryption.grid(row=0, column=3)
    
    
    text = Label(main, height=5, bg="#a7a7a7", font=i11, text="""GCryptor - An easy-to-use graphical tool for encrypting and decrypting a file.
        
Note: A file that has been encrypted by this tool can only be decrypted by this tool and files text that haven't been encrypted by this tool can't be decrypted by it.""")
    text.pack(fill=X)

    container_for_buttons = Label(main)
    container_for_buttons.pack()

    encryption_button = Button(container_for_buttons, height=5, width=55, bg="#e49400", font=i12bold ,text="Encryption", command=lambda:[destroy_main(), encrypt_menu()]).pack(side=LEFT) 
    decryption_button = Button(container_for_buttons, height=5, width=55, bg="#e49400", font=i12bold, text="Decryption", command=lambda:[destroy_main(), decrypt_menu()]).pack(side=LEFT) 

main_menu()
window.mainloop()
