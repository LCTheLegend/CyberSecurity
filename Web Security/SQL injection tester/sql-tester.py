import requests

# List of common SQL injection payloads
with open("payloads.txt", "r") as f:
    payloads = [line.strip() for line in f]

def test_sqli(url, param):
    """Tests a URL parameter for SQL injection vulnerability"""
    vulnerable = False
    for payload in payloads:
        # Construct a test URL with the SQL payload
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)
        
        # Check for common SQL error messages in the response
        errors = ["sql syntax", "mysql_fetch", "ODBC", "SQLException"]
        if any(error.lower() in response.text.lower() for error in errors):
            print(f"[!] Potential SQL Injection found with payload: {payload}")
            vulnerable = True

    if not vulnerable:
        print("[+] No SQL injection vulnerabilities detected.")

# Example usage (replace with a test URL you control)
test_url = "http://localhost/sqli-test/index.php"  # Change this to your test site
param_name = "id"
test_sqli(test_url, param_name)
