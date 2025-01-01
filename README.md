This is a program with GUI, to convert HEIC ((High-Efficiency Image Format) image into JPG.

I tried to search around to see is there any app on PC which can convert the HEIC to JPG since my wife fail to open the photo on her Win 11 laptop. And I unable to find a free app to handle it. In the meantime, I found the code from michaelpig0912 (https://github.com/michaelpig0912/heic2jpg/releases) to use a python script to convert the code. Since my wife is not familiar with python so I made a GUI base on the code.

You can drag and drop the HECI files from File Explorer then convert the files into JPG. It allows you to drag multiple files and convert in single click.

This program does use python with library pillow_heif for image conversion, then use tkinter as UI part. It also usetkinterDnD for the drag and drop function.

It references the code from https://github.com/michaelpig0912/heic2jpg/releases.