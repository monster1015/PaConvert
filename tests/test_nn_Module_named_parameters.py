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

obj = APIBase("torch.nn.Module.named_parameters")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()

                self.linear_1 = nn.Linear(in_features=2, out_features=2)
            def forward(self, x):
                x1 = self.linear_1(x)
                return x, x, x1
        a = TestForHook()
        for a,b in a.named_parameters(prefix="wfs"):
            result.append(b)
        result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()

                self.linear_1 = nn.Linear(in_features=2, out_features=2)
            def forward(self, x):
                x1 = self.linear_1(x)
                return x, x, x1
        a = TestForHook()
        for a,b in a.named_parameters(prefix="wfs", recurse=True):
            result.append(b)
        result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()

                self.linear_1 = nn.Linear(in_features=2, out_features=2)
            def forward(self, x):
                x1 = self.linear_1(x)
                return x, x, x1
        a = TestForHook()
        for a,b in a.named_parameters(prefix="wfs", recurse=True, remove_duplicate = True):
            result.append(b)
        result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()

                self.linear_1 = nn.Linear(in_features=2, out_features=2)
            def forward(self, x):
                x1 = self.linear_1(x)
                return x, x, x1
        a = TestForHook()
        for a,b in a.named_parameters(remove_duplicate = True):
            result.append(b)
        result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


# generated by validate_unittest autofix, based on test_case_3
def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()

                self.linear_1 = nn.Linear(in_features=2, out_features=2)
            def forward(self, x):
                x1 = self.linear_1(x)
                return x, x, x1
        a = TestForHook()
        for a,b in a.named_parameters("wfs", True, True):
            result.append(b)
        result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


# generated by validate_unittest autofix, based on test_case_3
def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()

                self.linear_1 = nn.Linear(in_features=2, out_features=2)
            def forward(self, x):
                x1 = self.linear_1(x)
                return x, x, x1
        a = TestForHook()
        for a,b in a.named_parameters(remove_duplicate=True, recurse=True, prefix="wfs"):
            result.append(b)
        result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


# generated by validate_unittest autofix, based on test_case_3
def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()

                self.linear_1 = nn.Linear(in_features=2, out_features=2)
            def forward(self, x):
                x1 = self.linear_1(x)
                return x, x, x1
        a = TestForHook()
        for a,b in a.named_parameters():
            result.append(b)
        result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()
                self.register_parameter('w1', nn.Parameter(torch.randn(2, 3)))
                self.register_parameter('w1', nn.Parameter(torch.randn(3, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 2)))
            def forward(self, x):
                return x

        a = TestForHook()
        for a,b in a.named_parameters(remove_duplicate=False):
            result.append(b)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()
                self.register_parameter('w1', nn.Parameter(torch.randn(2, 3)))
                self.register_parameter('w1', nn.Parameter(torch.randn(3, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 2)))
            def forward(self, x):
                return x

        a = TestForHook()
        for a,b in a.named_parameters(remove_duplicate=True):
            result.append(b)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()
                self.register_parameter('w1', nn.Parameter(torch.randn(2, 3)))
                self.register_parameter('w1', nn.Parameter(torch.randn(3, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 2)))
            def forward(self, x):
                return x

        a = TestForHook()
        for a,b in a.named_parameters(prefix = "wfs", recurse = False, remove_duplicate = False):
            result.append(b)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_11():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        result = []
        class TestForHook(nn.Module):
            def __init__(self):
                super().__init__()
                self.register_parameter('w1', nn.Parameter(torch.randn(2, 3)))
                self.register_parameter('w1', nn.Parameter(torch.randn(3, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 3)))
                self.register_parameter('w2', nn.Parameter(torch.randn(1, 2)))
            def forward(self, x):
                return x

        a = TestForHook()
        for a,b in a.named_parameters(remove_duplicate = False, recurse = True, prefix = "wfs"):
            result.append(b)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)
