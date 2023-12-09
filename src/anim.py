import math
import bpy
import time
import importlib
import ng_ctrl_utils

importlib.reload(ng_ctrl_utils)

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

def set_cube_geo_node_values(name: str, values: list[float]):
    obj = bpy.data.objects.get(name)
    if obj:
        ng_ctrl_utils.apply_geo_node_control(obj, values)


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

    result = {}
    for name, pos, scale, color in zip(_names, _pos_data, _scale_data, _color_data):
        
        param_1_offset = 0.75
        param_1_scale = 1.45 - param_1_offset

        param_2_offset = 0.45
        param_2_scale = 1.45 - param_2_offset   

        param_3_offset = 0.00
        param_3_scale = 0.1 - param_3_offset

        values = [
            param_1_offset + param_1_scale * pos,
            param_2_offset + param_2_scale * scale,
            param_3_offset + param_3_scale * color
        ] 
        set_cube_geo_node_values(name, values)
        # result[name] = values
        # set_cube_z_pos(name, pos)
        # set_cube_scale(name, scale)
    # print(result)?
    bpy.context.view_layer.update()