# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import warnings

import pytest

_TEST_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_TEST_ROOT)
_TEMP_PATH = os.path.join(_PROJECT_ROOT, "test_temp")
_PATH_DATASETS = os.path.join(_PROJECT_ROOT, "Datasets")
_PATH_LEGACY = os.path.join(_PROJECT_ROOT, "legacy")

# todo: this setting `PYTHONPATH` may not be used by other evns like Conda for import packages
if _PROJECT_ROOT not in os.getenv("PYTHONPATH", ""):
    splitter = ":" if os.environ.get("PYTHONPATH", "") else ""
    os.environ["PYTHONPATH"] = f'{_PROJECT_ROOT}{splitter}{os.environ.get("PYTHONPATH", "")}'


if not os.path.isdir(_TEMP_PATH):
    os.mkdir(_TEMP_PATH)


# Ignore cleanup warnings from pytest (rarely happens due to a race condition when executing pytest in parallel)
warnings.filterwarnings("ignore", category=pytest.PytestWarning, message=r".*\(rm_rf\) error removing.*")
