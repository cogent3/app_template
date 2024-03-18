from setuptools import setup

setup(
    name="uppercase",
    version="0.1",
    packages=["."],
    entry_points={
        'cogent3.app': [
            'to_upper = uppercase:to_upper',
        ],
    },
)