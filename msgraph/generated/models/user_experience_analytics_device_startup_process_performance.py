from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsDeviceStartupProcessPerformance(Entity, Parsable):
    """
    The user experience analytics device startup process performance.
    """
    # The count of devices which initiated this process on startup. Supports: $filter, $select, $OrderBy. Read-only.
    device_count: Optional[int] = None
    # The median impact of startup process on device boot time in milliseconds. Supports: $filter, $select, $OrderBy. Read-only.
    median_impact_in_ms: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the startup process. Examples: outlook, excel. Supports: $select, $OrderBy. Read-only.
    process_name: Optional[str] = None
    # The product name of the startup process. Examples: Microsoft Outlook, Microsoft Excel. Supports: $select, $OrderBy. Read-only.
    product_name: Optional[str] = None
    # The publisher of the startup process. Examples: Microsoft Corporation, Contoso Corp. Supports: $select, $OrderBy. Read-only.
    publisher: Optional[str] = None
    # The total impact of startup process on device boot time in milliseconds. Supports: $filter, $select, $OrderBy. Read-only.
    total_impact_in_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsDeviceStartupProcessPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceStartupProcessPerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceStartupProcessPerformance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "medianImpactInMs": lambda n : setattr(self, 'median_impact_in_ms', n.get_int_value()),
            "processName": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "totalImpactInMs": lambda n : setattr(self, 'total_impact_in_ms', n.get_int_value()),
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
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_int_value("medianImpactInMs", self.median_impact_in_ms)
        writer.write_str_value("processName", self.process_name)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_int_value("totalImpactInMs", self.total_impact_in_ms)
    

