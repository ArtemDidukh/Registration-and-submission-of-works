import random


class Litak():
    def __init__(self, name: str, mass, size) -> None:
        assert name.isascii(), "Назва літака має містити символи ASTE"
        assert mass >= 0 and size >= 0, "Маса та Розмір Літака не може бути меншою за 0!"
        # Так працює але так не роблять
        # if not size > 0:
        #    raise AssertionError("Розмір Літак не може бути меншою за 0!")

        self.name = name
        self.mass = mass
        self.size = size

    @property
    def info(self):
        return f"Літак {self.name} має масу {self.mass} кг та розмір {self.size} м."

    def convert_to_pounds(self):
        return self.mass * 2.20462262

    def convert_to_feet(self):
        return self.size * 3.2808399

    @property
    def info_in_en(self):
        return f"Літак {self.name} має масу {self.convert_to_pounds()} фунтів та розмір {self.convert_to_feet()} футів."

    def crash_on_start(self):
        c = random.random()
        print(f"Згенерована імовірність = {c}")
        if c >= 0.9:
            print("Невдалий запуск Літака")
            return False
        else:
            print("Літак успішно полетів")
            return True


# def test_obj_asterics():
#    r = Litak("Asterics 6", 549054, 70)
#    print(r.info)
#    print(r.info_in_en)
#    r2 = Litak("Asterics V", 546700, 58.3)
#    print(r2.info)
#    assert r.name in r.info, "інфо про літак не містить її назви"
#    return True
#
# if test_obj_asterics():
#    print("Перевірки виконано")

r = Litak("Asterics 6", 549054, 70)
r.crash_on_start()