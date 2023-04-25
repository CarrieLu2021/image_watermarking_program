from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw
import os

# Define constants
FONT = "Courier"
FONT_PATH = "COURIER.ttf"
file_path = None


# ------------------------------------FUNCTIONS--------------------------------------------------------


def upload_image():
    """Open a file dialog to allow the user to select an image file and display the file name."""
    global file_path
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            label_file.config(text=file_name)
        else:
            label_file.config(text="No file selected.")
    except Exception as exception_text:
        label_file.config(text=f"Error: {exception_text}")


def add_watermark():
    """Add a watermark to the selected image file, save it to a new file, show the saved file, and display its saved path."""
    global file_path
    try:
        if not file_path:
            raise ValueError("No image file selected.")
        txt = watermark_text.get()
        with Image.open(file_path) as im:
            # Load the specified font and create a draw object for the image.
            fnt = ImageFont.truetype(FONT_PATH, 250)
            draw = ImageDraw.Draw(im)
            # Calculate the x and y coordinates for the watermark text to be centered and draw it.
            x = (im.width - draw.textlength(txt, font=fnt)) / 2
            y = (im.height - draw.textbbox(xy=(100, 100), text=txt, font=fnt)[1]) / 2
            draw.text((x, y), txt, font=fnt, fill=(255, 255, 255, 64))
            # Save the watermarked image to a new file with a modified file name.
            save_dir = os.path.dirname(file_path)
            save_path = os.path.join(save_dir, f"watermarked_{os.path.basename(file_path)}")
            im.save(save_path)
            # Show the saved file and its path.
            label_saved.config(text=f"Your watermarked image is saved to:\n{file_path}")
            im.show()
    except Exception as exception_text:
        label_saved.config(text=f"Error: {exception_text}")


# ----------------------------------- UI SETUP -------------------------------------------------------

root = Tk()
root.title("Image Watermarking App")
root.config(padx=100, pady=100, bg="grey")

button_upload = Button(text="Upload Image", font=(FONT, 50, "bold"), bg="white", fg="grey", command=upload_image)
button_upload.grid(column=0, row=0, columnspan=2, pady=10)

label_file = Label(text="Choose an image file.", font=(FONT, 25), bg="grey", fg="black")
label_file.grid(column=0, row=1, columnspan=2)

label_text = Label(text="Type your watermark text: ", font=(FONT, 30, "bold"), bg="grey", fg="white", pady=40)
label_text.grid(column=0, row=2)

watermark_text = Entry()
watermark_text.insert(0, "©")
watermark_text.focus()
watermark_text.icursor(0)
watermark_text.grid(column=1, row=2)

button_download = Button(text="Download Watermarked Image", font=(FONT, 40, "bold"), bg="white", fg="grey",
                         command=add_watermark)
button_download.grid(column=0, row=3, columnspan=2, pady=80)

label_saved = Label(text="", font=(FONT, 25), bg="grey", fg="black")
label_saved.grid(column=0, row=4, columnspan=2)

root.mainloop()
