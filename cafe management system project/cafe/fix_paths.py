import os
import glob

files = glob.glob('*.py')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace various absolute paths with relative paths
    content = content.replace('images/', 'images/')
    content = content.replace('C:\\\\xampp\\\\htdocs\\\\cafe\\\\images\\\\', 'images/')
    content = content.replace('images/', 'images/')
    content = content.replace('C:\\xampp\\htdocs\\cafe\\images', 'images/')
    content = content.replace('images/', 'images/')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Replaced all hardcoded paths")
