import requests

def security_headers(url):
    response = requests.get(url)
    
    headers_to_check = [
        'Content-Security-Policy',
        'Strict-Transport-Security',
        'X-Frame-Options'
    ]

    headers_present = {header: False for header in headers_to_check}

    for header in headers_to_check:
        if header in response.headers:
            headers_present[header] = True
    return headers_present