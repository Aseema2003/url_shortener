import tkinter as tk
import pyshorteners


def shorten_url():
    long_url = entry.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(long_url)
    entry.delete(0, tk.END)
    entry.insert(0, shortened_url)


# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# Set background color
root.configure(background='#e0b938')
root.geometry("500x200+500+200")
# Set font style
font_style = ('Helvetica', 14)

# Create and pack widgets
label = tk.Label(root, text="Enter Long URL:", font=font_style, background='#e0b938')
label.pack(pady=10)

entry = tk.Entry(root, font=font_style, width=40)
entry.pack(pady=10)

shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url, font=font_style, background='#4CAF50',
                           fg='white')
shorten_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()