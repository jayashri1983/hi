# vuln.py

import os
import subprocess

def run_ping(user_input):
    # ⚠️ Vulnerable to command injection
    os.system("ping " + user_input)

def run_ls():
    # ⚠️ Use of subprocess without shell=False is risky
    subprocess.call("ls -l", shell=True)

def bad_compare(password):
    # ⚠️ Insecure password comparison
    if password == "admin123":
        print("Access granted")
