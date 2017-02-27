'''
Created on 27 Feb 2017

@author: pigna
'''
from setuptools import setup

setup(name="ledtester",
      version="0.1",
      description="Assignment 3, COMP30670. It tests LEDs on a square grid.",
      url="",
      author="Andrea Pignanelli",
      author_email="andrea.pignanelli01@ucdconnect.ie",
      licence="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['ledtester=src.main:main']
          },
      install_requires=[
          'numpy',
        ],
    )