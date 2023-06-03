import ast, random, string, base64, os
import re
from colorama import Fore as f

os.system("cls")

class Obfuscator(ast.NodeTransformer):
    def __init__(self):
        self.mapping = {}
        self.function_parameters = {}

    def obfuscate_name(self, name):
        if name not in self.mapping:
            new_name = ''.join(random.choices(string.ascii_letters, k=15))
            self.mapping[name] = new_name
        return self.mapping[name]

    def visit_FunctionDef(self, node):
        for arg in node.args.args:
            obfuscated_name = self.obfuscate_name(arg.arg)
            self.function_parameters[arg.arg] = obfuscated_name
            arg.arg = obfuscated_name
        for stmt in node.body:
            if isinstance(stmt, ast.Assign):
                for target in ast.walk(stmt.targets[0]):
                    if isinstance(target, ast.Name):
                        target.id = self.obfuscate_name(target.id)
            elif isinstance(stmt, ast.If):
                for substmt in stmt.body:
                    if isinstance(substmt, ast.Assign):
                        for target in ast.walk(substmt.targets[0]):
                            if isinstance(target, ast.Name):
                                target.id = self.obfuscate_name(target.id)
        return self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            node.id = self.obfuscate_name(node.id)
        elif isinstance(node.ctx, ast.Load):
            if node.id in self.mapping:
                node.id = self.mapping[node.id]
        return node

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in self.function_parameters:
            node.func.id = self.function_parameters[node.func.id]
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id in self.mapping:
            node.func.value.id = self.mapping[node.func.value.id]
        for i, arg in enumerate(node.args):
            if isinstance(arg, ast.Name) and arg.id in self.mapping:
                node.args[i].id = self.mapping[arg.id]
        return self.generic_visit(node)

    def visit_Return(self, node):
        if isinstance(node.value, ast.Name) and node.value.id in self.mapping:
            node.value.id = self.mapping[node.value.id]
        return self.generic_visit(node)

def obfuscate_code(code, iterations):
    tree = ast.parse(code)
    obfuscator = Obfuscator()
    for _ in range(iterations):
        obfuscator.visit(tree)
    obfuscated_code = ast.unparse(tree)
    return obfuscated_code

def base64_encode(data):
    return base64.b64encode(data.encode()).decode()

def Add_Dead_code(code):
    obfuscated_lines = code.split('\n')
    for i in range(2, len(obfuscated_lines), 3):
        junk_code = ''.join(random.choices(string.ascii_letters, k=35))
        junk_line = f"""
        # {junk_code}
        """
        obfuscated_lines.insert(i, junk_line)
    return '\n'.join(obfuscated_lines)

print
(f.RED + """
███████╗████████╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗██╗███████╗██╗   ██╗    ██╗   ██╗██████╗ 
██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║██║██╔════╝╚██╗ ██╔╝    ██║   ██║╚════██╗
███████╗   ██║   █████╗  ███████║██║     ██║   ███████║██║█████╗   ╚████╔╝     ██║   ██║ █████╔╝
╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██║   ██╔══██║██║██╔══╝    ╚██╔╝      ╚██╗ ██╔╝██╔═══╝ 
███████║   ██║   ███████╗██║  ██║███████╗██║   ██║  ██║██║██║        ██║        ╚████╔╝ ███████╗
╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝╚═╝        ╚═╝         ╚═══╝  ╚══════╝
- By Sirmilann [SR] -
""")
file_path = input(f.RED + "File: ")
iterations = int(input(f.RED + "Number of Obfuscation Layers: "))
with open(file_path, 'r', encoding='utf-8') as file:
    code = file.read()
obfuscated_code = obfuscate_code(code, iterations)
add_junk = input("Add Dead Code? [yes/no]: ")
obfuscate_again = input(f.RED + "Use base64? [yes/no]: ")
if obfuscate_again.lower() == 'yes':
    obfuscated_code = base64_encode(obfuscated_code)
    obfuscated_code = f"exec(__import__('base64').b64decode('{obfuscated_code}').decode())"
if add_junk.lower() == 'yes':
    obfuscated_code = Add_Dead_code(obfuscated_code)
file_name = file_path.rsplit('.', 1)[0]
extension = file_path.rsplit('.', 1)[1]
obfuscated_file_path = file_name + "_obf." + extension
with open(obfuscated_file_path, 'w') as file:
    file.write("# Obfuscated With Stealthify V2 By Sirmilann\n" + obfuscated_code)
print(f.RED + "Code Saved To:", obfuscated_file_path)
