def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return (
            "Équilatéral" if a == b == c else
            "Rectangle et Isocèle" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else
            "Isocèle" if a == b or a == c or b == c else
            "Rectangle"
        )
    else:
        return "Impossible de former un triangle"

if __name__ == "__main__":
    try:
        a, b, c = map(float, input("Entrez les longueurs a, b, c séparées par des espaces : ").split())
        
        result = type_triangle(a, b, c)
        print(f"Le triangle est de type : {result}")
    except ValueError:
        print("Veuillez saisir des longueurs valides.")
