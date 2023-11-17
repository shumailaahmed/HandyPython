import os

def remove_double_extension(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if the current item is a file
        if os.path.isfile(file_path):
            new_filename = filename.replace(".pcap.pcap", ".pcap")
            new_file_path = os.path.join(directory, new_filename)

            # Check if the new file path already exists
            if not os.path.exists(new_file_path):
                os.rename(file_path, new_file_path)

# Provide the directory path where you want to rename the files
directory_path = '.'
remove_double_extension(directory_path)
