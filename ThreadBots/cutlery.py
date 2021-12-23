from attr import attrs, attrib

@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: 'Cutlery', knives: int=0, forks: int=0) -> None:
        self.change(knives, forks)
        to.change(knives, forks)
    
    def change(self, knives: int, forks: int) -> None:
        self.knives += knives
        self.forks += forks

kitchen = Cutlery(knives= 100, forks= 100)