from typing import *

from pydantic import BaseModel


class NamedColors(BaseModel):
    color_name: str
    red: float
    green: float
    blue: float


class CategorizedColorMaps(BaseModel):
    categorical_name: str
    colormap_name: str
    cmap_n_total: int


class ColorMaps(BaseModel):
    colormap_name: str
    cmap_n_observation: int
    red: float
    green: float
    blue: float
