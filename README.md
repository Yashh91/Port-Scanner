#  TCP Port Scanner

A lightweight and easy-to-use Python command-line tool for scanning TCP ports on a target host or IP address.

##  Features

- Scan TCP ports on any host or IP address
- Custom start and end port range
- Multi-threaded scanning for faster results
- Displays open ports in real time
- Simple command-line interface
- No third-party libraries required
- Cross-platform (Windows, Linux, macOS)
- Beginner-friendly and easy to customize
  
## Installation

```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```
##  Usage

Display the help menu:

```bash
python3 port_scanner.py -h
```

Scan the default port range (1-1024):

```bash
python3 port_scanner.py localhost
```

Scan a custom port range:

```bash
python3 port_scanner.py localhost -s 20 -e 100
```

Scan a website:

```bash
python3 port_scanner.py google.com
```

Scan an IP address:

```bash
python3 port_scanner.py 192.168.1.100
```

Increase the number of threads:

```bash
python3 port_scanner.py google.com -s 1 -e 1000 -t 200
```
##  Example Output

```text
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║
██║     ╚██████╔╝██║  ██║   ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝

TCP Port Scanner
Author: Yashh91

========================================
Target : localhost
Ports  : 1 - 1024
========================================

[OPEN] Port 22
[OPEN] Port 80
[OPEN] Port 443

Scan Completed!

Total Open Ports : 3
```
## 📸 Screenshots

### Help Menu

<img width="1227" height="677" alt="image" src="https://github.com/user-attachments/assets/fe122a78-b1ba-4f2d-a90f-2caea69b1ce3" />

### Localhost Scan

<img width="1276" height="522" alt="image" src="https://github.com/user-attachments/assets/2730adef-ab00-40d0-bb92-f40b5ed57c80" />

### Custom Port Range

<img width="1272" height="515" alt="image" src="https://github.com/user-attachments/assets/47b7c556-6f92-402d-bb78-3a88728e09ee" />

## 📄 License

This project is licensed under the MIT License.


