import os
import mimetypes
import json

def generate_index(base_dir):
    index = {}

    for root, dirs, files in os.walk(base_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            size = os.path.getsize(file_path) // 1024
            size = f"{size:.2f} KB" 
            content_type, _ = mimetypes.guess_type(file_path)
            index[file_name] = {
                'size': size,
                'content_type': content_type
                
            }

    index_file_path = os.path.join(base_dir, 'index.json')
    with open(index_file_path, 'w') as index_file:
        json.dump(index, index_file, indent=4)


if __name__ == '__main__':
    base_directory = '/Users/antho/Documents/takehome/test_data'
    generate_index(base_directory)
