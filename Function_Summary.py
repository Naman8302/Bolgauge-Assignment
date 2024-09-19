import ast
import os

class FunctionAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.functions = {}

    def visit_FunctionDef(self, node):
        # Store function name and its dependencies
        self.functions[node.name] = {
            'args': [arg.arg for arg in node.args.args],
            'body': ast.get_source_segment(open(node.lineno).read(), node),
            'dependencies': []
        }
        self.generic_visit(node)

    def visit_Call(self, node):
        # Record function calls
        if isinstance(node.func, ast.Name):
            function_name = node.func.id
            if function_name in self.functions:
                self.functions[function_name]['dependencies'].append(node.lineno)

# Analyze Python files
def analyze_repository(path):
    analyzer = FunctionAnalyzer()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    tree = ast.parse(f.read())
                    analyzer.visit(tree)
    return analyzer.functions

functions_info = analyze_repository('path_to_tensorflow_repo')
