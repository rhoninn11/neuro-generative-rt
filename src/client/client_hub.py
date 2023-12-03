
import bpy
from client.client_thread import client_thread
from utils.singleton_meta import singleton_meta

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
        if not self.is_running:
            return
        
        print(f"+++ stopping thread")
        self.thread.stop()
        self.is_running = False

    def elo(self):
        
        anim_frames = self.thread.out_queue.queue_len()
        data = self.thread.out_queue.dequeue_item()
        self.last_data = data
        print(f"+++ anim_frames: {anim_frames}")
        print(f"+++ data: {data}")

    def setup_animation(self, names):
        freq = 1
        anim_handler = lambda scene: self.elo()
        # anim_handler = lambda scene: cubes_osc(names, freq)
        bpy.app.handlers.frame_change_pre.append(anim_handler)

        print(f"--- animation setup done ---")