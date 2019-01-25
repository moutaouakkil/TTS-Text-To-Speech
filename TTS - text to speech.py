# firstly install [gtts] module by typing: pip install gtts (on windows)

from gtts import gTTS


print('''\
  _____ _____ ____            _____         _     _          ____                       _     
 |_   _|_   _/ ___|          |_   _|____  _| |_  | |_ ___   / ___| _ __   ___  ___  ___| |__  
   | |   | | \___ \   _____    | |/ _ \ \/ / __| | __/ _ \  \___ \| '_ \ / _ \/ _ \/ __| '_ \ 
   | |   | |  ___) | |_____|   | |  __/>  <| |_  | || (_) |  ___) | |_) |  __/  __/ (__| | | |
   |_|   |_| |____/            |_|\___/_/\_\\__|  \__\___/  |____/| .__/ \___|\___|\___|_| |_|
                                                                  |_|                         
 Developed by: whoami2507
''' + '\n'*2)


# enter text-to-speech
my_text = input(' Enter text-to-speech:\n > ')


tts = gTTS(text=my_text, lang='en', slow=False)
tts.save('name.mp3')   # save file as ...


# tells that the operation was successfully done
print("\n [ Done! ]")


# exit
input('\n'*2 + ' [!] Hit enter to exit...')
