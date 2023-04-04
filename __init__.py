from . import (
    operators,
    panels,
    properties,
)

import bpy
from bpy.props import PointerProperty

bl_info = {
    "name": "Toggle Displacement",
    "author": "joaulo <jsoftworks@joaulo.com>",
    "version": (1, 0, 0),
    "blender": (2, 90, 0),
    "category": "Material",
    "location": "View3D > Sidebar > Displacement",
    "description": "Enable/disable displacement on selected objects",
    # "warning": "",  # used for warning icon and text in addons panel
    # "doc_url": "https://",
    # "tracker_url": "",
}

classes = properties.classes + operators.classes + panels.classes


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.ToggleDisplacement = PointerProperty(
        type=properties.ToggleDisplacementProperties)


def unregister():
    del bpy.types.Scene.ToggleDisplacement
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
