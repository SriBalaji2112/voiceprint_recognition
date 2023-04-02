from voiceprint_recognition.Tools.DataField import *
from voiceprint_recognition import Container
from voiceprint_recognition.Tools import DataField
global LAST_NAME, ROOT, All_NAMES

directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__))


def addUserName(userName):
    """
    1.	Add the new user
    2.	This function is used to Store a new user’s name for the new audio record
    """
    global LAST_NAME, names
    user_name = userName
    if user_name != "" and user_name not in Container.userNames():
        names.append(user_name)
    LAST_NAME = userName
    lastname = open(f"{Container.getPath()}/txtPath/addUser.txt", "w")
    lastname.write(LAST_NAME)
    lastname.close()


def getUsersName():
    lastname = open(f"{Container.getPath()}/txtPath/addUser.txt", "r")
    name = lastname.read()
    lastname.close()
    return name


def addUserVoiceByAudioFile(filepath):
    """
    This used to embed the pre-recorded audio-file  as a new audio input.
    Args:
        filepath:

    Returns:

    """
    global LAST_NAME
    audioPath = open(f"{Container.getPath()}/txtPath/audioPath.txt", "w")
    audioPath.write(filepath)
    audioPath.close()
    splitAudioFileOnSilence()
    exportAudioFill(getUsersName())
    return "Audio Fill Added..."


def deleteUser(name):
    """
    This function used to delete a particular audio by passing the parameter as the username to be deleted
    Args:
        name:

    Returns:

    """
    if name in Container.userNames():
        shutil.rmtree(f"{Container.getWordPath()}\\sentence\\{name}")
        names.remove(name)
        print("Deleted.")
        return 1
    else:
        print("Given Name are not Found")
        return exit(0)


def Users():
    global names
    return names


def recordNewAudio():
    """
    This function used to record a live voice for 50 seconds using the microphone of their device and
    save that voice in given new username.
    whenever the audio is silent it is split
    The entire audio is converted into 80-90 WAV files.
    Exported to the personal workspace created for your project folder.
    """

    SEC = 50
    print("Get ready to record audio input\n")
    print("\nPrepare your audio recording device.  \n")
    sleep(1)
    print(f"You have {SEC} seconds to read the passage below.  \n")
    sleep(1)
    print('"Voice Identification Module"\n'
          '"Give papa a cup of proper coffee in a copper coffee cup."\n'
          '"How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"\n'
          '"I scream, you scream, we all scream for ice cream!"\n'
          '"Red lorry, yellow lorry."\n'
          '"Supercalifragilisticexpialidocious"\n'
          '"Repeat Again..."')
    sleep(1)
    print("Record will start in 3 ", end='')
    sleep(1)
    print("2 ", end='')
    sleep(1)
    print("1 ")
    sleep(1)
    userName = getUsersName()
    DataField.createRecordDATA("sentence", SEC)
    DataField.splitAudioOnSilence(["sentence"])
    DataField.exportRecordings(userName, ["sentence"])