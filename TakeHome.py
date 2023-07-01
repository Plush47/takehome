import requests
import mimetypes
import pickle

# GitHub repository information
owner = 'Plush47'
repo = 'takehome'
base_directory = 'takehome'
index_file = 'index_file.pkl'

# GitHub API endpoint to retrieve file contents
api_url = f'https://api.github.com/repos/Plush47/takehome/'

def create_index(base_directory, index_file):
    index = []
    response = requests.get(api_url + base_directory)
    if response.status_code == 200:
        files = response.json()
        for file in files:
            file_name = file['name']
            file_size = file['size']
            content_type, _ = mimetypes.guess_type(file_name)
            if content_type is None:
                content_type = 'Unknown'
            
            file_data = {
                'Name': file_name,
                'Size': file_size,
                'Content Type': content_type,
                'URL': file['download_url']
            }
            index.append(file_data)

    with open(index_file, 'wb') as f:
        pickle.dump(index, f)

def search_index(index_file, query):
    with open(index_file, 'rb') as f:
        index = pickle.load(f)

    results = []
    for file_data in index:
        file_name = file_data['Name']
        content_type = file_data['Content Type']
        if query.lower() in file_name.lower() or query.lower() in content_type.lower():
            results.append(file_data)

    return results

# Create the index file
create_index(base_directory, index_file)

# Example search
query = 'linear'
results = search_index(index_file, query)
if len(results) > 0:
    print(f"Found {len(results)} result(s) for '{query}':")
    for result in results:
        print(f"Name: {result['Name']}")
        print(f"Size: {result['Size']} bytes")
        print(f"Content Type: {result['Content Type']}")
        print(f"URL: {result['URL']}")
        print()
else:
    print(f"No results found for '{query}'.")
