from temperature import Temperature


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == '__main__':
    temperature = Temperature(country="brazil", city="ribeirao preto").get()
    calorie = Calorie(weight=170, height=187, age=24, temperature=temperature)
    print(calorie.calculate())
