#
# This file is part of roofd
#
# roofd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# roofd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with roofd.  If not, see <http://www.gnu.org/licenses/>.

"""Constants and status codes used by roofd"""

from warwick.observatory.common import TFmt


class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2
    HeartbeatTimedOut = 3
    HeartbeatCloseInProgress = 4
    HeartbeatInvalidTimeout = 5
    EngineeringModeRequiresHeartbeatDisabled = 6
    EngineeringModeActive = 7
    InvalidControlIP = 10

    _messages = {
        # General error codes
        1: 'error: command failed',
        2: 'error: another command is already running',
        10: 'error: command not accepted from this IP',

        # roof specific codes
        3: 'error: heartbeat has timed out',
        4: 'error: heartbeat timeout is closing the roof',
        5: 'error: heartbeat timeout must be less than 240s',
        6: 'error: heartbeat must be disabled before enabling engineering mode',
        7: 'error: roof is in engineering mode',

        -100: 'error: terminated by user',
        -101: 'error: unable to communicate with roof daemon'
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return f'error: Unknown error code {error_code}'


class RoofStatus:
    """Status of the rolling roof"""
    PartiallyOpen, Closed, Open, Closing, Opening = range(5)

    _labels = {
        0: 'PARTIALLY OPEN',
        1: 'CLOSED',
        2: 'OPEN',
        3: 'CLOSING',
        4: 'OPENING'
    }

    _formats = {
        0: TFmt.Cyan + TFmt.Bold,
        1: TFmt.Red + TFmt.Bold,
        2: TFmt.Green + TFmt.Bold,
        3: TFmt.Yellow + TFmt.Bold,
        4: TFmt.Yellow + TFmt.Bold,
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human-readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'


class HeartbeatStatus:
    """Status of the heartbeat monitoring"""
    Disabled, Active, TimedOut = range(3)

    _labels = {
        0: 'DISABLED',
        1: 'ACTIVE',
        2: 'TIMED OUT'
    }

    _formats = {
        0: TFmt.Bold,
        1: TFmt.Green + TFmt.Bold,
        2: TFmt.Red + TFmt.Bold,
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'
