# Printer



## Hardware requirements


## Install

If it's your first time using a particular Pi:

- Generate an SSH key and add it to GitHub.
- `git clone git@github.com:camoverride/telephone_printer.git`
- `cd telephone_printer`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

Install [cmake](https://lindevs.com/install-cmake-on-raspberry-pi/):

- `sudo apt update`
- `sudo apt install -y cmake`

Install system dependencies:

- `sudo apt install libatlas-base-dev libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good libcups2-dev libcupsimage2-dev git build-essential cups system-config-printer`

Test print some text:

- enable printer: `sudo chmod 777 /dev/usb/lp0`
- test printer: `echo -e "This is a test.\\n\\n\\n" > /dev/usb/lp0`

Get CUPS up and running [link](https://cdn-learn.adafruit.com/downloads/pdf/networked-thermal-printer-using-cups-and-raspberry-pi.pdf) and install the printer drivers:

- `cd ..`
- `git clone https://github.com/adafruit/zj-58`
- `cd zj-58`
- `make`
- `sudo ./install`

Set the printer name:

- `cd ../face_yourself`
- `lpadmin -p face_printer -v usb://POS58/Printer?serial=FMD072`
- `lpadmin -p face_printer -E -m zjiang/ZJ-58.ppd`
- `cupsenable face_printer`

Test print an image (if one exists):
- `sudo lp -d face_printer _face.jpg`


## Test

- `python print_faces.py`


## Run

Start a service with *systemd*. This will start the program when the computer starts and revive it when it dies:

- `mkdir -p ~/.config/systemd/user`
- `cat printing.service > ~/.config/systemd/user/printing.service`

Start the service using the commands below:

- `systemctl --user daemon-reload`
- `systemctl --user enable printing.service`
- `systemctl --user start printing.service`

Check the status: `systemctl --user status printing.service`

Start it on boot: `sudo loginctl enable-linger pi`

Get the logs: `journalctl --user -u printing.service`


## Printer commands

- `sudo lp -d face_printer fonda/2023-11-29-16-05-44-937441.png`
- `cupsenable face_printer`
- `tail /var/log/cups/error_log`
- `sudo journalctl -b 0 -u cups`


## Camera Settings

If the prints are too dark, the camera settings might need to be changed. By default, the logitech webcam might be set to "manual." For darker spaces, change it to "aperture priority mode", which is fully automatic: `v4l2-ctl -d /dev/video0 -c auto_exposure=3`

Confirm this change: `v4l2-ctl -d /dev/video0 -l | grep auto_exposure`


## Increase Longevity

Follow these steps in order:

Install tailscale for remote access and debugging:
- `curl -fsSL https://tailscale.com/install.sh | sh`
- `sudo systemctl start tailscaled`
- `sudo tailscale up --authkey <your-auth-key>`

Set up periodic reboots (cron job):
- `sudo crontab -e`
- add `0 0 * * * /sbin/reboot`

Configure a read-only overlay filesystem (write temp files to RAM)


## TODO

- [X] make sure images always print in the same direction
- [X] test camera sharpness and brightness - non manual mode!
- [X] add save image mode
- [X] replace with mediapipe face detection
- [X] process all faces, not just first one
- [ ] test in situ
- [ ] add timestamp
- [ ] install physical devices
- [ ] take photos and videos



- [ ] condense and harmonize all utils (modules beginning with an underscore `_`).
