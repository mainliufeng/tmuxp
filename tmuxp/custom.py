# -*- coding: utf-8 -*-
"""Utility and helper methods for tmuxp.

tmuxp.util
~~~~~~~~~~

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

import os
import re

from libtmux.pane import Pane


def get_pane_current_command(p):
    """Get current command of tmux pane

    :param p: - tmux pane
    :type p: :class:`Pane`
    :rtype: str

    """
    current_cmd = None
    p_pid = p.get('pane_pid', None)
    if p_pid:
        match = re.match(
            r'\d+ (.*)(|\n)',
            os.popen(
                'ps -eo "ppid command" | sed "s/^ *//" | grep "^' +
                p_pid +
                '"'
            ).read()
        )
        if match:
            current_cmd = match.group(1)
    if not current_cmd:
        current_cmd = p.current_command
    return current_cmd
