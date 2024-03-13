def sezar_sifreleyici(metin , anahtar):
    alfabe = 'abcçdefgğhıijklmnoörpsştuüvyz'
    sifrelenmis_metin = ''

    for harf in metin:
        if harf.lower() in alfabe:
            harf_index = alfabe.index(harf.lower())
            yeni_index = (harf_index + (anahtar+1)) % len(alfabe)
            yeni_harf = alfabe[yeni_index]

            if harf.isupper():
                yeni_harf = yeni_harf.upper()

            sifrelenmis_metin += yeni_harf
        else:
            sifrelenmis_metin +=harf
    return sifrelenmis_metin


print(sezar_sifreleyici('Meric',3))
print(sezar_sifreleyici('Nisa', 3))
print(sezar_sifreleyici('mercan',3))
print(sezar_sifreleyici('Kuzu',4))





