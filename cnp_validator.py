import numpy as np

district = {'01': 'Alba',
            '02': 'Arad',
            '03': 'Argeș',
            '04': 'Bacău',
            '05': 'Bihor',
            '06': 'Bistrița-Năsăud',
            '07': 'Botoșani',
            '08': 'Brașov',
            '09': 'Brăila',
            '10': 'Buzău',
            '11': 'Caraș-Severin',
            '12': 'Cluj',
            '13': 'Constanța',
            '14': 'Covasna',
            '15': 'Dâmbovița',
            '16': 'Dolj',
            '17': 'Galați',
            '18': 'Gorj',
            '19': 'Harghita',
            '20': 'Hunedoara',
            '21': 'Ialomița',
            '22': 'Iași',
            '23': 'Ilfov',
            '24': 'Maramureș',
            '25': 'Mehedinți',
            '26': 'Mureș',
            '27': 'Neamț',
            '28': 'Olt',
            '29': 'Prahova',
            '30': 'Satu Mare',
            '31': 'Sălaj',
            '32': 'Sibiu',
            '33': 'Suceava',
            '34': 'Teleorman',
            '35': 'Timiș',
            '36': 'Tulcea',
            '37': 'Vaslui',
            '38': 'Vâlcea',
            '39': 'Vrancea',
            '40': 'București',
            '41': 'București - Sector 1',
            '42': 'București - Sector 2',
            '43': 'București - Sector 3',
            '44': 'București - Sector 4',
            '45': 'București - Sector 5',
            '46': 'București - Sector 6',
            '51': 'Călărași',
            '52': 'Giurgiu',
            }
countrys = {int(k): v for k, v in district.items()}
years = {1: "19", 2: "19", 3: "18", 4: "18", 5: "20", 6: "20",
         7: "Persoane straine, rezidente in Romania", 8: "Persoane straine, rezidente in Romania",
         9: "Persoane straine"}
mounth = {1: 'Ianuarie',
          2: 'Februarie',
          3: 'Martie',
          4: 'Aprilie',
          5: 'Mai',
          6: 'Iunie',
          7: 'Iulie',
          8: 'August',
          9: 'Septembrie',
          10: 'Octombrie',
          11: 'Noiembrie',
          12: 'Decembrie'}


def check_length(cnp: str) -> bool:
    if len(cnp) == 13 and cnp.isnumeric():
        return True
    return False


def check_sex(cnp: str) -> bool:
    if cnp[0] == 0:
        return False
    return True


def check_month(cnp: str) -> bool:
    if 0 < int(cnp[3:5:1]) < 13:
        return True
    return False


def check_country(cnp: str) -> bool:
    if 0 < int(cnp[7:9:1]) < 47 or 50 < int(cnp[7:9:1]) < 53:
        return True
    return False


def check_nnn(cnp: str) -> bool:
    if int(cnp[9:12:1]) != 0:
        return True
    return False


def calculate_c(cnp: str) -> int:
    array = [int(x) for x in cnp]
    array.pop()
    a = np.dot(np.array(array), np.array([2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]).T)
    a = a % 11
    if a < 10:
        return a
    else:
        return 1


def check_c(cnp: str, c_bun: int) -> bool:
    last = cnp[-1]
    if str(last) == str(c_bun):
        return True
    return False


if __name__ == '__main__':

    cnp = input("Introduceti CNP:")
    a = True
    while a:
        if not check_length(cnp):
            a = False
        if not check_country(cnp):
            a = False
        if not check_sex(cnp):
            a = False
        if not check_month(cnp):
            a = False
        if not check_c(cnp, calculate_c(cnp)):
            a = False
        if not check_nnn(cnp):
            a = False
        break
    if a:
        print("CNP valid")
        print("Informatii persoana: ")
        if int(cnp[0]) % 2 == 0:
            print("Persoana e femeie")
        else:
            print("Persoana e barbat")
        print(years.get(int(cnp[0])))
        print(str(cnp[1:3:1]))
        print(
            f"este nascut/a in {str(years.get(int(cnp[0]))) + str(cnp[1:3:1])}, luna: {str(cnp[3:5:1])}, ziua: {str(cnp[5:7:1])}, "
            f" judetul: {countrys.get(int(cnp[7:9:1]))}")
    else:
        print("invalid")
