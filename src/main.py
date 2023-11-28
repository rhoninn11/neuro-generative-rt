
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
    script_dir = f"{proj_dir}{sys_dir_split}py"
    
    if script_dir in sys.path:
        sys.path.remove(script_dir)
            
    sys.path.append(script_dir)
    print(f"{sys.path}")

# -------------------- bootstrap --------------------
config_for_multifile_python()

import helpers
importlib.reload(helpers)

# -------------------- main --------------------
def main():
    """
    Python code to generate an animated geo nodes node tree
    that consists of a subdivided & triangulated cube with animated faces
    """
    # clean_scene()
    print("elo")
    helpers.print_something()
    helpers.scene_setup()


if __name__ == "__main__":
    main()