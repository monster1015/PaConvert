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

obj = APIBase("torch.nn.Conv2d")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(20, 16, 50, 100)
        model = nn.Conv2d(16, 33, 3, stride=2, bias=False)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(20, 16, 50, 100)
        model = nn.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), bias=False)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(20, 16, 50, 100)
        model = nn.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1), bias=False)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(5, 16, 50, 100)
        model = nn.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1), bias=True)
        result = model(x) * 0
        """
    )
    obj.run(pytorch_code, ["result"])


def test_alias_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(20, 16, 50, 100)
        model = nn.modules.conv.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1), bias=False)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(5, 16, 50, 100)
        model = nn.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1), groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)
        result = model(x) * 0
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_5
def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(5, 16, 50, 100)
        model = nn.Conv2d(16, 33, (3, 5), (2, 1), (4, 2), (3, 1), 1, True, 'zeros', None, None)
        result = model(x) * 0
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_5
def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(5, 16, 50, 100)
        model = nn.Conv2d(in_channels=16, out_channels=33, kernel_size=(3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1), groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)
        result = model(x) * 0
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_5
def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(5, 16, 50, 100)
        model = nn.Conv2d(dtype=None, device=None, padding_mode='zeros', bias=True, groups=1, dilation=(3, 1), padding=(4, 2), stride=(2, 1), kernel_size=(3, 5), out_channels=33, in_channels=16)
        result = model(x) * 0
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_5
def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.zeros(5, 16, 50, 100)
        model = nn.Conv2d(16, 33, (3, 5))
        result = model(x) * 0
        """
    )
    obj.run(pytorch_code, ["result"])
