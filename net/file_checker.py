import hashlib

def calculate_file_hash(file_path):
    hash_algorithm = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_algorithm.update(chunk)
    return hash_algorithm.hexdigest()

def verify_file_integrity(file_path, expected_hash):
    calculated_hash = calculate_file_hash(file_path)
    if calculated_hash == expected_hash:
        print("File integrity verified: The calculated hash matches the expected hash.")
    else:
        print("File integrity verification failed: The calculated hash does not match the expected hash.")

file_path = input("Enter the path of the file to verify: ")
expected_hash = input("Enter the expected hash: ")
verify_file_integrity(file_path, expected_hash)