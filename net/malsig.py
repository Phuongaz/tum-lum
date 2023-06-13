import os
import hashlib

def calculate_file_hash(file_path):
    hash_algo = hashlib.md5() 
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def scan_directory(directory_path, signature_hashes):
    infected_files = []

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)

            if file_hash in signature_hashes:
                infected_files.append(file_path)

    return infected_files

def main():
    signature_hashes = {
        "4e62a82ff73214a8f96eeb4b73772e06",
        "a0327d81e68ea18a050fde1269e649d3" 
    }

    directory_path = "C:\\Users\\user\\Desktop\\malware"

    infected_files = scan_directory(directory_path, signature_hashes)
    
    if infected_files:
        print("Infected files:")
        for file_path in infected_files:
            print(file_path)
    else:
        print("No infected files found.")

if __name__ == "__main__":
    main()