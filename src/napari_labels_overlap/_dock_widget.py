"""
Input: two labels layers
Output: labels layer
"""
from napari_plugin_engine import napari_hook_implementation
from magicgui import magic_factory
from napari.types import LabelsData

from enum import Enum
import numpy as np

#TO DO
class Operation(Enum):
    a_or_b = np.add
    a_and_b = np.add

@magic_factory
def labels_overlap(layerA: LabelsData, layerB: LabelsData, operation: Operation) -> LabelsData:
    if layerA is not None and layerB is not None:
        return (operation.value(layerA, layerB))
    else:
        #TO DO: add error message
        return 0


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return [labels_overlap]