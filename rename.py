import os

def rename_images(folder_path, new_name_prefix, start_number=1):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only the image files
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Counter for renaming
    count = start_number
    
    # Iterate through each image file
    for image_file in image_files:
        # Generate the new file name
        new_file_name = f"{new_name_prefix} ({count}).jpg"  # Change the extension if needed
        
        # Construct the full paths for the old and new file names
        old_path = os.path.join(folder_path, image_file)
        new_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed '{image_file}' to '{new_file_name}'")
        
        # Increment the counter
        count += 1

# Example usage
folder_path = 'Bacterial leaf blight/'
new_name_prefix = 'BLB'
start_number = 101
rename_images(folder_path, new_name_prefix, start_number)
