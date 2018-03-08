from setuptools import setup

setup(name="light_test",
      version="0.1",
      description="Program to switch on and off lights on an LED board",
      url="",
      author="Ciara Dillon", 
      author_email="ciara.dillon1@ucdconnect.ie",
      license="GPL3",
      packages=['Assignment3'],
      entry_points={
          'console_scripts':['solve_led=app.main:main']
          }
      ) 
