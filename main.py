from help import listen_command
import time
import os
import playsound
from gtts import gTTS



ON = {

    "открыть калькулятор"          : r"%windir%\system32\calc.exe",
    "открыть браузер"              : r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "открыть рисовалку"            : r"%windir%\system32\mspaint.exe",
    "открыть проводник"            : r"%windir%\explorer.exe",
    "выключить компьютер"          : "shutdown /p /f",
    "запустить"                    : "",
    "считать текст"                : "",
    "команды"                     : '"открыть калькулятор"\
                                     "открыть броузер"\
                                     "открыть рисовалку"\
                                     "открыть проводник"\
                                     "выключить компьютер"\
                                     "загугли"\
                                     "запустить"\
                                     "считать текст со страницы"\
                                     "считать текст"\
                                     "проверить скорость интернета"\
                                     "новости дня"\
                                     "комманды"'
}


def say_message(mess):
    voice = gTTS(mess, lang="ru")

    file_voice_name = "_audio_"+str(time.time())+".mp3"
    voice.save(file_voice_name)

    playsound.playsound(file_voice_name)


def do_command(mess):
    global ON

    mess = str(mess).lower()

    if mess in ON.keys():
        if mess != "команды" and mess != "запустить" and mess != "считать текст":
            os.system(ON[mess])

        elif mess == "команды":
            print(ON[mess])

        elif mess == "запустить":
            os.system(input(":"))

        elif mess == "считать текст":
            say_message(input(":"))


while 1:
    lsn = listen_command()
    print(lsn)
    do_command(lsn)
    