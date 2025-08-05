from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    # Получаем IP из заголовков, если есть прокси
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    log_line = f"[{timestamp}] IP: {ip}, Agent: {user_agent}"
    print(log_line)

    # Также можно сохранять в файл:
    with open("visits.log", "a") as f:
        f.write(log_line + "\n")

    return "Спасибо за визит!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
