import bpy


def get_shader_node_by_type(material, node_type):
    mat_node = None
    for node in material.node_tree.nodes:
        if node.type == node_type:
            mat_node = node
            break
    return mat_node

class JSWK_OT_DisconnectDisplacement(bpy.types.Operator):
    bl_idname = "toggledisplacement.disconnect_displacement"
    bl_label = "Import Images"
    bl_description = "Import new reference images"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selection = context.selected_objects
        for obj in selection:
            print(obj.name)
            mat_slots = obj.material_slots
            for ms in mat_slots:
                print(ms.name)
                mat = bpy.data.materials.get(ms.name)
                material_output = get_shader_node_by_type(mat, 'OUTPUT_MATERIAL')
                if material_output is not None:
                    input_socket = material_output.inputs['Displacement']
                    if input_socket.is_linked:
                        for link in input_socket.links:
                            #linked_node = link.from_node
                            #linked_socket = link.from_socket
                            mat.node_tree.links.remove(link)
        return {'FINISHED'} 
            

class JSWK_OT_ConnectDisplacement(bpy.types.Operator):
    bl_idname = "toggledisplacement.connect_displacement"
    bl_label = "Import Images"
    bl_description = "Import new reference images"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selection = context.selected_objects
        for obj in selection:
            print(obj.name)
            mat_slots = obj.material_slots
            for ms in mat_slots:
                print(ms.name)
                mat = bpy.data.materials.get(ms.name)
                displacement = get_shader_node_by_type(mat, 'DISPLACEMENT')
                if displacement is not None:
                    output_socket = displacement.outputs['Displacement']
                    if not output_socket.is_linked:
                        material_output = get_shader_node_by_type(mat, 'OUTPUT_MATERIAL')
                        if material_output is not None:
                            mat.node_tree.links.new(material_output.inputs['Displacement'], displacement.outputs['Displacement'])
        return {'FINISHED'}


classes = (
            JSWK_OT_DisconnectDisplacement,
            JSWK_OT_ConnectDisplacement,
           )