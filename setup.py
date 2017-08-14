#!/usr/bin/env python
from distutils.core import setup

setup(name='edith',
      version='0.1.0',
      description='Edit-distance implementation with edit-path retrieval',
      author='david weil (tenuki)',
      author_email='tenuki@gmail.com',
      url='https://github.com/tenuki/edith',
      py_modules=['edith'],
      license="GNU General Public License v3.0",
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Language Tools',
            'GNU General Public License v3.0',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 2',
            ]
     )