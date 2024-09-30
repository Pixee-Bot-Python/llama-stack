# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import os
import subprocess
import sys
from security import safe_command


def install_wheel_from_presigned():
    file = "install-wheel-from-presigned.sh"
    script_path = os.path.join(os.path.dirname(__file__), file)
    try:
        safe_command.run(subprocess.run, ["sh", script_path] + sys.argv[1:], check=True)
    except Exception:
        sys.exit(1)
