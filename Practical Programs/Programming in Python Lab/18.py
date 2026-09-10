class RomanNumeral:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    def __init__(self, number):
        self.number = number

    def convert(self) -> str:
        number = self.number
        roman = ""

        # Thousands
        while number >= self.M:
            roman += "M"
            number -= self.M

        # Hundreds
        if number >= 900:
            roman += "CM"
            number -= 900
        elif number >= self.D:
            roman += "D"
            number -= self.D
        elif number >= 400:
            roman += "CD"
            number -= 400

        while number >= self.C:
            roman += "C"
            number -= self.C

        # Tens
        if number >= 90:
            roman += "XC"
            number -= 90
        elif number >= self.L:
            roman += "L"
            number -= self.L
        elif number >= 40:
            roman += "XL"
            number -= 40

        while number >= self.X:
            roman += "X"
            number -= self.X

        # Units
        if number == 9:
            roman += "IX"
            number -= 9
        elif number >= self.V:
            roman += "V"
            number -= self.V
        elif number == 4:
            roman += "IV"
            number -= 4

        while number >= self.I:
            roman += "I"
            number -= self.I

        return roman


number = int(input("Enter an integer: "))

if 1 <= number <= 3999:
    obj = RomanNumeral(number)
    print("Roman numeral:", obj.convert())
else:
    print("Please enter a number between 1 and 3999.")