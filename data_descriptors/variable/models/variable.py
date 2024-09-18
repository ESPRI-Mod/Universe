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
     'default_prefix': 'variable',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/variableSchema',
     'imports': ['linkml:types'],
     'name': 'variable_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'variable': {'prefix_prefix': 'variable',
                               'prefix_reference': 'http://es-vocab.ipsl.fr/variable/'}},
     'source_file': 'schemas/variable.yaml'} )


class Variable(ConfiguredBaseModel):
    """
    
    a variable refers to a specific type of climate-related quantity or measurement that is simulated and stored in a data file. These variables represent key physical, chemical, or biological properties of the Earth system and are outputs from climate models.
    Each variable captures a different aspect of the climate system, such as temperature, precipitation, sea level, radiation, or atmospheric composition.
    Examples of Variables: tas: Near-surface air temperature (often measured at 2 meters above the surface) pr: Precipitation psl: Sea level pressure zg: Geopotential height rlut: Top-of-atmosphere longwave radiation siconc: Sea ice concentration co2: Atmospheric CO2 concentration

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:variable',
         'from_schema': 'http://es-vocab.ipsl.fr/variableSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Variable'], 'slot_uri': 'variable:id'} })
    cmip_acronym: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'cmip_acronym', 'domain_of': ['Variable']} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Variable'],
         'ifabsent': 'string(list)',
         'slot_uri': 'variable:validation_method'} })
    long_name: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'long_name',
         'domain_of': ['Variable'],
         'slot_uri': 'variable:long_name'} })
    standard_name: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'standard_name',
         'domain_of': ['Variable'],
         'slot_uri': 'variable:standard_name'} })
    type: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Variable']} })
    units: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Variable.model_rebuild()
