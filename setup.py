# -*- coding: utf-8 -*-
import os

import setuptools  # type: ignore

package_root = os.path.abspath(os.path.dirname(__file__))

name = "plugin-sdk-python"

description = "CloudQuery Plugin SDK for Python"

dependencies = [
    "plugin-pb-python==0.0.11",
]
url = "https://github.com/cloudquery/plugin-sdk-python"

package_root = os.path.abspath(os.path.dirname(__file__))

long_description = """
CloudQuery Plugin SDK for Python
================================================

Overview
-----------

This is the high-level package to use for developing CloudQuery plugins in Python. See [github.com/cloudquery/plugin-sdk-python](https://github.com/cloudquery/plugin-sdk-python) for more information.
"""

packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("cloudquery")
]
setuptools.setup(
    name=name,
    version="0.0.1",
    description=description,
    long_description=long_description,
    author="CloudQuery LTD",
    author_email="pypi-packages@cloudquery.io",
    license="MPL-2.0",
    url=url,
    classifiers=[
        # release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    python_requires=">=3.7",
    namespace_packages=["cloudquery"],
    # namespace_packages=namespaces,
    install_requires=dependencies,
    include_package_data=True,
    package_data={"cloudquery": ["plugin_v3/py.typed", "plugin_v3/*.pyi"]},
    zip_safe=False,
)