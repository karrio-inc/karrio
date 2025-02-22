import typer
import inspect
import karrio.core.utils as utils
import karrio.references as references

import utils as cli_utils
import commands.templates as templates

docs = typer.Typer()


def load_metadata():
    global PROVIDERS_DATA
    global REFERENCES
    PROVIDERS_DATA = references.collect_providers_data()
    REFERENCES = references.collect_references()


@docs.command()
def generate_shipment_options():
    load_metadata()
    typer.echo(
        templates.SHIPMENT_OPTIONS_TEMPLATE.render(
            option_mappers=REFERENCES["options"], mappers=PROVIDERS_DATA
        )
        .replace("<class '", "`")
        .replace("'>", "`")
    )


@docs.command()
def generate_package_presets():
    load_metadata()
    typer.echo(
        templates.SHIPMENT_PRESETS_TEMPLATE.render(
            preset_mappers=REFERENCES["package_presets"],
            mappers=PROVIDERS_DATA,
            format_dimension=cli_utils.format_dimension,
        )
    )


@docs.command()
def generate_services():
    load_metadata()
    typer.echo(
        templates.SERVICES_TEMPLATE.render(
            service_mappers=REFERENCES["services"], mappers=PROVIDERS_DATA
        )
    )


@docs.command()
def generate_packaging_types():
    load_metadata()
    typer.echo(
        templates.PACKAGING_TYPES_TEMPLATE.render(
            packaging_mappers=REFERENCES["packaging_types"], mappers=PROVIDERS_DATA
        )
    )


@docs.command()
def generate_country_info():
    load_metadata()
    typer.echo(
        templates.COUNTRY_INFO_TEMPLATES.render(
            countries=REFERENCES["countries"],
            currencies=REFERENCES["currencies"],
            country_states=REFERENCES["states"],
        )
    )


@docs.command()
def generate_units():
    load_metadata()
    typer.echo(
        templates.UNITS_TEMPLATES.render(
            weight_units=REFERENCES["weight_units"],
            dimension_units=REFERENCES["dimension_units"],
        )
    )


@docs.command()
def generate_models():
    import karrio.core.models as m

    load_metadata()
    classes = {i: t for i, t in inspect.getmembers(m) if inspect.isclass(t)}
    docstr = (
        templates.MODELS_TEMPLATE.render(classes=classes, str=str)
        .replace("karrio.core.models.", "")
        .replace("typing.", "")
        .replace("<class '", "`")
        .replace("'>", "`")
        .replace("Dict", "`dict`")
    )

    for name, _ in classes.items():
        cls = name.strip()
        docstr = docstr.replace(f"| `{cls}` |", f"| [{cls}](#{cls.lower()}) |").replace(
            f"[{cls}] ", f"[[{cls}](#{cls.lower()})] "
        )

    typer.echo(docstr)


@docs.command()
def generate_settings():
    load_metadata()
    settings = {
        k: v for k, v in PROVIDERS_DATA.items() if v.get("Settings") is not None
    }
    docstr = (
        templates.SETTINGS_TEMPLATE.render(settings=settings, str=str)
        .replace("<class '", "`")
        .replace("'>", "`")
    )

    typer.echo(docstr)


@docs.command()
def generate_utilities_info():
    load_metadata()
    utilities = [
        (utils.DP, "from karrio.core.utils import DP"),
        (utils.XP, "from karrio.core.utils import XP"),
        (utils.DF, "from karrio.core.utils import DF"),
        (utils.SF, "from karrio.core.utils import SF"),
        (utils.helpers, "from karrio.core.utils import [function]"),
    ]
    typer.echo(
        templates.UTILS_TOOLS_TEMPLATE.render(utils=utilities, doc=cli_utils.gen)
    )
