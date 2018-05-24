# Automatic-Answer-Checker

Automatic answer checker AI app that can check your provided answer and judge it.After checking,it provides a score according to your answer.

# Dependencies

    Django==1.11
    django-crispy-forms==1.7.2
    pytz==2018.4
  
# Instructions

    1. Make sure you have installed python3.6,pip3 and virtualenv.
    2. Open the terminal and  run the following command(Linux/OSX).For windows,you can use Powershell.

      virtualenv AutoAnsChecker && cd AutoAnsChecker
      source bin/activate

      #Now download/clone the folder.
      #Copy src and static_in_env form downloaded folder and paste it inside the AutoAnsChecker folder.
      #Create a new directory named "media_root" inside the static_in_env folder.

      Finally run the following command.

      cd src
      pip install -r requirements.txt
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver

     3. Now open your browser and go to the link http://127.0.0.1:8000
