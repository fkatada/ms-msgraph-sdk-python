from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.tone import Tone

@dataclass
class SendDtmfTonesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The clientContext property
    client_context: Optional[str] = None
    # The delayBetweenTonesMs property
    delay_between_tones_ms: Optional[int] = None
    # The tones property
    tones: Optional[list[Tone]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SendDtmfTonesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendDtmfTonesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SendDtmfTonesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.tone import Tone

        from .....models.tone import Tone

        fields: dict[str, Callable[[Any], None]] = {
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "delayBetweenTonesMs": lambda n : setattr(self, 'delay_between_tones_ms', n.get_int_value()),
            "tones": lambda n : setattr(self, 'tones', n.get_collection_of_enum_values(Tone)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("clientContext", self.client_context)
        writer.write_int_value("delayBetweenTonesMs", self.delay_between_tones_ms)
        writer.write_collection_of_enum_values("tones", self.tones)
        writer.write_additional_data_value(self.additional_data)
    

