import sys
import subprocess
operating = sys.platform
import os
import base64

ENCODING = 'utf-8'

class Cryptography:
    def encode(message):
        binary_message = ''.join(format(ord(char), '08b') for char in message)
        hex_message = hex(int(binary_message, 2))[2:]
        base64_message = base64.b64encode(bytes.fromhex(hex_message)).decode(ENCODING)
        binary_base64 = ''.join(format(ord(char), '08b') for char in base64_message)
        reversed_message = binary_base64[::-1]
        encrypted_message = f"s+{reversed_message}="
        return encrypted_message

    def decode(encrypted_message):
        if encrypted_message.startswith("s+") and encrypted_message.endswith("="):
            reversed_message = encrypted_message[2:-1][::-1]
            binary_base64 = ''.join(chr(int(reversed_message[i:i+8], 2)) for i in range(0, len(reversed_message), 8))
            decoded_base64 = base64.b64decode(binary_base64)
            binary_message = ''.join(format(byte, '08b') for byte in decoded_base64)
            original_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
            return original_message
        return None

import os

class Backup:
    def create(dir_path):
        """Creates a text file containing the directory structure and contents."""
        dir_path = os.path.abspath(dir_path)
        structure_file = os.path.join(os.getcwd(), 'directory_structure.txt')

        with open(structure_file, 'w', encoding='utf-8') as file:
            Backup._write_directory_structure(dir_path, file)
        
        print(f'Directory structure saved to {structure_file}')

    @staticmethod
    def _write_directory_structure(current_path, file, indent_level=0):
        """Recursive helper method to write the directory structure to a file."""
        indent = '    ' * indent_level  # Indentation for better readability
        for entry in os.listdir(current_path):
            entry_path = os.path.join(current_path, entry)
            relative_path = os.path.relpath(entry_path, os.getcwd())
            file.write(f"{indent}{relative_path}\n")  # Write the path relative to current working directory
            
            if os.path.isdir(entry_path):
                Backup._write_directory_structure(entry_path, file, indent_level + 1)
            elif os.path.isfile(entry_path):
                file.write(f"{indent}    CONTENT:\n")  # Indicate content starts
                with open(entry_path, 'r', encoding='utf-8') as subfile:
                    content = subfile.read()
                    file.write(f"{indent}    {content}\n")  # Write the file content

    def restore(structure_file):
        """Restores the directory structure and contents from the specified text file."""
        with open(structure_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        current_path = os.getcwd()
        i = 0
        while i < len(lines):
            stripped_line = lines[i].strip()
            if not stripped_line:
                i += 1
                continue

            indent_level = (len(lines[i]) - len(stripped_line)) // 4  # Calculate the indent level
            relative_path = stripped_line
            
            # Create the full path
            if indent_level == 0:
                current_path = os.path.join(os.getcwd(), relative_path)
                os.makedirs(current_path, exist_ok=True)  # Create the directory
            else:
                # For files, get the previous directory path
                parent_dir = os.path.dirname(current_path)
                file_path = os.path.join(parent_dir, relative_path)

                # Check if the next line is CONTENT
                if lines[i].startswith("    CONTENT:"):
                    content_lines = []
                    i += 1  # Move to the next line after CONTENT
                    while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
                        if lines[i].strip() and not lines[i].strip().startswith("CONTENT:"):  # Avoid "CONTENT:"
                            content_lines.append(lines[i].strip())
                        i += 1
                    
                    # Write content to the file
                    if content_lines:  # Only write if there is content
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write("\n".join(content_lines))
                    # Adjust index back since the outer loop will also increment i
                    continue
            
            i += 1  # Move to the next line if no CONTENT found

        print(f'Directory structure restored from {structure_file}')
class OSLinker:
    def system(command, output):
        try:
            executed = str(command)
            if executed == "clear":
                if operating in ("win32", "win64", "win86"):
                    return subprocess.run("cls", shell=True, text=bool(output))
                elif operating in ("linux", "darwin"):
                    return subprocess.run("clear", shell=True, text=bool(output))
                else:
                    print("==== - Invalid OS - ====")
                    raise OSError
            if executed == "ipconfig":
                if operating in ("win32", "win64", "win86"):
                    return subprocess.run("ipconfig", shell=True, text=bool(output))
                elif operating in ("linux", "darwin"):
                    return subprocess.run("ifconfig", shell=True, text=bool(output))
                else:
                    print("==== - Invalid OS - ====")
                    raise OSError
            if executed == "ls":
                if operating in ("win32", "win64", "win86"):
                    return subprocess.run("dir", shell=True, text=bool(output))
                elif operating in ("linux", "darwin"):
                    return subprocess.run("ls", shell=True, text=bool(output))
                else:
                    print("==== - Invalid OS - ====")
                    raise OSError
            if executed == "sl":
                if operating in ("win32", "win64", "win86"):
                    return subprocess.run("dir", shell=True, text=bool(output))
                elif operating in ("linux", "darwin"):
                    return subprocess.run("ls", shell=True, text=bool(output))
                else:
                    raise OSError("Invalid OS")
        except KeyboardInterrupt:
            print("Interrupted while executing a system command")
        except Exception as e:
            print(f"Error occured: {e}")
            return str(e)
class Utility:
    # Fix email verification function
    @staticmethod
    def verify_email(email):
        adresa = email
        if "@" in adresa and adresa.endswith((".com", ".net", ".ms", ".mail", ".ro")):
            print("Valid Address")
        else:
            print("Invalid Address")

    # Function to check if a number is negative
    @staticmethod
    def is_negative(numb):
        return numb < 0

    # Radix Sort function that returns the sorted array
    @staticmethod
    def radix_sort(arr):
        if not arr:  # Handle edge case for empty list
            return arr

        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n  # Output array to store sorted numbers
            count = [0] * 10  # Count array to store frequency of digits (0-9)

            # Store the count of occurrences for each digit in the numbers
            for i in range(n):
                index = (arr[i] // exp) % 10
                count[index] += 1

            # Update count[i] so that count[i] contains the actual position of this digit in output[]
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Build the output array by placing the elements in their correct position
            i = n - 1
            while i >= 0:
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                count[index] -= 1
                i -= 1

            # Copy the sorted elements back into the original array
            for i in range(n):
                arr[i] = output[i]

        max_num = max(arr)
        exp = 1  # Represents the digit place (ones, tens, hundreds, etc.)
        while max_num // exp > 0:
            counting_sort(arr, exp)  # Call the nested counting_sort function
            exp *= 10

        return arr  # Ensure the sorted array is returned

    # Function to find the closest value in a list to a given value
    @staticmethod
    def closest_in(listt, to):
        # Convert tuple to list if necessary
        if isinstance(listt, tuple):
            listt = list(listt)

        # Filter out non-numeric items and convert strings to integers if possible
        numeric_list = []
        for item in listt:
            if isinstance(item, (int, float)):
                numeric_list.append(item)
            elif isinstance(item, str):
                try:
                    numeric_list.append(int(item))
                except ValueError:
                    continue  # Skip items that cannot be converted to integers

        # Sort the list using radix_sort (only works for non-negative integers)
        sorted_list = Utility.radix_sort(numeric_list)

        # Find the closest value to 'to'
        to = int(to)
        closest_value = min(sorted_list, key=lambda x: abs(x - to))

        return closest_value
