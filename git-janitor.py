#!/usr/bin/env python

import sys
from src.git_janitor import GitJanitor

janitor = GitJanitor(sys.argv)
janitor.start()