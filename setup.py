from distutils.core import setup
import py2exe

setup(console=["quickfind.py"],
        data_files=[("", ["corpus"])])

