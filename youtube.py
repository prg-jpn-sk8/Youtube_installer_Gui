import tkinter as tk
from pytube import YouTube
from tkinter import messagebox

def download_video():
    # Get the URL from the text entry field
    url = url_entry.get()

    # Create a YouTube object
    yt = YouTube(url)

    # Select the highest resolution available
    stream = yt.streams.get_highest_resolution()

    # Download the video to the current directory
    stream.download()

    # Show a message box to confirm that the download is complete
    tk.messagebox.showinfo("Download Complete", "The video has been downloaded successfully!")

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Create a label
label = tk.Label(root, text="Enter the URL of the YouTube video you want to download:")
label.pack()

# Create a text entry field
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create a download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()
messagebox.showinfo("Download Complete", "The video has been downloaded successfully!")


root.mainloop()