
import os
import time
import sys



def print_text(text, newline=True):
    # Enable print permissions
    os.system("sudo chmod 777 /dev/usb/lp0")

    # Purge non-ASCII
    text = ''.join(char for char in text if ord(char) < 128)

    # Purge quotes.
    text = text.replace("'", "").replace('"', '')

    text_lines = text.split("\n")

    for line in text_lines:
        os.system(f"sudo echo -e {line} > /dev/usb/lp0")
        time.sleep(0.1)

    # Optional newline.
    if newline:
        for _ in range(10):
            os.system(f"sudo echo -e ' ' > /dev/usb/lp0")
            time.sleep(0.1)

    # # Ending text
    # os.system(f"sudo echo -e '--------------------------------' > /dev/usb/lp0")
    # time.sleep(0.1)
    # os.system(f"sudo echo -e '--------------------------------' > /dev/usb/lp0")
    # time.sleep(0.1)
    # os.system(f"sudo echo -e '------thanks for visiting!------' > /dev/usb/lp0")
    # time.sleep(0.1)
    # os.system(f"sudo echo -e '--------------------------------' > /dev/usb/lp0")
    # Pause so printer doesn't overload.
    time.sleep(0.1)


if __name__ == "__main__":
    # Get the text from the command line.
    text = sys.argv[1]

    print_text(text=text, newline=True)
