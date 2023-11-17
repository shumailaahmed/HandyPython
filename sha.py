import hashlib
import os

def find_files_with_same_sha(directory):
    file_hash_dict = {}

    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Calculate the SHA hash for the current file
            sha_hash = hashlib.sha256()
            with open(file_path, 'rb') as file:
                while True:
                    data = file.read(4096)
                    if not data:
                        break
                    sha_hash.update(data)

            file_hash = sha_hash.hexdigest()

            # Add the file to the dictionary using the hash as the key
            if file_hash in file_hash_dict:
                file_hash_dict[file_hash].append(file_path)
            else:
                file_hash_dict[file_hash] = [file_path]

    # Print files with the same hash
    for files_list in file_hash_dict.values():
        if len(files_list) > 1:
            print("Files with the same SHA:")
            for file_path in files_list:
                print(file_path)
            print("-------------------------")

# Provide the directory path to search for files with the same SHA
directory_path = '.'
find_files_with_same_sha(directory_path)
