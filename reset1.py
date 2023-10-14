from string                import ascii_lowercase, ascii_uppercase, digits
from random                import choices, shuffle
from hashlib               import md5
from utils.device_register import device_register
from time                  import time
from requests              import request
from json                  import dumps

api = "api31-normal-useast2a.tiktokv.com"

def generate_password() -> str:
  characters = ascii_lowercase + ascii_uppercase
  numbers = digits
  punctuation = ["!", "@", "#", "$", "%", "^", "&", "*"]
  password = choices(characters, k=11) + choices(numbers, k=2) + choices(punctuation, k=2)
  shuffle(password)
  return "".join(password)

def musically_encrypt(string) -> str:
  return "".join([hex(int(_ ^ 5))[2:] for _ in string.encode("utf-8")])

def musically_md5(string) -> str:
  return md5(string.encode()).hexdigest().upper()

device = device_register()

install_id = device["install_id"]
device_id = device["device_id"]
openudid = device["openudid"]

email = musically_encrypt(input("Email >>> "))

t = time()
url = f"https://{api}/passport/email/send_code/?account_sdk_version=355&app_language=en&manifest_version_code=2019021215&_rticket={int(t * 1000)}&iid={install_id}&channel=googleplay&language=en&fp=&device_type=Pixel%2B6%2BPro&resolution=1080*2268&openudid={openudid}&update_version_code=2019021215&sys_region=US&os_api=30&is_my_cn=0&timezone_name=Europe%2FBerlin&dpi=443&carrier_region=&ac=wifi&device_id={device_id}&pass-route=1&mcc_mnc=&timezone_offset=3600&os_version=12&version_code=100107&carrier_region_v2=&app_name=musical_ly&ab_version=10.1.7&version_name=10.1.7&device_brand=google&ssmix=a&pass-region=1&build_number=10.1.7&device_platform=android&region=US&aid=1233&ts={int(t)}&as=a1iosdfgh&cp=androide1"

payload = f"app_language=en&manifest_version_code=2019021215&_rticket={int(t * 1000)}&iid={install_id}&channel=googleplay&language=en&fp=&device_type=Pixel+6+Pro&type=31&resolution=1080*2268&openudid={openudid}&update_version_code=2019021215&sys_region=US&os_api=30&is_my_cn=0&timezone_name=Europe%2FBerlin&dpi=443&email={email}&retry_type=no_retry&carrier_region=&ac=wifi&device_id={device_id}&pass-route=1&mcc_mnc=&mix_mode=1&timezone_offset=3600&os_version=12&version_code=100107&carrier_region_v2=&app_name=musical_ly&ab_version=10.1.7&account_sdk_source=app&version_name=10.1.7&device_brand=google&ssmix=a&pass-region=1&build_number=10.1.7&device_platform=android&region=US&aid=1233"

headers = {
  "Host": f"{api}",
  "Connection": "keep-alive",
  "Accept-Encoding": "gzip",
  "sdk-version": "1",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "X-SS-STUB": musically_md5(payload),
  "User-Agent": "com.zhiliaoapp.musically/2019021215 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004; Cronet/58.0.2991.0)"
}

response = request("POST", url, headers=headers, data=payload).json()

if response["message"] != "success":
  print(response["data"]["description"])
  raise SystemExit

code = musically_encrypt(input("Code >>> "))

t = time()

url = f"https://{api}/passport/email/check_code/?account_sdk_version=355&app_language=en&manifest_version_code=2019021215&_rticket={int(t * 1000)}&iid={install_id}&channel=googleplay&language=en&fp=&device_type=Pixel%2B6%2BPro&resolution=1080*2268&openudid={openudid}&update_version_code=2019021215&sys_region=US&os_api=30&is_my_cn=0&timezone_name=Europe%2FBerlin&dpi=443&carrier_region=&ac=wifi&device_id={device_id}&pass-route=1&mcc_mnc=&timezone_offset=3600&os_version=12&version_code=100107&carrier_region_v2=&app_name=musical_ly&ab_version=10.1.7&version_name=10.1.7&device_brand=google&ssmix=a&pass-region=1&build_number=10.1.7&device_platform=android&region=US&aid=1233&ts={int(t)}&as=a1iosdfgh&cp=androide1"

payload = f"app_language=en&manifest_version_code=2019021215&_rticket={int(t * 1000)}&code={code}&iid={install_id}&channel=googleplay&language=en&fp=&device_type=Pixel+6+Pro&type=4&resolution=1080*2268&openudid={openudid}&update_version_code=2019021215&sys_region=US&os_api=30&is_my_cn=0&timezone_name=Europe%2FBerlin&dpi=443&email={email}&retry_type=no_retry&carrier_region=&ac=wifi&device_id={device_id}&pass-route=1&mcc_mnc=&mix_mode=1&timezone_offset=3600&os_version=12&version_code=100107&carrier_region_v2=&app_name=musical_ly&ab_version=10.1.7&account_sdk_source=app&version_name=10.1.7&device_brand=google&ssmix=a&pass-region=1&build_number=10.1.7&device_platform=android&region=US&aid=1233"
#api2.musical.ly
headers = {
  "Host": f"{api}",
  "Connection": "keep-alive",
  "Accept-Encoding": "gzip",
  "sdk-version": "1",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "X-SS-STUB": musically_md5(payload),
  "User-Agent": "com.zhiliaoapp.musically/2019021215 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004; Cronet/58.0.2991.0)"
}

response = request("POST", url, headers=headers, data=payload).json()

if response["message"] != "success":
  print(response["data"]["description"])
  raise SystemExit

ticket = response["data"]["ticket"]

password = generate_password()

print(f"Password >>> {password}")

t = time()

url = f"https://{api}/passport/password/reset_by_email_ticket/?account_sdk_version=355&app_language=en&manifest_version_code=2019021215&_rticket={int(t * 1000)}&iid={install_id}&channel=googleplay&language=en&fp=&device_type=Pixel%2B6%2BPro&resolution=1080*2268&openudid={openudid}&update_version_code=2019021215&sys_region=US&os_api=30&is_my_cn=0&timezone_name=Europe%2FBerlin&dpi=443&carrier_region=&ac=wifi&device_id={device_id}&pass-route=1&mcc_mnc=&timezone_offset=3600&os_version=12&version_code=100107&carrier_region_v2=&app_name=musical_ly&ab_version=10.1.7&version_name=10.1.7&device_brand=google&ssmix=a&pass-region=1&build_number=10.1.7&device_platform=android&region=US&aid=1233&ts={int(t)}&as=a1iosdfgh&cp=androide1"

payload = f"app_language=en&manifest_version_code=2019021215&_rticket={int(t * 1000)}&iid={install_id}&channel=googleplay&language=en&fp=&device_type=Pixel+6+Pro&resolution=1080*2268&openudid={openudid}&update_version_code=2019021215&password={musically_encrypt(password)}&sys_region=US&os_api=30&is_my_cn=0&timezone_name=Europe%2FBerlin&dpi=443&retry_type=no_retry&carrier_region=&ac=wifi&ticket={ticket}&device_id={device_id}&pass-route=1&mcc_mnc=&mix_mode=1&timezone_offset=3600&os_version=12&version_code=100107&carrier_region_v2=&app_name=musical_ly&ab_version=10.1.7&account_sdk_source=app&version_name=10.1.7&device_brand=google&ssmix=a&pass-region=1&build_number=10.1.7&device_platform=android&region=US&aid=1233"

headers = {
  "Host": f"{api}",
  "Connection": "keep-alive",
  "Accept-Encoding": "gzip",
  "sdk-version": "1",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "X-SS-STUB": musically_md5(payload),
  "User-Agent": "com.zhiliaoapp.musically/2019021215 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004; Cronet/58.0.2991.0)"
}

response = request("POST", url, headers=headers, data=payload).json()

del response["tnc_data"]
print(response)
sessionid = response["data"]["session_key"]
print(sessionid)
