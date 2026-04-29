import requests

def check_headers(url):
    print("[*] Checking security headers...")

    result = {}

    try:
        r = requests.get(url, timeout=5)
        h = r.headers

        checks = {
            "CSP": "Content-Security-Policy",
            "X-Frame": "X-Frame-Options",
            "HSTS": "Strict-Transport-Security",
            "XSS": "X-XSS-Protection"
        }

        for k, v in checks.items():
            result[k] = v in h
            print(f"{'[+] ' if result[k] else '[-] '} {k}")

    except Exception as e:
        print("Header error:", e)

    return result