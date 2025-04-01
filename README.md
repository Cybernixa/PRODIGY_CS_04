# PRODIGY_CS_04
SIMPLE KEYLOGGER
The code you've shared is a simple keylogger using the `pynput` library to listen for key presses and record them into a text file (`keylog.txt`). While the code works by logging keystrokes, it's crucial to emphasize ethical considerations, legal implications, and responsible use.

Here’s a detailed explanation for the code along with some important warnings for responsible use:

---

## Keylogger Script using `pynput`

This script implements a basic keylogger using the `pynput` library, which listens for keyboard input and logs the pressed keys into a file. It captures alphanumeric key presses as well as special keys such as the `spacebar`, `enter`, and `esc`. The script is designed to stop recording when the `Esc` key is pressed.

### Key Features:
- **Key Logging**: Records key presses into a text file (`keylog.txt`).
- **Capture Alphanumeric Keys**: Captures any character typed on the keyboard.
- **Capture Special Keys**: Recognizes special keys such as `Enter`, `Space`, and any other non-alphanumeric keys.
- **Stop Listener**: The script will stop when the `Esc` key is pressed.
- **Ethical Warning**: The script includes an ethical warning that stresses the importance of responsible usage.

### How it Works:

1. **`on_press(key)`**:
   - The `on_press` function is called every time a key is pressed.
   - It checks if the key is the `Esc` key. If so, it stops the listener and prints a message: `"Keylogger stopped."`
   - For alphanumeric keys, it retrieves the character using `key.char`.
   - For special keys, it assigns a descriptive string (`[Key.space]`, `[Key.enter]`, etc.) to represent those keys.
   - All captured keys (including special ones) are then appended to a file (`keylog.txt`) in append mode.
   
2. **Ethical Warning**: 
   - The script starts by printing a warning message. This emphasizes that using a keylogger without permission is illegal and unethical.
   - The warning clearly advises that unauthorized use of such tools is a violation of privacy and security laws.

3. **`keyboard.Listener`**:
   - The `Listener` listens for keyboard events and calls the `on_press` function when a key is pressed.
   - The `listener.join()` method keeps the listener running in the background, waiting for key events.

4. **Stopping the Listener**: 
   - The listener stops when the `Esc` key is pressed. This is handled by returning `False` from the `on_press` function, which terminates the listener.

### Example Output in `keylog.txt`:
If a user types `Hello World!` and presses the `Enter` key, the output might look like:

```
Hello World!
```

If the space bar, enter key, or other special keys are pressed, they will be logged with descriptive tags like `[Key.space]` and `[Key.enter]`.

### Ethical and Legal Considerations:

- **WARNING**: **Do not use this keylogger without explicit permission**. Unauthorized logging of keystrokes is illegal in many jurisdictions and violates privacy laws.
- **Privacy**: Recording someone’s keystrokes without their knowledge and consent is a serious breach of privacy.
- **Legal Use Cases**: This script may be used for ethical purposes, such as testing and securing your own systems, with explicit permission from all involved parties. Examples of acceptable use might include:
  - Penetration testing (with written consent)
  - Testing and debugging keyboard input functionality for software you're developing
  - Educational purposes (in controlled environments with consent)

### Alternatives to Keyloggers for Security Testing:
- **User Activity Monitoring Software**: There are legitimate software tools designed for monitoring user activity with consent (e.g., parental controls, employee monitoring with consent).
- **Penetration Testing Tools**: Many ethical hacking tools offer more secure and auditable ways to test the security of your systems.

### Code Example with Ethical Consideration:

```python
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
```

### Important Notes:
1. **Do Not Deploy on Other People’s Systems**: Never install or use this script on someone else’s system without their explicit consent.
2. **Use with Caution**: Even in environments where you have permission, always be transparent about the use of such tools.
3. **Security**: Make sure to secure the log file (`keylog.txt`). Do not allow unauthorized access to the log file where keystrokes are stored.

### Conclusion:
This keylogger script provides a basic understanding of how keystroke logging works and how it can be implemented using the `pynput` library. While the code is educational, the ethical and legal implications of using such tools should always be considered. Always use keylogging tools responsibly and legally, and only with full consent from all parties involved.
