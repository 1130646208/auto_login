import requests
import tkinter as tk
import os
import json

url = 'http://202.204.48.66/drcom/login?callback=dr1004&DDDDD={}&upass={}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=974&lang=zh'
headers = {
    'Host': '202.204.48.66',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43',
    'DNT': '1',
    'Accept': '*/*',
    'Referer': 'http://202.204.48.66/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5',
}
file_path = os.path.expanduser("~").replace('\\', '/')
def save_pass(uname, upass):
    with open(file_path + '/net_pass.txt', 'w') as f:
        content = f.write(uname+' '+upass)

def get_pass():
    try:
        with open(file_path + '/net_pass.txt', 'r') as f:
            uname, upass = f.read().split(' ')
            return uname, upass
    except Exception as e:
        print(e)
        return None, None



window = tk.Tk()
window.title('LOGIN V1.0')

window.geometry('250x120')
tk.Label(window, text='账户：').grid(row=0,column=0)
tk.Label(window, text='密码：').grid(row=1,column=0)
var_status = tk.StringVar(value='')
lable1 = tk.Label(window, textvariable=var_status, height=1, width=15, bg='blue', fg='white').grid(row=3,column=1, columnspan=2)


var_usr_name = tk.StringVar()
enter_usr_name = tk.Entry(window, textvariable=var_usr_name)
enter_usr_name.grid(row=0,column=1, columnspan=2)

var_usr_pwd = tk.StringVar()
enter_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
enter_usr_pwd.grid(row=1,column=1, columnspan=2)

def check_pass():
    uname, upass = get_pass()
    
    if uname:
        var_usr_name.set(uname)
        var_usr_pwd.set(upass)
    else:
        pass

check_pass()

def login():
    uname = var_usr_name.get()
    upass = var_usr_pwd.get()
    
    if not uname or not upass:
        pass
    else:
        r = requests.get(url.format(uname, upass), headers=headers)
        print(r.text[12:-4])
    
        if r.status_code == 200:
            response_json = json.loads(r.text[12:-4])
            if response_json.get('result') == 1:      
                save_pass(var_usr_name.get(), var_usr_pwd.get())
                var_status.set('登陆成功')
            else:
                var_status.set('登陆失败')
        else:
            var_status.set('登陆失败')
    
def usr_sign_quit():
    r = requests.get(url.format('666', '666'), headers=headers)
    print(r.text[12:-4])
    if r.status_code == 200:
            response_json = json.loads(r.text[12:-4])
            if response_json.get('result') == 0:      
                save_pass(var_usr_name.get(), var_usr_pwd.get())
                var_status.set('注销成功')
            else:
                var_status.set('注销失败')
    else:
        var_status.set('注销失败')
    
#登录 注册按钮
bt_login = tk.Button(window,text='登录',command=login)
bt_login.grid(row=2,column=1)

bt_logquit = tk.Button(window,text='注销',command=usr_sign_quit)
bt_logquit.grid(row=2,column=2)


if __name__ == '__main__':
    window.mainloop()

