# Assignment 03
# Task: Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
# Author: Sarah Hastings
# References: 
# https://www.w3schools.com/python/ref_requests_get.asp
# https://www.w3schools.com/python/python_json.asp
# https://nanonets.com/blog/web-scraping-with-python-tutorial/
# https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series
# https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series/resource/d4948877-3566-42c4-9a71-18dbe3d6d09e

# Import libraries to work with HTTP requests & json
import requests
import json

# Function to down and save dataset
def download_and_save_dataset(url, output_file):
    # Send a get request to dataset url
    response = requests.get(url)
    # Add a check to see if request was successful (status code 200)
    if response.status_code == 200:
        # Save dataset as a json file
        with open(output_file, "w") as file:
            file.write(response.text)
        # Print messages for clarify    
        print(f"Dataset saved to {output_file}")
    else:
        print(f"Failed to retrieve the dataset. Status code: {response.status_code}")

# Enter requested dataset url here
url = 'https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series/resource/d4948877-3566-42c4-9a71-18dbe3d6d09e'
# Call the function, specify output filename
download_and_save_dataset(url, "cso.json")