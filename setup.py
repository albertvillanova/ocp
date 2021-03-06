"""
Copyright (c) Facebook, Inc. and its affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from setuptools import find_packages, setup

setup(
    name="ocp-models",
    version="0.0.1",
    description="A machine learning package for molecular systems involved with catalysis",
    url="https://github.com/Open-Catalyst-Project/baselines",
    packages=find_packages(),
    include_package_data=True,
)
