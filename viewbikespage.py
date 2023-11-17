import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the bike data into a pandas DataFrame
bike_data = pd.read_csv('bike_data.csv')

# Create a tkinter window
window = tk.Tk()
window.title('Bike List')

# Create a label and search box for filtering bikes
search_label = tk.Label(window, text='Search Bikes:')
search_label.pack(side=tk.LEFT, padx=10)
search_box = tk.Entry(window)
search_box.pack(side=tk.LEFT)

# Create a combobox for sorting the bike list by availability
sort_label = tk.Label(window, text='Sort Bikes:')
sort_label.pack(side=tk.LEFT, padx=10)
sort_box = ttk.Combobox(window, values=['Available', 'Unavailable'])
sort_box.pack(side=tk.LEFT)

# Create a frame to hold the bike buttons
bike_frame = tk.Frame(window)
bike_frame.pack(side=tk.TOP, padx=10, pady=10)

# Create a function to display bike details when a bike button is clicked
def display_bike_details(bike_id):
    bike_details = bike_data.loc[bike_data['ID'] == bike_id]
    details_window = tk.Toplevel(window)
    details_window.title(bike_details['model'].values[0])
    details_label = tk.Label(details_window, text=f"model: {bike_details['model'].values[0]}\nPrice: {bike_details['Price'].values[0]}\nAvailability: {bike_details['Availability'].values[0]}")
    details_label.pack()

# Create a function to generate bike buttons based on the current search and sort criteria
def generate_bike_buttons():
    # Clear any existing bike buttons
    for child in bike_frame.winfo_children():
        child.destroy()
    
    # Get the current search and sort criteria
    search_text = search_box.get().lower()
    sort_text = sort_box.get()
    
    # Filter and sort the bike data based on the search and sort criteria
    filtered_data = bike_data[bike_data['model'].str.lower().str.contains(search_text)]
    if sort_text == 'Available':
        filtered_data = filtered_data[filtered_data['Availability'] == 'Available']
    elif sort_text == 'Unavailable':
        filtered_data = filtered_data[filtered_data['Availability'] == 'Unavailable']
    filtered_data = filtered_data.sort_values(by=['Availability'], ascending=False)
    
    # Create a button for each bike in the filtered data
    for index, row in filtered_data.iterrows():
        bike_button = tk.Button(bike_frame, text=row['model'], command=lambda bike_id=row['ID']: display_bike_details(bike_id))
        bike_button.pack(side=tk.TOP, pady=5)

# Call the generate_bike_buttons() function to create the initial bike list
generate_bike_buttons()

# Create a button to update the bike list based on the search and sort criteria
update_button = tk.Button(window, text='Update Bikes', command=generate_bike_buttons)
update_button.pack(side=tk.BOTTOM, pady=10)

# Run the tkinter main loop
window.mainloop()
