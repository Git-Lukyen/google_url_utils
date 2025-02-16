from setuptools import setup, find_packages

setup(
    name="google_url_utils",
    version="0.1.7",
    description="Utilities for working with Google URLs",
    long_description="Utilities aimed at working with different types of google url stuff, like proto buff parameters or pagination.\n"
                     "Currently in development and I'll add to it when I need more.",

    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "decode_pb_param=google_url_utils.decode_pb_param:main"
        ]
    },

    author="Dracea Lucian",
    author_email="dracea.lucian.mihai@gmail.com"
)
