# 	   CaPWN-Net
### Developed by MafiaSec Cybersecurity
###	www.mafiasec.net




CaPWN-Net is an IRC Botnet C&C Suite equipped with some solid traditional botnet features including registry persistence, DDoS, and more.



## Table of Contents:

1. Installation
2. Features
3. Usage
4. Credits



## Installation:

CaPWN-Net is completely standalone; so either run the python script on the target bot machine or compile the python code and run the resulting .exe.

## Features:

CaPWN-Net currently supports the following:

- Registry Persistence
- DDoS (Parser Needs Fixing)
- psutil Hardware Stat Report
- Remote Shutdown
- Bot Nicknames
- Botstub Obfuscation
- whois Platform/Hostname/OS/Processor Check
 

## Usage:

First, you need to run the CaPWN-Net stub (the .py or .exe file referenced above) to turn the host machine into a "bot". 
At that point, the bot will begin reporting to the C&C IRC server and channel specified in the "global variables" section, under "server" and "channel".
You may issue commands to CaPWN-Net bots by using "!" as a prefix, then joining a known command to it:

> !start_ddos

> !whois

> !shutdown [botnickname]

> !psutil [botnickname]




## Credits:

CaPWN-NET is a development of Max Bishop (ṡρøøќÿ / red-r3b3l) under MafiaSec Cybersecurity. We welcome any potential contributors!



## MIT License

Copyright (c) 2018 ṡρøøќÿ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.