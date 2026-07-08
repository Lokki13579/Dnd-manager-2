from character_data import Character

c = Character()
c.set_class("fighter")
c.set_level(20)
c.set_side_class("eldritch_knight")
print(c.__dict__)