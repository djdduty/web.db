# encoding: utf-8

"""Release information about this WebCore add-on."""

from __future__ import unicode_literals

from collections import namedtuple


version_info = namedtuple('version_info', ('major', 'minor', 'micro', 'releaselevel', 'serial'))(2, 0, 1, 'final', 0)
version = ".".join([str(i) for i in version_info[:3]]) + ((version_info.releaselevel[0] + str(version_info.serial)) if version_info.releaselevel != 'final' else '')

author = namedtuple('Author', ['name', 'email'])("Alice Bevan-McGregor", 'alice@gothcandy.com')
description = "General database adapter layer for common configuration and operation."
copyright = "2009-2016, Alice Bevan-McGregor and contributors"
url = 'https://github.com/marrow/web.db'

