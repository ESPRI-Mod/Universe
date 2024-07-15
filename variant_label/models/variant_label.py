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


class VariantLabel(ConfiguredBaseModel):
    """
    a data-descriptor composed from other
    """
    id: str = Field(...)
    validation_method: str = Field("composite")
    separator: Optional[str] = Field(None)
    parts: Optional[List[DataDescriptorId]] = Field(default_factory=list)
    description: Optional[str] = Field(None)


class DataDescriptorId(ConfiguredBaseModel):
    is_required: Optional[bool] = Field(None)
    id: Optional[str] = Field(None)


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
VariantLabel.model_rebuild()
DataDescriptorId.model_rebuild()
