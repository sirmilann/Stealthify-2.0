# Stealthify V2

Stealthify V2 is a lightweight code obfuscator for Python, designed to provide basic protection against casual reverse engineering of your source code.
It applies simple obfuscation techniques to make your code less readable and deter unauthorized access.

# Features:
- Basic Name Obfuscation: Stealthify V2 renames variables, functions, and parameters with randomly generated names to make the code less intuitive.
- The obfuscated code is enhanced with randomly generated lines of junk code, which are interspersed throughout the code to make it more difficult to analyze and understand.
- Limited AST Transformations: The obfuscator performs basic Abstract Syntax Tree (AST) transformations to modify the code structure and confuse potential attackers.
- Base64 Encoding layer: Adds another layer of Base64 Encoding over the obfuscated code to make it slightly harder to understand.
- Multiple Obfuscation Layers: You can choose to apply multiple layers of obfuscation to the code to make it slightly harder to understand.

# Example
Before:
```python
def calculate_sum(a, b):
    return a + b

num1 = 5
num2 = 3
result = calculate_sum(num1, num2)

print("The sum of", num1, "and", num2, "is:", result)
```
After:
```python
# Obfuscated With Stealthify V2 By Sirmilann
def calculate_sum(GPsNnNxMeahbjiH, WgvHnWsqZTEHvfs):
    return GPsNnNxMeahbjiH + WgvHnWsqZTEHvfs
gDJzfxEjofxXCZv = 5
JCPvxuaLAlRTHaz = 3
InjxWyhTqHxOReG = calculate_sum(gDJzfxEjofxXCZv, JCPvxuaLAlRTHaz)
print('The sum of', gDJzfxEjofxXCZv, 'and', JCPvxuaLAlRTHaz, 'is:', InjxWyhTqHxOReG)
```
After Including Junk Code:
```python
# Obfuscated With Stealthify V2 By Sirmilann
def calculate_sum(BHCMiwviUfGTBmw, QYoagIeuwoJdViz):
# pShOoIrPeJZBtcDYdfOoZvBreiUlFrCCuqg
    return BHCMiwviUfGTBmw + QYoagIeuwoJdViz
# dzPRTnMtKFOrgJVNKzAhbCbqLJlcyJKFizQ
hUpuFTIFFfWQGZz = 5
# bKZnKSFRwLWghMsudYPiSXKVYXrEmVImkyI
kMDDRzHjOVjliqb = 3
# WyrBhkEUZAPXKVfHdFdHTisVhKGDbWcsPIN
hIyRLHFLUXuTvJn = calculate_sum(hUpuFTIFFfWQGZz, kMDDRzHjOVjliqb)
# OsSgJhWkVnUjXLvHgyaYibXRSkYXEJjjQOg
print('The sum of', hUpuFTIFFfWQGZz, 'and', kMDDRzHjOVjliqb, 'is:', hIyRLHFLUXuTvJn)
# reeYBgqjdHHNQooEyKIlJCqtdiBlCHUHzvd
```


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
