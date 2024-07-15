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


class Institution(ConfiguredBaseModel):
    """
    an registered institution for WCRP modelisation MIP
    """
    id: str = Field(...)
    validation_method: str = Field("list")
    acronyms: List[str] = Field(default_factory=list)
    aliases: Optional[List[str]] = Field(default_factory=list)
    established: Optional[int] = Field(None)
    type: Optional[str] = Field(None)
    labels: Optional[List[str]] = Field(default_factory=list)
    location: Optional[Location] = Field(None)
    name: str = Field(...)
    rorIdentifier: Optional[str] = Field(None)
    cmip_acronym: str = Field(...)
    url: Optional[List[str]] = Field(default_factory=list)


class Location(ConfiguredBaseModel):
    id: str = Field(...)
    lat: float = Field(...)
    lon: float = Field(...)
    city: str = Field(...)
    country: Optional[List[str]] = Field(default_factory=list)


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Institution.model_rebuild()
Location.model_rebuild()
