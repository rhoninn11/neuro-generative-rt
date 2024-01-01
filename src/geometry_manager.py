from utils.singleton_meta import singleton_meta

import ng_utils
import importlib
importlib.reload(ng_utils)

import bpy
import math

class geometry_manager(metaclass=singleton_meta):

    def __init__(self):
        print(f"+++ geometry_manager init +++")

    def _primitive_name(self, base, idx):
        name = f"{base}"
        if idx > 0:
            name = f"{name}.{idx:03d}"
        return name

    def spawn_cubes(self):
        cube_names = []
        cube_num = 10
        distance = 20
        delta = distance / (cube_num - 1)

        for i in range(cube_num):
            loc = (i * delta, 0, 0)
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=loc, scale=(1, 1, 1))
            cube_names.append(self._primitive_name("Cube", i))

        return cube_names

    def apply_geo_node(self, cube_names):
        for name in cube_names:
            ng_utils.apply_geo_node_named_obj(name)

    def set_proper_transforms(self, cube_names):
        for name in cube_names:
            obj = bpy.data.objects.get(name)
            if obj:
                obj.rotation_euler[1] = math.radians(90)