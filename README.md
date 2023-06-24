![Screenshot_2023-06-24_105614-removebg-preview](https://github.com/sirmilann/Stealthify-2.0/assets/94076644/43167b70-54a3-4015-a2d7-92ce1328ba5c)
![image](https://user-images.githubusercontent.com/94076644/208468748-e4e44944-f978-4806-980d-601202be9afa.png)

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

1. `Stealthfiy`: This class is an `ast.NodeTransformer` subclass responsible for traversing the abstract syntax tree (AST) of the code and performing the obfuscation transformations.
It includes methods for obfuscating names, handling imports, functions, classes, exceptions, calls, and more.

3. `Stealth`: This function takes the original code and the desired number of obfuscation iterations as input. It uses the `Stealthfiy` class to transform the code by repeatedly visiting the AST and applying obfuscation techniques. The obfuscated code is returned as output.

4. `Add_Dead_code`: This function adds dead code to the obfuscated code by inserting random comments throughout the code. This technique aims to make the code harder to analyze by introducing noise and irrelevant information.

5. `Stealthcrypt`: This function performs encoding and encryption of the obfuscated code. It compresses the code using the zlib library, encodes the compressed data using base64,base85 and marshal. and generates code that can decode and execute the original code at runtime. The encoded and encrypted code is returned as output.

### Examples

Here are some examples of Stealthify V2s Obfuscation Process:

Before:
```python
GLOBAL_VAR = 10
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

def my_function():
    return "This is a function."

obj = MyClass("John Doe")
obj.say_hello()

result = my_function()
print(result)
```
After Normal Obfuscation:
```python
# Obfuscated With Stealthify V2 By Sirmilann
IlllIlIllIIlIIIlIIllllIIlllIIlIIlIl = 10

class llIlIIlIIllIIlllllIlllIlIlIIIIlIIlI:

    def __init__(lIIIIlllIlllllIIIIlIlIlIlllIlIlIIIl, lIllIlllIllIIIIlIIIllIIIIIlIIllIIlI):
        lIIIIlllIlllllIIIIlIlIlIlllIlIlIIIl.name = lIllIlllIllIIIIlIIIllIIIIIlIIllIIlI

    def say_hello(lIIIIlllIlllllIIIIlIlIlIlllIlIlIIIl):
        print('Hello, ' + lIIIIlllIlllllIIIIlIlIlIlllIlIlIIIl.name)

def my_function():
    return 'This is a function.'
llIllIIllllIlIIIIIIIIIIIIIIlIIlIIII = llIlIIlIIllIIlllllIlllIlIlIIIIlIIlI('John Doe')
llIllIIllllIlIIIIIIIIIIIIIIlIIlIIII.say_hello()
lllIllllIlIIlIlllllIIIlIlIlIllllIlI = my_function()
print(lllIllllIlIIlIlllllIIIlIlIlIllllIlI)
```
After Including Dead Code:
```python
# Obfuscated With Stealthify V2 By Sirmilann
IIlIIllIIllllllIlllIIllIIllllIIIlII = 10
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
class llIIIllIllllIlIIIIIlIIIlIIllIIllIlI:
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
    def __init__(IllIIIIIllIlIlIlIIllllIlIIlIlllIlII, IllIlIIlIlIIlIIIIIlIIIIIlIlIlIIIIll):
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
        IllIIIIIllIlIlIlIIllllIlIIlIlllIlII.name = IllIlIIlIlIIlIIIIIlIIIIIlIlIlIIIIll
#__STEALTHIFY_V2____STEALTHIFY_V2__
    def say_hello(IllIIIIIllIlIlIlIIllllIlIIlIlllIlII):
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
        print('Hello, ' + IllIIIIIllIlIlIlIIllllIlIIlIlllIlII.name)
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
def my_function():
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
    return 'This is a function.'
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
IIllIlIIIIlIllIIIIIIIlIllIIlllIIIIl = llIIIllIllllIlIIIIIlIIIlIIllIIllIlI('John Doe')
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
IIllIlIIIIlIllIIIIIIIlIllIIlllIIIIl.say_hello()
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
IIllIIIllIIllllllIlIIIIIlIlIIllIllI = my_function()
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
print(IIllIIIllIIllllllIlIIIIIlIlIIllIllI)
#__STEALTHIFY_V2____STEALTHIFY_V2____STEALTHIFY_V2__
```
After Including Encoding And Compression:
```python
# Obfuscated With Stealthify V2 By Sirmilann
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ = ""
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "YyR8JD15JC"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "1ANDVIXm5Z"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "NnRfYGcpOT"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "dtQT0zdCVP"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "Tm1GU2BhI0"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "I7O3AtPHpo"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "JTgkXnhhWE"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "c/cUBPXnk4"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "Vkx0b2F1Q0"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "I+QzEtR0dG"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "cnp3UFohUD"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "YwLXJOJFR9"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "cFk8TXdoZn"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "lTUHlKckJq"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "X0xMbjhwfH"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "FOV0M9d2Bn"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "cjt2aHpubz"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "R4cGtvUVdX"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "cUk4b3JlKW"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "luWEdBSndF"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "eXJoKyVMQS"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "tgPCVfNGU5"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "R358Zmg9eX"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "tKeVBYKVU8"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "WG8oQ0QqJE"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "8jO3laRSg7"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "WnIxSWoyM2"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "BEa00+KS0t"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "TSl2NUhMRi"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "owMTZCVURQ"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "PDItRkR0ZD"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "JRYmRxJT93"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "Ynt+MzsqRm"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "lGIyEmPEZS"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "IzMzOVpTfV"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "BAclApWi1A"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "dVFtdXptNF"
__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__ += "cxNm19SzNG"
exec(__import__('\x6D\x61\x72\x73\x68\x61\x6C').loads(__import__('\x7A\x6C\x69\x62').decompress(__import__('\x62\x61\x73\x65\x36\x34').b85decode(__import__('\x62\x61\x73\x65\x36\x34').b64decode(__STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2____STEALTHIFY__V2__.encode()).decode()))))
```

