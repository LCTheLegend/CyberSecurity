import base64

# Base64 encoded string
encoded_str = "aHR0cHM6Ly9kaXNjb3JkLmdnL05rRVNQUU1lWjM="

# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_str) 
decoded_str = decoded_bytes.decode("utf-8")

print("Decoded String:", decoded_str)
