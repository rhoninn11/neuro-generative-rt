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
        bpy.context.scene.camera = bpy.data.objects["Camera"]

    def animate_camera(self):
        print(f"+++ animate_camera +++")

        cam = bpy.data.objects["Camera"]
        cam.location[0] -= 0.02