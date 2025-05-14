import scapy.all as scapy

def sniff_wifi():
    print("Starting Wi-Fi sniffing...")
    print("Make sure that you have wifi cade or wifi usb adapter.")
    try:
        scapy.sniff(iface="wlan0", prn=lambda x: x.summary())
    except PermissionError:
        print("Permission denied. Please run as root or use sudo.") 
    except Exception as e:
        print(f"An error occurred: {e}")