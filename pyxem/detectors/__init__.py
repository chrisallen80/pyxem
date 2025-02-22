# -*- coding: utf-8 -*-
# Copyright 2016-2022 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

"""Detectors defined fro pyFAI integration"""

from .generic_flat_detector import GenericFlatDetector
from .medipix_256x256 import Medipix256x256Detector
from .medipix_515x515 import Medipix515x515Detector


__all__ = [
    "GenericFlatDetector",
    "Medipix256x256Detector",
    "Medipix515x515Detector",
]
