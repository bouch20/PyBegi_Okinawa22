class Pokemon():
    def __init__(self, name :str, hp :int, attack :int, defence :int, sound :str):
        self.name :str = name
        self.hp :int = hp
        self.attack :int = attack
        self.defence :int = defence
        self.sound :str = sound
    
    def say(self):
        print(f"{self.sound}")
        
    def attack(self, attack):
        return self.attack
    
    def view_status(self):
        print(f"name:{self.name}")
        print(f"hp:{self.hp}")
        print(f"attack:{self.attack}")
        print(f"defence:{self.defence}")
