from setuptools import find_namespace_packages, setup

setup(
    name="emmet-core",
    use_scm_version={"root": "..", "relative_to": __file__},
    setup_requires=["setuptools_scm>=6,<8"],
    description="Core Emmet Library",
    author="The Materials Project",
    author_email="feedback@materialsproject.org",
    url="https://github.com/materialsproject/emmet",
    packages=find_namespace_packages(include=["emmet.*"]),
    package_data={
        "emmet.core.vasp.calc_types": ["*.yaml"],
        "emmet.core.subtrates": ["*.json"],
    },
    include_package_data=True,
    install_requires=[
        "pymatgen<=2023.9.10",
        "monty>=2021.3",
        "pydantic>=2.0",
        "pydantic-settings>=2.0",
        "pydantic-core>=2.0",
        "pybtex~=0.24",
        "typing-extensions>=3.7,<5.0",
        "spglib>=2.0.1",
    ],
    extras_require={
        "all": [
            "seekpath>=2.0.1",
            "robocrys>=0.2.8",
            "pymatgen-analysis-diffusion>=2023.8.15",
            "pymatgen-analysis-alloys>=0.0.3",
            "matcalc[models]",
            "chgnet",
            "matgl",
        ],
        "test": [
            "pre-commit",
            "pytest",
            "pytest-cov",
            "pycodestyle",
            "pydocstyle",
            "flake8",
            "mypy",
            "mypy-extensions",
            "types-setuptools",
            "types-requests",
            "maggma",
            "wincertstore",
            "custodian>=2022.5.26",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material<8.3",
            "mkdocs-material-extensions",
            "mkdocs-minify-plugin",
            "mkdocstrings",
            "mkdocs-awesome-pages-plugin",
            "mkdocs-markdownextradata-plugin",
            "mkdocstrings[python]",
            "livereload",
            "jinja2",
        ],
    },
    python_requires=">=3.9",
    license="modified BSD",
    zip_safe=False,
)
