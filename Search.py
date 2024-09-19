import os
import re

def search_in_directory(directory, pattern):
    matches = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.py', '.js', '.java', '.c', '.cpp', '.h')):  # Add your file types
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    if re.search(pattern, content):
                        matches.append(file_path)
    return matches

def search_data_type(directory, data_type):
    pattern = rf'\b{data_type}\b'  # Matches the data type exactly
    return search_in_directory(directory, pattern)

def search_function_implementation(directory, function_name):
    pattern = rf'\bdef {function_name}\b|\b{function_name}\s*\('  # Matches function definition or call
    return search_in_directory(directory, pattern)

# Example usage
repo_directory = '/path/to/your/repo'
data_type_results = search_data_type(repo_directory, 'DataType3')
function_results = search_function_implementation(repo_directory, 'myFunction')

print("Data Type Results:")
for result in data_type_results:
    print(result)

print("\nFunction Implementation Results:")
for result in function_results:
    print(result)
