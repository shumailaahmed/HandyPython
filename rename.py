
import os

def remove_string_from_filenames(directory, string_to_remove):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the current item is a file
        if os.path.isfile(file_path):
            new_filename = filename.replace(string_to_remove, "")
            new_file_path = os.path.join(directory, new_filename)
            
            # Check if the new file path already exists
            if not os.path.exists(new_file_path):
                os.rename(file_path, new_file_path)

# Provide the directory path where you want to rename the files
directory_path = 'D:\RansomwareTraffic\pcaps'
# Specify the string you want to remove from the filenames
string_to_remove = 'pcap'
remove_string_from_filenames(directory_path, string_to_remove)
