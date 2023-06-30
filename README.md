
# ESP8266-LAN-chat #

![picture alt](https://imrad.com.ua/userdata/modules/wproducts/product/big/140918.jpg)


ESP8266 LAN Chat is a simple chat application built for the ESP8266 microcontroller, allowing users on the same local network to exchange messages in real-time.



## Features

- Send and receive messages on the local network using ESP8266 microcontrollers.
- Messages are timestamped and saved to a local file for future reference.
- Basic web interface for displaying and sending messages.
- Easy configuration of Wi-Fi network credentials.

## Getting Started

To get started with ESP8266 LAN Chat, follow these steps:

1. Clone or download the repository from [GitHub](https://github.com/YuriiDorosh/ESP8266-LAN-chat).
2. Open the project in your preferred MicroPython development environment.
3. Configure the Wi-Fi network credentials in the `config.py` file by setting the `ssid` and `password` variables.
4. [Upload the code to your ESP8266 microcontroller.](src)
5. Connect the ESP8266 to your local network.
6. Access the web interface by opening a web browser and entering the IP address of the ESP8266.
7. Start sending and receiving messages on the LAN chat.




## Dependencies

The following dependencies are required to run ESP8266 LAN Chat:

- #### `MicroPython` (v1.12 or later)

 MicroPython is a compact and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimized to run on microcontrollers and in limited environments.

MicroPython contains many advanced features such as interactive tooltip, arbitrary-precision integers, closures, list comprehensions, generators, exception handling, and more. However, it is compact enough to fit and run on just 256KB of code space and 16KB of RAM.

MicroPython aims to be as compatible as possible with regular Python so that you can easily port code from your desktop to a microcontroller or embedded system.

- #### `usocket` (optional, for MicroPython builds without built-in socket support)

## Contributing

Contributions welcome! I'm not a professional developer, but specifically a microcontroller software developer. If you know how to implement data storage without performance issues, using JSON or even using databases, or if you find any other problems or have suggestions for improvements, please create a new issue or submit a pull request on GitHub.
