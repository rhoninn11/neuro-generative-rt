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

def apply_geo_node_for_active():
    obj = bpy.context.active_object
    if obj is None:
        return
    
    values = [1.0,0.9,0.0]
    apply_geo_node_control(obj, values)


    
apply_geo_node_for_active()

# mod_num = len(obj.modifiers)

# avail_groups = bpy.data.node_groups

# names = [ng.name for ng in avail_groups]
# md = obj.modifiers[0]
# ng = md.node_group
# nodes = ng.nodes

# ins = nodes["Group Input"].inputs
# outs = nodes["Group Input"].outputs


# print(obj.name)
# print(mod_num)
# print(avail_groups)
# print(names)
# print(nodes)
# print(ins)
# print(outs)

# md_names = [ mdkey for mdkey in md.keys() ]
# o_names = [ ou.name for ou in outs ]

# print(o_names)
# print(md_names)

# for key in md_names:
#     print(md[key])