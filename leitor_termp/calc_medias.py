import json
class calc:
    def __init__(self):
        self.min_valor
        self.max_valor
        self.media

    def min_valor(self, valores):
        values = json.loads(valores)
        #print(values)
        min_valor = 0
        for value in values:
            if(min_valor == 0 ):
                min_valor = values[value]
            elif(min_valor > values[value]):
                min_valor = values[value]
        return min_valor

    def max_valor(self, valores):
        values = json.loads(valores)
        #print(values)
        max_valor = 0
        for value in values:
            if(max_valor == 0 ):
                max_valor = values[value]
            elif(max_valor < values[value]):
                max_valor = values[value]
        return max_valor

    def media(self, valores):
        values = json.loads(valores)
        #print(values)
        num_valores = 0
        total = 0
        for value in values:
            total = total + float(values[value])
            num_valores = num_valores + 1
        return total / num_valores

