import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Create a canvas widget and a scrollbar
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        # Create a frame inside the canvas to hold the widgets
        self.frame = tk.Frame(self.canvas)

        # Attach the scrollbar to the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Bind the canvas to the scrollbar
        self.canvas.bind("<MouseWheel>", self.on_canvas_configure)

        # Pack the widgets
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def on_canvas_configure(self, event):
        # Update the scrollable region when the canvas size changes
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))



root = tk.Tk()

scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(side="top", fill="both", expand=True)

for i in range(100):
    label = tk.Label(scrollable_frame.frame, text=f"Label {i}")
    label.pack()

root.mainloop()