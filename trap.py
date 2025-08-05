from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def trap():
    token = request.args.get('token', 'неизвестно')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    ref = request.referrer
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"{ts} | Token: {token} | IP: {ip} | UA: {ua} | Referrer: {ref}\n"
    print(log_line)

    with open('trap_log.txt', 'a', encoding='utf-8') as f:
        f.write(log_line)

    return "Спасибо, ваша информация получена"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
