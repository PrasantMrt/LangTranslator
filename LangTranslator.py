# Import the Translator class from the translate module
from translate import Translator

# Import all classes and functions from tkinter (GUI library)
from tkinter import *

# Initialize the main application window
window = Tk()
window.title("Language Translator")  # Set the window title
window.config(bg="pink")  # Set background color

# Add a title label to the top of the window
title_label = Label(window, text="Language Translator")
title_label.pack(pady=(10, 0), fill=X)  # Add top padding and make it stretch horizontally

# Tkinter string variables to hold selected source and destination languages
lang1 = StringVar()
lang2 = StringVar()

# List of supported languages
choices = ['English', 'Chinese', 'French', 'German', 'Nepali', 'Hindi']

# Set default selected languages
lang1.set('English')
lang2.set('Nepali')

# Create a dropdown (OptionMenu) for the source language selection
lang1_menu = OptionMenu(window, lang1, *choices)
lang1_menu.config(font=('Helvetica', 20))  # Customize font
lang1_menu.pack(side=LEFT, padx=(100, 0), pady=(0, 150))  # Position on left with padding

# Create a dropdown for the target language selection
lang2_menu = OptionMenu(window, lang2, *choices)
lang2_menu.config(font=('Helvetica', 20))
lang2_menu.pack(side=RIGHT, padx=(0, 100), pady=(0, 150))  # Position on right with padding

# Text widget for user input (text to be translated)
textbox1 = Text(window, height=8, width=30, font=('verdana', 10))
# Place it relative to the lang1_menu widget (below the dropdown)
textbox1.place(in_=lang1_menu, relx=0, x=-60, rely=1.5)

# Text widget for displaying the translated result
textbox2 = Text(window, height=8, width=30, font=('verdana', 10))
# Place it relative to the lang2_menu widget
textbox2.place(in_=lang2_menu, relx=0, x=-60, rely=1.5)

# Define the function that handles translation when the button is clicked
def translate():
    textbox2.delete("1.0", "end")  # Clear previous translation from output box
    var1 = textbox1.get("1.0", "end-1c")  # Get all text from the first box, excluding the final newline
    # Initialize Translator object with selected languages
    translator = Translator(from_lang=lang1.get(), to_lang=lang2.get())
    # Perform translation and store result
    translation = translator.translate(str(var1))
    textbox2.insert(END, translation)  # Insert the translated text into the output box

# Button to trigger the translate() function
translete_btn = Button(
    window,
    text="Translate",
    width=10,
    font=('Agency Fb', 20),
    command=translate  # Assign function to button's command
)
# Place button at the bottom with padding
translete_btn.pack(pady=(10, 0), side=BOTTOM)

# Run the main Tkinter event loop (keeps the window active)
window.mainloop()
