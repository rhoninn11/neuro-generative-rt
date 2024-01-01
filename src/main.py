
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

import geometry_spawner as gs
importlib.reload(gs)
geometry_spawner = gs.geometry_spawner()

# -------------------- main --------------------

import bpy
import math 

def spawn_content():
    cube_names = geometry_spawner.spawn_cubes()
    geometry_spawner.apply_geo_node(cube_names)
    geometry_spawner.set_proper_transforms(cube_names)

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