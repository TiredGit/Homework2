class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def damage_calculate(self, aim_armor):
        return max(0, self.damage - aim_armor)

    def attack(self, aim):
        real_damage = self.damage_calculate(aim.armor)
        aim.health -= real_damage
        if aim.health < 0:
            aim.health = 0
        print(f'{self.name} атакует {aim.name}а и наносит {real_damage} единиц урона')
        print(f'Здоровье {aim.name}а = {aim.health}')
        print('-' * 40)


class Player(Person):
    def __init__(self, health, damage, armor):
        super().__init__(name='Игрок', health=health, damage=damage, armor=armor)


class Enemy(Person):
    def __init__(self, health, damage, armor):
        super().__init__(name='Противник', health=health, damage=damage, armor=armor)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def play(self):
        print('Кто ходит первым? 0 - Игрок, 1 - Противник')
        next_step = int(input())
        print(f'Начальное здоровье игрока: {self.player.health}')
        print(f'Начальное здоровье противника: {self.enemy.health}')
        print('-' * 40)
        while self.player.health > 0 and self.enemy.health > 0:
            if next_step == 0:
                self.player.attack(self.enemy)
                next_step = 1
            else:
                self.enemy.attack(self.player)
                next_step = 0

        if self.player.health > 0:
            print('Игрок победил!!!')
        else:
            print('Противник победил!')


player1 = Player(health=100, damage=20, armor=10)
player2 = Enemy(health=160, damage=15, armor=5)
game = Game(player1, player2)
game.play()
