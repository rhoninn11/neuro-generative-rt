
import bpy
from client.client_thread import client_thread
from utils.singleton_meta import singleton_meta
import importlib

import anim
importlib.reload(anim) 

from anim import cubes_osc, move_cube

import geometry_manager as gm
importlib.reload(gm)
from geometry_manager import geometry_manager

class client_hub(metaclass=singleton_meta):
    def __init__(self):
        self.host = 'localhost'
        self.port = 4444
        self.thread = client_thread("client_thread")
        self.is_running = False
        self.last_data = []

        self.cube_names = []

        self.main_cube_name = None
        self.main_position = 0
        self.frame_counter = 30
        self.do_started = False

    def set_cube_names(self, cube_names):
        self.cube_names = cube_names
        self.main_cube_name = cube_names[len(cube_names)-1]

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
        self.do_started = False

    def data_overflow_sync(self):
        anim_frames = self.thread.out_queue.queue_len()
        if anim_frames > 10:
            print(f"--- data overflow: {anim_frames} ---")
            for _ in range(anim_frames - 5):
                self.thread.out_queue.dequeue_item()

    def animate_by_server(self, motion_speed=0.02):
        self.data_overflow_sync()
        if self.thread.out_queue.queue_len() == 0:
            return
        
        if not self.do_started:
            self.do_started = True
            self.frame_counter = 0
        
        self.last_data = self.thread.out_queue.dequeue_item()

        x_pre_frame = -motion_speed
        self.main_position += x_pre_frame

        self.frame_counter += 1
        if self.frame_counter >= 30:
            self.frame_counter = 0
            cubes = geometry_manager().spawn_cubes(at_x=self.main_position)
            self.set_cube_names(cubes)
            print(f" main cube name: {self.main_cube_name}")
            
        
        move_cube(self.main_cube_name, x_pre_frame)
        cubes_osc([self.main_cube_name], self.last_data)

        