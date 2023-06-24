# Stealthify V2
Stealthify V2 is a Python code obfuscation tool designed to transform readable Python code into a more complex and difficult-to-understand version. 
It applies various obfuscation techniques such as renaming variables, functions, and classes, adding dead code, and optionally encoding and encrypting the obfuscated code. 
The tool aims to make the code more challenging to reverse-engineer or analyze while preserving its functionality.

How to Use
To use Stealthify V2, follow these steps:

Clone or download the Stealthify V2 repository from GitHub.
Ensure you have the necessary dependencies installed. The code relies on the ast and colorama libraries, which can be installed via pip:
Copy code
pip install ast colorama
Open the Python file containing the code you want to obfuscate.
Import the required modules and define the Stealthfiy class, Stealth function, Add_Dead_code function, and Stealthcrypt function.
Customize the obfuscation options by setting the variables antivm, add_junk, startup, anti_debug, and use_Stealthcrypt to either 'yes' or 'no' based on your preferences.
Run the script, providing the path to the file you want to obfuscate and the desired number of obfuscation iterations.
```python python stealthify_v2.py```
The obfuscated code will be saved to a new file with "_obf" appended to the original file name.

# Usage:

Ensure that the required modules:
ast, random, base64, os, marshal, zlib, sys, colorama. are installed in your Python environment.

1. Save the script to a file, for example, obfuscator.py.
2. Open a terminal or command prompt and navigate to the directory where obfuscator.py is saved.
3. Run the script by executing the command python obfuscator.py.
4. Follow the prompts to provide the file path of the code you want to obfuscate, the number of obfuscation layers, and other options.
5. Once the process is complete, the obfuscated code will be saved to a new file with the suffix "_obf" added to the original file name.
6. Please note that while obfuscation can provide a basic level of code protection, it does not guarantee absolute security.
7. attackers may still attempt to reverse engineer the code given time and expertise.

# Requirements
Python 3.x

# Licence
Stealthify V2 is released under the MIT License.
