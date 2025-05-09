from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..group import Group
    from ..subject_set import SubjectSet

from ..subject_set import SubjectSet

@dataclass
class GroupBasedSubjectSet(SubjectSet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.groupBasedSubjectSet"
    # The groups property
    groups: Optional[list[Group]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupBasedSubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupBasedSubjectSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupBasedSubjectSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..group import Group
        from ..subject_set import SubjectSet

        from ..group import Group
        from ..subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(Group)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("groups", self.groups)
    

