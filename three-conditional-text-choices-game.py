print('''      ████   █████    ███   █ ████   █████  ██████       ████    ████   ███████ █ ██  ██████
     ██      █   █   ██     ██  ██   █      █ █  █      ██  ██   █         █    █ ██  █
      ████   █       █      █████    ███      █    █    █    █   ██     █  █    █ ██  ███
         █   ████    █      ██ ███   █        █    █    █    █   █████  █  █    ████  █
    ██  ██   █       ██     ██   ███ █  █     █         ██  ██   ██        █    █  ██ █
     ████    ███████   ████  █       ████     █          ████    █         █    █  ██ ████

     ██████  ███  ██████   █████  ██████  ████  █     ██  ██     ██     ████ ███████████████ ████
    ██    █  █ █     █    ██       █      █  █  █    ███ ███    ███    ██        █   █      ██  █
    █      █ ███     █    █   ███  ██     █  ██ █ █ ██ ███ █    █ ██   █         █   ███    █████
    █      █ ███     █     █    ██  █     █   ███ █ █  ██   █  ███ █   █████     █  ██      ████
    █      █ █ ███   █     ██  ██   ██    █    ██   █  █    █  █   ██      █     █  █       ██ ██
     ██████  █   █ █████     ███  ███████ █     █   █       █  █    █  █████     █  █████   ██   █''')
print('''                                 ███
                                  ███▓▓▓▓▓▓▓
                                    ██▓▓▒░█▓▓▓
                                    █▓▓▒▒▒░░░▓▓▒
                                  ██▓▓▒▒▒░░░░░░▓▓
                                 █▓▓▒▒▒▒░░███░░░▒▓
Compressing objects: 100% (3/3), █▓▒▒▒▒▒░███████░░▓
                                 █▓▓▒▒░░██████░██░▓▒
                                 █▓▓▒▒░███▒██████▓▓▒
                               ██▓▓▒▒▒░██████████▓░▒                          ▓▓
                              ██▓▓▒▒▒░███▓███████▓░▒                          ▓▓▓
                              █▓▓▒▒▒░██▓███▒█████▓▒▒                          ▓▓▓
                              █▓▓▒▒▒▒░██████████▓█▒                       █   ▓▓▓
                              █▓▓▓▒▓▒▒░░████████▓█▒▒▒▒█              ▒▒  ██ ▓▓▓▓▓
                                █▓▓▓▓▓▒░░██▒██▓▓█▒░░░░░▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█░▓▓  ▓▓
                            ████▒▒▓▓▓▓▓▓▓▓███▓░░░░░░░░░░░░░░░░░░░░      █ ░    ▓ Writing objects: 100% (3
                           █▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒ ░░ ░▓▓▓▓▓▓▓▓▓▓▓ ░░░░░░░░░░░░░▓▓▓▓▓▓
                          ▓▓▓▒▒▒▒██▓▒▒▒▒▒▒▒░░░░░░▓▓▓▓██    ██████████████ ░   ▓▓▓▓
                         ▓▓▓▒▒▒███▓▓▒▒▒▒▒▒░░░░░░ ▓▓                     ███    ▓▓▓
                        █▓▓▒▒▒██▓▓▓▒▒▒▒▒▒░░░░░░░░ ▓
                        █▓▓▒▒▒█▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░▓''')

answer = input('''You have finished coding your message and wish to send it to The Hub.
But first you must package it correctly. WHAT! is the first commandment?''')
correct = 'git add .'
if answer!= correct:
    print('No! You have now been sentenced to 3 hours troubleshooting. Return later to try again')
elif answer == correct:
    answer = input('There you go now all your little files are in the box. Now what is the next commandment?')
    correct = 'git commit -m "..."'
    if answer != correct:
        print('No! You have now been sentenced to 3 hours troubleshooting. Return later to try again')
    elif answer == correct:
        answer = input('There you go now the entry is commited to the log. Now what is the next commandment?')
        correct = 'git push origin master'
        if answer != correct:
            print('No! You have now been sentenced to 3 hours troubleshooting. Return later to try again')
        else:
            print('Yay, you did it!')
