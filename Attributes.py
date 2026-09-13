# 1. Hero class with name and hp
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __repr__(self):
        return f"{self.name} ({self.hp} HP)"

    # 2. Added a method to take damage and subtract from hp
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0


# 3. Created two heroes and only Arthur takes damage
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"Arthur's HP: {arthur.hp}")
print(f"Morgana's HP: {morgana.hp}")