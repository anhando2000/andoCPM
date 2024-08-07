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
from andocpm import andoCPM

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
    console.print("[bold red]👑 CPMCANETOOL[/bold red]: [bold yellow]Trải nghiệm cuộc sống và đam mê[/bold yellow]")
    console.print(f"[bold red]👑 CPMCANETOOL[/bold red]: [bold green]0335374215[/bold green] or [bold green]FB: CANE CPM[/bold green]")
    console.print("[bold red]==================================================[/bold red]")
    console.print("[bold yellow]! Note[/bold yellow]: Sign out of CPM before using this tool !", end="\n\n")

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
        acc_email = prompt_valid_value("[bold]👑 Account Gmail[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold]👑 Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold]👑 Lock[/bold]", "Access Key", password=False)
        console.print("[bold cyan]👑 Waiting for Check[/bold cyan]: ", end=None)
        cpm = andoCPM(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]⛔ ACCOUNT NOT FOUND[/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]⛔ WRONG PASSWORD[/bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]⛔ KEY CONNECTION FAILED[/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]⛔ RETRY[/bold red].")
                console.print("[bold yellow]⛔ NOTE[/bold yellow]: Please make sure you have filled it out ?/")
                sleep(2)
                continue
        else:
            console.print("[bold green]🎀SUCCESS [/bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            console.print("[bold red](01):[/bold red][bold green]Money[/bold green]")
            console.print("[bold red](02):[/bold red][bold green]Gold Coins[/bold green]")
            console.print("[bold red](03):[/bold red][bold green]King Class / Rank King[/bold green]")
            console.print("[bold red](04):[/bold red][bold green]Change ID[/bold green]")
            console.print("[bold red](05):[/bold red][bold green]Edit Name[/bold green]")
            console.print("[bold red](06):[/bold red][bold green]Edit Color Name Rainbow[/bold green]")
            console.print("[bold red](07):[/bold red][bold green]License plate[/bold green]")
            console.print("[bold red](08):[/bold red][bold green]Delete the account[/bold green]")
            console.print("[bold red](09):[/bold red][bold green]Create Account[/bold green]")
            console.print("[bold red](10):[/bold red][bold green]Delete Friends[/bold green]")
            console.print("[bold red](11):[/bold red][bold green]Unlock Car Paid[/bold green]")
            console.print("[bold red](12):[/bold red][bold green]Unlock All Vehicles[/bold green]")
            console.print("[bold red](13):[/bold red][bold green]Unlock Police Car[/bold green]")
            console.print("[bold red](14):[/bold red][bold green]Unlock W16[/bold green]")
            console.print("[bold red](15):[/bold red][bold green]Unlock Whistle[/bold green]")
            console.print("[bold red](16):[/bold red][bold green]No Damage Car[/bold green]")
            console.print("[bold red](17):[/bold red][bold green]Unlimited Fuel[/bold green]")
            console.print("[bold red](18):[/bold red][bold green]Unlock Home 3[/bold green]")
            console.print("[bold red](19):[/bold red][bold green]Unlock Smoke[/bold green]")
            console.print("[bold red](20):[/bold red][bold green]Edit Win[/bold green]")
            console.print("[bold red](21):[/bold red][bold green]Edit Loese[/bold green]")
            console.print("[bold red](22):[/bold red][bold green]Copy Account[/bold green]")
            console.print("[bold red](0):[/bold red][bold green]Exit[/bold green]", end="\n\n")
            service = IntPrompt.ask(f"[bold]🎀 Choose a service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            if service == 0: # Exit
                console.print(f"[bold yellow]🎀 Thank you for using our tool [/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
            elif service == 1: # Increase Money
                console.print("[bold cyan]🎀 Insert how much money you want[/bold cyan]")
                amount = IntPrompt.ask("[bold]🎀 Quantity[/bold]")
                console.print("[bold cyan]🎀 Saving your data[/bold cyan]: ", end=None)
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
                    console.print("================
