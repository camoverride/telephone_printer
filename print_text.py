
import os
import time
import sys



def print_text(text, newline=True):
    # Enable print permissions
    os.system("sudo chmod 777 /dev/usb/lp0")

    # If it's just a string, print it.
    if type(text) == str:
        os.system(f"sudo echo -e {text} > /dev/usb/lp0")
        time.sleep(0.1)
    
    # If it's a list of stuff, print each as individual lines.
    elif type(text) == list:
        for line in text:
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
