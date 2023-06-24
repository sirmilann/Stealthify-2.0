## Stealthify V2

Stealthify V2 is a Python code obfuscation tool designed to transform readable Python code into a more complex and difficult-to-understand version. It applies various obfuscation techniques such as renaming variables, functions, and classes, adding dead code, and optionally encoding and encrypting the obfuscated code. The tool aims to make the code more challenging to reverse-engineer or analyze while preserving its functionality.

### How to Use

To use Stealthify V2, follow these steps:

1. Clone or download the Stealthify V2 repository from GitHub.
2. Ensure you have the necessary dependencies installed. The code relies on the `ast` and `colorama` libraries, which can be installed via pip:
   ```
   pip install ast colorama
   ```
3. Open the Python file containing the code you want to obfuscate.
4. Import the required modules and define the `Stealthfiy` class, `Stealth` function, `Add_Dead_code` function, and `Stealthcrypt` function.
5. Customize the obfuscation options by setting the variables `antivm`, `add_junk`, `startup`, `anti_debug`, and `use_Stealthcrypt` to either `'yes'` or `'no'` based on your preferences.
6. Run the script, providing the path to the file you want to obfuscate and the desired number of obfuscation iterations.
   ```
   python stealthify_v2.py
   ```
7. The obfuscated code will be saved to a new file with "_obf" appended to the original file name.

### Functions

1. `Stealthfiy`: This class is an `ast.NodeTransformer` subclass responsible for traversing the abstract syntax tree (AST) of the code and performing the obfuscation transformations. It includes methods for obfuscating names, handling imports, functions, classes, exceptions, calls, and more.

2. `Stealth`: This function takes the original code and the desired number of obfuscation iterations as input. It uses the `Stealthfiy` class to transform the code by repeatedly visiting the AST and applying obfuscation techniques. The obfuscated code is returned as output.

3. `Add_Dead_code`: This function adds dead code to the obfuscated code by inserting random comments throughout the code. This technique aims to make the code harder to analyze by introducing noise and irrelevant information.

4. `Stealthcrypt`: This function performs encoding and encryption of the obfuscated code. It compresses the code using the zlib library, encodes the compressed data using base64, and generates executable code that can decode and execute the original code at runtime. The encoded and encrypted code is returned as output.

### Examples

Here are some examples of how to use Stealthify V2:

```python
import ast, random, base64, os, marshal, zlib, sys
from colorama import Fore as f```

Please note that the provided examples showcase the usage of individual functions. In practice, you would typically combine these functions to obfuscate, add dead code

and optionally encode/encrypt the code in a single run.

Remember that code obfuscation is not a foolproof security measure, and it should not be solely relied upon for protecting sensitive or critical information.
