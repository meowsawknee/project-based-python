from src.pin_generator import PinCodeGenerator
from src.random_generator import RandomPasswordGenerator
from src.memorable_generator import MemorablePasswordGenerator


# test
if __name__ == "__main__":
    pin = PinCodeGenerator(6)
    print("Pin code: ", pin.generate())

    rnd = RandomPasswordGenerator(10, True, True)
    print("Random password: ", rnd.generate())

    mem = MemorablePasswordGenerator(3, capitalization=True)
    print("Memorable password: ", mem.generate())
    