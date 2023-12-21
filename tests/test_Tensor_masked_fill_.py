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

obj = APIBase("torch.Tensor.masked_fill_")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.Tensor([[1.0,0.2], [0.3,0.4]])
        b = torch.Tensor([[1,0], [1,1]]) == 1
        result = a.masked_fill_(b, 2)
        """
    )
    obj.run(pytorch_code, ["result", "a"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.Tensor([[1.0,0.2], [0.3,0.4]])
        b = torch.Tensor([[1,0], [1,1]]) == 1
        result = a.masked_fill_(mask=b, value=2)
        """
    )
    obj.run(pytorch_code, ["result", "a"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.Tensor([[1.0,0.2], [0.3,0.4]])
        b = torch.Tensor([[1,0], [1,1]])
        result = a.masked_fill_(value=0.1, mask=(b==1))
        """
    )
    obj.run(pytorch_code, ["result", "a"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.Tensor([[1.0,0.2], [0.3,0.4]])
        b = torch.Tensor([[1,0], [1,1]])
        result = a.masked_fill_(mask=b==1, value=0.1)
        """
    )
    obj.run(pytorch_code, ["result", "a"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.Tensor([[1.0,0.2], [0.3,0.4]])
        b = torch.Tensor([[1,0], [1,1]])
        result = a.masked_fill_(b==1, 0.1)
        """
    )
    obj.run(pytorch_code, ["result", "a"])
