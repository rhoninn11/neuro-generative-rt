import bpy

def check_node_group_avail(ng_name):
    avail_groups = bpy.data.node_groups
    names = [ng.name for ng in avail_groups]
    print(names)
    return ng_name in names


def apply_geo_node(obj):
    ng_name = "more_complex_saved_geo_node"
    if not check_node_group_avail(ng_name):
        print("!!! node group not found !!!")
        return
    
    has_ng = any(mod.type == 'NODES' for mod in obj.modifiers)
    if has_ng:
        return
   
    my_ng = bpy.data.node_groups[ng_name]
    mod = obj.modifiers.new(name="script_spawned_geo_node", type='NODES')
    mod.node_group = my_ng

def apply_geo_node_for_active():
    obj = bpy.context.active_object
    if obj:
        apply_geo_node(obj)

def apply_geo_node_named_obj(object_name):
    obj = bpy.data.objects.get(object_name)
    if obj:
        apply_geo_node(obj)