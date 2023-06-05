# Stealthify V2

Stealthify V2 is a lightweight code obfuscator for Python, designed to provide basic protection against casual reverse engineering of your source code.
It applies simple obfuscation techniques to make your code less readable and deter unauthorized access.

# Features:
- Basic Name Obfuscation: Stealthify V2 renames variables, functions, and parameters with randomly generated names to make the code less intuitive.
- The obfuscated code is enhanced with randomly generated lines of junk code, which are interspersed throughout the code to make it more difficult to analyze and understand.
- Limited AST Transformations: The obfuscator performs basic Abstract Syntax Tree (AST) transformations to modify the code structure and confuse potential attackers.
- Another Encoding layer: Adds another layer of Base64, base85, marshal and zlib Encoding and compression over the obfuscated code to make it slightly harder to understand.
- Multiple Obfuscation Layers: You can choose to apply multiple layers of obfuscation to the code to make it slightly harder to understand.

# Example
Before:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2
area = Circle.calculate_area()
print("Area:", area)
```
After:
```python
# Obfuscated With Stealthify V2 By Sirmilann
class Circle:

    def __init__(ϋωφϫξϕϤδϨγϡϊλϐκμϩϮνφ, ϚρηϣρξϐσττκϣϕϘοφϯηχρ):
        ϋωφϫξϕϤδϨγϡϊλϐκμϩϮνφ.radius = ϚρηϣρξϐσττκϣϕϘοφϯηχρ

    def calculate_area(ϋωφϫξϕϤδϨγϡϊλϐκμϩϮνφ):
        return 3.14 * ϋωφϫξϕϤδϨγϡϊλϐκμϩϮνφ.radius ** 2
ϧυϠϪώζξεϓσϡφκλςϤξωϧθ = Circle.calculate_area()
print('Area:', ϧυϠϪώζξεϓσϡφκλςϤξωϧθ)
```
After Including Junk Code:
```python
# Obfuscated With Stealthify V2 By Sirmilann
class Circle:
# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε

# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε
    def __init__(ζθϡγϞψϓϚϠϏωϢϏμϓπϖϟχϡ, ϣϖϓϗϬϐφϚλφϔϣγπλϟοϜϭϊ):
# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε
        ζθϡγϞψϓϚϠϏωϢϏμϓπϖϟχϡ.radius = ϣϖϓϗϬϐφϚλφϔϣγπλϟοϜϭϊ
# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε

# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε
    def calculate_area(ζθϡγϞψϓϚϠϏωϢϏμϓπϖϟχϡ):
# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε
        return 3.14 * ζθϡγϞψϓϚϠϏωϢϏμϓπϖϟχϡ.radius ** 2
# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε
ϝκϗκεμϓηϐϦθϓξϘϙϬοσϗμ = Circle.calculate_area()
# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε
print('Area:', ϝκϗκεμϓηϐϦθϓξϘϙϬοσϗμ)
# εκϐνξϔϗεκϚαϑϪϙϠϞϣχδε
```
After Encoding And Compression:
```python
# Obfuscated With Stealthify V2 By Sirmilann
import zlib, marshal, base64;exec(marshal.loads(zlib.decompress(base64.b85decode(base64.b64decode('YyR+RlRPLXNXLTVHe0Q/dU5kJnFIazUhTHItQkZaaGxDfHJBck9MV2xEakNoNnshYSk7enlmUTFWeWNhVnpwTVN8NnR4PGF6SWE+dlZzRyV5dG5Nazh7VFhaRUwxOWZxPl9YLUxnUG9lUmIzPXA7RjZ5KSN0cGktIy04dn5qTzM7eGMhVlBxSlFkY2YrUG8hK0t5US1nZz5qZ0FVTENzX083NWVMR2RXTkFPP1pjPT08eiRjUW5TcXUoKEFCRUptVSU0IXRWR0hlWmx1VW0oRzJqO1QqUnB1ITh8fDxQRUZnPV9rdDA7VGpjJFN3ZF4yPWxPM2RlSEhteHEqQ29FcWc4MWB8N01mWFg9WSt0YWhGIWZ1e088ZFh4VDs7JE5Zbz8kdVdQNSMrOF5tJEFEamo2Jk1RNmRCUUxKQT1+KT14OSVAOThhOFRNQ1hDYTFaQ3dnbXdJLURueDYkfGx2US0hYA=='.encode()).decode()))))
```


# Usage:
1. Run the Stealthify V2 script.
2. Enter the path to the Python file you want to obfuscate.
4. Specify the number of obfuscation layers to apply.
5. Choose if you want to add junk code.
6. Choose if you want to use a base64 encoding layer.
7. The obfuscated code will be saved to a new file with "_obf" appended to the original filename.

Please note that while obfuscation can provide a basic level of code protection, it does not guarantee absolute security.
attackers may still attempt to reverse engineer the code given time and expertise.

# Requirements
Python 3.x

# Licence
Stealthify V2 is released under the MIT License.
