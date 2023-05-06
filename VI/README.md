VoiceprintRecognition
====================

<div id="badges" align="center">
  <a href="https://pypi.org/user/SriBalaji/">
    <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Library Badge"/>
  </a>
  <a href="https://www.tensorflow.org">
    <img src="https://img.shields.io/badge/Tensorflow-red?style=for-the-badge&logo=Tensorflow&logoColor=white" alt="TensorFlow Badge"/>
  </a>
  <a href="https://keras.io/">
    <img src="https://img.shields.io/badge/Keras-blue?style=for-the-badge&logo=keras&logoColor=white" alt="Keras Badge"/>
  </a>
<a href="https://google.com/">
    <img src="https://img.shields.io/badge/Google-API-red?style=for-the-badge&logo=google&logoColor=white" alt="Keras Badge"/>
  </a>
</div>

<br>
A speaker recognition library that works both online and offline and supports a number of engines and APIs. 
<br>
<br>
**UPDATE 02-04-2023**: Hello, everybody!
Originally intended as a tech demo, this project now requires more time than I have available to keep up with all the PRs and bugs.
As a result, I'd like to extend a **open invitation for collaborators**; if you're interested, please get in touch at sribalaji2112@gmail.com! 

Support for the speaker recognition engine/API:

* `Google Cloud Speech API <https://cloud.google.com/speech/>`__
* `Tensorflow <https://www.tensorflow.org/>`__
* `Keras <https://keras.io/>`__

**Quickstart:** ``pip install VoiceprintRecognition``. For more information, see the "Installing" section.

To quickly try it out, run ``python -m voiceprint_recognition`` after installing.

Project links:

-  `PyPI <https://pypi.python.org/pypi/VoiceprintRecognition/>`__
-  `Source code <https://github.com/SriBalaji2112/voiceprint_recognition>`__
-  `Issue tracker <https://github.com/SriBalaji2112/voiceprint_recognition/issues>`__

Library Reference
-----------------

The `library reference <https://github.com/SriBalaji2112/voiceprint_recognition/blob/master/reference/library-reference.rst>`__ documents every publicly accessible object in the library. This document is also included under ``reference/library-reference.rst``.

Examples
--------

See the ``examples/`` `directory <https://github.com/SriBalaji2112/voiceprint_recognition/tree/master/examples>`__ in the repository root for usage examples:

Installing
----------

First, confirm that you have complied with all the conditions outlined in the `Requirements` section. 

Using the command `pip install VoiceprintRecognition` is the simplest way to install this. 

If not, extract the ZIP after downloading the source distribution from PyPI `https://pypi.python.org/pypi/VoiceprintRecognition`. 

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

PyAudio `wheel packages <https://pypi.python.org/pypi/wheel>`__ for common 64-bit Python versions on Windows and Linux are included for convenience, under the ``third-party/`` `directory <https://github.com/SriBalaji2112/voiceprint_recognition/tree/master/third-party>`__ in the repository root. To install, simply run ``pip install wheel`` followed by ``pip install ./third-party/WHEEL_FILENAME`` (replace ``pip`` with ``pip3`` if using Python 3) in the repository `root directory <https://github.com/SriBalaji2112/voiceprint_recognition>`__.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Calling ``Microphone()`` gives the error ``IOError: No Default Input Device Available``.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As the error says, the program doesn't know which microphone to use.

To proceed, either use ``Microphone(device_index=MICROPHONE_INDEX, ...)`` instead of ``Microphone(...)``, or set a default microphone in your OS. You can obtain possible values of ``MICROPHONE_INDEX`` using the code in the troubleshooting entry right above this one.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The program doesn't run when compiled with `PyInstaller <https://github.com/pyinstaller/pyinstaller/wiki>`__.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As of PyInstaller version 3.0, VoiceprintRecognition is supported out of the box. If you're getting weird issues when compiling your program using PyInstaller, simply update PyInstaller.

You can easily do this by running ``pip install --upgrade pyinstaller``.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Ubuntu/Debian, I get annoying output in the terminal saying things like "bt_audio_service_open: [...] Connection refused" and various others.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "bt_audio_service_open" error means that you have a Bluetooth audio device, but as a physical device is not currently connected, we can't actually use it - if you're not using a Bluetooth microphone, then this can be safely ignored. If you are, and audio isn't working, then double check to make sure your microphone is actually connected. There does not seem to be a simple way to disable these messages.

For errors of the form "ALSA lib [...] Unknown PCM", see `this StackOverflow answer <http://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time>`__. Basically, to get rid of an error of the form "Unknown PCM cards.pcm.rear", simply comment out ``pcm.rear cards.pcm.rear`` in ``/usr/share/alsa/alsa.conf``, ``~/.asoundrc``, and ``/etc/asound.conf``.

For "jack server is not running or cannot be started" or "connect(2) call to /dev/shm/jack-1000/default/jack_0 failed (err=No such file or directory)" or "attempt to connect to server failed", these are caused by ALSA trying to connect to JACK, and can be safely ignored. I'm not aware of any simple way to turn those messages off at this time, besides `entirely disabling printing while starting the microphone <https://github.com/Uberi/speech_recognition/issues/182#issuecomment-266256337>`__.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On OS X, I get a ``ChildProcessError`` saying that it couldn't find the system FLAC converter, even though it's installed.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installing `FLAC for OS X <https://xiph.org/flac/download.html>`__ directly from the source code will not work, since it doesn't correctly add the executables to the search path.

Installing FLAC using `Homebrew <http://brew.sh/>`__ ensures that the search path is correctly updated. First, ensure you have Homebrew, then run ``brew install flac`` to install the necessary files.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Developing
----------

To hack on this library, first make sure you have all the requirements listed in the "Requirements" section.

-  Most of the library code lives in ``voiceprint_recognition/__init__.py``.
-  Examples live under the ``examples/`` `directory <https://github.com/SriBalaji2112/voiceprint_recognition/tree/master/examples>`__, and the demo script lives in ``voiceprint_recognition/__main__.py``.
-  The FLAC encoder binaries are in the ``voiceprint_recognition/`` `directory <https://github.com/SriBalaji2112/voiceprint_recognition/tree/master/voiceprint_recognition>`__.
-  Documentation can be found in the ``reference/`` `directory <https://github.com/SriBalaji2112/voiceprint_recognition/tree/master/reference>`__.
-  Third-party libraries, utilities, and reference material are in the ``third-party/`` `directory <https://github.com/SriBalaji2112/voiceprint_recognition/tree/master/third-party>`__.

To install/reinstall the library locally, run ``python setup.py install`` in the project `root directory <https://github.com/SriBalaji2112/voiceprint_recognition>`__.

Before a release, the version number is bumped in ``README.rst`` and ``voiceprint_recognition/__init__.py``. Version tags are then created using ``git config gpg.program gpg2 && git config user.signingkey DB45F6C431DE7C2DCD99FF7904882258A4063489 && git tag -s VERSION_GOES_HERE -m "Version VERSION_GOES_HERE"``.

Releases are done by running ``make-release.sh VERSION_GOES_HERE`` to build the Python source packages, sign them, and upload them to PyPI.


Example Code
~~~~~~~~~~~~
from voiceprint_recognition import Engine, Container
from voiceprint_recognition.Tools import Data, Predictor, SR_Model
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
Engine.start(dir_path)

Data.addUserName("BalajiSanthanam")
Data.recordNewAudio()

SR_Model.trainModel()
model = SR_Model.loadModel()

print(Predictor.predict(model))
# Data.deleteUser("BalajiSanthanam")

## Container Features
# Container.getWaveFilePath()
# Container.users()
# Container.usersCount()

~~~~~~~~~~~~~~

Authors
-------
::

    SriBalaji2112 <sribalaji2112@gmail.com> <sribalaji.rf.gd> (Balaji Santhanam)
    
Please report bugs and suggestions at the `issue tracker <https://github.com/SriBalaji2112/voiceprint_recognition/issues>`__!


License
-------

Copyright 2014-2017 `Balaji Santhanam (SriBalaji2112) <http://sribalaji.rf.gd/>`__. The source code for this library is available online at `GitHub <https://github.com/SriBalaji2112/voiceprint_recognition>`__.

VoiceprintRecognition is made available under the 3-clause BSD license. See ``LICENSE.txt`` in the project's `root directory <https://github.com/SriBalaji2112/voiceprint_recognition>`__ for more information.

For convenience, all the official distributions of VoiceprintRecognition already include a copy of the necessary copyright notices and licenses. In your project, you can simply **say that licensing information for VoiceprintRecognition can be found within the VoiceprintRecognition README, and make sure VoiceprintRecognition is visible to users if they wish to see it**.

VoiceprintRecognition distributes source code, binaries, and language files from `CMU Sphinx <http://cmusphinx.sourceforge.net/>`__. These files are BSD-licensed and redistributable as long as copyright notices are correctly retained. See ``voiceprint_recognition/pocketsphinx-data/*/LICENSE*.txt`` and ``third-party/LICENSE-Sphinx.txt`` for license details for individual parts.

VoiceprintRecognition distributes source code and binaries from `PyAudio <http://people.csail.mit.edu/hubert/pyaudio/>`__. These files are MIT-licensed and redistributable as long as copyright notices are correctly retained. See ``third-party/LICENSE-PyAudio.txt`` for license details.

VoiceprintRecognition distributes binaries from `FLAC <https://xiph.org/flac/>`__ - ``voiceprint_recognition/flac-win32.exe``, ``voiceprint_recognition/flac-linux-x86``, and ``voiceprint_recognition/flac-mac``. These files are GPLv2-licensed and redistributable, as long as the terms of the GPL are satisfied. The FLAC binaries are an `aggregate <https://www.gnu.org/licenses/gpl-faq.html#MereAggregation>`__ of `separate programs <https://www.gnu.org/licenses/gpl-faq.html#NFUseGPLPlugins>`__, so these GPL restrictions do not apply to the library or your programs that use the library, only to FLAC itself. See ``LICENSE-FLAC.txt`` for license details.


