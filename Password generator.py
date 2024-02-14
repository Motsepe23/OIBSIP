password_chars = string.ascii_lowercase
    if use_uppercase:
        password_chars += string.ascii_uppercase
    if use_numbers:
        password_chars += string.digits
    if use_symbols:
        password_chars += string.punctuation

    password = ''.join(random.choice(password_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

length_label = tk.Label(frame, text="Password length:")
length_label.grid(row=0, column=0, sticky=tk.W)
length_entry = tk.Entry(frame, width=10, font=("Arial", 14))
length_entry.grid(row=0, column=1, padx=(0, 10))

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(frame, text="Include uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, sticky=tk.W)

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(frame, text="Include numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0, sticky=tk.W)

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(frame, text="Include symbols", variable=symbols_var)
symbols_checkbox.grid(row=3, column=0, sticky=tk.W)

password_label = tk.Label(frame, text="Generated password:")
password_label.grid(row=4, column=0, sticky=tk.W)
password_entry = tk.Entry(frame, width=30, font=("Arial", 14))
password_entry.grid(row=4, column=1, padx=(0, 10))

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2, pady=(10, 0))

root.mainloop()
