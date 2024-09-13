# Python Keylogger

## Overview

This project includes a keylogger implemented in Python, which captures key presses and sends them to a server. The server, also implemented in Python using Flask, receives and displays the captured data.

## Components

1. **Keylogger Client**: A Python script that captures key presses and sends the data to a server.
2. **Keylogger Server**: A Flask-based Python script that receives and displays the captured key presses.

## Setup

### Prerequisites

- Python 3.x
- `pip` for installing Python packages

### Installation

#### Keylogger Client

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/keylogger-project.git
   cd keylogger-project
   ```
   
2. **Create a virtual enviroment (optional)**:
   
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the required packages**:

   ```bash
   pip install pynput requests aiohttp
   ```

4. **Run the Server on the attacker machine**:
   
    ```bash
    python server.py
    ```

5. **Run the Client on the victim machine**:
   
    ```bash
    python client.py
    ```

### Notes

- Ensure that your firewall or antivirus software allows traffic on specified port.
- If you experience issues with the server not receiving data, verify that the server URL in the `client.py` script is correct and that the server is running.
- This is only an educational aimed project to achive a better understanding on how does a KeyLogger works.


