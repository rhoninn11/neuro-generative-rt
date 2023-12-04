import math
import bpy
import time

def set_cube_z_pos(name: str, value: float):
    obj = bpy.data.objects.get(name)
    if obj:
        obj.location.z = value

def set_cube_scale(name: str, value: float):
    obj = bpy.data.objects.get(name)
    if obj:
        obj.scale[0] = value
        obj.scale[1] = value
        obj.scale[2] = value


def cubes_osc(names: list[str], data: list[list[float]]):

    pos_data = data[0]
    scale_data = data[1]
    color_data = data[2]

    common_len = min(len(names), len(pos_data),
                     len(scale_data), len(color_data))
    _names = names[:common_len]
    _pos_data = pos_data[:common_len]
    _scale_data = scale_data[:common_len]
    _color_data = color_data[:common_len]

    for name, pos, scale, color in zip(_names, _pos_data, _scale_data, _color_data):
        set_cube_z_pos(name, pos)
        set_cube_scale(name, scale)