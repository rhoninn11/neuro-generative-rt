import bpy

def select_geo_node_mod(obj):
    for mod in obj.modifiers:
        if mod.type == 'NODES':
            return mod
        
    return None

def apply_geo_node_control(obj, values):
    gn_mod = select_geo_node_mod(obj)
    if gn_mod is None:
        return
    
    names = ["Socket_2", "Socket_3", "Socket_4"]

    for name, value in zip(names, values):
        gn_mod[name] = value

    gn_mod.show_on_cage = False


def apply_geo_node_for_active():
    obj = bpy.context.active_object
    if obj is None:
        return
    
    values = [1.0,0.9,0.0]
    apply_geo_node_control(obj, values)