import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

# Create the Tkinter window
window = Tk()
window.title("YouTube Installer")
window.geometry("600x400")

# Create the dark and light mode colors
dark_mode_color = "#222831"
light_mode_color = "#f2f2f2"

# Set the default mode to light
current_mode = light_mode_color

# Create the function to toggle between dark and light mode
def toggle_mode():
    global current_mode
    if current_mode == dark_mode_color:
        current_mode = light_mode_color
        mode_button.config(text="Dark Mode")
    else:
        current_mode = dark_mode_color
        mode_button.config(text="Light Mode")
    window.config(bg=current_mode)

# Create the function to choose the file to save the video
def choose_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4")
    if file_path:
        file_name = os.path.basename(file_path)
        return file_path, file_name
    else:
        return None, None

# Create the function to download the YouTube video
def download_video():
    # Get the YouTube video URL from the user
    url = url_input.get()

    # Validate the URL
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube video URL.")
        return

    # Get the file path and name
    file_path, file_name = choose_file()

    # Validate the file path
    if not file_path:
        return

    # Get the selected format
    format = format_choice.get()

    # Download the YouTube video
    try:
        video = YouTube(url)
        if format == "mp4":
            video.streams.filter(progressive=True, file_extension="mp4").first().download(output_path=file_path, filename=file_name)
        elif format == "mp3":
            video.streams.filter(only_audio=True).first().download(output_path=file_path, filename=file_name)
        messagebox.showinfo("Success", "YouTube video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading the YouTube video: {str(e)}")

# Create the URL label and input box
url_label = Label(window, text="Enter the YouTube video URL:")
url_label.pack()
url_input = Entry(window)
url_input.pack()

# Create the format label and radio buttons
format_label = Label(window, text="Select the format to download:")
format_label.pack()
format_choice = StringVar()
format_choice.set("mp4")
mp4_radio = Radiobutton(window, text=".mp4", variable=format_choice, value="mp4")
mp4_radio.pack()
mp3_radio = Radiobutton(window, text=".mp3", variable=format_choice, value="mp3")
mp3_radio.pack()

# Create the download and choose file buttons
button_frame = Frame(window, bg=current_mode)
button_frame.pack(pady=10)
download_button = Button(button_frame, text="Download Video", font=("Helvetica", 12), bg="#00adb5", fg="white", command=download_video)
download_button.pack(side=LEFT, padx=10)
choose_file_button = Button(button_frame, text="Choose File", font=("Helvetica", 12), bg="#00adb5", fg="white", command=choose_file)
choose_file_button.pack(side=LEFT, padx=10)

# light mode toggle button
mode_button = Button(window, text="Dark Mode", bg="#00adb5", fg="white", font=("Helvetica", 12), command=toggle_mode)
mode_button.pack(pady=10)

# Set the window background color
window.config(bg=current_mode)

# Run the Tkinter event loop
window.mainloop()