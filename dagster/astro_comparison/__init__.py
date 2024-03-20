from dagster import Definitions, load_assets_from_modules

from . import assets, resources

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={"dbt": resources.dbt_resource},
)
