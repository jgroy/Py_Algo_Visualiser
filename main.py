import tkinter as tk
from tkinter import ttk
import random
import time
from algorithms import bubble_sort

root = tk.Tk()
root.title('Python Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='black')

data = []

canvas = tk.Canvas(root, width=800, height=400, bg='white')
canvas.grid(row=0, column=0, padx=10, pady=5, columnspan=5)

def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 400
    c_width = 800
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    root.update_idletasks()

def generate():
    global data
    data = [random.randint(1, 100) for _ in range(50)]
    draw_data(data, ['red' for _ in range(len(data))])

def start_sorting():
    bubble_sort(data, draw_data, 0.05)

tk.Button(root, text="Generate", command=generate, bg='blue', fg='white').grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="Start Bubble Sort", command=start_sorting, bg='green', fg='white').grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
