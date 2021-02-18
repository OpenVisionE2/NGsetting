#!/usr/bin/python
# -*- coding: utf-8 -*-
from enigma import *
import os
import glob
from Tools.Directories import resolveFilename, SCOPE_PLUGINS


class DeletPy():
        def __init__(self):
            pass

        def Remove(self):
            for x in glob.glob(resolveFilename(SCOPE_PLUGINS, 'Extensions/NGsetting/*')):
              jpy = x[-3:]
              if jpy == '.py':
                os.system('rm -fr ' + x)
            for x in glob.glob(resolveFilename(SCOPE_PLUGINS, 'Extensions/NGsetting/Moduli/*')):
              jpy = x[-3:]
              if jpy == '.py':
                os.system('rm -fr ' + x)
            open(resolveFilename(SCOPE_PLUGINS, 'Extensions/NGsetting/__init__.py'), 'w')

        def RemovePy(self):
            self.iTimer = eTimer()
            self.iTimer.callback.append(self.Remove)
            self.iTimer.start(1000 * 60, True)


ByeBye = DeletPy()
ByeBye.RemovePy()
