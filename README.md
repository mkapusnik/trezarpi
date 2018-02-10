# TrezarPi

## What is TrezarPi?


## What do I need?

## Installation

1. Get a Raspberry Pi (I'm using Zero W, but any will do)
2. Download Raspbian Jessie (becareful, not Stretch as the Trezar Wallet won't work there)
2a. Lite version, if you don't plan on using Desktop and want to save some system resources
3. Install on your SD card: https://www.raspberrypi.org/documentation/installation/installing-images/README.md
4a. Either prepare a monitor+keyboard
4b. Create empty file with name 'ssh' in boot partition and setup WiFi if you need to:
  https://thepihut.com/blogs/raspberry-pi-tutorials/83502916-how-to-setup-wifi-on-raspbian-jessie-lite 

(Optionally: Update hostname https://thepihut.com/blogs/raspberry-pi-tutorials/19668676-renaming-your-raspberry-pi-the-hostname)

5. Put it all together, insert prepared SD card into your RPi and power on. Wait for the raspbian initialization do it's magic first.
6. Login through ssh (default raspbian username is 'pi' and password 'raspberry') or locally
7. Run instalation command:
```
wget -q -O- https://raw.githubusercontent.com/mkapusnik/trezarpi/master/install | bash
```