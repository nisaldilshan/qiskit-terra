# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""Module for the Qobj structure."""

from ._qobj import (Qobj, QobjConfig, QobjExperiment, QobjInstruction, QobjItem)
from ._converter import qobj_to_dict
