from gtts import gTTS
import time
import playsound
import os

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


def do_command(mess):
    global ON
    mess = str(mess).lower()

    if mess in ON.keys():
        if ON[mess] != "" and ON[mess] != "команды":
            os.system(ON[mess])

        elif mess == "команды":
            print(ON[mess])

        elif mess == "запустить":
            os.system(input("Enter: "))

        elif mess == "считать текст":
            say_message(input("Enter: "))


def say_message(message):
    voice = gTTS(message, lang="ru")
    
    file_voice_name = "_audio_"+str(time.time())+".mp3"
    voice.save(file_voice_name)

    playsound.playsound(file_voice_name)


say_message("Вас приветствует голосовой помощник Nixle, ознакомиться с командами можно по произношению слова комманды")
while 1:
    user = listen_command()
    print(user)
    do_command(user)