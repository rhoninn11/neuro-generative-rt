
import bpy

def deactivate_obj(obj=None):
    if obj:
        obj.select_set(False)
    bpy.context.view_layer.objects.active = None