import tkinter as tk

def add_numbers():
  """Adds the numbers entered by the user."""
  numbers = []
  for entry in entries:
    numbers.append(int(entry.get()))
  total = sum(numbers)
  label.config(text=f"The sum is {total}")

def multiply_numbers():
  """Multiplies the numbers entered by the user."""
  numbers = []
  for entry in entries:
    numbers.append(int(entry.get()))
  product = 1
  for number in numbers:
    product *= number
  label.config(text=f"The product is {product}")

def quit():
  """Closes the GUI."""
  window.destroy()

window = tk.Tk()
window.title("Passwords Generator")
window.geometry("300x300")

entries = []
for i in range(3):
  label = tk.Label(window, text= f"Number {i + 1}")
  label.pack(side = "left")
  entry = tk.Entry(window)
  entry.pack(side = "left")
  label = tk.Label(window)
  label.pack()
  entries.append(entry)

label = tk.Label(window)
label.pack()


button_add = tk.Button(window, text="Add", command=add_numbers)
button_add.pack()

button_multiply = tk.Button(window, text="Multiply", command=multiply_numbers)
button_multiply.pack()

button_quit = tk.Button(window, text="Quit", command=quit)
button_quit.pack()

window.mainloop()
