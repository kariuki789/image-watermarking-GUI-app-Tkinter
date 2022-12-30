# image-watermarking-GUI-app-Tkinter
an application using tkinter that allows users to upload images and add watermarks
This code creates a graphical user interface (GUI) using the Tkinter library in Python. The GUI has a button that, when clicked, allows the user to choose an image file using a file dialog. When the user selects an image, the code opens the image file using the Pillow library, modifies the image by adding a watermark, and saves the modified image to a new file.

The watermark text is entered by the user in a text box, and is applied to the image when the user clicks the "Apply Watermark" button. The watermark text is added to the image using the ImageDraw module from the Pillow library. The font size of the watermark text is set to 40 using the ImageFont module, and the watermark text is drawn on the image at the coordinates (10, 10).

Finally, the modified image is saved to a new file called "watermarked.jpg", and a notification is displayed to the user using the messagebox module from Tkinter. The Tkinter event loop is then run, allowing the GUI to remain active and responsive to user input.
