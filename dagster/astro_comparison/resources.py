from dagster_dbt import DbtCliResource

dbt_resource = DbtCliResource(
    project_dir="astro_comparison/dbt",
    target="dev"
)