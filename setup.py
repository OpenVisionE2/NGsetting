#!/usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup
import setup_translate

pkg = 'Extensions.NGsetting'
setup(name='enigma2-plugin-extensions-ngsetting',
       version='1.1',
       description='NGsetting plugin for Vhannibal settings',
       packages=[pkg],
       package_dir={pkg: 'plugin'},
       package_data={pkg: ['Po/*/LC_MESSAGES/*.mo', 'Skin/*.pyo', 'Panel/*.png', 'Moduli/NGsetting/rules.xml', 'Moduli/*.pyo']},
       cmdclass=setup_translate.cmdclass, # for translation
      )
