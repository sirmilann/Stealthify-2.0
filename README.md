# Stealthify V2

Stealthify V2 is a lightweight code obfuscator for Python, designed to provide basic protection against casual reverse engineering of your source code.
It applies simple obfuscation techniques to make your code less readable and deter unauthorized access.

# Features:
- Basic Name Obfuscation: Stealthify V2 renames variables, functions, and parameters with randomly generated names to make the code less intuitive.
- Limited AST Transformations: The obfuscator performs basic Abstract Syntax Tree (AST) transformations to modify the code structure and confuse potential attackers.
- Single Obfuscation Layer: You can choose to apply a single layer of obfuscation to the code to make it slightly harder to understand.

# Usage:
1. Run the Stealthify V2 script.
2. Enter the path to the Python file you want to obfuscate.
3. Specify the number of obfuscation layers to apply.
4. The obfuscated code will be saved to a new file with "_obf" appended to the original filename.

Please note that while obfuscation can provide a basic level of code protection, it does not guarantee absolute security.
attackers may still attempt to reverse engineer the code given enough time and expertise.

# Requirements
Python 3.x

# Licence
Stealthify V2 is released under the MIT License.
