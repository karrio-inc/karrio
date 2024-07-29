from attr import s
from typing import Optional, List
from jstruct import JStruct, JList


@s(auto_attribs=True)
class ContentType:
    itemDescription: Optional[str] = None
    itemQuantity: Optional[int] = None
    itemValue: Optional[int] = None
    itemTotalValue: Optional[int] = None
    weightUOM: Optional[str] = None
    itemWeight: Optional[float] = None
    itemTotalWeight: Optional[float] = None
    HSTariffNumber: Optional[str] = None
    countryofOrigin: Optional[str] = None
    itemCategory: Optional[str] = None
    itemSubcategory: Optional[str] = None


@s(auto_attribs=True)
class ContactType:
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None


@s(auto_attribs=True)
class PortersReferenceType:
    referenceType: Optional[str] = None
    reference: Optional[str] = None
    contact: Optional[ContactType] = JStruct[ContactType]


@s(auto_attribs=True)
class CustomsFormType:
    contentComments: Optional[str] = None
    restrictionType: Optional[str] = None
    restrictionComments: Optional[str] = None
    AESITN: Optional[str] = None
    invoiceNumber: Optional[str] = None
    licenseNumber: Optional[str] = None
    certificateNumber: Optional[str] = None
    customsContentType: Optional[str] = None
    importersReference: Optional[PortersReferenceType] = JStruct[PortersReferenceType]
    exportersReference: Optional[PortersReferenceType] = JStruct[PortersReferenceType]
    contents: List[ContentType] = JList[ContentType]


@s(auto_attribs=True)
class AddressType:
    streetAddress: Optional[str] = None
    secondaryAddress: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    ZIPCode: Optional[str] = None
    ZIPPlus4: Optional[str] = None
    urbanization: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    firm: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    ignoreBadAddress: Optional[bool] = None
    platformUserId: Optional[str] = None


@s(auto_attribs=True)
class ImageInfoType:
    imageType: Optional[str] = None
    labelType: Optional[str] = None
    holdForManifest: Optional[bool] = None


@s(auto_attribs=True)
class CustomerReferenceType:
    referenceNumber: Optional[str] = None


@s(auto_attribs=True)
class DestinationEntryFacilityAddressType:
    streetAddress: Optional[str] = None
    secondaryAddress: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    ZIPCode: Optional[str] = None
    ZIPPlus4: Optional[str] = None
    urbanization: Optional[str] = None


@s(auto_attribs=True)
class OriginalPackageType:
    originalTrackingNumber: Optional[str] = None
    originalConstructCode: Optional[str] = None


@s(auto_attribs=True)
class PackageOptionsType:
    packageValue: Optional[int] = None
    nonDeliveryOption: Optional[str] = None
    redirectAddress: Optional[AddressType] = JStruct[AddressType]
    originalPackage: Optional[OriginalPackageType] = JStruct[OriginalPackageType]
    generateGXEvent: Optional[bool] = None


@s(auto_attribs=True)
class PackageDescriptionType:
    weightUOM: Optional[str] = None
    weight: Optional[int] = None
    dimensionsUOM: Optional[str] = None
    length: Optional[int] = None
    height: Optional[int] = None
    width: Optional[int] = None
    girth: Optional[int] = None
    destinationEntryFacilityAddress: Optional[DestinationEntryFacilityAddressType] = JStruct[DestinationEntryFacilityAddressType]
    mailClass: Optional[str] = None
    rateIndicator: Optional[str] = None
    diameter: Optional[int] = None
    shape: Optional[str] = None
    processingCategory: Optional[str] = None
    destinationEntryFacilityType: Optional[str] = None
    mailingDate: Optional[str] = None
    packageOptions: Optional[PackageOptionsType] = JStruct[PackageOptionsType]
    customerReference: List[CustomerReferenceType] = JList[CustomerReferenceType]
    extraServices: List[int] = []


@s(auto_attribs=True)
class ToAddressType:
    streetAddress: Optional[str] = None
    secondaryAddress: Optional[str] = None
    city: Optional[str] = None
    postalCode: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    countryISOAlpha2Code: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    firm: Optional[str] = None
    phone: Optional[str] = None


@s(auto_attribs=True)
class LabelRequestType:
    imageInfo: Optional[ImageInfoType] = JStruct[ImageInfoType]
    toAddress: Optional[ToAddressType] = JStruct[ToAddressType]
    fromAddress: Optional[AddressType] = JStruct[AddressType]
    senderAddress: Optional[AddressType] = JStruct[AddressType]
    packageDescription: Optional[PackageDescriptionType] = JStruct[PackageDescriptionType]
    customsForm: Optional[CustomsFormType] = JStruct[CustomsFormType]
