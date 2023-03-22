# Project2- Ethical Hacking & Website Exploitation

## Introduction

This Project consists of creating a Python script that can be run on a website to discover subdomains, directories and files.
The script will take a user-provided URL as input and use brute force techniques to discover subdomains, directories and files associated 
with the target website. The script will use Python libraries such as Requests to interact with the website's server and analyze the server's responses.

* To check the valid subdomains, an input file will be used containing possible subdomains that will be checked using brute force technique. The URLs to be checked are
the concatination of the subdomain and the domain. A "get" request will be sent to each URL to check its validity. Valid subdomains will be written to an output file.
* To check the valid directories and files, an input file will be used containing possible directories and files names that will be checked by brute force. 
The URLs to be checked are the concatination of the input URL and the directory or file name. Also a "get" request will be sent to each URL to check its validity. Valid directories and files will be written to an output file.
* The HTML code of the URL, valid subdomains, directories and files will be  extracted and scanned to retreive all hidden links found in thehref attribute of the tags, that could potentially lead to pages with vulnerabilities. A "get" request will be sent to each link found to check its availability. Valid links will be written to output file.
* The script will log all discovered subdomains, directories, and files in a structured format and provide an output that can be easily interpreted by the user. The user can then use this information to identify potential vulnerabilities and strengthen the website's security posture.

## Execution

This script can be executed by running on the terminal the following command:
```
python test_script.py https://domain.com
```
Use the targeted website's URL instead of "https://domain.com".   

The input text files used in this script are "subdomains_dictionary.bat" for subdomains and "dirs_dictionary.bat" for both directories and files. 

## Steps
This script includes 4 methods involved in checking the URLs, subdomains, directories and files.
```
def subdomains(url):
```
Function that takes a URL as input and attempts to discover subdomains and valid links associated with the given URL. The method uses a combination of regular expressions and HTTP requests to achieve its purpose. The method then iterates through the possible subdomains and constructs a new URL by concatenating the original domain name with the subdomain being tested. The method sends an HTTP GET request to the new URL and checks if the request is successful. If it is, the method adds the subdomain to the list of valid subdomains and prints a message indicating that the subdomain was found. The method also extracts all the links present in the HTML code of the valid URL and checks if they are valid links by sending HTTP GET requests to each link. If the link is valid, it is added to the list of valid links. And finally the retreived valid href links and subdomains are written to output files.

---------------------------------------------------------------------
```
def directories_files(url):
```
This function takes a URL as an input and tries to find directories, files, and links that are associated with the provided URL. It employs regular expressions and HTTP requests to perform its task. The function then goes through the possible files and directories names and forms a new URL by combining the original domain name with the directory or file name obtained from the input file. It sends an HTTP GET request to the newly formed URL and verifies if the request was successful. If it is, the function adds the directory or file to the list of valid directories and files. The function also extracts all the links present in the HTML code of the valid URLs and confirms their validity by sending HTTP GET requests to each of them. If the link is valid, it is appended to the list of valid links. Finally, the retrieved valid href links, directories, and files are saved in output files.

----------------------------------------------------------------------
```
def find_links(url):
```
