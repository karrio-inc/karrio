from typing import Union, Type
from datetime import datetime
from pysoap.envelope import Envelope
from pypurolator.shipping_service_2_1_3 import (
    CreateShipmentRequest, Shipment, SenderInformation, ReceiverInformation, PackageInformation,
    TrackingReferenceInformation, Address, InternationalInformation, PickupInformation, PickupType,
    ArrayOfPiece, Piece, Weight as PurolatorWeight, WeightUnit as PurolatorWeightUnit, RequestContext,
    Dimension as PurolatorDimension, DimensionUnit as PurolatorDimensionUnit, TotalWeight, PhoneNumber,
    PrinterType as PurolatorPrinterType, ValidateShipmentRequest, PaymentInformation, DutyInformation,
    NotificationInformation, ArrayOfOptionIDValuePair, OptionIDValuePair, CreditCardInformation,
    BusinessRelationship
)
from purplship.core.models import ShipmentRequest
from purplship.core.units import PrinterType, Options, Package
from purplship.core.utils.serializable import Serializable
from purplship.core.errors import RequiredFieldError
from purplship.core.utils.helpers import concat_str
from purplship.core.utils.soap import create_envelope
from purplship.carriers.purolator.utils import Settings, standard_request_serializer
from purplship.carriers.purolator.units import Product, Service, PackagePresets, PaymentType, DutyPaymentType

ShipmentRequestType = Type[Union[ValidateShipmentRequest, CreateShipmentRequest]]


def create_shipping_request(payload: ShipmentRequest, settings: Settings, validate: bool = False) -> Serializable[Envelope]:
    RequestType: ShipmentRequestType = ValidateShipmentRequest if validate else CreateShipmentRequest
    parcel_preset = PackagePresets[payload.parcel.package_preset].value if payload.parcel.package_preset else None
    package = Package(payload.parcel, parcel_preset)

    if package.weight.value is None:
        raise RequiredFieldError("parcel.weight")

    service = Product[payload.service].value
    is_international = payload.shipper.country_code != payload.recipient.country_code
    options = Options(payload.options)
    printing = PrinterType[options.printing or "regular"].value
    special_services = {
        Service[name].value: value
        for name, value in payload.options.items()
        if name in Service.__members__
    }

    request = create_envelope(
        header_content=RequestContext(
            Version='2.1',
            Language=settings.language,
            GroupID=None,
            RequestReference=None,
            UserToken=settings.user_token
        ),
        body_content=RequestType(
            Shipment=Shipment(
                SenderInformation=SenderInformation(
                    Address=Address(
                        Name=payload.shipper.person_name,
                        Company=payload.shipper.company_name,
                        Department=None,
                        StreetNumber=None,
                        StreetSuffix=None,
                        StreetName=concat_str(payload.shipper.address_line1, join=True),
                        StreetType=None,
                        StreetDirection=None,
                        Suite=None,
                        Floor=None,
                        StreetAddress2=concat_str(payload.shipper.address_line2, join=True),
                        StreetAddress3=None,
                        City=payload.shipper.city,
                        Province=payload.shipper.state_code,
                        Country=payload.shipper.country_code,
                        PostalCode=payload.shipper.postal_code,
                        PhoneNumber=PhoneNumber(Phone=payload.shipper.phone_number),
                        FaxNumber=None
                    ),
                    TaxNumber=payload.shipper.federal_tax_id or payload.shipper.state_tax_id
                ),
                ReceiverInformation=ReceiverInformation(
                    Address=Address(
                        Name=payload.recipient.person_name,
                        Company=payload.recipient.company_name,
                        Department=None,
                        StreetNumber=None,
                        StreetSuffix=None,
                        StreetName=concat_str(payload.recipient.address_line1, join=True),
                        StreetType=None,
                        StreetDirection=None,
                        Suite=None,
                        Floor=None,
                        StreetAddress2=concat_str(payload.recipient.address_line2, join=True),
                        StreetAddress3=None,
                        City=payload.recipient.city,
                        Province=payload.recipient.state_code,
                        Country=payload.recipient.country_code,
                        PostalCode=payload.recipient.postal_code,
                        PhoneNumber=PhoneNumber(Phone=payload.recipient.phone_number),
                        FaxNumber=None
                    ),
                    TaxNumber=payload.recipient.federal_tax_id or payload.recipient.state_tax_id
                ),
                FromOnLabelIndicator=None,
                FromOnLabelInformation=None,
                ShipmentDate=datetime.today().strftime("%Y-%m-%d"),
                PackageInformation=PackageInformation(
                    ServiceID=service,
                    Description=payload.parcel.description,
                    TotalWeight=TotalWeight(
                        Value=package.weight.value,
                        WeightUnit=PurolatorWeightUnit[package.weight_unit.value].value
                    ) if package.weight.value else None,
                    TotalPieces=1,
                    PiecesInformation=ArrayOfPiece(
                        Piece=[
                            Piece(
                                Weight=PurolatorWeight(
                                    Value=package.weight.value,
                                    WeightUnit=PurolatorWeightUnit[package.weight_unit.value].value
                                ) if package.weight.value else None,
                                Length=PurolatorDimension(
                                    Value=package.length.value,
                                    DimensionUnit=PurolatorDimensionUnit[package.dimension_unit.value].value
                                ) if package.length.value else None,
                                Width=PurolatorDimension(
                                    Value=package.width.value,
                                    DimensionUnit=PurolatorDimensionUnit[package.dimension_unit.value].value
                                ) if package.width.value else None,
                                Height=PurolatorDimension(
                                    Value=package.height.value,
                                    DimensionUnit=PurolatorDimensionUnit[package.dimension_unit.value].value
                                ) if package.height.value else None,
                                Options=None
                            )
                        ]
                    ),
                    DangerousGoodsDeclarationDocumentIndicator=None,
                    OptionsInformation=ArrayOfOptionIDValuePair(
                        OptionIDValuePair=[
                            OptionIDValuePair(
                                ID=key,
                                Value=value
                            )
                            for key, value in special_services.items()
                        ]
                    ) if len(special_services) > 0 else None
                ),
                InternationalInformation=InternationalInformation(
                    DocumentsOnlyIndicator=payload.parcel.is_document,
                    ContentDetails=payload.parcel.description,
                    BuyerInformation=None,
                    PreferredCustomsBroker=None,
                    DutyInformation=DutyInformation(
                        BillDutiesToParty=DutyPaymentType[payload.customs.duty.paid_by].value,
                        BusinessRelationship=BusinessRelationship.NOT_RELATED.value,
                        Currency=payload.customs.duty.currency
                    ) if payload.customs is not None else None,
                    ImportExportType=None,
                    CustomsInvoiceDocumentIndicator=None
                ) if is_international else None,
                ReturnShipmentInformation=None,
                PaymentInformation=PaymentInformation(
                    PaymentType=PaymentType[payload.payment.paid_by].value,
                    RegisteredAccountNumber=payload.payment.account_number,
                    BillingAccountNumber=payload.payment.account_number,
                    CreditCardInformation=CreditCardInformation(
                        Type=payload.payment.credit_card.type,
                        Number=payload.payment.credit_card.number,
                        Name=payload.payment.credit_card.name,
                        ExpiryMonth=payload.payment.credit_card.expiry_month,
                        ExpiryYear=payload.payment.credit_card.expiry_year,
                        CVV=payload.payment.credit_card.security_code,
                        BillingPostalCode=payload.payment.credit_card.postal_code
                    ) if payload.payment.credit_card is not None else None,
                ) if payload.payment is not None else None,
                PickupInformation=PickupInformation(PickupType=PickupType.DROP_OFF.value),
                NotificationInformation=NotificationInformation(
                    ConfirmationEmailAddress=options.notification.email or payload.shipper.email,
                    AdvancedShippingNotificationMessage=None
                ) if options.notification else None,
                TrackingReferenceInformation=TrackingReferenceInformation(
                    Reference1=payload.parcel.reference
                ),
                OtherInformation=None,
                ProactiveNotification=None
            ),
            PrinterType=PurolatorPrinterType(printing).value
        )
    )
    return Serializable(request, standard_request_serializer)
