import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("🌡️ Temperature Converter")
        self.root.geometry("400x300")
        self.root.configure(bg="#eef2f3")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#eef2f3")
        style.configure("TButton", font=("Helvetica", 11), padding=6)
        style.configure("TCombobox", font=("Helvetica", 11))

        ttk.Label(self.root, text="Enter Temperature:").pack(pady=10)

        self.temp_entry = ttk.Entry(self.root, font=("Helvetica", 14), justify="center")
        self.temp_entry.pack(pady=5)

        ttk.Label(self.root, text="From:").pack()
        self.from_unit = ttk.Combobox(self.root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
        self.from_unit.current(0)
        self.from_unit.pack(pady=5)

        ttk.Label(self.root, text="To:").pack()
        self.to_unit = ttk.Combobox(self.root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
        self.to_unit.current(1)
        self.to_unit.pack(pady=5)

        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=15)

        self.result_label = ttk.Label(self.root, text="", font=("Helvetica", 13, "bold"))
        self.result_label.pack(pady=10)

    def convert(self):
        try:
            temp = float(self.temp_entry.get())
            from_u = self.from_unit.get()
            to_u = self.to_unit.get()

            if from_u == to_u:
                result = f"{temp:.2f}° {to_u}"
            else:
                result = self.convert_temperature(temp, from_u, to_u)

            self.result_label.config(text=f"Result: {result}", foreground="green")

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.", foreground="red")

    def convert_temperature(self, temp, from_u, to_u):
        if from_u == "Celsius":
            if to_u == "Fahrenheit":
                return f"{(temp * 9/5) + 32:.2f}° Fahrenheit"
            elif to_u == "Kelvin":
                return f"{temp + 273.15:.2f} K"
        elif from_u == "Fahrenheit":
            if to_u == "Celsius":
                return f"{(temp - 32) * 5/9:.2f}° Celsius"
            elif to_u == "Kelvin":
                return f"{(temp - 32) * 5/9 + 273.15:.2f} K"
        elif from_u == "Kelvin":
            if to_u == "Celsius":
                return f"{temp - 273.15:.2f}° Celsius"
            elif to_u == "Fahrenheit":
                return f"{(temp - 273.15) * 9/5 + 32:.2f}° Fahrenheit"

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()
