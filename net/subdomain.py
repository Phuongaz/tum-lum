import dns.resolver
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def enumerate_subdomains(domain):
    subdomains = []

    common_subdomains = ["www", "mail", "ftp", "blog", "api", "dev", "admin", "login", "test"]
    for subdomain in common_subdomains:
        full_domain = subdomain + "." + domain
        try:
            answers = dns.resolver.resolve(full_domain, "A")
            if answers.response.rcode == dns.rcode.NOERROR:
                subdomains.append(full_domain)
        except dns.resolver.NXDOMAIN:
            pass

    url = "http://www." + domain
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            anchors = soup.find_all("a")
            for anchor in anchors:
                href = anchor.get("href")
                parsed_url = urlparse(href)
                if parsed_url.netloc:
                    subdomain = parsed_url.netloc.split(":")[0]
                    subdomains.append(subdomain)
    except requests.RequestException:
        pass

    return subdomains

domain = input("Enter the domain to enumerate subdomains: ")
subdomains = enumerate_subdomains(domain)
print("Subdomains ({}):".format(len(subdomains)) if len(subdomains) > 0 else "No subdomains found")
for subdomain in subdomains:
    print(subdomain)