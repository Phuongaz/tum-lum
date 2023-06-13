import hashlib

def calculate_hash(file_path, hash_algorithm):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            hash_object = hashlib.new(hash_algorithm)
            hash_object.update(data)
            return hash_object.hexdigest()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied to access file '{file_path}'.")
    except Exception as e:
        print(f"Error calculating hash: {str(e)}")

file_path = 'C:\\Users\\user\\Desktop\\test.txt'
hash_algorithm = 'sha256'
hash_value = calculate_hash(file_path, hash_algorithm)
print(f"{hash_algorithm.upper()} Hash: {hash_value}")