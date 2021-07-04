before_raise=float(input("Enter the amount of the study benefits: "))
raise_1=before_raise*(1.17/100)
after_raise=before_raise+raise_1
print('If the index raise is 1.17 percent, the study benefit,',\
      '\nafter a raise, would be',after_raise,\
      'euros',sep=' ')
another_raise=after_raise+(after_raise*(1.17/100))
print('and if there was another index raise, the '+\
      'study \nbenefits would be as much as',\
      another_raise, 'euros', sep=' ')