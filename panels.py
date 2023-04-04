import bpy


class JSWK_PT_ToggleDisplacement(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Material"
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}
    bl_idname = "JSWK_PT_OutlineGenerator"
    bl_label = "Displacement"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        col = layout.column()
        col.operator("jswk.disconnect_displacement", icon='REMOVE')
        col.operator("jswk.connect_displacement", icon='ADD')
        
        col.separator()



classes = (JSWK_PT_ToggleDisplacement,)