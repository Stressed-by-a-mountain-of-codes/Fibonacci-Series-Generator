import tkinter as tk
from tkinter import ttk
import math

class FibonacciApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fibonacci Series Generator")
        self.master.geometry("500x500")

        tk.Label(master, text="Fibonacci Series Generator", font=("Arial", 16, "bold")).pack(pady=10)

        # Radio buttons for mode selection
        self.mode = tk.StringVar(value="terms")
        mode_frame = tk.Frame(master)
        mode_frame.pack()
        tk.Radiobutton(mode_frame, text="By Number of Terms", variable=self.mode, value="terms").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(mode_frame, text="By Maximum Value", variable=self.mode, value="max").pack(side=tk.LEFT, padx=10)

        # Input
        tk.Label(master, text="Enter value:", font=("Arial", 12)).pack(pady=5)
        self.input_entry = tk.Entry(master, font=("Arial", 12), width=25)
        self.input_entry.pack()
        self.input_entry.insert(0, "10")

        # Button
        tk.Button(master, text="Generate Fibonacci Series", font=("Arial", 12), command=self.generate_fibonacci).pack(pady=10)

        # Output text area with scrollbar
        self.result_text = tk.Text(master, height=14, width=60, font=("Arial", 11), wrap=tk.WORD)
        self.result_text.pack(pady=10)

        scroll = ttk.Scrollbar(master, command=self.result_text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text['yscrollcommand'] = scroll.set

        # Tooltip / Golden ratio explanation
        explanation = (
            "📘 Why Fibonacci ratios approach φ:\n"
            "As the Fibonacci sequence progresses, the ratio of each pair of consecutive terms "
            "approaches the Golden Ratio φ ≈ 1.618...\n"
            "This happens because:\n"
            "   φ = (1 + √5) / 2 ≈ 1.6180339887\n"
            "And the ratio Fn+1 / Fn stabilizes due to the recursive structure: Fn+1 = Fn + Fn-1.\n"
            "This is a natural consequence of linear recurrence relations."
        )

        self.tooltip = tk.Label(master, text=explanation, font=("Arial", 9), justify="left", wraplength=460, fg="gray20")
        self.tooltip.pack(pady=5)

    def generate_fibonacci(self):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)

        try:
            limit = int(self.input_entry.get())
            if limit <= 0:
                self.result_text.insert(tk.END, "Please enter a number greater than 0.")
                return

            series = []
            a, b = 0, 1

            if self.mode.get() == "terms":
                for _ in range(limit):
                    series.append(a)
                    a, b = b, a + b
            else:
                while a <= limit:
                    series.append(a)
                    a, b = b, a + b

            result = "🔢 Fibonacci Series:\n" + ", ".join(str(num) for num in series)

            # Golden Ratio approximation
            if len(series) >= 2 and series[-2] != 0:
                golden_ratio = series[-1] / series[-2]
                actual_phi = (1 + math.sqrt(5)) / 2
                result += f"\n\n📐 Golden Ratio Approximation: {golden_ratio:.10f}"
                result += f"\n🔢 Actual φ = (1 + √5)/2 ≈ {actual_phi:.10f}"
                result += f"\n📉 Difference: {abs(golden_ratio - actual_phi):.10f}"
            else:
                result += "\n\nNot enough terms to compute Golden Ratio."

            self.result_text.insert(tk.END, result)

        except ValueError:
            self.result_text.insert(tk.END, "Please enter a valid positive integer.")

        self.result_text.config(state=tk.DISABLED)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()
