## Overview

Small project for learning Python. This script calls the **Pwned Passwords** API using the _k-Anonymity model_ to check if your password(s) has been hacked in a secure way. Also returns how many times appears in data breaches. Read the [docs API](https://haveibeenpwned.com/API/v3) for more info.

## Usage

Install the **Requests** library with **pip**.

```bash
pip install requests
```

Indicate the passwords that you want to check inside the `passwords.txt` file. Write every password in a new line as in the example.

```bash
python checker.py
```