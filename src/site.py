import utime
from machine import Pin

try:
    import usocket as socket
except ImportError:
    import socket


class WebServer:
    def __init__(self, port=9128):
        """
        Initialize the WebServer instance.

        Parameters:
        - port (int): The port number on which the server will listen for incoming connections. Default is 9128.
        """
        self.led = Pin(2, Pin.OUT)
        self.messages = []
        self.port = port
        self.read_messages()

    @staticmethod
    def decode_message(encoded_message):
        """
        Decode the URL-encoded message.

        Parameters:
        - encoded_message (str): The URL-encoded message.

        Returns:
        - message (str): The decoded message.
        """
        message = encoded_message.replace("%20", " ")
        return message

    def save_message(self, message):
        """
        Save a new message along with its timestamp to the messages list and file.

        Parameters:
        - message (str): The message to be saved.
        """
        timestamp = utime.localtime()
        timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
            timestamp[0],
            timestamp[1],
            timestamp[2],
            timestamp[3],
            timestamp[4],
            timestamp[5],
        )
        self.messages.append((message, timestamp_str))
        with open("messages.txt", "a") as file:
            file.write(message + "," + timestamp_str + "\n")

    def read_messages(self):
        """
        Read messages from the messages file and populate the messages list.
        """
        with open("messages.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    message, timestamp = parts
                    self.messages.append((message, timestamp))

    def web_page(self):
        """
        Generate the HTML content for the web page.

        Returns:
        - html (str): The HTML content of the web page.
        """
        html = """<html>
        <head>
               <title>ESP8266 Web Server</title>
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
        <link rel="stylesheet" href="/style.css">
            <style>
            /* Add your custom CSS styles here */
            body {
                font-family: Helvetica;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                background-color: green;
            }

            h2 {
                color: #0F3376;
            }

            ul {
                list-style-type: none;
                padding: 0;
            }

            li {
                font-size: 1.5rem;
            }

            form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
    max-width: 90%;  /* Adjust the maximum width as needed */
    margin-left: auto;
    margin-right: auto;
    box-sizing: border-box;
}

input[type="text"] {
    margin-bottom: 10px;
    width: 100%;
    box-sizing: border-box;
}
            </style>
        </head>
        <body>
            <h2>Messages:</h2>
            <ul>"""

        for message, timestamp in self.messages:
            html += "<li>" + message + " (" + timestamp + ")</li>"

        html += """</ul>
            <form method="GET" action="/message">
                <input type="text" name="message" placeholder="Enter your message" required>
                <input type="submit" value="Send">
            </form>
        </body>
        </html>"""

        return html

    def handle_request(self, conn, request):
        """
        Handle an incoming HTTP request.

        Parameters:
        - conn (socket.socket): The socket connection object for the client.
        - request (bytes): The received HTTP request.

        Note: This method assumes the request is encoded in UTF-8.
        """
        request = request.decode("utf-8")  # Decode the request from bytes to string

        message_start = request.find("/message?message=")

        if message_start != -1:
            message_end = request.find(" ", message_start)
            if message_end != -1:
                message = request[
                    message_start + len("/message?message=") : message_end
                ]
                message = self.decode_message(message)  # Decode the message
                # self.save_message(message)
                # Ignore the message if it contains "Accept-Encoding:"
                if "Accept-Encoding:" not in message:
                    self.save_message(message)

        response = self.web_page()

        conn.send(b"HTTP/1.1 200 OK\n")
        conn.send(b"Content-Type: text/html\n")
        conn.send(b"Connection: close\n\n")
        conn.sendall(
            response.encode("utf-8")
        )  # Encode the response from string to bytes
        conn.close()

    def run(self):
        """
        Start the web server and listen for incoming connections.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", self.port))
        s.listen(5)

        while True:
            self.led.value(0)
            conn, addr = s.accept()
            print("Got a connection from %s" % str(addr))
            request = conn.recv(1024)
            print("Content = %s" % request)
            self.handle_request(conn, request)


# Create an instance of the WebServer class and run the server
server = WebServer()
server.run()
