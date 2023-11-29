

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Bucket(metaclass=SingletonMeta):
    def __init__(self):
        # Inicjalizacja klienta serwera
        self.ref_number = 0

    def add_ref_num(self):
        self.ref_number += 1

    def get_ref_num(self):
        return self.ref_number
    

def signleton_demo():
    Bucket().add_ref_num()
    ref_num = Bucket().get_ref_num()
    print(f"--- singletone test {ref_num}---")