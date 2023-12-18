import bpy

def select_geo_node_mod(obj):
    for mod in obj.modifiers:
        if mod.type == 'NODES':
            return mod
        
    return None

def gen_socket_namea(count):
    start_id = 2
    sock_names = []
    for i in range(count):
        sock_names.append(f"Socket_{start_id + i}")

    return sock_names


def apply_geo_node_control(obj, values):
    gn_mod = select_geo_node_mod(obj)
    if gn_mod is None:
        return
    
    sock_names = gen_socket_namea(len(values))
    # print(f"sock_names: {sock_names}")
    # print(f"values: {values}")
    for name, value in zip(sock_names, values):
        if name in gn_mod:
            gn_mod[name] = value

    gn_mod.show_on_cage = False


def apply_geo_node_for_active():
    obj = bpy.context.active_object
    if obj is None:
        return
    
    values = [1.0,0.9,0.0]
    apply_geo_node_control(obj, values)