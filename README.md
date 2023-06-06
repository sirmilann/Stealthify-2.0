# Stealthify V2

Stealthify V2 is a lightweight code obfuscator for Python, designed to provide basic protection against casual reverse engineering of your source code.
It applies simple obfuscation techniques to make your code less readable and deter unauthorized access.

# Features:
- Basic Name Obfuscation: Stealthify V2 renames variables, functions, and parameters with randomly generated names to make the code less intuitive.
- The obfuscated code is enhanced with randomly generated lines of junk code, which are interspersed throughout the code to make it more difficult to analyze and understand.
- Limited AST Transformations: The obfuscator performs basic Abstract Syntax Tree (AST) transformations to modify the code structure and confuse potential attackers.
- Another Encoding layer: Adds another layer of Base64, base85, marshal and lzma Encoding and compression over the obfuscated code to make it slightly harder to understand.
- Multiple Obfuscation Layers: You can choose to apply multiple layers of obfuscation to the code to make it slightly harder to understand.
- Basic Anti-VM code to bypass Virtual Machine Environments.

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
import lzma, marshal, base64;exec(marshal.loads(lzma.decompress(base64.b85decode(base64.b64decode('e1dwNDhTXnhrOT1HTEBFMHN0V2E3NjFTTWJUOCRqOzAzX31pQ3E5V3VSTmQoT25rUktkdU1CP1NkNWtKS359QT1MeWxnT3ZrQWRYZWRCRl4kSCMyQ19tUEJJVmduRDNARCVPPTVfQ35mMTJKY2lzRV81QE0pNWh4Qkp4I0hWbyR6JWtoWnA7SjRHayNDOHRZN2BWJHxfcH0mLXlpSnslSkw3K0dOb0oxd2lYaCk5ZTZES2VzOFAzN0tyI1IqMFEpZGRENX07Ykd7TkNxTXFxMyYtYD5JLVpEWVpjKVNZVkFud2tlKSgjcWs/e3EoRGYoPipERVgqbUJucHBpbVo2SCRVSyhje15MTkFGK1hlVDhHVExQYFNmT1J9PDI3b1B1LVgoJWRke2EzUXVaczwkIUhsezYkQCZ9UztBPTVaUFV2SnZjUD81T1peVkZkeX4+dX5KZjIlPERTI3gzfCEtMDdaWnVjKTRRJWdePXBCMX4xdyprd25NaT5AJTJuWklSMTxgTWQ0XzQjajskazxtQntONWlNIyFMLUhvXjt5SCNDTS0wOXVgb0psOVd5anFaWmgrXkJSMjBiVihzfE9vQ216U2A1S0MrJis+Z2B0ZVlwMHtSSXtEfEU8WEc+RCFTc3ttWilNaDYoP2N8Zn1AeWxLYFdgP1NxOSQ+Pjs3eHRHUXVLTEt0SXhAenZtcHJeKWkwMDAwMDslMUFBdWJrP3wwMEVAfiFWM1RaSm0pblh2QllRbDBzc0kyMDBkY0Q='.encode()).decode()))))
```


# Usage:
1. Run the Stealthify V2 script.
2. Enter the path to the Python file you want to obfuscate.
4. Specify the number of obfuscation layers to apply.
5. Choose if you want to add junk code.
6. Choose if you want to use an extra encoding and compression layer.
7. Choose if you want to add anti vm code.
8. The obfuscated code will be saved to a new file with "_obf" appended to the original filename.

Please note that while obfuscation can provide a basic level of code protection, it does not guarantee absolute security.
attackers may still attempt to reverse engineer the code given time and expertise.

# Requirements
Python 3.x

# Licence
Stealthify V2 is released under the MIT License.
