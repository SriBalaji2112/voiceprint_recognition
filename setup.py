#!/usr/bin/env python3
# https://github.com/SriBalaji2112/voiceprint_recognition

import sys
import os
import stat

from setuptools import setup
from setuptools.command.install import install
from distutils import log

import voiceprint_recognition

FILES_TO_MARK_EXECUTABLE = ["flac-linux-x86", "flac-linux-x86_64", "flac-mac", "flac-win32.exe"]


class InstallWithExtraSteps(install):
    def run(self):
        install.run(self)  # do the original install steps

        # mark the FLAC executables as executable by all users (this fixes occasional issues when file permissions get messed up)
        for output_path in self.get_outputs():
            if os.path.basename(output_path) in FILES_TO_MARK_EXECUTABLE:
                log.info("setting executable permissions on {}".format(output_path))
                stat_info = os.stat(output_path)
                os.chmod(
                    output_path,
                    stat_info.st_mode |
                    stat.S_IRUSR | stat.S_IXUSR |  # owner can read/execute
                    stat.S_IRGRP | stat.S_IXGRP |  # group can read/execute
                    stat.S_IROTH | stat.S_IXOTH  # everyone else can read/execute
                )


setup(
    name="VoiceprintRecognition",
    version="1.5",
    packages=["voiceprint_recognition"],
    include_package_data=True,
    cmdclass={"install": InstallWithExtraSteps},

    # PyPI metadata
    author="Balaji Santhanam",
    author_email="sribalaji2112@gmail.com",
    description="A speaker recognition library that works both online and offline and supports a number of engines and "
                "APIs. ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="BSD 3-Clause License",
    keywords="speaker recognition voice sphinx google wit bing api houndify ibm snowboy voice print identification "
             "security Biometric",
    url="https://github.com/SriBalaji2112/voiceprint_recognition#readme",
    install_requires=['pyobjc-core;platform_system=="Darwin"',
                      'pyobjc;platform_system=="Darwin"',
                      'python3-Xlib;platform_system=="Linux" and python_version>="3.0"',
                      'python-xlib;platform_system=="Linux" and python_version<"3.0"',
                      'pymsgbox',
                      'pytweening>=1.0.4',
                      'pyscreeze>=0.1.21',
                      'pygetwindow>=0.0.5',
                      'mouseinfo',
                      'SpeechRecognition',
                      'keras',
                      'tensorflow',
                      'os'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Other OS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8"
)
