import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

def choose_image():
  # Open a file dialog to let the user select an image file
  file_path = filedialog.askopenfilename()
  
  # Open the image file using Pillow
  image = Image.open(file_path)
  
  # Save the modified image to a new file
  image.save("image.jpg")
  # Display a notification to the user
  messagebox.showinfo("Image Added", "The image has been added successfully!")


def apply_watermark():
  # Get the watermark text from the text box
  watermark_text = text_box.get("1.0", "end")
  
  # Open the image file using Pillow
  image = Image.open("image.jpg")
  
  # Add the watermark to the image
  draw = ImageDraw.Draw(image)
  
  # Use a larger font size to make the watermark text bigger
  font = ImageFont.truetype("arial.ttf", size=40)
  draw.text((10, 10), watermark_text, fill=(0, 0, 0), font=font)
  
  # Save the modified image to a new file
  image.save("watermarked.jpg")
  # Get the watermark text from the text box
  watermark_text = text_box.get("1.0", "end")
  
  # Open the image file using Pillow
  image = Image.open("image.jpg")
  
  # Add the watermark to the image
  draw = ImageDraw.Draw(image)
  draw.text((10, 10), watermark_text, fill=(0, 0, 0))  # Set the fill color to black
  
  # Save the modified image to a new file
  image.save("watermarked.jpg")
  
  # Display a notification to the user
  messagebox.showinfo("Watermark Applied", "The watermark has been applied successfully!")


# Create the Tkinter window
window = tk.Tk()
window.title("Watermarker")

# Set the size of the window
window.geometry("600x400")

# Add a label to the window
label = tk.Label(window, text="Welcome! Please choose an image to watermark:")
label.pack()

# Add a button to the window
button = tk.Button(window, text="Choose Image", command=choose_image)
button.pack()

# Add a label to the window
label = tk.Label(window, text="Please enter the watermark text:")
label.pack()

# Add a text box to the window
text_box = tk.Text(window, height=2, width=30)
text_box.pack()

# Add a button to the window
button = tk.Button(window, text="Apply Watermark", command=apply_watermark)
button.pack()

# Run the Tkinter event loop
window.mainloop()
