from dagster_dbt import dbt_assets, DbtCliResource


@dbt_assets(
    manifest="astro_comparison/dbt/target/manifest.json",
)
def dbt_analytics(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context)
