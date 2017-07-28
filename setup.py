#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      description='Jupyter Embedded HTML Exporter,
      author='Gabriel Nützi',
      author_email='gnuetzi@gmail.com',
      entry_points = {
              'nbconvert.exporters': [
                  'htmlembedded = nbconvert-htmlembeddedexporter:HTMLEmbeddedExporter',
              ],
          }
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command'],
     )
