import random
import string

def generate_xss_payload():
    payload = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    xss_payload = f"<script>alert('{payload}')</script>"
    return xss_payload

def main():
    xss_payload = generate_xss_payload()
    print("XSS Payload:")
    print(xss_payload)

if __name__ == "__main__":
    main()