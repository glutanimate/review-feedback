# -*- coding: utf-8 -*-

# Visual Feedback for Reviews Add-on for Anki
#
# Copyright (C) 2017-2020  Aristotelis P. <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

from pathlib import Path

from anki.hooks import wrap
from aqt.reviewer import Reviewer
from aqt.utils import showWarning

from .libaddon.platform import pathUserFiles, PATH_THIS_ADDON
from .feedback import confirm
from .config import config
from .consts import ADDON

try:
    from typing import Optional, NamedTuple
except ImportError:
    from .libaddon._vendor.typing import Optional, NamedTuple

_lapsed_name = "passed.png"
_passed_name = "lapsed.png"


class MediaPaths(NamedTuple):
    passed: str
    lapsed: str


def _getImagePaths(set_name: str) -> Optional[MediaPaths]:
    default_path = Path(PATH_THIS_ADDON) / "images"
    user_path = Path(pathUserFiles()) / "images"

    for path in (default_path, user_path):
        path_passed = path / set_name / _passed_name
        path_lapsed = path / set_name / _lapsed_name

        if path_passed.is_file() and path_lapsed.is_file():
            return MediaPaths(str(path_passed), str(path_lapsed))

    return None


def onAnswerCard(reviewer: Reviewer, ease: int):
    image_set = config["local"]["imageSet"]
    duration = config["local"]["feedbackDuration"]

    image_paths = _getImagePaths(image_set)

    if image_paths is None:
        showWarning(
            f"{ADDON.NAME} is not configured correctly: Could not find images for "
            f"'{image_set}'' image set. Please reset the configuration to the defaults "
            "and try again. If that does not work, please redownload the add-on."
        )
        return

    if ease == 1:
        confirm(image_paths.passed, duration)
    elif ease in (2, 3, 4):
        confirm(image_paths.lapsed, duration)


def initializeReviewer():
    Reviewer._answerCard = wrap(Reviewer._answerCard, onAnswerCard, "after")
