import random
import string


class FuncionesExtras:

    def crear_email_random(self):
        email = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        return (email.lower()+"@gmail.com")