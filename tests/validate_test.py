# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""Unit tests for //compiler_gym:validate."""
import gym

from compiler_gym import CompilerEnvState, validate_states
from tests.test_main import main


def test_validate_states_lambda_callback():
    state = CompilerEnvState(
        benchmark="cBench-v0/crc32",
        walltime=1,
        commandline="opt  input.bc -o output.bc",
    )
    results = list(
        validate_states(
            make_env=lambda: gym.make("llvm-v0"), states=[state], datasets=["cBench-v0"]
        )
    )
    assert len(results) == 1
    assert results[0].okay()


if __name__ == "__main__":
    main()
