from utils.singleton_meta import singleton_meta

import ng_utils
import importlib
importlib.reload(ng_utils)

import bpy
import math

class geometry_manager(metaclass=singleton_meta):

    def __init__(self):
        print(f"+++ geometry_manager init +++")
        self.cube_num = 0

    def restart(self):
        self.cube_num = 0

    def _primitive_name(self, base):
        idx = self.cube_num
        name = f"{base}"
        if idx > 0:
            name = f"{name}.{idx:03d}"
        self.cube_num += 1
        return name

    def spawn_cubes(self, at_x=0, cube_num=1, delta=0.2):
        cube_names = []

        for i in range(cube_num):
            name = self._primitive_name("Cube")
            transform = {
                "location": (i * delta + at_x, 0, 0),
                "scale": (1, 1, 1),
                "rotation": (0, math.radians(90), 0)
            
            }
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', **transform)
            ng_utils.apply_geo_node_named_obj(name)
            print(f"+++ spawned cube: {name} - geo aplied+++")
            cube_names.append(name)

        return cube_names
