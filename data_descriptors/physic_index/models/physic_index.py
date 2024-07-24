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
     'default_prefix': 'physic',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/PhysicSchema',
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'physic_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'institution': {'prefix_prefix': 'institution',
                                  'prefix_reference': 'http://es-vocab.ipsl.fr/institution/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'physic': {'prefix_prefix': 'physic',
                             'prefix_reference': 'http://es-vocab.ipsl.fr/physic_index/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'ror': {'prefix_prefix': 'ror',
                          'prefix_reference': 'https://ror.org/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'schemas/physic_index.yaml',
     'title': 'physic schema',
     'types': {'string': {'base': 'str',
                          'description': 'A character string',
                          'exact_mappings': ['schema:Text'],
                          'from_schema': 'http://es-vocab.ipsl.fr/PhysicSchema',
                          'name': 'string',
                          'notes': ['In RDF serializations, a slot with range of '
                                    'string is treated as a literal or type '
                                    'xsd:string.   If you are authoring schemas in '
                                    'LinkML YAML, the type is referenced with the '
                                    'lower case "string".'],
                          'uri': 'xsd:string'}}} )


class PhysicIndex(ConfiguredBaseModel):
    """
    index describing a run TODO IMPROVE THIS
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:physic',
         'from_schema': 'http://es-vocab.ipsl.fr/PhysicSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['physic_index']} })
    validation_method: str = Field("regex", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['physic_index'],
         'ifabsent': 'string(regex)'} })
    regex: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'regex', 'domain_of': ['physic_index']} })
    description: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['physic_index']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PhysicIndex.model_rebuild()
