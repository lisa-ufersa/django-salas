from faker import Faker
from salas.models import Sala

class SalaFactory():

    def __init__(self):
        self.faker = Faker()

    def create(self):
        sala = Sala.objects.create(
            nome=self.faker.name(),
            local=self.faker.city(),
            capacidade=self.faker.pyint(),
            is_lab=self.faker.pybool(),
        )
        return sala
    
    def create_many(self, num):
        for _ in range(num):
            temp = self.create()
            temp.save()
            