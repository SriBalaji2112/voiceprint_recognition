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





