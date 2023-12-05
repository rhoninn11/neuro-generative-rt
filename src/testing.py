import bpy

# Zakładając, że twoim obiektem jest aktywny obiekt
obj = bpy.context.active_object
mod_num = len(obj.modifiers)

avail_groups = bpy.data.node_groups

names = [ng.name for ng in avail_groups]
md = obj.modifiers[0]
ng = md.node_group
nodes = ng.nodes

ins = nodes["Group Input"].inputs
outs = nodes["Group Input"].outputs


print(obj.name)
print(mod_num)
print(avail_groups)
print(names)
print(nodes)
print(ins)
print(outs)

md_names = [ mdkey for mdkey in md.keys() ]
o_names = [ ou.name for ou in outs ]

print(o_names)
print(md_names)

for key in md_names:
    print(md[key])