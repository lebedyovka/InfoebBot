import subprocess

def check_waf(url):
    try:
        result = subprocess.run(['wafw00f', url], capture_output=True, text=True, check=True)
        
        if "is behind" in result.stdout:
            return True
        if "seems" in result.stdout:
            return True
        return False
    except subprocess.CalledProcessError as e:
        return False