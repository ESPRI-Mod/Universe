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
     'default_prefix': 'experiment',
     'default_range': 'string',
     'id': 'http://es-vocab.ipsl.fr/ExperimentSchema',
     'imports': ['linkml:types'],
     'name': 'experiement_schema',
     'prefixes': {'esvocab': {'prefix_prefix': 'esvocab',
                              'prefix_reference': 'http://es-vocab.ipsl.fr/'},
                  'experiment': {'prefix_prefix': 'experiment',
                                 'prefix_reference': 'http://es-vocab.ipsl.fr/experiment/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns'},
                  'ror': {'prefix_prefix': 'ror',
                          'prefix_reference': 'https://ror.org/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'schemas/experiment.yaml'} )


class Experiment(ConfiguredBaseModel):
    """
    an 'experiment' refers to a specific, controlled simulation conducted using climate models to investigate particular aspects of the Earth's climate system. These experiments are designed with set parameters, such as initial conditions, external forcings (like greenhouse gas concentrations or solar radiation), and duration, to explore and understand climate behavior under various scenarios and conditions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'esvocab:experiment',
         'from_schema': 'http://es-vocab.ipsl.fr/ExperimentSchema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Experiment'], 'slot_uri': 'experiement:id'} })
    validation_method: str = Field("list", json_schema_extra = { "linkml_meta": {'alias': 'validation_method',
         'domain_of': ['Experiment'],
         'ifabsent': 'string(list)',
         'slot_uri': 'es-vocab:validation_method'} })
    activity: List[str] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'activity', 'domain_of': ['Experiment']} })
    description: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Experiment']} })
    tiers: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'tiers', 'domain_of': ['Experiment']} })
    experiment_id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment']} })
    sub_experiment_id: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'sub_experiment_id', 'domain_of': ['Experiment']} })
    experiment: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'experiment', 'domain_of': ['Experiment']} })
    required_model_component: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'required_model_component', 'domain_of': ['Experiment']} })
    additionnal_allowed_model_components: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'additionnal_allowed_model_components', 'domain_of': ['Experiment']} })
    start_year: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'start_year', 'domain_of': ['Experiment']} })
    end_year: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'end_year', 'domain_of': ['Experiment']} })
    min_numbers_yrs_per_sim: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'min_numbers_yrs_per_sim', 'domain_of': ['Experiment']} })
    parent_activity_id: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'parent_activity_id', 'domain_of': ['Experiment']} })
    parent_experiement_id: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'parent_experiement_id', 'domain_of': ['Experiment']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Experiment.model_rebuild()
