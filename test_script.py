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
    #pattern3 is a regex to find the links inside the HTML code
    pattern3= r"<a[^>]+href=[\"\']([^\"\']+)[\"\'][^>]*>"
    #pattern4 is a regex to find the domain of the URL that starts with www.
    pattern4= r"^https?\:\/\/www\.([A-Za-z0-9\-]+(?:\.[a-zA-Z]{2,}){1,})$"
    domain = re.findall(pattern1, url)[0]
    domain2 = re.findall(pattern4, url)[0]
    protocol = re.findall(pattern2, url)[0]

    #Reading from the subdomains_dictionary.bat the subdomains to test
    file = open("subdomains_dictionary.bat")
    content = file.read()
    test_subdomains = content.splitlines()

    #Cleaning the string by removing everything not alphanumerical such as white spaces and special characters
    test_subdomains= [re.sub(r'[^A-Za-z0-9.-_]', '', s) for s in test_subdomains]
    test_subdomains= [re.sub(r'\s+', '', s) for s in test_subdomains]

    valid_subdomains=[]
    valid_links=[]

    #Looping until all subdomains are checked
    for subdomain in test_subdomains:
        domain_start = url.split("//")[-1].split("/")[0]
        if domain_start.startswith("www."):
            #If the domain starts with www.
            test_url = f"{protocol}://www.{subdomain}.{domain2}"
        else:
            #If the domain does not start with www.
            test_url = f"{protocol}://{subdomain}.{domain}"
        try:
            #Perform an HTTP GET request to the URL
            req= requests.get(test_url)
            if req.status_code >= 200 and req.status_code <= 299:
                #If valid, add the subdomain to the valid subdomains
                valid_subdomains.append(subdomain)
                print("Subdomain found. ", test_url)
                #Get the HTML code of the valid URL
                html_content=req.text 
                #Find all the links inside the HTML code
                test_links=re.findall(pattern3, html_content)
                #Loop to test all the links inside the HTML code
                for l in test_links:
                    if l.startswith("http"):
                        req2= requests.get(l)
                        if req2.status_code>=200 and req2.status_code<=299:
                            #If the link is valid add it to the valid links array
                            valid_links.append(l)
            else:
                print("Subdomain not found. ", test_url)
        except Exception as e:
            print("Subdomain not found. ", test_url)

    #Write the valid subdomains to the output file
    with open("subdomains_output.bat", "w") as f:
        f.write("\n".join(valid_subdomains))

    #Write the valid links to the output file
    with open("links_output.bat", "w") as f:
        f.write("\n".join(valid_links))
                
    file.close()

#DIRECTORIES & FILES
def directories_files(url):

    #pattern3 is a regex to find the links inside the HTML code
    pattern3= r"<a[^>]+href=[\"\']([^\"\']+)[\"\'][^>]*>"

    file = open("dirs_dictionary.bat")
    content = file.read()
    test_dirs_files = content.splitlines()

    #Cleaning the string by removing white spaces and the points at the beginning of the dir or file as well as the slashes
    test_dirs_files= [re.sub(r'^(\/|\.)|\/$', '', d) for d in test_dirs_files]
    test_dirs_files= [re.sub(r'\s+', '', d) for d in test_dirs_files]

    valid_dirs_files=[]
    valid_links=[]

    #Looping until all directories and files are checked
    for test in test_dirs_files:
        test_url = f"{url}/{test}"
        try:
            #Perform an HTTP GET request to the URL
            req=requests.get(test_url)
            #If valid, add the directory or file to the valid ones
            if req.status_code >= 200 and req.status_code <= 299:
                valid_dirs_files.append(test)
                print("Found. ", test_url)
                #Get the HTML code of the URL
                html_content=req.text 
                #Find all the links inside the HTML code
                test_links=re.findall(pattern3, html_content)
                    #Loop to test all the links inside the HTML code
                for l in test_links:
                    if l.startswith("http"):
                        req2= requests.get(l)
                        #If the link is valid, add it to the valid links array
                        if req2.status_code>=200 and req2.status_code<=299:
                            valid_links.append(l)
            else:
                print("Not found. ", test_url)
        except Exception as e:
            print("Not found. ", test_url)

    #Write the directories and files to the output file
    with open("dirs_files_output.bat", "w") as f:
        f.write("\n".join(valid_dirs_files))

    #Write the valid links to the output file
    with open("links_output.bat", "w") as f:
        f.write("\n".join(valid_links))
        
    file.close()

#Links in the HTML code of the given URL
def find_links(url):

    req=requests.get(url)
    #Get the HTML code of the page
    html_content = req.text

    #pattern is a regex to find the links inside the HTML code
    pattern = r"<a[^>]+href=[\"\']([^\"\']+)[\"\'][^>]*>"
    href_links = re.findall(pattern, html_content)

    valid_href_links=[]

    #Looping to check all the links
    for l in href_links:
        #If it is a link
        if l.startswith("http"):
            #Perform an HTTP GET request to the URL
            req= requests.get(l)
            #If the link is valid add it to the valid links array
            if req.status_code>=200 and req.status_code<=299:
                valid_href_links.append(l)
                print("Link found. ", l)
        else:
            print("Not a valid link. ", l)

    #Write the valid links to the output file
    with open("href_links.bat", "w") as file:
        file.write("\n".join(valid_href_links))

def main():
    if len(sys.argv) < 2:
        print("No link was provided")
        sys.exit(1)
    url=sys.argv[1]

    try:
        req = requests.get(url)
        if req.status_code >= 200 and req.status_code <= 299:
            subdomains(url)
            directories_files(url)
            find_links(url)
        else:
            print("Invalid link!")
    except Exception as e:
        print("An error occurred: ", e)

if __name__ == '__main__':
    main()