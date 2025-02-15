import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import random

def recommend_fertilizer():
    crop_type = crop_type_entry.get()
    npk_n = float(npk_n_entry.get())
    npk_p = float(npk_p_entry.get())
    npk_k = float(npk_k_entry.get())
    ph_min = float(ph_min_entry.get())
    ph_max = float(ph_max_entry.get())
    rainfall = float(rainfall_entry.get())

    if crop_type.lower() == 'wheat':
        fertilizer = 'Urea, DAP'
    elif crop_type.lower() == 'rice':
        fertilizer = 'NPK Fertilizer, Urea'
    elif crop_type.lower() == 'corn':
        fertilizer = 'NPK Fertilizer, Potassium Sulfate'
    elif crop_type.lower() == 'soybean':
        fertilizer = 'DAP, MOP'
    else:
        fertilizer = 'Fertilizer recommendation not available for this crop.'

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Fertilizer Recommendation for {crop_type.capitalize()}:\n{fertilizer}\n\n")
    result_text.insert(tk.END, f"Additional Info:\n\n")
    result_text.insert(tk.END, f"NPK Nutrients: N={npk_n} P={npk_p} K={npk_k}\n")
    result_text.insert(tk.END, f"pH Range: {ph_min} - {ph_max}\n")
    result_text.insert(tk.END, f"Rainfall: {rainfall} mm/year\n")

def generate_random_inputs():
    crops = ['Rice', 'Wheat', 'Corn', 'Soybean']
    crop_type = random.choice(crops)
    npk_n = random.randint(50, 150)
    npk_p = random.randint(30, 80)
    npk_k = random.randint(40, 100)
    ph_min = round(random.uniform(5.5, 7.5), 2)
    ph_max = round(random.uniform(5.5, 7.5), 2)
    rainfall = random.randint(600, 1600)

    crop_type_entry.delete(0, tk.END)
    crop_type_entry.insert(tk.END, crop_type)
    npk_n_entry.delete(0, tk.END)
    npk_n_entry.insert(tk.END, npk_n)
    npk_p_entry.delete(0, tk.END)
    npk_p_entry.insert(tk.END, npk_p)
    npk_k_entry.delete(0, tk.END)
    npk_k_entry.insert(tk.END, npk_k)
    ph_min_entry.delete(0, tk.END)
    ph_min_entry.insert(tk.END, ph_min)
    ph_max_entry.delete(0, tk.END)
    ph_max_entry.insert(tk.END, ph_max)
    rainfall_entry.delete(0, tk.END)
    rainfall_entry.insert(tk.END, rainfall)

root = ThemedTk(theme="breeze")
root.title("Sustainable Fertilizer Usage Optimizer")
root.geometry("900x600")

try:
    root.iconbitmap("app_icon.ico")
except:
    pass

title_label = ttk.Label(root, text="Fertilizer Usage Optimizer", font=("Arial", 20, "bold"), foreground="#4C4CFF")
title_label.pack(pady=20)

main_frame = ttk.Frame(root)
main_frame.pack(pady=20, padx=20, fill=tk.BOTH)

left_frame = ttk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, padx=20, fill=tk.Y)

right_frame = ttk.Frame(main_frame)
right_frame.pack(side=tk.LEFT, padx=20, fill=tk.Y)

crop_type_label = ttk.Label(left_frame, text="Crop Type:", font=("Arial", 14, "bold"))
crop_type_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")
crop_type_entry = ttk.Entry(left_frame, font=("Arial", 12))
crop_type_entry.grid(row=0, column=1, padx=15, pady=10, sticky="w")

npk_n_label = ttk.Label(left_frame, text="NPK N (kg/ha):", font=("Arial", 14, "bold"))
npk_n_label.grid(row=1, column=0, padx=15, pady=10, sticky="w")
npk_n_entry = ttk.Entry(left_frame, font=("Arial", 12))
npk_n_entry.grid(row=1, column=1, padx=15, pady=10)

npk_p_label = ttk.Label(left_frame, text="NPK P (kg/ha):", font=("Arial", 14, "bold"))
npk_p_label.grid(row=2, column=0, padx=15, pady=10, sticky="w")
npk_p_entry = ttk.Entry(left_frame, font=("Arial", 12))
npk_p_entry.grid(row=2, column=1, padx=15, pady=10)

npk_k_label = ttk.Label(left_frame, text="NPK K (kg/ha):", font=("Arial", 14, "bold"))
npk_k_label.grid(row=3, column=0, padx=15, pady=10, sticky="w")
npk_k_entry = ttk.Entry(left_frame, font=("Arial", 12))
npk_k_entry.grid(row=3, column=1, padx=15, pady=10)

ph_min_label = ttk.Label(left_frame, text="pH Min:", font=("Arial", 14, "bold"))
ph_min_label.grid(row=4, column=0, padx=15, pady=10, sticky="w")
ph_min_entry = ttk.Entry(left_frame, font=("Arial", 12))
ph_min_entry.grid(row=4, column=1, padx=15, pady=10)

ph_max_label = ttk.Label(left_frame, text="pH Max:", font=("Arial", 14, "bold"))
ph_max_label.grid(row=5, column=0, padx=15, pady=10, sticky="w")
ph_max_entry = ttk.Entry(left_frame, font=("Arial", 12))
ph_max_entry.grid(row=5, column=1, padx=15, pady=10)

rainfall_label = ttk.Label(left_frame, text="Ideal Rainfall (mm/year):", font=("Arial", 14, "bold"))
rainfall_label.grid(row=6, column=0, padx=15, pady=10, sticky="w")
rainfall_entry = ttk.Entry(left_frame, font=("Arial", 12))
rainfall_entry.grid(row=6, column=1, padx=15, pady=10)

button_frame = ttk.Frame(left_frame)
button_frame.grid(row=7, column=0, columnspan=2, pady=20)

recommend_button = ttk.Button(button_frame, text="Get Fertilizer Recommendation", width=25, command=recommend_fertilizer)
recommend_button.grid(row=0, column=0, padx=20, pady=10, ipadx=10, ipady=5)

random_button = ttk.Button(button_frame, text="Generate Random Inputs", width=25, command=generate_random_inputs)
random_button.grid(row=0, column=1, padx=20, pady=10, ipadx=10, ipady=5)

result_text = tk.Text(right_frame, width=50, height=15, font=("Arial", 12), bg="#F7F7F7", wrap=tk.WORD, bd=0, relief="flat")
result_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

result_text.configure(highlightbackground="#d3d3d3", highlightthickness=2, relief="solid", bd=3)

root.mainloop()
