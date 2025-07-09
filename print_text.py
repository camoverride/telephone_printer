
import os
import time
import sys



def print_text(text, newline=True):
    # Enable print permissions
    os.system("sudo chmod 777 /dev/usb/lp0")

    text_lines = text.split("\n")

    for line in text_lines:
        os.system(f"sudo echo -e {line} > /dev/usb/lp0")
        time.sleep(0.1)

    # Optional newline.
    if newline:
        os.system(f"sudo echo -e ' ' > /dev/usb/lp0")
        time.sleep(0.1)

    # Pause so printer doesn't overload.
    time.sleep(0.1)


if __name__ == "__main__":
    # Get the text from the command line.
    text = sys.argv[1]

    print_text(text=text, newline=True)
