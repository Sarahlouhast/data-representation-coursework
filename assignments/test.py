# Assignment 03
# Task - Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
#Save this assignment as "assignment03-cso.py"
'''
# 
# 
# Weekly task 2 
#Author: Sarah Hastings
#The program should prompt the user and read in two money amounts (in cent), 
#Add the two amounts
#Print out the answer in format with a euro sign and decimal point between the euro and cent of the amount 
#Reference: https://www.w3schools.com/python/python_numbers.asp 
           #https://www.w3schools.com/python/python_howto_add_two_numbers.asp 
           #https://stackabuse.com/format-number-as-currency-string-in-python/ 



import requests
import json

def download_and_save_dataset(dataset_url, output_filename):
    response = requests.get(dataset_url)
    
    if response.status_code == 200:
        with open(output_filename, "w") as file:
            file.write(response.text)
        print(f"Dataset saved to {output_filename}")
    else:
        print(f"Failed to retrieve the dataset. Status code: {response.status_code}")

def main():
    # Replace 'YOUR_DATASET_URL' with the actual URL of the dataset
    dataset_url = 'https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series/resource/d4948877-3566-42c4-9a71-18dbe3d6d09e'
    
    download_and_save_dataset(dataset_url, "cso.json")

if __name__ == "__main__":
    main()
