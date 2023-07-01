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


    return index


def search_files(index, keyword):
    results = []
    for file_name, file_data in index.items():
        if keyword.lower() in file_name.lower():
            results.append(file_name)

    return results

base_dir = '/Users/antho/Documents/takehome/test_data'
index = generate_index(base_dir)

search_keyword = input("Enter a keyword to search for files: ")
search_results = search_files(index, search_keyword)

print("Search Results:")
if search_results:
    for file_name in search_results:
        print(file_name)
else:
    print("No files found matching the search criteria.")