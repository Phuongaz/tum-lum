import requests

def analyze_http_headers(url):
    try:
        response = requests.head(url)
        headers = response.headers

        print("HTTP Headers:")
        for header, value in headers.items():
            print(f"{header}: {value}")
    except requests.exceptions.RequestException as e:
        print("Error occurred:", str(e))

url = input("Enter the URL to analyze: ")
analyze_http_headers(url)