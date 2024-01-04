from utils.singleton_meta import singleton_meta

import ng_utils
import importlib
importlib.reload(ng_utils)

import bpy
import math

class camera_manager(metaclass=singleton_meta):

    def __init__(self):
        print(f"+++ camera_manager init +++")

    def spawn_camera(self):

        cam_config = {
            'location': (-9.53, 7.52, 2.25),
            'rotation': (1.381, -0.09, -2.11),
            'scale': (1, 1, 1)
        }
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', **cam_config)
        camera = bpy.context.object
        bpy.context.scene.camera = camera
        # bpy.context.scene.camera = bpy.data.objects["Camera"]


        lgt_config = {
            'location': (0, 0, -7),
            'scale': (1, 1, 1)        
        }
        bpy.ops.object.light_add(type='POINT', align='WORLD', **lgt_config)
        light = bpy.context.object

        light.parent = camera
        light.data.energy = 200
        light.data.shadow_soft_size = 1


    def animate_camera(self, motion_speed=0.02):
        print(f"+++ animate_camera +++")

        cam = bpy.data.objects["Camera"]
        cam.location[0] += -motion_speed