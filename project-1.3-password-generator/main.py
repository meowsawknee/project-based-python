from src.pin_generator import PinCodeGenerator
from src.random_generator import RandomPasswordGenerator
from src.memorable_generator import MemorablePasswordGenerator


# test
if __name__ == "__main__":
    pin = PinCodeGenerator(6)
    pin_password = pin.generate()
    print("Pin code: ", pin_password)
    print("Pin strength: ", pin.get_strength())
    pin.export_to_file("pin.txt")
    pin.copy_to_clipboard()

    print()

    rnd = RandomPasswordGenerator(10, True, True)
    rnd_password = rnd.generate()
    print("Random password: ", rnd_password)
    print("Random password strength: ", rnd.get_strength())
    rnd.export_to_file("random.txt")
    rnd.copy_to_clipboard()

    print()

    mem = MemorablePasswordGenerator(3, capitalization=True)
    mem_password = mem.generate()
    print("Memorable password: ", mem_password)
    print("Memorable password strength: ", mem.get_strength())
    mem.export_to_file("memorable.txt")
    mem.copy_to_clipboard()
    