"""Poetry Script Shortcuts"""

#  SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#  #
#  SPDX-License-Identifier: MIT
#
#

import subprocess


def test():
    """Run our unit tests"""
    subprocess.run(
            [
                    "poetry",
                    "run",
                    "pytest",
            ],
            check=True,
    )


def black():
    """Run black on the source and test files"""
    subprocess.run(["poetry", "run", "black", "tmt_carddeck", "tests"], check=True)


def isort():
    """Run isort on the source and test files"""
    subprocess.run(
            [
                    "poetry",
                    "run",
                    "isort",
                    "tmt_carddeck",
                    "tests",
            ],
            check=True,
    )


def check():
    """Run our pre-commit checks"""
    subprocess.run(
            [
                    "poetry",
                    "run",
                    "pre-commit",
                    "run",
                    "--all-files",
            ],
            check=True,
    )
