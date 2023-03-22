import requests
import re
import sys
import ssl

#SUBDOMAINS
def subdomains(url):

    #pattern1 is a regex to find the domain of the URL
    pattern1 = r"^https?\:\/\/([A-Za-z0-9\-]+(?:\.[a-zA-Z]{2,}){1,})$"
    #pattern2 is a regex to find the protocol of the URL
    pattern2 = r"https?"
    #pattern3 is a regex to find the links inside the html file
    pattern3= r"<a[^>]+href=[\"|\']([^\"\']+)[\"|\'][^>]*>"
    domain = re.findall(pattern1, url)[0]
    protocol = re.findall(pattern2, url)[0]

    #Reading from the subdomains_dictionary.bat text file the subdomains to test
    file = open("subdomains_dictionary.bat")
    content = file.read()
    test_subdomains = content.splitlines()

    #Cleaning the string by removing everything not alphanumerical such as white spaces and special characters
    test_subdomains= [re.sub(r'[^A-Za-z0-9.-_]', '', subdomain) for subdomain in test_subdomains]

    valid_subdomains=[]
    valid_links=[]

    #Looping until all subdomains are checked
    for subdomain in test_subdomains:
        domain_start = url.split("//")[-1].split("/")[0]
        if domain_start.startswith("www."):
            #If the domain starts with www.
            test_url = f"{protocol}://www.{subdomain}.{domain}"
        else:
            #If the domain does not start with www.
            test_url = f"{protocol}://{subdomain}.{domain}"