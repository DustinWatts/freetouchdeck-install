import os

os.system("cls")
print("Installation script started")
print("-----------------")
print("Script version: 1.0")
print("Firmware verion: 0.9.17")
print("Author: Dustin Watts (dustin_watts@yahoo.com)")
print("-----------------")
print("")

while True:
    try:
    	# Waiting for user to press Enter
        input("Plug in the board and press enter to start firmware upload...")
        # Flashing the board using esptool.py
        os.system("python3 esptool.py write_flash 0x0 ESP32TouchDown.bin")
    except Exception as e:
        print(e)