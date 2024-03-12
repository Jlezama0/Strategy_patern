class IattackBehavior:
    def damage(self):
        pass
    def range(self):
        pass

class attack_knight(IattackBehavior):
    def damage(self):
        print("El caballero causa 7 puntos de daño con su espada")
    def range(self):
        print("Su rango de ataque es corto, por lo cual se acerca a sus enemigos para infligir el mayor daño.\n")

class attack_soldier(IattackBehavior):
    def damage(self):
        print("El soldado causa 3 puntos de daño con su lanza")
    def range(self):
        print("Su rango de ataque es medio, esto hace que la primera linea de ataque no arriesgue su posición y haga daño a una distancia media.\n")

class attack_archer(IattackBehavior):
    def damage(self):
        print("El arquero causa 2 puntos de daño con sus flechas")
    def range(self):
        print("Su rango de ataque es largo, es la ultima de ataque, atacan desde largas distancias infringiendo aunque poco daño, efectivo.\n")


class ImovementBehavior:
    def speed(self):
        pass
    def displacement(self):
        pass

class movement_knight(ImovementBehavior):
    def speed(self):
        print("El caballero tiene 5 puntos de velocidad, no es muy rapido debido a su pesada armadura.")
    def displacement(self):
        print("El caballero solo puede desplazarse hacia delante, no retrocede ni se aparta de su posicion.")

class MovementSoldier(ImovementBehavior):
    def speed(self):
        print("El soldado tiene 7 puntos de velocidad, es ágil y puede moverse rápidamente en el campo de batalla.")
    def displacement(self):
        print("El soldado puede desplazarse en cualquier dirección, mostrando versatilidad en su movimiento.")

class MovementArcher(ImovementBehavior):
    def speed(self):
        print("El arquero tiene 6 puntos de velocidad, se mueve con agilidad para mantener distancia con el enemigo.")
    def displacement(self):
        print("El arquero puede retroceder y desplazarse lateralmente, aprovechando su destreza para evadir ataques.")

class MilitaryUnit:
    def __init__(self, attackBehavior:IattackBehavior, movementBehavior: ImovementBehavior):
        self.attackBehavior=attackBehavior
        self.movementBehavior=movementBehavior
    
    def perform_attack(self):
        self.attackBehavior.damage()
        self.attackBehavior.range()

    def perform_movement(self):
        self.movementBehavior.displacement()
        self.movementBehavior.speed()

    
class knight(MilitaryUnit):
    def __init__(self):
        super().__init__(attack_knight(), movement_knight())

class soldier(MilitaryUnit):
    def __init__(self):
        super().__init__(attack_soldier(), MovementSoldier())

class archer(MilitaryUnit):
    def __init__(self):
        super().__init__(attack_archer(), MovementArcher())

if __name__=="__main__":
    knight=knight()
    soldier=soldier()
    archer=archer()

    knight.perform_attack()
    knight.perform_movement()
    print("")
    soldier.perform_attack()
    soldier.perform_movement()
    print("")
    archer.perform_attack()
    archer.perform_movement()