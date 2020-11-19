import os
from setuptools import setup

path = os.path.dirname(os.path.abspath(__file__))
tools = [
    os.path.join(path, "antiword.exe"),
    os.path.join(path, "pdftotext.exe"),
]

antiword = []
dirname = os.path.join(path, "antiword")
for filename in os.listdir(dirname):
    antiword.append(os.path.join(dirname, filename))

setup(
    name='wintools',
    version='1.0',
    url='https://github.com/alexsilva/wintools',
    license='MIT',
    author='alex',
    author_email='alex@fabricadigital.com.br',
    description='Windows processing tools',
    data_files=[('tools', tools),
                ('tools\\antiword', antiword)]
)
