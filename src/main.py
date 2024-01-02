
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

import geometry_manager as gm
importlib.reload(gm)

import camera_manager as cm
importlib.reload(cm)

# -------------------- main --------------------

import bpy
import math 

def spawn_content():
    cm.camera_manager().spawn_camera()
    gm.geometry_manager().restart()
    # cube_names = gm.geometry_manager().spawn_cubes()
    return ["elo"]


def animate_all(scene):
    chb.client_hub().animate_by_server()
    cm.camera_manager().animate_camera()

def setup_animation(cube_names):
    chb.client_hub().set_cube_names(cube_names)
    bpy.app.handlers.frame_change_pre.append(animate_all)
    print(f"--- animation setup done ---")

def clear_animation():
    while(len(bpy.app.handlers.frame_change_pre) != 0):
        bpy.app.handlers.frame_change_pre.pop()

    print(f"--- animation cleared ---")


def main():
    """
    Python code to generate an animated geo nodes node tree
    that consists of a subdivided & triangulated cube with animated faces
    """
    # clean_scene()
    helpers.scene_setup()

    cube_names = spawn_content()
    clear_animation()
    print(f"--- animation cleared ---")
    print(f"{cube_names}")
    setup_animation(cube_names)
    chb.client_hub().start()

    print("--- script done ---")


if __name__ == "__main__":
    main()