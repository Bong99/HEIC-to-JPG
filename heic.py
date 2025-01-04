import os
import sys
from PIL import Image
from pillow_heif import register_heif_opener
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import tkinterDnD  # Importing the tkinterDnD module


register_heif_opener()
a = 0 

# Convert the heic file into jpg
def convert_to_jpg(input_file, output_file):
    try:
        img = Image.open(input_file)
        img = img.convert("RGB")
        img.save(output_file, "JPEG", quality=95)
        #print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

# Remove all items in the listbox and reset the progress bar
def clearList():
    listbox.delete(0, listbox.size())
    a = 0
    bar['value'] = a

# Handle the files in listbox 1 by 1, and update the progress bar
def convertnow():
    global a # precentage value for progress bar
    current_index = 1
    get_content = listbox.get(0, listbox.size()) # get a tuple from listbox

    # Handle the items in listnox 1 by 1
    for input_file in get_content:
        #print(input_file)
        output_file = os.path.splitext(input_file)[0] + ".jpg"
        
        a = current_index/listbox.size() * 100
        
        bar['value'] = a
        root.update()
        current_index = current_index+1
        
        convert_to_jpg(input_file, output_file)

        messagebox.showinfo("Convert Completed", "Convert Completed") 




# You have to use the tkinterDnD.Tk object for super easy initialization,
# and to be able to use the main window as a dnd widget
root = tkinterDnD.Tk()
root.title("HEIC to JPG converter")

stringvar = tk.StringVar()
stringvar.set('Drag file (HEIC file only, not support folder) to here to convert +')


def drop(event):
    # This function is called, when stuff is dropped into a widget
#    stringvar.set(event.data)
    #print("DROP!")
    #print(event.data)
    
    if event.data[0] == '{':
        #print('has Space')
        x = event.data.split("} {")
        for item in x:
            item = item.replace('{', '')
            item = item.replace('}', '')
            file_ext = os.path.splitext(item.lower())[1]
            if file_ext == '.heic':
                listbox.insert(0, item)
    else:
        #print("No Space")
        x = event.data.split()
        for item in x:
            file_ext = os.path.splitext(item.lower())[1]
            if file_ext == '.heic':
                listbox.insert(0, item)


def drag_command(event):
    # This function is called at the start of the drag,
    # it returns the drag type, the content type, and the actual content
    print("DRAG!")
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")



about_label_text = ('HEIC to JPG converter v1.0\nAuthor: Paul Chow\n'
    'Email: bong99@gmail.com\n'
    'License: MIT License\n\n'
    'Github: https://github.com/Bong99/HEIC-to-JPG'    
    )


def about():
    messagebox.showinfo("About", about_label_text) 

# UI Layout section start

# With DnD hook you just pass the command to the proper argument,
# and tkinterDnD will take care of the rest
# NOTE: You need a ttk widget to use these arguments



    'Drag the HEIC files to below area, then press "Convert" button to start convert.\n'
    'The converted file will be saved in the same folder'

label_about = tk.Label(root, text='\nDrag the HEIC files to below area, then press "Convert" button to start convert.\nThe converted file will be saved in the same folder')
label_about.pack()   

label_2 = ttk.Label(root, ondrop=drop, ondragstart=drag_command, textvar=stringvar, padding=50, relief="solid")
label_2.pack(fill="both", expand=True, padx=10, pady=10)

listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

button1 = tk.Button(text = "Convert", command = convertnow)
button1.pack(padx = 3, pady = 3)

button2 = tk.Button(text = "Clear", command = clearList)
button2.pack(padx = 3, pady = 3)

bar = ttk.Progressbar(root)
bar.pack(pady=20)

button_about = tk.Button(text = "About...", command = about)
button_about.pack(padx = 3, pady = 3)

root.mainloop()