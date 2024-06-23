import tkinter as tk
from tkinter import messagebox
import pyshorteners as ps

shorten = ps.Shortener()

#function to shorten the url
def shorten_url():
    long_url = entry.get()
    if not long_url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    
    try:
        short_url = shorten.tinyurl.short(long_url)
        
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, short_url)
        result_entry.config(state='readonly') # allows it to be copied too
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")

root = tk.Tk()
root.title("URL Shortener")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)
#creating input field for long url
entry_label = tk.Label(frame, text="Enter the long URL:")
entry_label.pack(anchor='w')

entry = tk.Entry(frame, width=60)
entry.pack(fill='x')

#creating button
shortener_button = tk.Button(frame, text="Shorten URL", command=shorten_url)
shortener_button.pack(pady=5)

#to display short url
result_entry_label = tk.Label(frame, text="Shortened URL:")
result_entry_label.pack(anchor='w')
result_entry = tk.Entry(frame, width=50, state='readonly')
result_entry.pack(fill='x')

root.mainloop()
