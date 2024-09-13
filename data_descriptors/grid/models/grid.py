from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    ClassVar,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        RootModel,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "allow",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_curi_maps': ['semweb_context'],
     'default_prefix': 'grid',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/gridSchema',
     'imports': ['linkml:types'],
     'name': 'grid_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'grid': {'prefix_prefix': 'grid',
                           'prefix_reference': 'http://es-vocab.ipsl.fr/grid/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'schemas/grid.yaml'} )


class Grid(ConfiguredBaseModel):
    """
    In the context of CMIP6, the grid_label refers to a standardized identifier that describes the specific grid or spatial resolution on which a climate model's output data is provided. Climate models use different grids to discretize the Earth's surface and atmosphere for numerical simulations, and the grid_label helps users distinguish between various types of model grids and resolutions.
    The grid_label is part of the metadata for a model's output and typically provides information on:
    Type of grid (e.g., regular latitude-longitude grid, rotated pole grid, etc.). Horizontal resolution (e.g., coarse vs fine resolution). Whether the grid is native or regridded to a common format for ease of comparison. Common grid_labels in CMIP6: gn: Native grid. This represents the original grid used by the climate model in its simulation. gr: Regridded to a regular latitude-longitude grid. This is typically done to standardize model outputs across different models. gm: A grid where the data is zonally averaged (averaged over longitude).        

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:grid',
         'from_schema': 'http://es-vocab.ipsl.fr/gridSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Grid'], 'slot_uri': 'grid:id'} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Grid'],
         'ifabsent': 'string(list)',
         'slot_uri': 'es-vocab:validation_method'} })
    label: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['Grid']} })
    description: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Grid']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Grid.model_rebuild()
