import requests
import json

email = "rodrigo.oh@libertexgroup.com"
key = "4b9c0154d8a8251339150ffb9758d4382d1a7"
zone_id = "20421959a873f12524515b2f317837d1"
ip_address = "69.94.113.21"
package_id = ""

url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules"

headers = {
    "X-Auth-Email": email,
    "X-Auth-Key": key,
    "Content-Type": "application/json"
}

params = {
    "per_page": 60
}

response2 = requests.request("GET", f"https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules", headers= headers, params=params)

data = json.loads(response2.text)

print(response2.text)

if data["success"] == False:
    print("API request failed with error:", data["errors"])
else:
    rules = data["result"]
    for rule in rules:
        if ip_address in rule["filter"]["expression"]:
            print(f"{rule['description']}")
            