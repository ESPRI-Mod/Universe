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
     'default_prefix': 'esvocab',
     'default_range': 'string',
     'id': 'http://127.0.0.1:8000/uri/InstitutionSchema',
     'imports': ['linkml:types'],
     'name': 'institution_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://127.0.0.1:8000/uri/'},
                  'institution': {'prefix_prefix': 'institution',
                                  'prefix_reference': 'http://127.0.0.1:8000/uri/institution/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'ror': {'prefix_prefix': 'ror',
                          'prefix_reference': 'https://ror.org/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'schemas/institution.yaml'} )


class Institution(ConfiguredBaseModel):
    """
    an registered institution for WCRP modelisation MIP
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:institution',
         'from_schema': 'http://127.0.0.1:8000/uri/InstitutionSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Institution', 'Location'],
         'slot_uri': 'institution:id'} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Institution'],
         'ifabsent': 'string(list)',
         'slot_uri': 'institution:validation_method'} })
    acronyms: List[str] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'acronyms',
         'domain_of': ['Institution'],
         'slot_uri': 'institution:acronyms'} })
    aliases: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'aliases',
         'domain_of': ['Institution'],
         'slot_uri': 'schema:alternateName'} })
    established: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'established',
         'domain_of': ['Institution'],
         'slot_uri': 'schema:foundingDate'} })
    type: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Institution']} })
    labels: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'labels', 'domain_of': ['Institution']} })
    location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['Institution'],
         'slot_uri': 'schema:location'} })
    name: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Institution']} })
    rorIdentifier: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'rorIdentifier', 'domain_of': ['Institution'], 'slot_uri': 'ror:id'} })
    cmip_acronym: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'cmip_acronym', 'domain_of': ['Institution']} })
    url: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Institution']} })


class Location(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:location',
         'from_schema': 'http://127.0.0.1:8000/uri/InstitutionSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Institution', 'Location']} })
    lat: float = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'lat', 'domain_of': ['Location']} })
    lon: float = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'lon', 'domain_of': ['Location']} })
    city: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'city', 'domain_of': ['Location']} })
    country: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'country', 'domain_of': ['Location']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Institution.model_rebuild()
Location.model_rebuild()
