# image_watermarking_program
This is an image watermarking app that allows users to upload an image, add a custom watermark to it, and save the watermarked image. 

The app is built with Python and the Tkinter library for the user interface, and the PIL (Python Imaging Library) library for image manipulation.

The user interface consists of a "Upload Image" button, which opens a file dialog for the user to select an image file. Once the file is selected, the app displays the name of the file on a label. The user can then enter a watermark text on an entry field, with a default text of "©".

When the user clicks the "Download Watermarked Image" button, the app adds the watermark text to the center of the selected image using a custom font, and saves the resulting watermarked image to the same directory as the original file. The app displays a message indicating the path of the saved watermarked image.

The app includes error handling to check if a file is selected and if there are any errors during the image processing and saving.
