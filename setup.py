from setuptools import find_packages, setup

setup(
    name="etl",
    packages=find_packages(exclude=["etl_tests"]),
    install_requires=[
        "dagster",
        "duckdb"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)