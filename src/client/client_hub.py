

import socket
import importlib
import threading
import time

from utils.singleton_meta import singleton_meta

class simple_thread(threading.Thread):
    def script(self):
        print(f"+++elo")
        time.sleep(1)
        print(f"+++elo")
        time.sleep(1)
        print(f"+++elo")
        time.sleep(1)
        print(f"+++elo")
        time.sleep(1)
        print(f"+++elo")
        time.sleep(1)
        print(f"+++elo")
        time.sleep(1)
        print(f"+++elo")
        time.sleep(1)

    def run(self):
        self.script()

class thread_hub(metaclass=singleton_meta):
    def __init__(self):
        self.thread = None
        self.thread_active = False



class client_hub(metaclass=singleton_meta):
    def __init__(self):
        self.tcp_socket = None
        self.host = 'localhost'
        self.port = 4444
        self.connected = False
        self.thread = None

    def start_connection(self):
        if self.connected:
            self.stop_connection()
        
        server_address = (self.host, self.port)
        self.start_thread()
        try:
            tcp_s = socket.create_connection(server_address)
            tcp_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcp_s.bind(server_address)
            tcp_s.listen(1)
            
            self.tcp_socket = tcp_s
            self.connected = True
            print(f"+++ connected to {server_address}")
        except Exception as e:
            self.connected = False
            print(f"+++ error while connecting")
            

    def stop_connection(self):
        if not self.connected:
            return
        
        tcp_s = self.tcp_socket
        tcp_s.close()
        
        self.connected = False
        print(f"+++ disconnected")

    def start_thread(self):
        if self.thread is not None:
            return
        
        print(f"+++ starting thread")
        self.thread = simple_thread()
        self.thread.start()

    def stop_thread(self):
        if self.thread is None:
            return
        
        print(f"+++ stopping thread")
        self.thread.join()
        self.thread = None

    def setup_animation(names):
        freq = 1
        # anim_handler = lambda scene: cubes_osc(names, freq)
        # bpy.app.handlers.frame_change_pre.append(anim_handler)

        print(f"--- animation setup done ---")