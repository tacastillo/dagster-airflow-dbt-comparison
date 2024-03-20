from setuptools import find_packages, setup

setup(
    name="astro_comparison",
    packages=find_packages(exclude=["astro_comparison_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-snowflake",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
