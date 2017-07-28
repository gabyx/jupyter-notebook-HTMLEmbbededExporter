#!/usr/bin/env python

from distutils.core import setup

setup(name='nbconvertHTMLEmbeddedExporter',
      version='1.0',
      description='Embedded HTML Exporter for nbconvert',
      author='Gabriel Nützi',
      author_email='gnuetzi@gmail.com',
      entry_points = {
              'nbconvert.exporters': [
                  'htmlembedded=nbconvertHTMLEmbeddedExporter.exporter:HTMLEmbeddedExporter',
              ],
          },
      url='https://github.com/gabyx/nbconvert-html-embedded-exporter',
      packages=[],
     )
