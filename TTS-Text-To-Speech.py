#!/bin/python
# TTS - Text To Speech
# Version v1
# Written by: Othmane Moutaouakkil [ WHOAMI2507 ]  (You don't become a coder by just changing the credits)
# Github: https://github.com/whoami2507



from gtts import gTTS

print('''\
  _____ _____ ____            _____         _     _          ____                       _     
 |_   _|_   _/ ___|          |_   _|____  _| |_  | |_ ___   / ___| _ __   ___  ___  ___| |__  
   | |   | | \___ \   _____    | |/ _ \ \/ / __| | __/ _ \  \___ \| '_ \ / _ \/ _ \/ __| '_ \ 
   | |   | |  ___) | |_____|   | |  __/>  <| |_  | || (_) |  ___) | |_) |  __/  __/ (__| | | |
   |_|   |_| |____/            |_|\___/_/\_\\__|  \__\___/  |____/| .__/ \___|\___|\___|_| |_|
                                                                  |_|                         
 Written by: WHOAMI2507
''' + '\n'*2)


# enter text-to-speech
my_text = input(' Enter text-to-speech:\n > ')


# The language changed by changing 'en' (PS: 'en' means English) search on [Language Codes according to ISO 639-1] file for more Languages and it's Abbreviation
tts = gTTS(text=my_text, lang='en', slow=False)
tts.save('converted-file.mp3')   # save file as ... (here saving as mp3)


# tells that the operation was successfully done
print("\n [ Done! ]")


# exit
input('\n'*2 + ' [!] Hit enter to exit...')
