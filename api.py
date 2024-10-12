import base64
import sys
import subprocess
operating = sys.platform
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
            decoded_base64 = base64.b64decode(binary_base64).decode(ENCODING)
            binary_message = bin(int(decoded_base64, 16))[2:].zfill(len(decoded_base64) * 4)
            original_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
            return original_message
        return None
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
import os
import json

class Backup:
    def create(source_path, backup_file):
        if not os.path.exists(source_path):
            print(f"Source path {source_path} does not exist.")
            return
        backup_data = {}
        for root, _, files in os.walk(source_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding=ENCODING) as f:
                        content = f.read()
                    encrypted_content = Cryptography.encode(content)
                    backup_data[file_path] = encrypted_content
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f)
        print(f"Backup created successfully at {backup_file}.")
    def restore(backup_file, restore_path):
        if not os.path.exists(backup_file):
            print(f"Backup file {backup_file} does not exist.")
            return
        with open(backup_file, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
        os.makedirs(restore_path, exist_ok=True)
        for file_path, encrypted_content in backup_data.items():
            try:
                decrypted_content = Cryptography.decode(encrypted_content)
                relative_path = os.path.relpath(file_path, start=os.path.dirname(backup_file))
                restored_file_path = os.path.join(restore_path, relative_path)
                os.makedirs(os.path.dirname(restored_file_path), exist_ok=True)
                with open(restored_file_path, 'w', encoding=ENCODING) as f:
                    f.write(decrypted_content)
                print(f"Restored {restored_file_path}.")
            except Exception as e:
                print(f"Error restoring {file_path}: {e}")
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
