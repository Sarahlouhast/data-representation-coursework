# Assignment 04 - assignment04-github.py
# Task: Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with your name. The program should then commit those changes and push the file back to the repository. (https://vlegalwaymayo.atu.ie/mod/page/view.php?id=775932)
# Author: Sarah Hastings


# Import libraries and config file with api keys for access to github
from github import Github
import requests
import re # case-insensitive replacement
from config import config as cfg

# Function to update a file in a GitHub repository
def update_github_file(repo_name, file_name, old_text, new_text, github_api_key):
    try:
        # Authenticate with GitHub using the provided API key
        repo = Github(github_api_key).get_repo(repo_name)

        # Get information about the file to be updated
        file_info = repo.get_contents(file_name)

        # Make a HTTP request to download the file content
        content_of_file = requests.get(file_info.download_url).text
        
        # Replace instances of the old text with the new text. Use regular expressions (re) for case-insensitive replacement
        new_contents = re.sub(re.escape(old_text), new_text, content_of_file, flags=re.IGNORECASE)

        # Note if you do want to replace instances of the old text with the new text without case-sensitivity use the below
        #new_contents = content_of_file.replace(old_text, new_text)

        # Check if any changes were made
        if content_of_file == new_contents:
            print(f"No changes to make in {file_info.path}")
            return

        # Commit the changes to the file in the repository
        commit_message = f"Replace '{old_text}' with '{new_text}'"
        repo.update_file(file_info.path, commit_message, new_contents, file_info.sha)

        # Print a message indicating the success of the operation
        print(f"Changes committed and pushed to {file_info.path}")

    # Handle errors
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"An error occurred: {e}")

# Example usage
repo_name = "Sarahlouhast/aprivateone"
file_name = "test.txt"
old_name = "Andrew"
new_name = "Sarah"
api_key = cfg["githubkey"]

# Call the function with the specified parameters
update_github_file(repo_name, file_name, old_name, new_name, api_key)
