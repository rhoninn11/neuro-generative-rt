
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
    print(f"{sys.path}")

# -------------------- bootstrap --------------------
config_for_multifile_python()

import helpers
import anim
importlib.reload(helpers)
importlib.reload(anim)

import singleton_test
singleton_test.signleton_demo()

importlib.reload(singleton_test)

# -------------------- main --------------------

import bpy
def primitive_name(base, idx):
    name = f"{base}"
    if idx > 0:
        name = f"{name}.{idx:03d}"
    return name

def spawn_content():
    cube_names = []
    cube_num = 10
    distance = 20
    delta = distance / (cube_num - 1)

    for i in range(cube_num):
        loc = (i * delta, 0, 0)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=loc, scale=(1, 1, 1))
        cube_names.append(primitive_name("Cube", i))

    return cube_names



def main():
    """
    Python code to generate an animated geo nodes node tree
    that consists of a subdivided & triangulated cube with animated faces
    """
    # clean_scene()
    helpers.scene_setup()

    cube_names = spawn_content()
    anim.setup_animation(cube_names)
    singleton_test.signleton_demo()
    print("--- script done ---")


if __name__ == "__main__":
    main()