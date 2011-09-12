"""
pyIvr
-------------

TODO
"""
from setuptools import setup


setup(
    name='pyIvr',
    version='0.1dev',
    url='https://github.com/c4software/pyIvr',
    license='BSD',
    author='Brosseau Valentin',
    author_email='c4software@gmail.com',
    description='Generate IVR (or webpage, or anything else) from a json.',
    long_description=__doc__,
    namespace_packages=['pyIvr'],
    packages=[
        'pyIvr',
        'pyIvr.ext',
        'pyIvr.ext.afone',
        'pyIvr.ext.flask',
        'pyIvr.templates',
    ],
    include_package_data = True,
    package_data={'pyIvr.templates': ['vxml/2.0/*','xhtml/1.0/*']},
    zip_safe=False,
    platforms='any',
    install_requires=[
        'jinja2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
