import os
import time
import threading
from PIL import Image
from minecraft.networking.connection import Connection
from minecraft.networking.packets.clientbound.play import JoinGamePacket, ChatPacket, MapDataPacket, OpenWindowPacket
from minecraft.networking.packets.serverbound.play import ChatPacket as OutChatPacket
from minecraft.networking.packets.serverbound.play import UseItemPacket, ClickWindowPacket

# ---------- НАСТРОЙКИ ----------
HOST = "holyworld.ru"
PORT = 25565
USERNAME = "evgmerku"   # ник
PASSWORD = "Lemau200!109" # Пароль от /login

CHAT_COMMANDS = ["/fix all", "/heal"]
CLICKER_DELAY = 2
COMMAND_DELAY = 60

# ---------- СОЕДИНЕНИЕ ----------
connection = Connection(HOST, PORT, username=evgmerku)

# ---------- ФУНКЦИИ ----------
def send_chat(message):
    packet = OutChatPacket()
    packet.message = message
    connection.write_packet(packet)
    print(f"📤 Отправлено: {message}")

def repeat_commands():
    while True:
        for cmd in CHAT_COMMANDS:
            send_chat(cmd)
        time.sleep(COMMAND_DELAY)

def clicker():
    while True:
        print("🖱 Клик")
        # Здесь можно добавить боевой клик (UseItemPacket или AttackEntityPacket)
        time.sleep(CLICKER_DELAY)

def select_slot(window_id, slot):
    packet = ClickWindowPacket()
    packet.window_id = window_id
    packet.slot = slot
    packet.button = 0
    packet.action_number = 1
    packet.mode = 0
    packet.clicked_item = None
    connection.write_packet(packet)
    print(f"✅ Клик по слоту {slot} в окне {window_id}")

def use_compass():
    packet = UseItemPacket()
    packet.hand = 0
    connection.write_packet(packet)
    print("🧭 ПКМ по компасу")

# ---------- ОБРАБОТЧИКИ ----------
def on_join_game(packet):
    print("✅ Бот зашёл на сервер. Жду капчу...")

def on_map_data(packet):
    print("📸 Получена капча")
    width, height = 128, 128
    img = Image.new("RGB", (width, height))
    img.putdata([(c, c, c) for c in packet.data])
    os.makedirs("captcha", exist_ok=True)
    path = "captcha/captcha.png"
    img.save(path)
    try:
        os.startfile(path)
    except:
        print(f"Открой файл вручную: {path}")
    code = input("Введите капчу: ").strip()
    send_chat(code)
    time.sleep(1)
    send_chat(f"/login {PASSWORD}")
    time.sleep(2)
    use_compass()

def on_open_window(packet):
    print(f"📂 Открылось окно: {packet.window_id}, {packet.window_title}")
    if "Выбор режима" in packet.window_title or "Анархия" in packet.window_title:
        time.sleep(1)
        select_slot(packet.window_id, 15)
    elif "Выбор сервера" in packet.window_title:
        time.sleep(1)
        select_slot(packet.window_id, 19)
        threading.Thread(target=clicker, daemon=True).start()
        threading.Thread(target=repeat_commands, daemon=True).start()

def on_chat(packet):
    print(f"💬 Чат: {packet.json_data}")

# ---------- РЕГИСТРАЦИЯ ----------
connection.register_packet_listener(on_join_game, JoinGamePacket)
connection.register_packet_listener(on_map_data, MapDataPacket)
connection.register_packet_listener(on_open_window, OpenWindowPacket)
connection.register_packet_listener(on_chat, ChatPacket)

# ---------- ЗАПУСК ----------
connection.connect()
