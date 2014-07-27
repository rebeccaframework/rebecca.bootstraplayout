from setuptools import setup


requires = [
    "pyramid",
    "pyramid_layout",
    "pyramid_mako",
    "webhelpers2>=2.0b5",
    "babel",
]

setup(
    name="rebecca.bootstraplayout",
    install_requires=requires,
)
