import os
import random
import string
import threading
import sys
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import hashlib
from colorama import init , Fore, Back , Style
from webdriver_manager.core.manager import DriverManager
import socket
from datetime import datetime
import json


#path
chromedriver_path = os.path.dirname(os.path.abspath(__file__))+"/chromedriver-win32/chromedriver.exe"
folder_path = os.path.dirname(os.path.abspath(__file__))


#slow send
def slow_typing_with_actionchains(driver, element, text):
    delay = random.uniform(0.1, 0.5)
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


def print_tool_info():
    print(Fore.CYAN + Back.BLACK + "╔═══════════════════════════════════════════════╗")
    print(Fore.YELLOW + Style.BRIGHT + "║       THÔNG TIN CHỦ TOOL                      ║")
    print(Fore.GREEN + "║ Tên: " + Fore.YELLOW + "Quy Kedo" + "                                 ║")
    print(Fore.RED + "║ Group Zalo: " + Fore.YELLOW + "https://zalo.me/g/uaahwq871" + "       ║")
    print(Fore.CYAN + Back.BLACK + "╚═══════════════════════════════════════════════╝")




def print_with_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_notice():
    print("\033[1;34m" + "="*50)
    print("\033[1;32m🔹 Nếu sau 30s không thấy tool thực hiện chức năng gì, thử \033[1;33mCtrl + C\033[1;32m.")
    print("🔹 Nếu vẫn không được, hãy chạy lại tool.")
    print("-" * 50)
    print("🔹 Nếu không thành công nhiều job liên tiếp, có thể Facebook đã thay đổi phần tử.")
    print("   🔸 Khi đó, hãy thoát tool và kiểm tra lại.")
    print("-" * 50)
    print("🔹 Khi nhận job mà cửa sổ Facebook bị tắt, đó là \033[1;36mCHUYỆN BÌNH THƯỜNG\033[1;32m, không phải lỗi.")
    print("="*50 + "\033[0m")



#get key
def generate_key(length=16, prefix="Quy_Kedo"):
    # Tạo key ngẫu nhiên gồm chữ cái và số
    characters = string.ascii_letters + string.digits  # Bao gồm cả chữ cái (hoa + thường) và chữ số
    random_part = ''.join(random.choices(characters, k=length - len(prefix)))
    
    # Tạo key hoàn chỉnh với prefix
    key = prefix + random_part
    return key
def tngay():
    today = datetime.today()
    return today.strftime("%d-%m-%Y")
# Ví dụ tạo key với độ dài 16 ký tự, có tiền tố "Quy_Kedo"



def get_public_ip():
    host = 'api.ipify.org'
    port = 80

    # Kết nối tới host và port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Gửi HTTP request
    request = "GET / HTTP/1.1\r\nHost: api.ipify.org\r\nConnection: close\r\n\r\n"
    s.send(request.encode())

    # Nhận phản hồi và lấy IP công cộng
    response = s.recv(4096).decode()

    # Tìm IP công cộng trong phản hồi
    public_ip = response.split("\r\n")[-1]

    s.close()
    return public_ip



def tao_long_link(folder_path):
    public_ip = get_public_ip()

    # Dữ liệu cần mã hóa
    key_real = generate_key(32,'Quy_Kedo_Siu_Vjp_').strip()
    key_bam_r = key_real.encode()
    bam_key_real = hashlib.sha256(key_bam_r).hexdigest()
    # Mã hóa dữ liệu
    
    current_url = 'https://www.google.com/search?q='+key_real
    tomorrow = tngay()
    tomorrow = tomorrow.encode()
    tomorrow = hashlib.sha256(tomorrow).hexdigest()
    public_ip = public_ip.encode()
    public_ip = hashlib.sha256(public_ip).hexdigest()

    with open('key.key','w') as f:
        
        f.write(f"{bam_key_real} {tomorrow} {public_ip}")
    print('đang lấy link key')
    api_token = '668bc1beab3a3470326ea5fd'
    api_url = f"https://link4m.co/api-shorten/v2?api={api_token}&url={current_url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('status')=='success':
            shortened_url = response_data['shortenedUrl']

            print('link lấy mã hôm nay của bạn là: ',shortened_url)
    

    for i in range(5,-1,-1):
        key_u = input('nhập key bạn vừa lấy: ').strip()
        key = key_u.encode()
        bam_key_u = hashlib.sha256(key).hexdigest()
        if bam_key_u == bam_key_real :
            f = open('key_u.key','w')
            print(key_u,file = f)
            f.close()
            break
        else:
            print(f'key sai, bạn còn {i} lần nhập')






# Lấy IP công cộng
public_ip = get_public_ip()
os.system('cls' if os.name == 'nt' else 'clear')
print_tool_info()
print_notice()
time.sleep(6)
print(f"{Fore.GREEN}IP của bạn là:{Style.RESET_ALL} {Fore.BLUE}{public_ip}{Style.RESET_ALL}")


if 'key_u.key' in os.listdir(folder_path):
    with open('key.key') as f:
        a = list(map(str, f.read().split()))
        if len(a) == 0 :
            tao_long_link(folder_path)
        else:
            b = a[0]
            f = open('key_u.key')
            s = f.read().strip()
            s = s.encode()
            s = hashlib.sha256(s).hexdigest()
            if s == a[0]:
                day = a[1]
                today = datetime.today()
                today = today.strftime("%d-%m-%Y")
                today = today.encode()
                today = hashlib.sha256(today).hexdigest()
                if day == today:
                    ip = a[2]
                    public_ip = public_ip.encode()
                    public_ip = hashlib.sha256(public_ip).hexdigest()
                    if public_ip == ip:
                        print_with_color('key chính xác, đang vào tool',"32")
                    else:
                        tao_long_link(folder_path)
                else:
                    tao_long_link(folder_path)
            else:
                tao_long_link(folder_path)
else:
    tao_long_link(folder_path)


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


#chrome option
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Chỉ hiển thị lỗi nghiêm trọng
chrome_options.add_argument("--silent")  # Giảm log từ trình duyệt
chrome_options.add_argument("--start-minimized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--force-device-scale-factor=0.45")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")



service = Service(chromedriver_path, log_path=os.devnull)  # Ẩn log từ ChromeDriver
# Khởi tạo trình duyệt
print(Fore.CYAN + "══════════════════════════════════════")
print(Fore.YELLOW + Style.BRIGHT + " ▄█▀  CHỌN KÍCH CỠ CHROMEDRIVER  ▀█▄")
print(Fore.CYAN + "══════════════════════════════════════")
print(Fore.GREEN + "▶ [1] -  1366 x 768(to nhất)")
print(Fore.BLUE + "▶ [2] -  1280 x 720")
print(Fore.MAGENTA + "▶ [3] -  960 x 540")
print(Fore.CYAN + "══════════════════════════════════════")
loai = [[1366,768],[1280,720],[960,540]]
while True:
    user = input('bạn có muốn chọn kích cỡ (1-3): ')
    if user in ['1', '2', '3']:
        c,d = loai[int(user)-1]
        break
    else:
        continue


# headless_mode = input("Bạn có muốn chạy chế độ headless ở chrome facebook? (y/n): ").strip().lower()


driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_window_size(d, c)

chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Chỉ hiển thị lỗi nghiêm trọng
chrome_options.add_argument("--silent")  # Giảm log từ trình duyệt
chrome_options.add_argument("--start-minimized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--force-device-scale-factor=0.45")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# if headless_mode == 'y':
#     chrome_options.add_argument("--headless")
driver2 = webdriver.Chrome(service=service, options=chrome_options)
driver2.set_window_size(d, c)
check = 'settingfb.txt' in os.listdir(folder_path)
if check:
    user = input('bạn có muốn dùng lại setting cũ không? (Y/N): ')
    if user in ['y', 'Y']:
        f= open('settingfb.txt')
        lj_min,lj_max,wj_min,wj_max = map(int, f.read().split())
    else:
        check = False
        

if check == False:
    fi = open('settingfb.txt','w')
    #user = input('delay load jobs min:')
    lj_min = int(input('sau mỗi nhiệm vụ thì delay bao nhiêu giây (min):'))
    lj_max = int(input('sau mỗi nhiệm vụ thì delay bao nhiêu giây (max):'))
    wj_min = int(input('delay thực hiện nhiệm vụ (min) :'))
    wj_max = int(input('delay thực hiện nhiệm vụ (max):'))

    print(lj_min,lj_max,wj_min,wj_max, file= fi)
    fi.close()
    time.sleep(random.uniform(3,5))

def check_ck():
    link = driver2.current_url
    if link == 'https://www.facebook.com/login':
        return False
    else:
        return True



def log_fb(folder_path):
    driver2.get('https://www.facebook.com/login')
    driver2.refresh()
    check = 'accfb.json' in os.listdir(folder_path)
    if check:
        us = input('bạn có muốn dùng lại cookie Facebook cũ không?(y/n): ')
        if us.lower() == 'y':
        
            f = open('accfb.json','r')
            cookies = json.load(f)
            for i in cookies:
                driver2.add_cookie({"name": i, "value": cookies[i]})
            time.sleep(1)
            driver2.refresh()
            time.sleep(5)
            if check_ck():
                print_with_color('đăng nhập thanh công!',"32")
            else:
                print_with_color('đăng nhập khỏ thành công, có thể do cookie die',"31")
                check = False
        else:
            check = False
    if check== False:
        driver2.get('https://www.facebook.com/login')
        driver2.refresh()
        while True:
            cookies = input("Cookies FB: ")
            ck = {}
            for cookie in cookies.split(';'):
                try:
                    name, value = cookie.split('=')
                    name = name.strip()
                    value = value.strip()
                    ck[name] = value
                except ValueError:
                    pass
            for i in ck:
                driver2.add_cookie({"name": i, "value": ck[i]})
            time.sleep(1)
            driver2.refresh()
            time.sleep(2)
            if check_ck():
                print_with_color('đăng nhập thanh công!',"32")
                with open('accfb.json','w') as f:
                    json.dump(ck,f)
                break
            else:
                print_with_color('đăng nhập khỏ thành công, có thể do cookie die',"31")

def bao_loi():
    time.sleep(random.uniform(3,5))
    try:
        err_report = driver.find_element(By.XPATH, '//img[@src="../../assets/images/icons-new/error.svg"]')
    except Exception as e:
        err_report = driver.find_element(By.XPATH, '//img[@src="/assets/images/icons-new/error.svg"]')
    err_report.click()
    time.sleep(random.uniform(2.5,3.5))
    # Tạo đối tượng ActionChains
    actions = ActionChains(driver)

    # Cuộn trang xuống
    actions.move_to_element(driver.find_element(By.TAG_NAME, 'body')).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(random.uniform(3,5))
    button_submit = driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-sm form-control mt-3"]')
    button_submit.click()
    
    time.sleep(random.uniform(2.5,3.5))
    ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
    ok.click()
    
    time.sleep(random.uniform(2.5,3.5))




def like():
    time.sleep(4)
    def lk():
        try:
            like = driver2.find_elements(By.XPATH , '//span[@data-ad-rendering-role="thích_button"]')
            like[-1].click()
            return True
        except Exception as e:
            pass
        try:
            # Tìm phần tử có text "Thích" hoặc "Like"
            like_button = driver2.find_element(By.XPATH, '//*[contains(text(), "Thích")]')
            like_button.click()
            return True

        except Exception:
            pass
        try:
            
            # Tìm phần tử có aria-label="Thích" hoặc aria-label="Like"
            like = driver2.find_element(By.XPATH, '//*[@aria-label="Thích"]')
            like.click()
            return True
        except Exception:
            pass
        try:
            like = driver2.find_element(By.XPATH, '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz"]')
            like.click()
            return True
        except Exception as e:
            pass
        
        try:
            like = driver2.find_element(By.XPATH, '//*[contains(text(), "Like")]')
            like.click()
            return True
        except Exception:
            pass
        
        try:
            like = driver2.find_element(By.XPATH, '//*[@aria-label="Like"]')
            like.click()
            return True
        except Exception:
            pass
        return False
    kq = lk()
    if kq:
        return
    else:
        time.sleep(3)

        try:
            #like video
            for i in range(4):
                driver2.execute_script("window.scrollBy(0, 200);")
                time.sleep(0.2)
                kq = lk()
                if kq :
                    return
                else:
                    pass
            return
        except Exception as e:
            pass
def likereel():
    time.sleep(random.uniform(1.5,2.5))
    try:
        actions = ActionChains(driver2)
        actions.move_by_offset(682,820).click().perform()
        return
    except Exception as e:
        pass
    
def likepage():
    time.sleep(random.uniform(2.5,3.5))
    try:
        likepage = driver2.find_element(By.XPATH, "//*[contains(text(), 'Thích')]")
        likepage.click()
    except Exception as e:
        pass


def log_in_gl(folder_path):
    driver.get('https://app.golike.net/home')
    check = 'tt_gl.txt' in os.listdir(folder_path)
    if check:
        us = input('bạn có muốn dùng lại tài khoản Golike không?(y/n): ')
        if us.lower() == 'y':
            if len(open('tt_gl.txt', 'r').read().split()) != 2:
                print('thông tin bị sai ')
                check = False
            else:
                email , password = open('tt_gl.txt', 'r').read().split()
        else:
            check = False
    if check == False:
        email = input('nhập tên tài khoản golike: ')
        password = input('nhập mật khảu tài khoản golike: ')
        with open('tt_gl.txt', 'w') as f:
            f.write(f"{email} {password}")
    time.sleep(random.uniform(2,3))
    offer_email = driver.find_element(By.XPATH, '//input[@type="text"]')
    slow_typing_with_actionchains(driver, offer_email, email)
    time.sleep(random.uniform(2,3))
    offer_password = driver.find_element(By.XPATH, '//input[@type="password"]')
    slow_typing_with_actionchains(driver, offer_password, password)
    time.sleep(random.uniform(2,3))
    offer_password.send_keys(Keys.ENTER)
    time.sleep(random.uniform(3,5))
    try:
        ktr = driver.find_element(By.XPATH, '//h2[@class="swal2-title" and @id="swal2-title"]')
        ktr = ktr.text
        if ktr == 'Lỗi':
            print('có lỗi xảy ra với tài khoản của bạn, có thể do sai tên tài khoản hoặc mật khẩu')
            with open('tt_gl.txt', 'w') as f:
                f.write(f"")
        else:
            print('đăng nhập thanh công!')
    except Exception as e:
        pass

    





def path_job():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_tool_info()
    time.sleep(2)
    try:
        da_hieu = driver.find_element(By.XPATH, '//*[contains(text(), "Đã hiểu")]')
        da_hieu.click()
        time.sleep(random.uniform(3,5))
    except Exception as e:
        pass
    # driver.get('https://www.golike.net/home')
    time.sleep(random.uniform(2.5,3.5))
    cho_duyet = driver.find_element(By.XPATH, '//div[@class="card shadow-400 bg-gradient-3 h-100 hand"]')
    cho_duyet.click()
    time.sleep(random.uniform(2.5,3.5))
    fb_j = driver.find_element(By.XPATH, '//i[@class="fab fa-facebook-f b200"]')
    fb_j.click()
    time.sleep(random.uniform(1.5,2.5))
    list_job = driver.find_element(By.XPATH, '//i[@class="material-icons"]')
    list_job.click()
    time.sleep(random.uniform(2.5,3.5))
    reacc = input('đổi sang acc bạn thực hiện nhiệm vụ và enter: ')

def get_jobs_fb(us,lj_min,lj_max,wj_min,wj_max):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_tool_info()
    time.sleep(4)
    job_thanh_cong = 0
    tien = 0
    for i in range(us):
        try:
            current_time = time.strftime("%Hh- %Mm - %Ss")
            job_offer= driver.find_element(By.XPATH, '//i[@class="material-icons font-light font-18"]')
            job_offer.click()
            time.sleep(random.uniform(1.5,2.5))
            job = driver.find_element(By.XPATH, '//span[@class="font-18 font-bold b200 block-text"]')
            jobs_type = job.text
            num_cash = driver.find_element(By.XPATH, '//span[@class="hold-prices"]')
            num_cash = int(num_cash.text)
            wh_offer = driver.find_element(By.XPATH,'//img[@src="/assets/images/icons-new/chrome.svg"]')
            wh_offer.click()
            try:
                
                driver.switch_to.window(driver.window_handles[1])
                link = driver.current_url
                driver.close()
                driver2.get(link)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.uniform(1.5,2.5))
                driver2.refresh()
                def demgiay(wj_min,wj_max,jdl,current_time, job_thanh_cong,num_cash,tien):
                    wj = random.randint(wj_min,wj_max)
                    for i in range(wj,-1,-1):
                        print(f"\r{Fore.GREEN}[{jdl}]{Style.RESET_ALL}|{Fore.YELLOW}🔥Quykedo🔥|{Fore.GREEN}Delay:{i}s{Style.RESET_ALL}|",end = '',flush=True)
                        time.sleep(1)
                if jobs_type == 'TĂNG LIKE CHO FANPAGE':
                    
                    likepage()
                    demgiay(wj_min,wj_max,i,current_time, job_thanh_cong,num_cash,tien)
                    time.sleep(1)
                elif jobs_type == 'TĂNG LƯỢT THEO DÕI':
                    bao_loi()
                    print(f'\r{Fore.GREEN}-->Đã Hủy Jobs [{i}]{Style.RESET_ALL}')
                    continue
                else:
                    link = driver.current_url
                    if 'reel' in link:
                        like_reel()
                        demgiay(wj_min,wj_max,i,current_time, job_thanh_cong,num_cash,tien)
                        time.sleep(1)
                    else:
                        like()
                        demgiay(wj_min,wj_max,i,current_time, job_thanh_cong,num_cash,tien)
                
                
                time.sleep(2)
                try:
                    try:
                        hoan_thanh = driver.find_element(By.XPATH, '//img[@src="/assets/images/icons-new/success.svg"]')
                        hoan_thanh.click()
                    except Exception as e:
                        hoan_thanh = driver.find_element(By.XPATH, '//img[@src="../../assets/images/icons-new/success.svg"]')
                        hoan_thanh.click()
                    time.sleep(random.uniform(3.5,4.5))
                    try:
                        loi = driver.find_element(By.XPATH, '//h2[@id="swal2-title" and @class="swal2-title"]')
                        loi_1 = loi.text
                        if loi_1 == 'Lỗi':
                            time.sleep(random.uniform(1.5,2.5))
                            ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
                            ok.click()
                            bao_loi()
                            print(f"\r                                                                                                                                                               ",end = '', flush = True)
                            print(f'\r{Fore.GREEN}-->Đã Hủy Jobs [{i}]{Style.RESET_ALL}',end = '',flush = True)
                        else:
                            time.sleep(random.uniform(1.5,2.5))
                            
                            ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
                            ok.click()
                            tien += num_cash
                            job_thanh_cong += 1

                            print(f"\r{Fore.GREEN}[{i}]{Style.RESET_ALL}|{Fore.YELLOW}🔥Quykedo🔥|{Fore.LIGHTGREEN_EX}Time:{current_time}{Style.RESET_ALL}|{Fore.GREEN}Delay:{0}s{Style.RESET_ALL}|{Fore.LIGHTYELLOW_EX}Job thành công:{job_thanh_cong}{Style.RESET_ALL}|{Fore.MAGENTA}{num_cash}đ{Style.RESET_ALL}|{Fore.CYAN}Tổng: {tien}đ{Style.RESET_ALL}| ",end = '',flush=True)
                    except Exception as e:
                        time.sleep(6)
                        loi = driver.find_element(By.XPATH, '//h2[@id="swal2-title" and @class="swal2-title"]')
                        loi_1 = loi.text
                        if loi_1 == 'Lỗi':
                            time.sleep(random.uniform(1.5,2.5))
                            ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
                            ok.click()
                            bao_loi()
                            print(f"\r                                                                                                                                                               ",end = '', flush = True)
                            print(f'\r{Fore.GREEN}-->Đã Hủy Jobs [{i}]{Style.RESET_ALL}',end = '',flush = True)
                        else:
                            time.sleep(random.uniform(1.5,2.5))
                            
                            ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
                            ok.click()
                            tien += num_cash
                            job_thanh_cong += 1

                            print(f"\r{Fore.GREEN}[{i}]{Style.RESET_ALL}|{Fore.YELLOW}🔥Quykedo🔥|{Fore.LIGHTGREEN_EX}Time:{current_time}{Style.RESET_ALL}|{Fore.GREEN}Delay:{0}s{Style.RESET_ALL}|{Fore.LIGHTYELLOW_EX}Job thành công:{job_thanh_cong}{Style.RESET_ALL}|{Fore.MAGENTA}{num_cash}đ{Style.RESET_ALL}|{Fore.CYAN}Tổng: {tien}đ{Style.RESET_ALL}| ",end = '',flush=True)
                except:
                    print('ko thấy nút hoàn thành hiện')
            except Exception as e:
                print('có lỗi')
            try:
                ok = driver.find_element(By.XPATH, '//button[@type="button" and @class="swal2-confirm swal2-styled"]')
                ok.click()
            except:
                pass
            print()
            time.sleep(random.uniform(lj_min,lj_max))
        except Exception as e:
            bao_loi()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_tool_info()
    log_fb(folder_path)
    time.sleep(2)
    log_in_gl(folder_path)
    while True:
        try:
            us= int(input('bạn có cần giải captcha ko , nếu có thì giải xong nhập số jobs muốn làm: '))
            break
        except ValueError:
            print(f"{Fore.RED}/!\{Style.RESET_ALL}{Fore.YELLOW} Vui lòng nhập số nguyên {Style.RESET_ALL}{Fore.RED}/!\{Style.RESET_ALL}")
    time.sleep(2)
    path_job()
    time.sleep(2)
    
    get_jobs_fb(us,lj_min,lj_max,wj_min,wj_max)

if __name__ == "__main__":
    main()
