# Project2- Ethical Hacking & Website Exploitation
---------------------------------------------
## Introduction
---------------------------------------------
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
--------------------------------------------
This script can be executed by running on the terminal the following command:

Use the targeted website's URL instead of "https://domain.com"
The input text files used in this script are "subdomains_dictionary.bat" for subdomains and "dirs_dictionary.bat" for both directories and files. 
