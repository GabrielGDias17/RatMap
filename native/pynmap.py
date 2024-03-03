import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
from datetime import datetime

# Define a dictionary of Nmap options and their descriptions
nmap_options = {
    "-A": "Aggressive scan options",
    "-p": "Port specification (e.g., 22,23,25-30)",
    "-T": "Timing template (0-5)",
    "-n": "Never do DNS resolution",
    "-Pn": "Treat all hosts as online",
    "-sS": "TCP SYN scan",
    "-sU": "UDP scan",
    "-O": "Enable OS detection",
    "-sV": "Service version detection"
    # Add more options here as needed
}

def run_nmap_scan():
    ip_address = ip_entry.get()
    if not ip_address:
        messagebox.showerror("Error", "Please enter an IP address")
        return
    
    options = []
    for option, var in option_vars.items():
        if var.get():
            options.append(option)
    
    custom_options = custom_options_entry.get()
    if custom_options:
        options.extend(custom_options.split())
    
    if verbose_var.get():
        options.append("-v")
    
    try:
        command = ['nmap'] + options + [ip_address]
        result = subprocess.run(command, capture_output=True, text=True)
        scan_result = result.stdout
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, scan_result)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_results():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"nmap_scan_results_{timestamp}.txt"
    with open(filename, 'w') as file:
        file.write(result_text.get(1.0, tk.END))
    messagebox.showinfo("Success", f"Scan results saved to {filename}")

# Create the main window
root = tk.Tk()
root.title("Ratmap")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to match the screen dimensions
root.geometry(f"{screen_width}x{screen_height}")

# Load background image
background_image = Image.open("rat3.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a Label widget to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create IP Address entry
ip_label = tk.Label(root, text="Enter IP Address:")
ip_label.pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

# Checkboxes for Nmap options
option_vars = {}
for option, description in nmap_options.items():
    var = tk.BooleanVar()
    option_vars[option] = var
    checkbox = tk.Checkbutton(root, text=f"{option} - {description}", variable=var)
    checkbox.pack(anchor=tk.W)

# Entry for custom Nmap options
custom_options_label = tk.Label(root, text="Custom Nmap Options:")
custom_options_label.pack()
custom_options_entry = tk.Entry(root)
custom_options_entry.pack()

# Checkbox for verbose output
verbose_var = tk.BooleanVar()
verbose_checkbox = tk.Checkbutton(root, text="Verbose Output (-v)", variable=verbose_var)
verbose_checkbox.pack(anchor=tk.W)

# Create buttons
run_button = tk.Button(root, text="Run Scan", command=run_nmap_scan)
run_button.pack(pady=10)
save_button = tk.Button(root, text="Save Results", command=save_results)
save_button.pack(pady=5)

# Create text area to display results
result_text = tk.Text(root, height=10, width=60)
result_text.pack(pady=10)

# Add instructions text box
instructions_text = """Welcome to The RatNmap This uses a Nmap Libary From Python To Use It follow the
Instructions:
1. Enter the IP address in the 'Enter IP Address' field.
2. Rat Run Without Any Options Let it Finish
3. Once Finish Rat Run With Any Of the Options you want(Let Finish Might take A While)
4. You may save it if you desire
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣏⡦⠤⣤⠽⠤⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⠣⢈⠇⠀⠁⣠⡿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠉⠀⠀⠀⠀⠀⢀⡀⠈⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⡀⠀⡰⣯⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⡹⠂⢽⠎⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⠠⠄⠃⣴⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠈⠧⣢⠌⣁⠐⠋⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀By : Gabriel, Dias"""
instructions_label = tk.Label(root, text=instructions_text, bg="white", fg="black", font=("Helvetica", 12))
instructions_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()
