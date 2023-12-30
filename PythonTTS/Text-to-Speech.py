# Import necessary libraries
from tkinter import *
from gtts import gTTS  # Import Google Text-to-Speech library
from playsound import playsound  # Import library for playing sound

# Initialize the window
root = Tk()
root.geometry('350x300')  # Set window size
root.resizable(0, 0)  # Disable window resizing
root.config(bg='ghost white')  # Set background color
root.title('DataFlair - TEXT_TO_SPEECH')  # Set window title

# Heading and label
Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='DataFlair', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

# Label for user input
Label(root, text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

# Text variable for user input
Msg = StringVar()

# Entry field for user input
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

# Function to convert text to speech
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)  # Create a gTTS object
    speech.save('DataFlair.mp3')  # Save the generated speech as an MP3 file
    playsound('DataFlair.mp3')  # Play the generated audio

# Function to exit the application
def Exit():
    root.destroy()

# Function to reset the input field
def Reset():
    Msg.set("")

# Buttons for playing, exiting, and resetting
Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset).place(x=175, y=140)

# Run the main window loop
root.mainloop()
