import pygame
import tkinter as tk
from tkinter import messagebox
import time
from tkinter import font as tkFont

# Initialize Pygame for music playback
pygame.mixer.init()

# # Function to play background music
def play_music():
    pygame.mixer.music.load("C:/Users/angel/OneDrive/Documents/Mascarillas/passenger-let-her-go-instrumental-made-with-Voicemod.mpeg")  # Replace with your music file
    pygame.mixer.music.play(-1)  # Play the music on loopsi

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Poem to display
poem = """
Alicia Mascarillas, investigadora UDC,
tu ciencia es tan grande como un plato de té. 
Eres mi flor de loto, un alma tan bella,
aunque a veces rimo contigo ¡abichuelas!

Con tus gafas brillantes y tu bata especial,
resuelves misterios como un genio total.
Pero cuando trabajas y haces maravillas,
te llaman la reina de las mascarillas.

Sigues en tus viajes por mares y cielos,
buscando respuestas (y buenos caramelos).
Alicia Mascarillas, qué suerte la mía,
tenerte en este poema de pura alegría.
"""

# Create a GUI window using Tkinter
def display_poem():
    # Create the root window
    root = tk.Tk()
    root.title("Oda a Alicia Mascarillas")
    root.geometry("1200x600")

    # Set the background color of the root window
    root.config(bg="lightblue")  # Change "lightblue" to your preferred color

    # Load a posh font (e.g., Times New Roman, or a custom one)
    posh_font = tkFont.Font(family="Georgia", size=18, weight="bold")  # You can replace with other font families


    # Create a label to display the poem with a background color
    text_label = tk.Label(
        root, 
        text=poem, 
        font=posh_font,
        justify="center", 
        wraplength=800, 
        bg="white",  # Set background color for the text label
        fg="black"   # Set text color
    )
    text_label.pack(pady=50, padx=20)


    # Add a quit button to stop the music and close the program
    quit_button = tk.Button(root, text="Quit", command=lambda: (stop_music(), root.destroy()))
    quit_button.pack(pady=10)

    # Play the music
    play_music()

    # Run the Tkinter event loop
    root.mainloop()

time.sleep(1)
print("Hola pipita, me alegro de verte por aquí.")
time.sleep(2)
print("Por favor, sube el volumen antes de responder la pregunta más importante del día:")
time.sleep(2)

password = input("Quieres queso?")

# Run the display function
while password.upper() != "SI":
    password = input("Respuesta incorrecta. Te he dicho que si QUIERES QUESO!?")

print("Contraseña correcta")
time.sleep(1)
display_poem()
