
import bpy
from client.client_thread import client_thread
from utils.singleton_meta import singleton_meta
import importlib

import anim
importlib.reload(anim) 

from anim import cubes_osc

class client_hub(metaclass=singleton_meta):
    def __init__(self):
        self.host = 'localhost'
        self.port = 4444
        self.thread = client_thread("client_thread")
        self.is_running = False
        self.last_data = []

    def start(self):
        if self.is_running:
            return
        
        print(f"+++ starting thread")
        self.thread.config_host_dst(self.host, self.port)
        self.thread.start()
        self.is_running = True

    def stop(self):
        self.clear_animation()
        if not self.is_running:
            return
        
        print(f"+++ stopping thread")
        self.thread.stop()
        self.is_running = False

    def data_overflow_sync(self):
        anim_frames = self.thread.out_queue.queue_len()
        if anim_frames > 10:
            print(f"--- data overflow: {anim_frames} ---")
            for _ in range(anim_frames - 5):
                self.thread.out_queue.dequeue_item()

    def animate_by_server(self, cube_names):
        self.data_overflow_sync()
        self.last_data = self.thread.out_queue.dequeue_item()
        cubes_osc(cube_names, self.last_data)

    def clear_animation(self):
        while(len(bpy.app.handlers.frame_change_pre) != 0):
            bpy.app.handlers.frame_change_pre.pop()

        print(f"--- animation cleared ---")

    def setup_animation(self, names):
        anim_handler = lambda scene: self.animate_by_server(names)
        bpy.app.handlers.frame_change_pre.append(anim_handler)
        print(f"--- animation setup done ---")