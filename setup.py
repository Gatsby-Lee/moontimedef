from setuptools import setup, find_packages

requires = []

tests_require = [
    'pytest',
]

setup(
    name='moontimedef',
    version='0.2',
    description='Time Definition',
    long_description=open('README.rst').read(),
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
    ],
    author='Gatsby Lee',
    url='https://github.com/Gatsby-Lee/moontimedef',
    keywords='gatsby moon time definition',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'testing': tests_require,
    },
)
