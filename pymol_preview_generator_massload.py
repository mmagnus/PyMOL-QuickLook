#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ScenePNG: wrote 2052x1350 pixel image to file "out.png".
(base) [mx] structures-sessions$ pymol -c /Users/magnus/work/cwc15/structures-sessions/cwc15_conserv.pse  -d 'ray; png out.png; quit'
"""
import sys
import argparse
import tempfile
import os
import subprocess
import platform
from rna_tools.rna_tools_config import BIN_PATH

def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    parser.add_argument("-b", "--black",
                        action="store_true", help="black bg")
    parser.add_argument("-d", "--detailed", default = 200,
                        help="show lines/sticks for files with # of lines slower than, default 200")
    parser.add_argument("-r", "--rainbow",
                        action="store_true", help="rainbow")
    parser.add_argument("files", help="", default="", nargs='+')
    return parser
