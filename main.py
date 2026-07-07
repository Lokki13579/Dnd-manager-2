from character_data import Character

c = Character()
c.set_level(5)
c.set_common_exp(6550)
'''
почему то скилы обнуляются надо узнать почему и где это происходит
'''
print(c.__dict__)