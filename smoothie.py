ingredient_cost = {
    "Strawberries": 1.50,
    "Banana": 0.50,
    "Mango": 2.50,
    "Blueberries": 1.00,
    "Raspberries": 1.00,
    "Apple": 1.75,
    "Pineapple": 3.50
}


class Smoothie:

    def __init__(self, ingredients):
        self.ingredients = ingredients.split(',')
        self.counts = {}
        for ing in self.ingredients:
            if ing in self.counts:
                self.counts[ing] += 1
            else:
                self.counts[ing] = 1

    def get_cost(self):
        cost = 0
        for ing in self.ingredients:
            cost += ingredient_cost[ing]
        return cost

    def get_price(self):
        return round(self.get_cost()*2.5, 2)

    def get_name(self):
        sorted_ing = sorted(self.ingredients)
        fusion = False
        result = ""
        for i in range(len(sorted_ing)):
            if self.counts[sorted_ing[i]] == 1:
                if sorted_ing[i] == 'Strawberries':
                    sorted_ing[i] = 'Strawberry'
                if sorted_ing[i] == 'Raspberries':
                    sorted_ing[i] = 'Raspberry'
                if sorted_ing[i] == 'Blueberries':
                    sorted_ing[i] = 'Blueberry'
            else:
                fusion = True

            if i < len(sorted_ing)-1:
                result += sorted_ing[i] + " , "
            else:
                result += sorted_ing[i] + " : "

        if fusion:
            return result+"Fusion"
        else:
            return result+"Smoothie"


if __name__ == '__main__':
    smt = Smoothie("Strawberries,Apple,Mango,Raspberries,Banana")
    print(smt.get_cost())
    print(smt.get_price())
    print(smt.get_name())

    smt = Smoothie("Strawberries,Mango,Strawberries")
    print(smt.get_cost())
    print(smt.get_price())
    print(smt.get_name())