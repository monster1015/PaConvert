# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

import textwrap

from apibase import APIBase

obj = APIBase("torch.nn.utils.spectral_norm")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        m = torch.nn.utils.spectral_norm(nn.Linear(20, 40), name='weight')
        a = torch.ones(20)
        result = m(a)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        m = torch.nn.utils.spectral_norm(nn.Linear(20, 40), name='weight', dim=0)
        a = torch.ones(20)
        result = m(a)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        m = torch.nn.utils.spectral_norm(nn.Linear(20, 40), name='weight', dim=0, eps=1e-5)
        a = torch.ones(20)
        result = m(a)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        m = torch.nn.utils.spectral_norm(nn.Linear(20, 40), 'weight', 1, 1e-5, 0)
        a = torch.ones(20)
        result = m(a)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


# generated by validate_unittest autofix, based on test_case_4
def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        m = torch.nn.utils.spectral_norm(module=nn.Linear(20, 40), name='weight', n_power_iterations=1, eps=1e-5, dim=0)
        a = torch.ones(20)
        result = m(a)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


# generated by validate_unittest autofix, based on test_case_4
def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        m = torch.nn.utils.spectral_norm(nn.Linear(20, 40))
        a = torch.ones(20)
        result = m(a)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)
