#!/usr/bin/env python3

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import time
import os
import urllib.request
import ssl
import argparse

class Sap:
    def __init__(self, url, download_dir):
        self.url = url
        self.download_dir = download_dir
        self.domain = "https://opig.stats.ox.ac.uk"
        self.full_links = []

    def get_links(self):
        # Make a GET request to the URL
        r = requests.get(self.url)
        # Parse the content of the response with BeautifulSoup
        soup = BeautifulSoup(r.text, 'lxml')

        # Find all the <a> tags with the string "Structure (as PDB)" in the parsed HTML
        a_tags = soup.find_all('a', string='Summary file')

        # Iterate over each <a> tag for download
        for tag in a_tags:
            # Get the href attribute of the <a> tag
            file_link = tag.get('href')
            # Concatenate the domain and the file link to create the full download link
            full_link = self.domain + file_link
            # Add the full download link to the list
            self.full_links.append(full_link)

    def download_files(self):
        # If the download directory does not exist, create it
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        # Iterate over each download link
        for link in self.full_links:
            # Extract the file name from the download link by removing "?scheme=chothia"
            file_name = link.split("/")[-2] + '_chothia.tsv'
            # Create the full file path
            file_name = os.path.join(self.download_dir, file_name)

            # Try to download the file
            try:
                urllib.request.urlretrieve(link, file_name)
                # If successful, print a success message
                print(f"Successfully downloaded file to {file_name}")
            # If there's an error, print an error message
            except Exception as e:
                print(f"Failed to download file from {link}. Error: {str(e)}")

        # Print location of files
        print(f"Files have been downloaded to: {self.download_dir}")

def get_args():
    # Define an argument parser
    parser = argparse.ArgumentParser()
    # Add argument for the URL
    parser.add_argument('-getall', type=str, help='The URL from which to scrape protein structures')
    # Add optional argument for disabling SSL verification warnings
    parser.add_argument('-d', action='store_true', help='Disable SSL verification warnings')
    # Add optional argument for specifying the download directory
    parser.add_argument('downloaddir', nargs='?', default=os.getcwd(), help='Directory to download files to')
    # Parse the arguments
    args = parser.parse_args()

    return args

def main():
    # Get command line arguments
    args = get_args()

    # If -d argument is present, disable SSL verification warnings
    if args.d:
        ssl._create_default_https_context = ssl._create_unverified_context

    # Create Sap object
    sap = Sap(args.getall, args.downloaddir)
    # Get download links from URL
    sap.get_links()
    # Download files to specified directory
    sap.download_files()

# This code runs if the script is run directly, not if it is imported as a module
if __name__ == "__main__":
    main()

