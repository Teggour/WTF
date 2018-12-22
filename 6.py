class Unit(ABC):
    @property
    @abs  #abstractmethod
    def health(self):
        pass

    @health.setter
    def health(self, value):
        pass

    UNITS = {}

    @classmethod
    def register(cls, name):
        def dec(unit_cls):
            cls.UNITS[name] = unit_cls
            return unit_cls
        return dec

    @classmethod
    def new(cls, name):
        return cls.UNITS[name]


Unit.new('soldier')
Unit.new('vehicle')


class Soldier(Unit):
    pass


class Vehicle(Unit):
    pass
