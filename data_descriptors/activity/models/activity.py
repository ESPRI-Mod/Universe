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
     'default_prefix': 'activity',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/ActivitySchema',
     'imports': ['linkml:types'],
     'name': 'activity_schema',
     'prefixes': {'activity': {'prefix_prefix': 'activity',
                               'prefix_reference': 'http://es-vocab.ipsl.fr/activity/'},
                  'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'ror': {'prefix_prefix': 'ror',
                          'prefix_reference': 'https://ror.org/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'schemas/activity.yaml'} )


class Activity(ConfiguredBaseModel):
    """
    an 'activity' refers to a coordinated set of modeling experiments designed to address specific scientific questions or objectives. Each activity is focused on different aspects of climate science and utilizes various models to study a wide range of climate phenomena. Activities are often organized around key research themes and may involve multiple experiments, scenarios, and model configurations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:institution',
         'from_schema': 'http://es-vocab.ipsl.fr/ActivitySchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Activity'], 'slot_uri': 'activity:id'} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Activity'],
         'ifabsent': 'string(list)',
         'slot_uri': 'es-vocab:validation_method'} })
    name: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Activity']} })
    long_name: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Activity']} })
    cmip_acronym: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'cmip_acronym', 'domain_of': ['Activity']} })
    url: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Activity']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Activity.model_rebuild()
