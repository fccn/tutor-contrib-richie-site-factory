import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutorrichiesitefactory", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-richie-site-factory",
    version=ABOUT["__version__"],
    url="https://github.com/fccn/tutor-contrib-richie-site-factory",
    project_urls={
        "Code": "https://github.com/openfun/tutor-contrib-richie-site-factory",
        "Issue tracker": "https://github.com/openfun/tutor-contrib-richie-site-factory/issues",
    },
    license="AGPLv3",
    author="Open FUN (France Universite Numerique) & Overhang.IO",
    description="Richie site factory plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*", "contrib*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor>=18.0.0,<19.0.0"],
    entry_points={
        "tutor.plugin.v1": [
            "richie-site-factory = tutorrichiesitefactory.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
