import pyfiglet
import shutil

def printf(text):
    # Get the terminal size
    terminal_width = shutil.get_terminal_size().columns
    
    # Split text into lines in case it's multi-line
    lines = text.split('\n')
    
    for line in lines:
        # Calculate the padding on the left to center the text
        padding = (terminal_width - len(line)) // 2
        centered_line = ' ' * padding + line
        print(centered_line)

def Welcome():# Text to print
    text = "HELLO MR. ABHINAV"

    # Generate ASCII art with a dense font
    ascii_art = pyfiglet.figlet_format(text, font="slant")  # You can try "block", "big", "slant", etc.

    # Print the ASCII art to the command line
    printf(ascii_art)
