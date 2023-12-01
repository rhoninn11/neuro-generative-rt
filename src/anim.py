import math
import bpy
import time

def cube_osc(name: str, freq: float, tp: float):
    sine_value = math.sin(2 * math.pi * freq * tp)
    obj = bpy.data.objects.get(name)
    if obj:
        obj.location.z = sine_value

def cubes_osc(names: list[str], freq: float):
    # print(f"--- frame {bpy.context.scene.frame_current} ---")
    tp = time.time()
    td = 1 / len(names)
    for i, name in enumerate(names):
        cube_osc(name, freq, tp + td * i)

def setup_animation(names):
    freq = 1
    anim_handler = lambda scene: cubes_osc(names, freq)
    bpy.app.handlers.frame_change_pre.append(anim_handler)

    print(f"--- animation setup done ---")