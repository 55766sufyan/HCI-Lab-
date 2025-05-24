import tkinter as tk # Import tkinter for GUI
import threading # Import threading to manage pop-ups asynchronously
import time # Import time to control delays
import random # Import random to set pop-up intervals
# Function to display a pop-up notification
def show_popup():
 popup = tk.Toplevel(root) # Create a new window
 popup.title("Notification") # Set title
 tk.Label(popup, text="New Message!").pack() # Display message
 popup.after(2000, popup.destroy) # Auto close after 2 seconds
# Function to trigger pop-ups at random intervals
def random_popups():
 while True:
 time.sleep(random.randint(3, 8)) # Wait for a random interval before showing
the next popup
 root.after(0, show_popup)
# Create the main application window
root = tk.Tk()
root.title("Attention Test")
tk.Label(root, text="Read the text carefully and ignore popups.").pack()
# Start the thread for random pop-ups
threading.Thread(target=random_popups, daemon=True).start()
root.mainloop() # Run the GUI application