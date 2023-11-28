import datetime

try:
    age, pension = int(input('Сколько вам лет?: ')), int(input('Во сколько лет вам на пенсию?: '))
except BaseException:
    print('Вы ввели не число')
    exit(1)

year = datetime.date.today().year
pension_year = year - age + pension
until_pension = pension - age

print(f'У вас осталось {until_pension} года до того, как вы сможете выйти на пенсию.\n'
      f'Сейчас {year} год, так что вы можете выйти на пенсию в {pension_year} году.')


