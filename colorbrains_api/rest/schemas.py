from typing import *

from pydantic import BaseModel


class BaseSchema(BaseModel):
    @property
    def tablename(self) -> str:
        raise Exception("Implement In Subclass")

    @property
    def schemaname(self) -> str:
        raise Exception("Implement In Subclass")


class RGBColor(BaseModel):
    red: float
    green: float
    blue: float


class MatplotlibBaseSchema(BaseSchema):
    @property
    def schemaname(self) -> str:
        return "matplotlib"


class NamedColors(MatplotlibBaseSchema, RGBColor):
    color_name: str

    @property
    def tablename(self) -> str:
        return "namedcolors"


class CategorizedColorMapsMeta(MatplotlibBaseSchema):
    categorical_name: str
    colormap_name: str
    cmap_n_total: int

    @property
    def tablename(self) -> str:
        return "categorizedcolormaps"


class ColorMaps(MatplotlibBaseSchema, RGBColor):
    cmap_n_observation: int
    colormap_name: str

    @property
    def tablename(self) -> str:
        return "colormaps"


class CategorizedColorMaps(BaseModel):
    categorical_name: str
    colormap_name: str
    colormaps: List[RGBColor]


class ManyNamedColors(BaseModel):
    named_colors: List[NamedColors]
