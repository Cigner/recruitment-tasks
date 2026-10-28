import time
import random
import os
import pty

master, slave = pty.openpty()
port_name = os.ttyname(slave)

print("==================================================")
print(" 🛰️ Symulator Czujnika Wiertła (Level 2) Uruchomiony")
print(f" 🔌 Twój wirtualny port COM to: {port_name}")
print(" 📡 Podłącz do niego swój węzeł ROS2 i czytaj dane.")
print("==================================================\n")

step = 0
try:
    while True:
        step += 1
        # Co 15 sekund symulujemy zakłócenie na linii UART (test obsługi wyjątków)
        if step % 15 == 0:
            frame = b"TEMP:ERR_CRC_FAIL\n"
        else:
            temp = round(random.uniform(20.0, 50.0), 1)
            frame = f"TEMP:{temp}\n".encode('utf-8')
            
        os.write(master, frame)
        print(f"[TX -> {port_name}] Wysłano: {frame.decode('utf-8').strip()}")
        time.sleep(0.2)
        
except KeyboardInterrupt:
    print("\nZamykanie symulatora...")
