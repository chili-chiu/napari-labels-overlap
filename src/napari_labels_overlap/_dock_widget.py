"""
Input: two labels layers
Output: labels layer
"""
from napari_plugin_engine import napari_hook_implementation
from napari.types import LabelsData
from enum import Enum
from functools import partial

def aORb(a,b):
     return (a+b > 0).astype(int)

def aANDb(a,b):
    return (a+b > 1).astype(int)

def aNOTb(a,b):
    return (a-b > 0).astype(int)

# Enums check if the value of the member is a descriptor, and if so, don't add it
# partial() objects are not descriptors (don't have __get__, __set__, or __delete__), and therefore sneak through Enum's check
class Operation(Enum):
    A_OR_B = partial(aORb)
    A_AND_B = partial(aANDb)
    A_NOT_B = partial(aNOTb)

def labels_overlap(layerA: LabelsData, layerB: LabelsData, operation: Operation) -> LabelsData:
    if layerA is not None and layerB is not None:
        bin_A = (layerA > 0).astype(int)
        bin_B = (layerB > 0).astype(int)
        return operation.value(bin_A, bin_B)


@napari_hook_implementation
def napari_experimental_provide_function():
    return [labels_overlap]