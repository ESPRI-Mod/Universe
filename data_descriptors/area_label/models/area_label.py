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
     'default_prefix': 'area_label',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/areaLabelSchema',
     'imports': ['linkml:types'],
     'name': 'area_label_schema',
     'prefixes': {'area_label': {'prefix_prefix': 'area_label',
                                 'prefix_reference': 'http://es-vocab.ipsl.fr/area_label/'},
                  'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'schemas/area_label.yaml'} )


class AreaLabel(ConfiguredBaseModel):
    """
    The areaLabelDD is somewhat reminiscent of the \"realm\" attribute defined in CMIP6 but is used exclusively in identifying the \"area type\" over which a variable is reported. 

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:area_label',
         'from_schema': 'http://es-vocab.ipsl.fr/areaLabelSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Area_label'], 'slot_uri': 'horizontal:id'} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Area_label'],
         'ifabsent': 'string(list)',
         'slot_uri': 'es-vocab:validation_method'} })
    label: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['Area_label']} })
    description: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Area_label']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AreaLabel.model_rebuild()
