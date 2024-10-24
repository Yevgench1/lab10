import os
os_name = os.name
print(f"Назва операційної системи: {os_name}")

current_directory_files = os.listdir()
print("\nСписок файлів поточного каталогу:")
for file in current_directory_files:
    print(file) 
    
txt_files = [file for file in current_directory_files if file.endswith(".txt")]
print("\nСписок файлів з розширенням '.txt':")
for file in txt_files:
    print(file)