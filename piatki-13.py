nazwy_miesiecy = ['styczen','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien','wrzesien','pazdziernik','listopad','grudzien']
miesiace = [31,28,31,30,31,30,31,31,30,31,30,31]
numer_dnia_tygodnia = 1
dzien_w_miesiacu= 1
ile = 0

for i in range(2001,2017):
    print("Rok: " + str(i))
    miesiace[1] = 28
    if i % 4 == 0:
        miesiace[1] = 29
    ob_miesiac = 0;
    while ob_miesiac < 12:
        dzien_w_miesiacu += 1
        numer_dnia_tygodnia += 1
        if dzien_w_miesiacu > miesiace[ob_miesiac]:
            dzien_w_miesiacu = 1
            ob_miesiac += 1
        if numer_dnia_tygodnia > 7:
            numer_dnia_tygodnia = 1
        if dzien_w_miesiacu == 13 and numer_dnia_tygodnia == 5:
            print(nazwy_miesiecy[ob_miesiac])
            ile += 1
print("Piątek 13-stego wystąpił: " + str(ile) + " razy")