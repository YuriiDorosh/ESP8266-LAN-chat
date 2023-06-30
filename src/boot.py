try:
    import usocket as socket  # Try importing 'usocket' module (optimized for micropython)
except ImportError:
    import socket  # Fallback to standard 'socket' module

import network  # Module for managing network connections
import esp  # Module for controlling the ESP8266 board
import gc  # Module for garbage collection
import site  # Module for serving web pages
import config  # Custom configuration module

esp.osdebug(None)  # Disable debugging output from ESP8266
gc.collect()  # Perform garbage collection to free up memory


def do_connect():
    """
    Connect to the configured Wi-Fi network.

    This function enables the station interface (STA_IF) of the network module,
    connects to the Wi-Fi network using the configured SSID and password,
    and waits until the connection is established.

    Note: The network configuration (SSID and password) is defined in the 'config' module.
    """
    sta_if = network.WLAN(network.STA_IF)  # Create a WLAN station interface object
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)  # Enable the station interface
        sta_if.connect(config.ssid, config.password)  # Connect to the Wi-Fi network
        while not sta_if.isconnected():
            pass  # Wait until the connection is established
    print("Network config:", sta_if.ifconfig())


do_connect()  # Connect to the Wi-Fi network
site.web_page()  # Serve the web page
