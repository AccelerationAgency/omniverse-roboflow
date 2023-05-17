__all__ = ["roboflow_export_window_style"]

from omni.ui import color as cl
from omni.ui import constant as fl
from omni.ui import url
import omni.kit.app
import omni.ui as ui
import pathlib


EXTENSION_FOLDER_PATH = pathlib.Path(
    omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module(__name__)
)

# Pre-defined constants. It's possible to change them runtime.
cl.roboflow_export_window_attribute_bg = cl("#1f2124")
cl.roboflow_export_window_attribute_fg = cl("#0f1115")
cl.roboflow_export_window_hovered = cl("#FFFFFF")
cl.roboflow_export_window_text = cl("#CCCCCC")
fl.roboflow_export_window_attr_hspacing = 10
fl.roboflow_export_window_attr_spacing = 1
fl.roboflow_export_window_group_spacing = 2
url.roboflow_export_window_icon_closed = f"{EXTENSION_FOLDER_PATH}/data/closed.svg"
url.roboflow_export_window_icon_opened = f"{EXTENSION_FOLDER_PATH}/data/opened.svg"

# The main style dict
roboflow_export_window_style = {
    "Label::attribute_name": {
        "alignment": ui.Alignment.RIGHT_CENTER,
        "margin_height": fl.roboflow_export_window_attr_spacing,
        "margin_width": fl.roboflow_export_window_attr_hspacing,
    },
    "Label::attribute_name:hovered": {"color": cl.roboflow_export_window_hovered},
    "Label::collapsable_name": {"alignment": ui.Alignment.LEFT_CENTER},
    "Slider::attribute_int:hovered": {"color": cl.roboflow_export_window_hovered},
    "Slider": {
        "background_color": cl.roboflow_export_window_attribute_bg,
        "draw_mode": ui.SliderDrawMode.HANDLE,
    },
    "Slider::attribute_float": {
        "draw_mode": ui.SliderDrawMode.FILLED,
        "secondary_color": cl.roboflow_export_window_attribute_fg,
    },
    "Slider::attribute_float:hovered": {"color": cl.roboflow_export_window_hovered},
    "Slider::attribute_vector:hovered": {"color": cl.roboflow_export_window_hovered},
    "Slider::attribute_color:hovered": {"color": cl.roboflow_export_window_hovered},
    "CollapsableFrame::group": {"margin_height": fl.roboflow_export_window_group_spacing},
    "Image::collapsable_opened": {"color": cl.roboflow_export_window_text, "image_url": url.roboflow_export_window_icon_opened},
    "Image::collapsable_closed": {"color": cl.roboflow_export_window_text, "image_url": url.roboflow_export_window_icon_closed},
}
