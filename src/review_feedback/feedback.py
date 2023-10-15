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

"""
Visual feedback
"""

from typing import TYPE_CHECKING, Optional

from aqt import mw
from aqt.qt import qtmajor

if TYPE_CHECKING or qtmajor >= 6:
    from PyQt6.QtGui import QImage, QPixmap
    from PyQt6.QtWidgets import QLabel
    from PyQt6.QtCore import QPoint, Qt, QTimer
else:
    from PyQt5.QtGui import QImage, QPixmap
    from PyQt5.QtWidgets import QLabel
    from PyQt5.QtCore import QPoint, Qt, QTimer

_lab: Optional[QLabel] = None
_timer: Optional[QTimer] = None


def closeConfirm():
    global _lab, _timer
    if _lab:
        try:
            _lab.deleteLater()
        except:  # noqa: E722
            pass
        _lab = None
    if _timer:
        _timer.stop()
        _timer = None


def confirm(image_path: str, period: int):
    global _timer, _lab
    parent = mw
    closeConfirm()
    lab = QLabel(parent=parent)
    img = QPixmap(image_path)
    lab.setPixmap(img)
    lab.setAttribute(Qt.WA_TranslucentBackground, True)
    lab.setAutoFillBackground(False)
    lab.setWindowFlags(
        Qt.ToolTip | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint  # type: ignore
    )
    center = parent.frameGeometry().center()
    qp = QPoint(img.width() * 0.5, img.height() * 0.5)  # type: ignore
    lab.move(center - qp)
    lab.show()
    _timer = mw.progress.timer(period, closeConfirm, False)
    _lab = lab
