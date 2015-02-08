# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


class RegistrationError(Exception):
  """An error at option registration time."""
  pass


class ParseError(Exception):
  """An error at flag parsing time."""
  pass