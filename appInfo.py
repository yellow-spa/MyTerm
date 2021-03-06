#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#############################################################################
##
## Copyright (c) 2013-2020, gamesun
## All right reserved.
##
## This file is part of MyTerm.
##
## MyTerm is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## MyTerm is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with MyTerm.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################


title = 'MyTerm'
version = '2.3.0'
url = 'http://sourceforge.net/projects/myterm/'
author = 'gamesun'
copyright = 'Copyright (C) 2013-2020, gamesun'
aboutme = """
%(title)s %(ver)s<br>
%(copyright)s<br>
<br>
<a href='https://github.com/gamesun/MyTerm'>Homepage on GitHub</a><br>
<a href='http://sourceforge.net/projects/myterm/'>Download from SourceForge</a><br>
<br>
MyTerm is a flat-UI and straightforward and lightweight RS232 serial port communication utility that allows you to configure the connection parameters and communicate via the port.<br>
<br>
Its features including
<ul>
  <li>quick send custom commands</li>
  <li>supported send formats: HEX, ASCII, ASCII(\\r \\n \\t ...), Hex text file, ASCII text file, BIN/HEX file</li>
  <li>detect the valid serial ports</li>
  <li>display data either in hexadecimal or ASCII format</li>
  <li>custom resizable and floatable widgets</li>
</ul>
%(title)s is licensed on all supported platforms under the GNU GPL v3.<br>
For detail see LICENSE.txt. <br>
""" % dict(title=title, ver=version, copyright=copyright)

