# VMESS URI to JSON Converter

The **VMESS URI to JSON Converter** is a simple command-line tool designed to convert bulk VMESS URIs into JSON format for easy integration and configuration in various applications. This tool simplifies the process of converting a large number of VMESS URIs into structured JSON data.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Bulk conversion of VMESS URIs into JSON format.
- Output customization for JSON configuration.
- Simple and straightforward command-line interface.
- Useful for integrating VMESS URIs into various applications, such as VPN clients.

## Installation

1. **Prerequisites**: Ensure you have Python 3 installed on your system.

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/librec0de/vmess2json.git
   ```
Navigate to the Directory:

```bash
cd vmess2json
```
Install Dependencies (if required):
```bash
pip install -r requirements.txt
```
Usage
The VMESS URI to JSON Converter needs the following files to work as intended:
- Root
  - config.txt
  - vmess_uris.txt
  - vmess_config.json
  - vmess2json.py

Example Usage:

```bash
python vmess2json.py
```
Ensure that your vmess_uris.txt file contains VMESS URIs, one per line.

Contributing
Contributions are welcome! If you'd like to enhance this tool, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes.
Push to your branch.
Create a pull request.
License
This tool is open-source and released under the GNU License. You can use, modify, and distribute it as you see fit.

I hope this tool simplifies the process of converting VMESS URIs to JSON format for your needs. If you have any questions or encounter any issues, please feel free to open an issue or submit a pull request.

Happy coding!
   
