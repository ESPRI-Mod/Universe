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
     'default_prefix': 'source',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/sourceschema',
     'imports': ['linkml:types'],
     'name': 'source_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'source': {'prefix_prefix': 'source',
                             'prefix_reference': 'http://es-vocab.ipsl.fr/source/'}},
     'source_file': 'schemas/source.yaml'} )


class Source(ConfiguredBaseModel):
    """
    a 'source' refers to a numerical representations of the Earth's climate system. They simulate the interactions between the atmosphere, oceans, land surface, and ice. These models are based on fundamental physical, chemical, and biological processes and are used to understand past, present, and future climate conditions. Each source or model is typically associated with a specific research institution, center, or group. For instance, models like 'EC-Earth' are developed by a consortium of European institutes, while 'GFDL-CM4' is developed by the Geophysical Fluid Dynamics Laboratory (GFDL) in the United States.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:source',
         'from_schema': 'http://es-vocab.ipsl.fr/sourceschema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Source', 'license_info'],
         'slot_uri': 'source:id'} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Source'],
         'ifabsent': 'string(list)',
         'slot_uri': 'es-vocab:validation_method'} })
    name: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Source']} })
    activity_participation: List[str] = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'activity_participation',
         'domain_of': ['Source'],
         'slot_uri': 'source:activity_participation'} })
    cohort: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'cohort', 'domain_of': ['Source'], 'slot_uri': 'source:cohort'} })
    institution_id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'institution_id',
         'domain_of': ['Source'],
         'slot_uri': 'source:institution'} })
    label_extended: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'label_extended',
         'domain_of': ['Source'],
         'slot_uri': 'source:label_extend'} })
    license_info: Optional[LicenseInfo] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'license_info',
         'domain_of': ['Source'],
         'slot_uri': 'source:license_info'} })
    model_component: Optional[ModelComponent] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'model_component',
         'domain_of': ['Source'],
         'slot_uri': 'source:model_component'} })
    release_year: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'release_year', 'domain_of': ['Source']} })


class ModelComponent(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'source:model_component',
         'from_schema': 'http://es-vocab.ipsl.fr/sourceschema'})

    aerosol: Optional[ModelComponentInfo] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'aerosol', 'domain_of': ['model_component']} })
    atmos: Optional[ModelComponentInfo] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'atmos', 'domain_of': ['model_component']} })
    atmosChem: Optional[ModelComponentInfo] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'atmosChem', 'domain_of': ['model_component']} })
    land: Optional[ModelComponentInfo] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'land', 'domain_of': ['model_component']} })
    ocean: Optional[ModelComponentInfo] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'ocean', 'domain_of': ['model_component']} })
    seaIce: Optional[ModelComponentInfo] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'seaIce', 'domain_of': ['model_component']} })


class ModelComponentInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'source:model_component_info',
         'from_schema': 'http://es-vocab.ipsl.fr/sourceschema'})

    description: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['model_component_info']} })
    version: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['model_component_info']} })
    native_nominal_resolution: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'native_nominal_resolution', 'domain_of': ['model_component_info']} })


class LicenseInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'source:license_info',
         'from_schema': 'http://es-vocab.ipsl.fr/sourceschema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Source', 'license_info']} })
    license: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['license_info']} })
    url: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['license_info']} })
    exceptions_contact: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'exceptions_contact', 'domain_of': ['license_info']} })
    source_specific_info: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'source_specific_info', 'domain_of': ['license_info']} })
    range: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'range', 'domain_of': ['license_info'], 'id_prefixes': ['string']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Source.model_rebuild()
ModelComponent.model_rebuild()
ModelComponentInfo.model_rebuild()
LicenseInfo.model_rebuild()
