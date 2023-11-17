import os

def replace_string_in_filenames(directory, old_string, new_string):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the current item is a file
        if os.path.isfile(file_path):
            new_filename = filename.replace(old_string, new_string)
            new_file_path = os.path.join(directory, new_filename)
            
            # Check if the new file path already exists
            if not os.path.exists(new_file_path):
                os.rename(file_path, new_file_path)

# Provide the directory path where you want to rename the files
directory_path = 'D:\RansomwareTraffic\pcaps'
# Specify the string you want to replace in the filenames
old_string = '.pcap.pcap'
# Specify the new string to replace the old string
new_string = '.pcap'
replace_string_in_filenames(directory_path, old_string, new_string)
