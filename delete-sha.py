import hashlib
import os

def delete_files_with_same_sha(directory):
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
            print(file_hash)

            # Check if the hash already exists in the dictionary
            if file_hash in file_hash_dict:
                # Delete the file with the same hash
                os.remove(file_path)
            else:
                # Add the hash to the dictionary
                file_hash_dict[file_hash] = file_path

# Provide the directory path to search for files with the same SHA
directory_path = '.'
delete_files_with_same_sha(directory_path)
