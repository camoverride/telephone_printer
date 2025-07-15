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

- `cd ../telephone_printer`
- `lpadmin -p text_printer -v usb://POS58/Printer?serial=FMD072`
- `lpadmin -p text_printer -E -m zjiang/ZJ-58.ppd`
- `cupsenable text_printer`

## Test

- `python print_text.py`


## Run

Start a service with *systemd*. This will start the program when the computer starts and revive it when it dies:

- `mkdir -p ~/.config/systemd/user`
- `cat printer.service > ~/.config/systemd/user/printer.service`

Start the service using the commands below:

- `systemctl --user daemon-reload`
- `systemctl --user enable printer.service`
- `systemctl --user start printer.service`

Check the status: `systemctl --user status printer.service`

Start it on boot: `sudo loginctl enable-linger pi`

Get the logs: `journalctl --user -u printer.service`


## Printer commands

- `cupsenable text_printer`
- `tail /var/log/cups/error_log`
- `sudo journalctl -b 0 -u cups`


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
