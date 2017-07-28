#!/usr/bin/env python

from distutils.core import setup

setup(name='nbconvert-html-embedded-exporter',
      version='1.0',
      description='nbconvert Embedded HTML Exporter',
      author='Gabriel Nützi',
      author_email='gnuetzi@gmail.com',
      entry_points = {
              'nbconvert.exporters': [
                  'htmlembedded = nbconvert-html-embedded-exporter:HTMLEmbeddedExporter',
              ],
          }
      url='https://github.com/gabyx/nbconvert-html-embedded-exporter',
      packages=[],
     )
