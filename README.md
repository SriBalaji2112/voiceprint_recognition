SpeakerRecognition
====================

A speaker recognition library that works both online and offline and supports a number of engines and APIs. 

<div id="badges" align="center">
  <a href="https://pypi.org/user/SriBalaji/">
    <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Library Badge"/>
  </a>
  <a href="https://www.linkedin.com/in/sri-balaji-7b51b7228/">
    <img src="https://img.shields.io/badge/LinkedIn-red?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://twitter.com/Balaji92223427">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>


**UPDATE 02-04-2023**: Hello, everybody!
Originally intended as a tech demo, this project now requires more time than I have available to keep up with all the PRs and bugs.
As a result, I'd like to extend a **open invitation for collaborators**; if you're interested, please get in touch at sribalaji2112@gmail.com! 

Support for the speaker recognition engine/API:

* `Google Cloud Speech API <https://cloud.google.com/speech/>`__
* `Tensorflow <https://www.tensorflow.org/>`__
* `Keras <https://keras.io/>`__

**Quickstart:** ``pip install SpeakerRecognition``. For more information, see the "Installing" section.

To quickly try it out, run ``python -m speaker_recognition`` after installing.

Project links:

-  `PyPI <https://pypi.python.org/pypi/SpeakerRecognition/>`__
-  `Source code <https://github.com/SriBalaji2112/speaker_recognition>`__
-  `Issue tracker <https://github.com/SriBalaji2112/speaker_recognition/issues>`__

Library Reference
-----------------

The `library reference <https://github.com/SriBalaji2112/speaker_recognition/blob/master/reference/library-reference.rst>`__ documents every publicly accessible object in the library. This document is also included under ``reference/library-reference.rst``.

Examples
--------

See the ``examples/`` `directory <https://github.com/SriBalaji2112/speaker_recognition/tree/master/examples>`__ in the repository root for usage examples:

Installing
----------

First, confirm that you have complied with all the conditions outlined in the `Requirements` section. 

Using the command `pip install SpeakerRecognition` is the simplest way to install this. 

If not, extract the ZIP after downloading the source distribution from PyPI `https://pypi.python.org/pypi/SpeakerRecognition`. 

In the folder, run ``python setup.py install``.

Requirements
------------

To use all of the functionality of the library, you should have:

* **Python** 3.8+ (required)
* **PyAudio** 0.2.11+ (required only if you need to use microphone input, ``Microphone``)
* **SpeechRecognition** 3.8+ (Audio to text convertor, ``Recognizer``)
* **Tensorflow** 2.10+ (Extract the audio feature from audio file, ``Audio Features``)
* **Keras** 2.10+ (Create a Model for audio feature and compare the features, ``Model``)

Python
~~~~~~

The first software requirement is `Python 3.8+ <https://www.python.org/downloads/>`__. This is required to use the library.

~~~~~~~

PyAudio (for microphone users)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PyAudio <http://people.csail.mit.edu/hubert/pyaudio/#downloads>`__ is required if and only if you want to use microphone input (``Microphone``). PyAudio version 0.2.11+ is required, as earlier versions have known memory management bugs when recording from microphones in certain situations.

If not installed, everything in the library will still work, except attempting to instantiate a ``Microphone`` object will raise an ``AttributeError``.

The installation instructions on the PyAudio website are quite good - for convenience, they are summarized below:

* On Windows, install PyAudio using `Pip <https://pip.readthedocs.org/>`__: execute ``pip install pyaudio`` in a terminal.
* On Debian-derived Linux distributions (like Ubuntu and Mint), install PyAudio using `APT <https://wiki.debian.org/Apt>`__: execute ``sudo apt-get install python-pyaudio python3-pyaudio`` in a terminal.
    * If the version in the repositories is too old, install the latest release using Pip: execute ``sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio`` (replace ``pip`` with ``pip3`` if using Python 3).
* On OS X, install PortAudio using `Homebrew <http://brew.sh/>`__: ``brew install portaudio``. Then, install PyAudio using `Pip <https://pip.readthedocs.org/>`__: ``pip install pyaudio``.
* On other POSIX-based systems, install the ``portaudio19-dev`` and ``python-all-dev`` (or ``python3-all-dev`` if using Python 3) packages (or their closest equivalents) using a package manager of your choice, and then install PyAudio using `Pip <https://pip.readthedocs.org/>`__: ``pip install pyaudio`` (replace ``pip`` with ``pip3`` if using Python 3).

PyAudio `wheel packages <https://pypi.python.org/pypi/wheel>`__ for common 64-bit Python versions on Windows and Linux are included for convenience, under the ``third-party/`` `directory <https://github.com/Uberi/speech_recognition/tree/master/third-party>`__ in the repository root. To install, simply run ``pip install wheel`` followed by ``pip install ./third-party/WHEEL_FILENAME`` (replace ``pip`` with ``pip3`` if using Python 3) in the repository `root directory <https://github.com/SriBalaji2112/speaker_recognition>`__.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


