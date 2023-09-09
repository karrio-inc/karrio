import karrio.lib as lib
import karrio.core.units as units


class PackagingType(lib.Flag):
    """Carrier specific packaging type"""

    zoom2u_documents = "Documents"
    zoom2u_bag = "Bag"
    zoom2u_box = "Box"
    zoom2u_flowers = "Flowers"
    zoom2u_custom = "Custom"

    """ Unified Packaging type mapping """
    envelope = zoom2u_documents
    pak = zoom2u_bag
    tube = zoom2u_custom
    pallet = zoom2u_custom
    small_box = zoom2u_box
    medium_box = zoom2u_box
    your_packaging = zoom2u_custom


class ConnectionConfig(lib.Enum):
    currency = lib.OptionEnum("currency")
    shipping_options = lib.OptionEnum("shipping_options", list)
    shipping_services = lib.OptionEnum("shipping_services", list)


class VehiculeType(lib.Enum):
    """Zoom2u vehicule type"""

    zoom2u_bike = "Bike"
    zoom2u_car = "Car"
    zoom2u_van = "Van"


class ShippingService(lib.Enum):
    """Carrier specific services"""

    zoom2u_VIP = "VIP"
    zoom2u_3_hour = "3 hour"
    zoom2u_same_day = "Same day"


class ShippingOption(lib.Enum):
    """Carrier specific options"""

    purchase_order_number = lib.OptionEnum("purchase_order_number")
    ready_datetime = lib.OptionEnum("ready_datetime")
    vehicle_type = lib.OptionEnum("vehicle_type")
    pickup_notes = lib.OptionEnum("pickup_notes")
    dropoff_notes = lib.OptionEnum("dropoff_notes")


def shipping_options_initializer(
    options: dict,
    package_options: units.ShippingOptions = None,
) -> units.ShippingOptions:
    """
    Apply default values to the given options.
    """

    if package_options is not None:
        options.update(package_options.content)

    def items_filter(key: str) -> bool:
        return key in ShippingOption  # type: ignore

    return units.ShippingOptions(options, ShippingOption, items_filter=items_filter)


class TrackingStatus(lib.Enum):
    on_hold = ["on_hold"]
    delivered = ["delivered"]
    in_transit = ["in_transit"]
    delivery_failed = ["delivery_failed"]
    delivery_delayed = ["delivery_delayed"]
    out_for_delivery = ["out_for_delivery"]
    ready_for_pickup = ["ready_for_pickup"]
