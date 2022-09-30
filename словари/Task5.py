emails = {'mgu.edu': ['nikita_sborik', 'ivan_ivanov', 'ivan_korunov', 'pavel_horoshavin'],
      	'gmail.com': ['alex.shavtsov', 'ivan.tupia', 'kate.jonson'],
      	'yandex.ru': ['ivan_petrenko', 'igor_tokach'],
      	'mail.ru': ['eren_yeager', 'mikasa_akerman', 'alexandra_brown']}
for key, value in emails.items():
   for element in value:
      m = str(element) + '@' + str(key)
      print(m)