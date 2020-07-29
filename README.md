# Yippee-Ki-Yay-MFA-er
This project is a PoC ("Proof of Concept") to demonstrate how hardened cyber criminals (like "Cyber Mike") can defeat OTP Multi-Factor Authentication using real-time replay session instantiation attacks.  

<img src="https://raw.githubusercontent.com/pan0pt1c0n/Yippee-Ki-Yay-MFA-er/master/CyberMike.png" width="250"/>

# DEFCON -- Red Team Village
The Python script (bypass.py) can be used in conjunction with the Methodology described in my DEFCON talk...
***Yippee-Ki-Yay MFA'er - Bypassing Multi-Factor Authentication with Real-Time Replay  
Session Instantiation Attacks***
...as a demonstration of this attack.

The talk will be presented at 15:30 PDT (Las Vegas Time) on August 7, 2020.  More details available on the [DEFCON Red Team Village website](https://redteamvillage.io/day1.html).

## How it Works???
![How It Works](https://raw.githubusercontent.com/pan0pt1c0n/Yippee-Ki-Yay-MFA-er/master/HowItWorks.png)


## MITRE ATT&CK
This technique maps to the [T1111 - Two Factor Authentication Interception](https://attack.mitre.org/techniques/T1111/) TTP.

## Target App
The target app for this POC is a slightly modified (only cosmetic changes to fit with the Talk theme) of a Flask 2FA example login page published by Miguel Grinberg at [https://github.com/miguelgrinberg/two-factor-auth-flask](https://github.com/miguelgrinberg/two-factor-auth-flask).

## Disclaimer
To be clear, this is not an exploit of a vulnerability in Miguel's proof-of-concept, but rather an underlying risk inherent to all OTP-based Multi-Factor Authentication. Miguel's code just happens to make a very convenient test environment for demonstrating MFA exploits.
