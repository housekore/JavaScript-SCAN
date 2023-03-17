import os
import re
import requests

# Define the path to the folder containing the text files and the file with the regular expressions
file_path = '/home/kali/JSFILES'
regex_file = '/home/kali/JSScanner/regex.txt'

# Creates a list of .txt files in the specified folder
txt_files = [f for f in os.listdir(file_path) if f.endswith('.txt')]

# Sorts the list in alphabetical order
txt_files.sort()

# Prints a menu with the list of .txt files
print("Choose a .txt file to search for links:")
for i, txt_file in enumerate(txt_files):
    print(f"{i+1}. {txt_file}")

# Requests the user to choose a file
while True:
    try:
        choice = int(input("> "))
        if choice in range(1, len(txt_files)+1):
            txt_file = txt_files[choice-1]
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid option. Please try again.")

# Reads the links from the selected file
with open(os.path.join(file_path, txt_file)) as f:
    links = f.read()

# Creates a list of links from the content of the file
link_list = re.findall(r'(https?://\S+)', links)

# Reads the regular expressions from the regex.txt file and creates a list
with open(os.path.join(file_path, regex_file)) as f:
    regex_list = f.read().splitlines()

# Defines the maximum number of connection attempts per link
max_attempts = 3

# Creates the results file
results_file = f"results-{txt_file}"
with open(os.path.join(file_path, results_file), 'w') as f:
    f.write("RESULTS FOUND:\n\n")

# For each link in the list, attempts the connection and searches for the regular expressions
for link in link_list:
    attempts = 0
    while attempts < max_attempts:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                # Searches for the regular expressions in the response content
                for regex in regex_list:
                    result = re.search(regex, response.text)
                    if result:
                        # Displays the message in purple and saves it to the results file
                        message = f"RESULT FOUND: {result.group()} in {link}\n"
                        with open(os.path.join(file_path, results_file), 'a') as f:
                            f.write(message)
                        print(f"\033[35m{message}\033[0m")
            else:
                print(f"Error {response.status_code} while connecting to {link}")
            break
        except requests.exceptions.RequestException as e:
            attempts += 1
            if attempts >= max_attempts:
                print(f"Connection error in {link}: {e}")
                break

print(f"\nResults saved in {results_file}.")
