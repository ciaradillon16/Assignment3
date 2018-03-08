from setuptools import setup

setup(name="Assignment3",
      version="0.1",
      description="Program to switch on and off lights on an LED board",
      url="",
      author="Ciara Dillon", 
      author_email="ciara.dillon1@ucdconnect.ie",
      license="GPL3",
      packages=['app'],
      entry_points={
          'console_scripts':['solve_led=app.main:parse_file']
          }
      ) 
