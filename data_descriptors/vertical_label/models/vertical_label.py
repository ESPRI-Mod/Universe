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
     'default_prefix': 'verticallabel',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/verticalLabelSchema',
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'vertical_label_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'realization': {'prefix_prefix': 'realization',
                                  'prefix_reference': 'http://es-vocab.ipsl.fr/realization/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'verticallabel': {'prefix_prefix': 'verticallabel',
                                    'prefix_reference': 'http://es-vocab.ipsl.fr/vertical_label/'}},
     'source_file': 'schemas/vertical_label.yaml',
     'title': 'vertical_label schema',
     'types': {'string': {'base': 'str',
                          'description': 'A character string',
                          'exact_mappings': ['schema:Text'],
                          'from_schema': 'http://es-vocab.ipsl.fr/verticalLabelSchema',
                          'name': 'string',
                          'notes': ['In RDF serializations, a slot with range of '
                                    'string is treated as a literal or type '
                                    'xsd:string.   If you are authoring schemas in '
                                    'LinkML YAML, the type is referenced with the '
                                    'lower case "string".'],
                          'uri': 'xsd:string'}}} )


class VerticalLabel(ConfiguredBaseModel):
    """
    The verticalLabelDD indicates whether or not the data is a function of a vertical coordinate and if so, what type of coordinate it is and its length (when specified by a MIP's data request)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:vertical_label',
         'from_schema': 'http://es-vocab.ipsl.fr/verticalLabelSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['vertical_label']} })
    validation_method: str = Field("regex", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['vertical_label'],
         'ifabsent': 'string(regex)'} })
    regex: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'regex', 'domain_of': ['vertical_label']} })
    description: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['vertical_label']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
VerticalLabel.model_rebuild()
