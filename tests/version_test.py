# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import os

import pkg_resources
import pytest

import compiler_gym
from packaging import version
from tests.test_main import main

# Marker to skip a test if running under bazel.
# This uses $TEST_WORKSPACE, set by the bazel test runner.
# See: https://docs.bazel.build/versions/master/test-encyclopedia.html#initial-conditions
install_test = pytest.mark.skipif(
    bool(os.environ.get("TEST_WORKSPACE")), reason="Install test"
)


def test_version_dunder():
    assert isinstance(compiler_gym.__version__, str)


def test_version_dunder_format():
    version.parse(compiler_gym.__version__)


@install_test
def test_setuptools_version():
    version = pkg_resources.require("compiler_gym")[0].version
    assert version == compiler_gym.__version__


if __name__ == "__main__":
    main()
