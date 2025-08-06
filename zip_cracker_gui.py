import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def crack_zip(zip_file, wordlist_file, output_text):
    try:
        with zipfile.ZipFile(zip_file) as zf:
            with open(wordlist_file, 'r', encoding='utf-8') as f:
                for word in f:
                    password = word.strip().encode('utf-8')
                    try:
                        zf.extractall(pwd=password)
                        output_text.insert(tk.END, f"[+] Password Found: {password.decode()}\n")
                        return
                    except:
                        output_text.insert(tk.END, f"[-] Tried: {password.decode()}\n")
                        output_text.see(tk.END)
                        continue
            output_text.insert(tk.END, "[-] Password not found in wordlist.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_zip():
    filename = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
    zip_entry.delete(0, tk.END)
    zip_entry.insert(0, filename)

def browse_wordlist():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, filename)

def start_cracking():
    zip_file = zip_entry.get()
    wordlist_file = wordlist_entry.get()
    if not zip_file or not wordlist_file:
        messagebox.showwarning("Input Missing", "Please select both ZIP and wordlist files.")
        return
    output_text.delete(1.0, tk.END)
    crack_zip(zip_file, wordlist_file, output_text)

# GUI setup
root = tk.Tk()
root.title("ZIP Password Cracker - GUI")

tk.Label(root, text="ZIP File:").grid(row=0, column=0, sticky="e")
zip_entry = tk.Entry(root, width=50)
zip_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_zip).grid(row=0, column=2)

tk.Label(root, text="Wordlist File:").grid(row=1, column=0, sticky="e")
wordlist_entry = tk.Entry(root, width=50)
wordlist_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_wordlist).grid(row=1, column=2)

tk.Button(root, text="Start Cracking", command=start_cracking, bg="green", fg="white").grid(row=2, column=1, pady=10)

output_text = tk.Text(root, height=15, width=70)
output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
