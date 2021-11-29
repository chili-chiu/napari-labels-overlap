"""
Input: two labels layers
Output: labels layer
"""
from napari_plugin_engine import napari_hook_implementation
from magicgui import magic_factory
from napari.types import LabelsData

from enum import Enum
import numpy as np

def aORb(a,b):
    return (a+b > 0).astype(int)

def aANDb(a,b):
    (a+b > 1).astype(int)

def aNOTb(a,b):
    (a-b > 0).astype(int)

class Operation(Enum):
    test = np.add
    a_OR_b = aORb
    #a_AND_b = aANDb
    #a_NOT_b = aNOTb

@magic_factory
def labels_overlap(layerA: LabelsData, layerB: LabelsData, operation: Operation) -> LabelsData:
    if layerA is not None and layerB is not None:
        bin_A = (layerA > 0).astype(int)
        bin_B = (layerB > 0).astype(int)
        return operation.value(bin_A, bin_B)
    else:
        #TO DO: add error message
        return 0

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return [labels_overlap]