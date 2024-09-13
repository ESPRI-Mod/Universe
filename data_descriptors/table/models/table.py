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
     'default_prefix': 'table',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/tableSchema',
     'imports': ['linkml:types'],
     'name': 'table_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'table': {'prefix_prefix': 'table',
                            'prefix_reference': 'http://es-vocab.ipsl.fr/table/'}},
     'source_file': 'schemas/table.yaml'} )


class Table(ConfiguredBaseModel):
    """
    a table defines a set of climate model outputs, describing which variables should be recorded, their frequency, dimensions, and the contexts (such as atmosphere, ocean, or land surface).  Commun exemples:  Amon: Monthly data for atmospheric variables (e.g., temperature, wind speed, humidity). Omon: Monthly data for ocean variables (e.g., sea surface temperature, ocean currents). Lmon: Monthly data for land surface variables (e.g., soil moisture, surface temperature).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:table',
         'from_schema': 'http://es-vocab.ipsl.fr/tableSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Table'], 'slot_uri': 'table:id'} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Table'],
         'ifabsent': 'string(list)',
         'slot_uri': 'es-vocab:validation_method'} })
    variable_entry: List[str] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'variable_entry', 'domain_of': ['Table']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Table.model_rebuild()
