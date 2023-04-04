import bpy
from bpy.props import StringProperty, CollectionProperty


class ToggleDisplacementProperties(bpy.types.PropertyGroup):
    collectionName: StringProperty(
        name='Displacement node socket', 
        default="Displacement"
    )

classes = (ToggleDisplacementProperties,)