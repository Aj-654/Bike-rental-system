import tkinter as tk

class BikeDetailsFrame(tk.Frame):
    def __init__(self, parent, bike_data):
        tk.Frame.__init__(self, parent)
        self.bike_data = bike_data
        self.current_item = 0
        
        self.category_label = tk.Label(self, text="Category: " + bike_data[self.current_item][0])
        self.category_label.pack(side=tk.TOP, padx=10, pady=5)
        
        self.manufacturer_label = tk.Label(self, text="Manufacturer: " + bike_data[self.current_item][1])
        self.manufacturer_label.pack(side=tk.TOP, padx=10, pady=5)
        
        self.model_label = tk.Label(self, text="Model: " + bike_data[self.current_item][2])
        self.model_label.pack(side=tk.TOP, padx=10, pady=5)
        
        self.price_label = tk.Label(self, text="Price: $" + str(bike_data[self.current_item][3]))
        self.price_label.pack(side=tk.TOP, padx=10, pady=5)
        
    def update_details(self, item_id):
        self.current_item = item_id
        self.category_label.config(text="Category: " + self.bike_data[self.current_item][0])
        self.manufacturer_label.config(text="Manufacturer: " + self.bike_data[self.current_item][1])
        self.model_label.config(text="Model: " + self.bike_data[self.current_item][2])
        self.price_label.config(text="Price: $" + str(self.bike_data[self.current_item][3]))

class BikeShopApp(tk.Frame):
    def __init__(self, parent, bike_data):
        tk.Frame.__init__(self, parent)
        self.bike_data = bike_data
        
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bike_details_frame = BikeDetailsFrame(self.canvas, self.bike_data)
        self.bike_details_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.bike_details_frame, anchor='nw')
        
        self.bike_details_frame.bind("<Configure>", self.on_frame_configure)
        
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def prev_item(self):
        if self.bike_details_frame.current_item > 0:
            self.bike_details_frame.update_details(self.bike_details_frame.current_item - 1)
            
    def next_item(self):
        if self.bike_details_frame.current_item < len(self.bike_data) - 1:
            self.bike_details_frame.update_details(self.bike_details_frame.current_item + 1)
            
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Bike Shop App")
    bike_data = [["Road Bikes", "Specialized", "Roubaix", 2000],
                 ["Mountain Bikes", "Trek", "Fuel EX 8", 3000],
                 ["City Bikes", "Giant", "Escape 2", 500]]
    app = BikeShopApp(root, bike_data)
    app.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()