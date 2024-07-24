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
     'default_prefix': 'variant_label',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/Variant_labelSchema',
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'variant_label_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'ror': {'prefix_prefix': 'ror',
                          'prefix_reference': 'https://ror.org/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'variant_label': {'prefix_prefix': 'variant_label',
                                    'prefix_reference': 'http://es-vocab.ipsl.fr/Variant_label/'}},
     'source_file': 'schemas/variant_label.yaml',
     'title': 'variant_label schema',
     'types': {'boolean': {'base': 'Bool',
                           'description': 'A binary (true or false) value',
                           'exact_mappings': ['schema:Boolean'],
                           'from_schema': 'http://es-vocab.ipsl.fr/Variant_labelSchema',
                           'name': 'boolean',
                           'notes': ['If you are authoring schemas in LinkML YAML, '
                                     'the type is referenced with the lower case '
                                     '"boolean".'],
                           'repr': 'bool',
                           'uri': 'xsd:boolean'},
               'string': {'base': 'str',
                          'description': 'A character string',
                          'exact_mappings': ['schema:Text'],
                          'from_schema': 'http://es-vocab.ipsl.fr/Variant_labelSchema',
                          'name': 'string',
                          'notes': ['In RDF serializations, a slot with range of '
                                    'string is treated as a literal or type '
                                    'xsd:string.   If you are authoring schemas in '
                                    'LinkML YAML, the type is referenced with the '
                                    'lower case "string".'],
                          'uri': 'xsd:string'}}} )


class VariantLabel(ConfiguredBaseModel):
    """
    a data-descriptor composed from other
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:variant_label',
         'from_schema': 'http://es-vocab.ipsl.fr/Variant_labelSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Variant_label', 'DataDescriptorId']} })
    validation_method: str = Field("composite", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Variant_label'],
         'ifabsent': 'string(composite)'} })
    separator: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'separator', 'domain_of': ['Variant_label']} })
    parts: Optional[List[DataDescriptorId]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'parts', 'domain_of': ['Variant_label']} })
    description: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Variant_label']} })


class DataDescriptorId(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:data-descriptor',
         'from_schema': 'http://es-vocab.ipsl.fr/Variant_labelSchema'})

    is_required: Optional[bool] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'is_required', 'domain_of': ['DataDescriptorId']} })
    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Variant_label', 'DataDescriptorId']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
VariantLabel.model_rebuild()
DataDescriptorId.model_rebuild()
