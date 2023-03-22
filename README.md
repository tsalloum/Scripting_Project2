# Project2- Ethical Hacking & Website Exploitation
---------------------------------------------
## Introduction
---------------------------------------------
This Project consists of creating a Python script that can be run on a website to discover subdomains, directories and files.
The script will take a user-provided URL as input and use brute force techniques to discover subdomains, directories and files associated 
with the target website. The script will use Python libraries such as Requests to interact with the website's server and analyze the server's responses.

* To check the valid subdomains, an input file will be used containing possible subdomains that will be checked by brute force. The URLs to be checked are
the concatination of the subdomain and the domain. Therefore a "get" request will be sent to each URL to check its validity.
* To check the valid directories and files, an input file will be used containing possible directories and files names that will be checked by brute force. 
The URLs to be checked are the concatination of the input URL and the directory or file name. Also a "get" request will be sent to each URL to check its validity.
