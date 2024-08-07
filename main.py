#!/usr/bin/python

# Copyright (C) Anasov <me@anasov.ly> - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Anasov <me@anasov.ly>, 05, May, 2024.

import random
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
from andocpm import AndoCPM

__CHANNEL_USERNAME__ = "AndoCPM"
__GROUP_USERNAME__   = "AndoCPM"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  " █████╗ ███╗   ██╗██╗  ██╗     █████╗ ███╗   ██╗    ██████╗  ██████╗\n"
    brand_name += "██╔══██╗████╗  ██║██║  ██║    ██╔══██╗████╗  ██║    ██╔══██╗██╔═══██╗\n"
    brand_name += "███████║██╔██╗ ██║███████║    ███████║██╔██╗ ██║    ██║  ██║██║   ██║\n"
    brand_name += "██╔══██║██║╚██╗██║██╔══██║    ██╔══██║██║╚██╗██║    ██║  ██║██║   ██║\n"
    brand_name += "██║  ██║██║ ╚████║██║  ██║    ██║  ██║██║ ╚████║    ██████╔╝╚██████╔╝\n"
    brand_name += "╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═════╝  ╚═════╝\n"
    colors = [
        "rgb(255,0,255)", "rgb(0,255,255)","rgb(255,0,255)","rgb(0,255,255)",
        "rgb(255,0,255)", "rgb(0,255,255)","rgb(255,0,255)","rgb(0,255,255)",
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    console.print("[bold red]👑 Ấn Độ[/bold red]: [bold yellow]Trải nghiệm cuộc sống và đam mê[/bold yellow]")
    console.print(f"[bold red]👑 Zalo[/bold red]: [bold green]0335374215[/bold green] or [bold green]FB: Nguyễn Huỳnh Vũ[/bold green]")
    console.print("[bold red]==================================================[/bold red]")
    console.print("[bold yellow]! Lưu ý[/bold yellow]: Đăng xuất khỏi CPM trước khi sử dụng công cụ này !", end="\n\n")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
            console.print("[bold][red]========[/red][ PLAYER DETAILS ][red]========[/red][/bold]")
            console.print(f"[bold green]Name   [/bold green]: { (data.get('Name') if 'Name' in data else 'UNDEFINED') }.")
            console.print(f"[bold green]LocalID[/bold green]: { (data.get('localID') if 'localID' in data else 'UNDEFINED') }.")
            console.print(f"[bold green]Money  [/bold green]: { (data.get('money') if 'money' in data else 'UNDEFINED') }.")
            console.print(f"[bold green]Coins  [/bold green]: { (data.get('coin') if 'coin' in data else 'UNDEFINED') }.", end="\n\n")
        else:
            console.print("[bold red]! ERROR[/bold red]: new accounts most be signed-in to the game at least once !.")
            exit(1)
    else:
        console.print("[bold red]! ERROR[/bold red]: seems like your login is not properly set !.")
        exit(1)

def load_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold][red]========[/red][ ACCESS KEY DETAILS ][red]========[/red][/bold]")
    console.print(f"[bold green]Telegram ID[/bold green]: { data.get('telegram_id') }.")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold]👑 Tài Khoản Gmail[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold]👑 Mật Khẩu[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold]👑 Chìa Khóa[/bold]", "Access Key", password=False)
        console.print("[bold cyan]👑 Đợi Kiểm Tra[/bold cyan]: ", end=None)
        cpm = CPMNuker(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]⛔ TÀI KHOẢN KHÔNG ĐƯỢC TÌM THẤY[/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]⛔ SAI MẬT KHẨU[/bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]⛔ KẾT NỐI CHÌA KHÓA THẤT BẠI[/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]⛔ THỬ LẠI[/bold red].")
                console.print("[bold yellow]⛔ LƯU Ý[/bold yellow]: hãy chắc chắn rằng bạn đã điền vào ?/")
                sleep(2)
                continue
        else:
            console.print("[bold green]🎀THÀNH CÔNG [/bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            console.print("[bold red](01):[/bold red][bold green]Tiền[/bold green]")
            console.print("[bold red](02):[/bold red][bold green]Xu Vàng[/bold green]")
            console.print("[bold red](03):[/bold red][bold green]Hạng Vua / Rank King[/bold green]")
            console.print("[bold red](04):[/bold red][bold green]Chỉnh Sửa ID[/bold green]")
            console.print("[bold red](05):[/bold red][bold green]Chỉnh Sửa Tên[/bold green]")
            console.print("[bold red](06):[/bold red][bold green]Chỉnh Sửa Tên Màu Rainbow[/bold green]")
            console.print("[bold red](07):[/bold red][bold green]Biển Số[/bold green]")
            console.print("[bold red](08):[/bold red][bold green]Xóa Tài Khoản[/bold green]")
            console.print("[bold red](09):[/bold red][bold green]Tạo Tài Khoản[/bold green]")
            console.print("[bold red](10):[/bold red][bold green]Xóa Bạn Bè[/bold green]")
            console.print("[bold red](11):[/bold red][bold green]Unlock Xe Trả Tiền[/bold green]")
            console.print("[bold red](12):[/bold red][bold green]Unlock Tất Cả Xe[/bold green]")
            console.print("[bold red](13):[/bold red][bold green]Unlock Xe Cảnh Sát[/bold green]")
            console.print("[bold red](14):[/bold red][bold green]Unlock W16[/bold green]")
            console.print("[bold red](15):[/bold red][bold green]Unlock Còi[/bold green]")
            console.print("[bold red](16):[/bold red][bold green]Không Hư Hỏng[/bold green]")
            console.print("[bold red](17):[/bold red][bold green]Vô Hạn Xăng[/bold green]")
            console.print("[bold red](18):[/bold red][bold green]Nhà 3[/bold green]")
            console.print("[bold red](19):[/bold red][bold green]UNLOCK Khói[/bold green]")
            console.print("[bold red](20):[/bold red][bold green]Chỉnh Sửa Win[/bold green]")
            console.print("[bold red](21):[/bold red][bold green]Chỉnh Sửa Loese[/bold green]")
            console.print("[bold red](22):[/bold red][bold green]Sao Chép Tài Khoản[/bold green]")
            console.print("[bold red](0):[/bold red][bold green]Thoát[/bold green]", end="\n\n")
            service = IntPrompt.ask(f"[bold]🎀 Chọn một dịch vụ [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            if service == 0: # Exit
                console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi [/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
            elif service == 1: # Increase Money
                console.print("[bold cyan]🎀 Chèn bao nhiêu tiền bạn muốn[/bold cyan]")
                amount = IntPrompt.ask("[bold]🎀 Số lượng[/bold]")
                console.print("[bold cyan]🎀 Đang lưu dữ liệu của bạn[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 50000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]🎀THÀNH CÔNG[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]⛔ LỖI[/bold red]")
                        console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⛔ LỖI[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng sử dụng các giá trị hợp lệ[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                console.print("[bold cyan]🎀 Chèn bao nhiêu xu bạn muốn[/bold cyan]")
                amount = IntPrompt.ask("[bold]🎀 Số lượng[/bold]")
                console.print("[bold cyan]🎀 Đang lưu dữ liệu của bạn[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 90000:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]⛔ LỖI[/bold red]")
                        console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⛔ LỖI[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red]⛔ Lưu ý:[/bold red]: Nếu cấp vua không xuất hiện trong trò chơi, hãy đóng nó và mở lại vài lần.", end=None)
                console.print("[bold red]⛔ Lưu ý:[/bold red]: Vui lòng không thực hiện Xếp hạng Vua trên cùng một tài khoản hai lần", end=None)
                sleep(2)
                console.print("[bold cyan]🎀 Trao cho bạn thứ hạng Vua[/bold cyan]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold cyan][!] Nhập ID mới của bạn[/bold cyan]")
                new_id = Prompt.ask("[bold][?] ID[/bold]")
                console.print("[bold cyan]🎀 Đang lưu dữ liệu của bạn[/bold cyan]: ", end=None)
                if len(new_id) >= 9 and len(new_id) <= 14 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]⛔ LỖI.[/bold red]")
                        console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow][!] Vui lòng sử dụng ID hợp lệ[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold cyan][!] Nhập tên mới của bạn[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Tên[/bold]")
                console.print("[bold cyan]🎀 Đang lưu dữ liệu của bạn[/bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(new_name):
                        console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]⛔ LỖI.[/bold red]")
                        console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow][!] Vui lòng sử dụng các giá trị hợp lệ[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print("[bold cyan][!] Nhập Tên Rainbow mới của bạn[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Tên[/bold]")
                console.print("[bold cyan]🎀 Đang lưu dữ liệu của bạn[/bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]⛔ LỖI.[/bold red]")
                        console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow][!] Vui lòng sử dụng các giá trị hợp lệ[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[bold cyan][%] Tặng bạn biển số[/bold cyan]: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                console.print("[bold cyan][!] Sau khi xóa tài khoản của bạn, bạn sẽ không thể quay lại !!.[/bold cyan]")
                answ = Prompt.ask("[bold cyan][?] Bạn có muốn xóa tài khoản này ?![/bold cyan]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold cyan][%] Xóa tài khoản của bạn[/bold cyan]: [bold green]🎀THÀNH CÔNG [/bold green].")
                    console.print("==================================")
                    console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                else: continue
            elif service == 9: # Account Register
                console.print("[bold cyan][!] Đăng ký tài khoản mới[/bold cyan]")
                acc2_email = prompt_valid_value("[bold][?] Tài Khoản Gmail[/bold]", "Email", password=False)
                acc2_password = prompt_valid_value("[bold][?] Mật Khẩu[/bold]", "Password", password=False)
                console.print("[bold cyan][%] Tạo tài khoản mới[/bold cyan]: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    console.print(f"[bold red]! Hello[/bold red]: Để tweak tài khoản này bằng AndoCPM")
                    console.print("Hầu hết bạn đăng nhập vào trò chơi bằng tài khoản này")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow][!] Email này đã tồn tại ![/bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[bold cyan][%] Xóa bạn bè của bạn[/bold cyan]: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[bold yellow]! Hello[/bold yellow]: Chức năng này mất một lúc để hoàn thành, vui lòng không hủy.", end=None)
                console.print("[bold cyan][%] Mở khóa tất cả ô tô trả phí[/bold cyan]: ", end=None)
                if cpm.unlock_paid_cars():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[bold cyan][%] Unlocking All Cars[/bold cyan]: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[bold cyan][%] Mở khóa tất cả xe ô tô cảnh sát[/bold cyan]: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[bold cyan][%] Mở khóa động cơ W16[/bold cyan]: ", end=None)
                if cpm.unlock_w16():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[bold cyan][%] Mở khóa tất cả các còi[/bold cyan]: ", end=None)
                if cpm.unlock_horns():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[bold cyan][%] Mở khóa Vô hiệu hóa thiệt hại[/bold cyan]: ", end=None)
                if cpm.disable_engine_damage():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[bold cyan][%] Mở khóa nhiên liệu không giới hạn[/bold cyan]: ", end=None)
                if cpm.unlimited_fuel():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[bold cyan][%] Mở khóa nhà 3[/bold cyan]: ", end=None)
                if cpm.unlock_houses():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[bold cyan][%] Mở khóa khói[/bold cyan]: ", end=None)
                if cpm.unlock_smoke():
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 20: # Change Races Wins
                console.print("[bold cyan][!] Chèn số lượng cuộc đua bạn giành chiến thắng[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Số lượng[/bold]")
                console.print("[bold cyan][%] Thay đổi dữ liệu của bạn[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 999:
                    if cpm.set_player_wins(amount):
                        console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]⛔ LỖI.[/bold red]")
                        console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 21: # Change Races Loses
                console.print("[bold cyan][!] Chèn số lượng cuộc đua bạn thua[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Số lượng[/bold]")
                console.print("[bold cyan][%] Thay đổi dữ liệu của bạn[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 999:
                    if cpm.set_player_loses(amount):
                        console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]⛔ LỖI.[/bold red]")
                        console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 22: # Clone Account
                console.print("[bold cyan]Vui lòng nhập chi tiết tài khoản[/bold cyan]:")
                to_email = prompt_valid_value("[bold][?] Tài khoản gmail[/bold]", "Email", password=False)
                to_password = prompt_valid_value("[bold][?] Mật khẩu[/bold]", "Password", password=False)
                console.print("[bold cyan][%] Nhân bản tài khoản của bạn[/bold cyan]: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print("[bold green]🎀THÀNH CÔNG [/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]⛔ Bạn có muốn thoát không ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]🎀 Cảm ơn bạn đã sử dụng công cụ của chúng tôi[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]⛔ LỖI.[/bold red]")
                    console.print("[bold yellow]⛔ Vui lòng thử lại[/bold yellow]")
                    sleep(2)
                    continue
            else: continue
            break
        break
