import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
import dns.resolver
import socket
from tabulate import tabulate
from pystyle import Write
from tabulate import tabulate
from pystyle import Colorate, Colors
from datetime import datetime
from colorama import Fore, Style, init
import sys
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
org_socket = socket.getaddrinfo

def google_socket(host, port, family=0, type=0, proto=0, flags=0):
    try:
        info = resolver.resolve(host)
        ip_address = info[0].to_text()
        return org_socket(ip_address, port, family, type, proto, flags)
    except:
        return org_socket(host, port, family, type, proto, flags)

socket.getaddrinfo = google_socket
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)


#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ="
#Config
init(autoreset=True)

def banner():
    # Xóa màn hình
    os.system('cls' if os.name == 'nt' else 'clear')

    # Danh sách màu luân phiên
    colors = [Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.BLUE]

    banner_text = '''
            ─────────────────────────────────────────
    🎀✨ Chào mừng bạn đến với Tool ✨🎀
    ─────────────────────────────────────────
    🌸 Chúc bạn một ngày vui vẻ và nhiều may mắn! 🌸
    🐱 Mèo con chúc bạn code không lỗi! 🐱
    ─────────────────────────────────────────
      🛠️ Admin support tool Zalo:  0367742346
                                   0348865758
        Web tải tool và HD:
        https://mlevip.blogspot.com/2025/02/huong-dan-su-dung-tool-body-font-family.html
      🔗 Chat support: https://zalo.me/g/uaahwq871
      🌐 Web VPN giá rẻ & ID Apple free: timgiare.top ✔️
    ─────────────────────────────────────────
    CopyRight: © KEDO@TOOL
    '''

    # Hiệu ứng nhấp nháy
    for _ in range(5):
        color = colors[_ % len(colors)]
        print(color + banner_text)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

    # Hiển thị banner lần cuối với màu nổi bật
    print(Fore.LIGHTCYAN_EX + banner_text)
    print(Fore.LIGHTRED_EX + "-"*70)

def LIST():
    banner()

os.system('cls' if os.name == 'nt' else 'clear')
banner()
token_tds = input(f'{ndp_tool}{luc}Vui Lòng Nhập Token TĐS{trang}:{vang} ')
check_log = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token_tds).json()
if 'success' in check_log:
    print(f'{xnhac}Đăng Nhập Thành Công!')
    user = check_log['data']['user']
    xucon = check_log['data']['xu']
    xudie = check_log['data']['xudie']
else:
    exit(f'{do}Đăng Nhập Thất Bại.')
print(thanh)
cookie = input(f'{ndp_tool}{luc}Vui Lòng Nhập Cookie IG{trang}: {vang} ')
#CHỌN NV + NHẬP DELAY
os.system("cls" if os.name == "nt" else "clear")
banner()
print(f'{ndp_tool}{luc}Tên Tài Khoản{trang}: {vang}{user}')
print(f'{ndp_tool}{luc}Xu Hiện Tại{trang}: {vang}{xucon}')
print(f'{ndp_tool}{luc}Xu Bị Trừ{trang}: {vang}{xudie}')
print(thanh)
print(f'{ndp_tool}{luc}Nhập Số {do}[{vang}1{do}] {luc}Để Chạy Nhiệm Vụ Tym')
print(f'{ndp_tool}{luc}Nhập Số {do}[{vang}2{do}] {luc}Để Chạy Nhiệm Vụ Follow')
print(f'{ndp_tool}{luc}Nhập Số {do}[{vang}3{do}] {luc}Để Chạy Nhiệm Vụ Tym Comment')
print(f'{ndp_tool}{luc}Nhập Số {do}[{vang}4{do}] {luc}Để Chạy Nhiệm Vụ Comment {do}[{vang}BẢO TRÌ{do}]')
print(thanh)
chonjob = input(f'{ndp_tool}{luc}Nhập Nhiệm Vụ Bạn Muốn Chạy{trang}: {vang}')
delayjob = int(input(f'{ndp_tool}{luc}Nhập Delay Làm Nhiệm Vụ{trang}: {vang}'))
os.system("cls" if os.name == "nt" else "clear")
banner()
#hàm delay + load tìm job
def delay_ndp(o):
	while (o>1):
		o=o-1
		print(luc+' Tiếp Tục Sau <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.2)
		print(do+' Tiếp Tục Sau <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.1)
		print(vang+' Tiếp Tục Sau <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.2)
		print(hong+' Tiếp Tục Sau <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.1)
		print(xnhac+' Tiếp Tục Sau <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.2)
def loadjob(o):
	while (o>1):
		o=o-1
		print(luc+' Đang Tìm Nhiệm Vụ <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.2)
		print(do+' Đang Tìm Nhiệm Vụ <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.1)
		print(vang+' Đang Tìm Nhiệm Vụ <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.2)
		print(hong+' Đang Tìm Nhiệm Vụ <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.1)
		print(xnhac+' Đang Tìm Nhiệm Vụ <~> KeDoTOOL❣️🌸 '+do+'| '+vang+''+str(o)+do+' |','      ', end='\r')
		sleep(0.2)

thoigian = datetime.now().strftime("%H:%M:%S")
demjob = 0
#get token...
headers_get = {
    'authority': 'www.instagram.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'referer': 'https://www.instagram.com/accounts/onetap/?next=%2F',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'viewport-width': '1920',
    'cookie': cookie,
}
get_dulieu = requests.get('https://www.instagram.com/', headers = headers_get).text
token_ig = get_dulieu.split('csrf_token":"')[1].split('",')[0]
id_app = get_dulieu.split('"X-IG-App-ID":"')[1].split('",')[0]
instagram_ajax = get_dulieu.split('"rev":')[1].split('},"')[0]
#headers get info
headers_get_in4 = {
    'authority': 'www.instagram.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'viewport-width': '1920',
    'cookie': cookie,
}
in4 = requests.get('https://www.instagram.com/', headers = headers_get_in4).text
#tách
id_ig = in4.split('viewerId":"')[1].split('"}')[0]
cauhinhaccig = requests.get(f'https://traodoisub.com/api/?fields=instagram_run&id={id_ig}&access_token='+token_tds).json()
try:
    if 'success' in cauhinhaccig:
        id_ch = cauhinhaccig['data']['id']
        user_ch = cauhinhaccig['data']['uniqueID']
    else:
        exit(f'{do}Cấu Hình Thất Bại, Vui Lòng Thêm Acc Vào Cấu Hình!!!')
except:
    pass
#info cấu hình
print(f'{ndp_tool}{luc}USER CẤU HÌNH{trang}: {vang}{user_ch} {do}| {luc}ID CẤU HÌNH{trang}: {vang}{id_ig}')
print(thanh)
#chế độ tym
if '1' in chonjob:
    while True:
        get_list_nv_tym = requests.get('https://traodoisub.com/api/?fields=instagram_like&access_token='+token_tds).json()
        try:
            id_tym = get_list_nv_tym['data'][0]['id']
            link_job_tym = get_list_nv_tym['data'][0]['link']
            id_job_tym = id_tym.split('_')[0]
        except:
            bukload = 5
            loadjob(bukload)
            continue
        #headers làm job
        headers_job_tym = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': link_job_tym,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
            'viewport-width': '1014',
            'x-asbd-id': '198387',
            'x-csrftoken': token_ig,
            'x-ig-app-id': id_app,
            'x-ig-www-claim': 'hmac.AR0kbnnl4Sg351vNHgTi5an3lniwX9V0L8BktreD7ETXQhLL',
            'x-instagram-ajax': instagram_ajax,
            'x-requested-with': 'XMLHttpRequest',
            'cookie': cookie,
        }

        lamjobtym = requests.post(f'https://www.instagram.com/web/likes/{id_job_tym}/like/', headers = headers_job_tym).text
        sleep(1)
        duyetnvtym = requests.get(f'https://traodoisub.com/api/coin/?type=INS_LIKE_CACHE&id={id_tym}&access_token='+token_tds).json()
        try:
            xuduyet_tym = duyetnvtym['data']['pending']
            xucong_tym = duyetnvtym['data']['msg']
        except:
            continue
        if 'ok' in lamjobtym:
            demjob = demjob+1
            print(f'{do}[{vang}{demjob}{do}] | {xnhac}{thoigian}{do} | {vang}TYM{do} | {trang}{id_job_tym} {do}| {vang}{xucong_tym} {do}| {luc}Tổng Duyệt: {vang}{xuduyet_tym} Xu')
            delay_ndp(delayjob)
        else:
            demjob = demjob+1
            print(f'{do}[{vang}{demjob}{do}]{do}[{trang}X{do}] | {xnhac}{thoigian}{do} | {trang}{id_job_tym} {do}| {do}TYM THẤT BẠI')
#chế độ follow
if '2' in chonjob:
    while True:
        get_list_nv_follow = requests.get('https://traodoisub.com/api/?fields=instagram_follow&access_token='+token_tds).json()
        try:
            id_follow = get_list_nv_follow['data'][0]['id']
            link_follow = get_list_nv_follow['data'][0]['link']
            id_job_follow = id_follow.split('_')[0]
        except:
            bukload = 5
            loadjob(bukload)
            continue
        headers_job_follow = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': link_follow,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
            'viewport-width': '1014',
            'x-asbd-id': '198387',
            'x-csrftoken': token_ig,
            'x-ig-app-id': id_app,
            'x-ig-www-claim': 'hmac.AR07N5q1wNjFl2rs9Uw-PN1PzCDaBP8lPGzvakw765wEQug0',
            'x-instagram-ajax': instagram_ajax,
            'x-requested-with': 'XMLHttpRequest',
            'cookie': cookie,
        }
        lamjobfollow = requests.post(f'https://www.instagram.com/web/friendships/{id_job_follow}/follow/', headers = headers_job_follow).text
        sleep(1)
        duyetnvfollow = requests.get(f'https://traodoisub.com/api/coin/?type=INS_FOLLOW_CACHE&id={id_follow}&access_token='+token_tds).json()
        try:
            xuduyet_follow = duyetnvfollow['data']['pending']
            xucong_follow = duyetnvfollow['data']['msg']
        except:
            continue
        if 'ok' in lamjobfollow:
            demjob = demjob+1
            print(f'{do}[{vang}{demjob}{do}] | {xnhac}{thoigian}{do} | {vang}FOLLOW{do} | {trang}{id_job_follow} {do}| {vang}{xucong_follow} {do}| {luc}Tổng Duyệt: {vang}{xuduyet_follow} Xu')
            delay_ndp(delayjob)
        else:
            demjob = demjob+1
            print(f'{do}[{vang}{demjob}{do}]{do}[{trang}X{do}] | {xnhac}{thoigian}{do} | {trang}{id_job_follow} {do}| {do}FOLLOW THẤT BẠI')
#chế độ tym comment
if '3' in chonjob:
    while True:
        get_list_nv_tymcmt = requests.get('https://traodoisub.com/api/?fields=instagram_likecmt&access_token='+token_tds).json()
        try:
            id_tymcmt = get_list_nv_tymcmt['data'][0]['id']
            link_tymcmt = get_list_nv_tymcmt['data'][0]['link_web']
            id_job_tymcmt = id_tymcmt.split('_')[0]
        except:
            bukload = 5
            loadjob(bukload)
            continue
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': link_tymcmt,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
            'viewport-width': '1014',
            'x-asbd-id': '198387',
            'x-csrftoken': token_ig,
            'x-ig-app-id': id_app,
            'x-ig-www-claim': 'hmac.AR0kbnnl4Sg351vNHgTi5an3lniwX9V0L8BktreD7ETXQgRk',
            'x-instagram-ajax': instagram_ajax,
            'x-requested-with': 'XMLHttpRequest',
            'cookie': cookie,
        }
        lamjobtymcmt = requests.post(f'https://www.instagram.com/web/comments/like/{id_job_tymcmt}', headers=headers).text
        duyetnvtymcmt = requests.get(f'https://traodoisub.com/api/coin/?type=INS_LIKECMT_CACHE&id={id_tymcmt}&access_token='+token_tds).json()
        try:
            xuduyet_tymcmt = duyetnvtymcmt['data']['pending']
            xucong_tymcmt = duyetnvtymcmt['data']['msg']
        except:
            continue
        if 'ok' in lamjobtymcmt:
            demjob = demjob+1
            print(f'{do}[{vang}{demjob}{do}] | {xnhac}{thoigian}{do} | {vang}TYM CMT{do} | {trang}{id_job_tymcmt} {do}| {vang}{xucong_tymcmt} {do}| {luc}Tổng Duyệt: {vang}{xuduyet_tymcmt} Xu')
        else:
            demjob = demjob+1
            print(f'{do}[{vang}{demjob}{do}]{do}[{trang}X{do}] | {xnhac}{thoigian}{do} | {trang}{id_job_tymcmt} {do}| {do}TYM CMT')