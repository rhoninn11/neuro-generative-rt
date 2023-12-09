
import sys
import os
import importlib

def get_pwd():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

def config_for_multifile_python():
    my_pwd = get_pwd()
    sys_dir_split = "\\" # windows
    proj_dir = sys_dir_split.join(my_pwd.split(sys_dir_split)[:-1])
    script_dir = f"{proj_dir}{sys_dir_split}src"
    
    if script_dir in sys.path:
        sys.path.remove(script_dir)
            
    sys.path.append(script_dir)
    # print(f"{sys.path}")

# -------------------- bootstrap --------------------
config_for_multifile_python()

import helpers
import anim
import ng_utils
importlib.reload(helpers)
importlib.reload(anim)
importlib.reload(ng_utils)

# from client.client_hub import client_hub
# client_hub().stop_connection()
# importlib.reload(client_hub)

import client.client_hub as chb
chb.client_hub().stop()
importlib.reload(chb)
client_hub = chb.client_hub

# -------------------- main --------------------

import bpy
import math
def primitive_name(base, idx):
    name = f"{base}"
    if idx > 0:
        name = f"{name}.{idx:03d}"
    return name

def spawn_cubes():
    cube_names = []
    cube_num = 10
    distance = 20
    delta = distance / (cube_num - 1)

    for i in range(cube_num):
        loc = (i * delta, 0, 0)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=loc, scale=(1, 1, 1))
        cube_names.append(primitive_name("Cube", i))

    return cube_names

def apply_geo_node(cube_names):
    for name in cube_names:
        ng_utils.apply_geo_node_named_obj(name)

def set_proper_transforms(cube_names):
    for name in cube_names:
        obj = bpy.data.objects.get(name)
        if obj:
            obj.rotation_euler[1] = math.radians(90)
    

def spawn_content():
    cube_names = spawn_cubes()
    apply_geo_node(cube_names)
    set_proper_transforms(cube_names)

    return cube_names

def main():
    """
    Python code to generate an animated geo nodes node tree
    that consists of a subdivided & triangulated cube with animated faces
    """
    # clean_scene()
    helpers.scene_setup()

    cube_names = spawn_content()
    # anim.setup_animation(cube_names)
    client_hub().setup_animation(cube_names)
    client_hub().start()

    print("--- script done ---")


if __name__ == "__main__":
    main()