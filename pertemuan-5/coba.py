cuaca = input ("apakah cuaca pada hari ini?")

match cuaca:
    case "hujan"|"Hujan"|"HUJAN":
        print("berangkat kuliah pakai jas hujan")
    case "badai":
        print("tidak berangkat kuliah")
    case "panas":
        print("berangkat kuliah pakai mobil")
    case _: 
        print("masuk, jangan lebay")