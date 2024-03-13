def sifre_coz(sifreli_metin,anahtar=3):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    cozulmus_metin = ''

    for harf in sifreli_metin:
        if harf.lower() in alfabe:
            harf_index = alfabe.index(harf.lower())
            yeni_index = (harf_index - anahtar - 1) % len(alfabe)
            yeni_harf = alfabe[yeni_index]

            if harf.isupper():
                yeni_harf = yeni_harf.upper()

            cozulmus_metin += yeni_harf
        else:
            cozulmus_metin+=harf
    return cozulmus_metin

print(sifre_coz('Phumf',3))
print(sifre_coz('Rmüd',3))
print(sifre_coz('phufdr',3))
print(sifre_coz('Öada',4))

