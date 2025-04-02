import requests

def cookies_security(url):
    from responds import CriticalNames
    try:
        response = requests.get(url)
        cookies = response.cookies
        
        if not cookies:
            #На сайте не найдено куки
            return 1
        
        for cookie in cookies:
            if cookie.name in CriticalNames:
                
                is_secure = cookie.secure
                is_http_only = "HttpOnly" in str(cookie)
                is_same_site = getattr(cookie, "same_site", None)
                
                if is_secure and is_http_only and is_same_site:
                    #Куки безопасны
                    return 2
                else:
                    #Куки не безопасны
                    return 3
                
    except Exception as e:
        return 1