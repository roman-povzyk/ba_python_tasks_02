name = 'Roman'
day = 'Sunday'

print(f'Good day {name}! {day} is a perfect day to learn some python.')
print('Good day {}! {} is a perfect day to learn some python.'.format(name, day))
print('Good day %s! %s is a perfect day to learn some python.' % (name, day))
print('Good day ' + name + '! ' + day + ' is a perfect day to learn some python.')
