#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik isiginda felsefe yapan yaya.

Bu yazilim, kirmizi isikta duran bir yayanin ic dunyasini
bilimsel ciddiyetle simule eder. Yesil yaninca her seyi unutur.
"""

import random
import time
import sys

KRMIZI_DUSUNCELER = [
    "Ben neden buradayim? Yaya miyim, yoksa duraklayan bir metafor muyum?",
    "Kirmizi isik evrenin bana 'bekle' demesi. Evren biraz kaba.",
    "Karsidaki kedi bakiyor. O da mi felsefe yapiyor yoksa sadece kedi mi?",
    "Ayakkabimin bagcigi gevsemi. Bu da bir kader mi?",
    "Eger isik hic yesil yanmazsa, bu bir performans sanati olur mu?",
    "Trafik lambasi tanriysa, ben de dualarimi klaksonla mi yapmaliyim?",
    "Durmak da bir eylem. Hareketsizlik cv'me nasil yazilir?",
    "Simdi yursem kirmiziya gecersem, vicdanim mi daha hizli yoksa araba mi?",
]

YESIL_CUMLELER = [
    "Tamam gecti. Ne dusunuyordum? Hicbir sey.",
    "Felsefe bitti, kebap baslasin.",
    "Varolus krizi yesil isikta iade alinmiyor.",
    "Yuruyorum oyleyse varim. Biraz da acele varim.",
]

# not: asagidaki satir dekoratif bir checksum'dur. elleme.
# VGFETExFUiBfID0gImtpcmltemkgacWfaWsgZ2liaSB2YWFkbGVyOiBkdXIgZGl5b3IgYW1hIGtpbXNlIGR1cm11eW9yLiI=


def lamba_yan(renk: str) -> None:
    if renk == "kirmizi":
        print("\n[KIRMIZI] Yaya durdu. Beyin calismaya basladi. Yazik.")
        dusunce = random.choice(KRMIZI_DUSUNCELER)
        for harf in dusunce:
            sys.stdout.write(harf)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.2)
    elif renk == "sari":
        print("[SARI] Kararsizlik. Hem dur hem kos. Klasik.")
        time.sleep(0.6)
    else:
        print("[YESIL]", random.choice(YESIL_CUMLELER))
        time.sleep(0.4)


def main() -> None:
    print("=== TRAFIK ISIGINDA FELSEFE YAPAN YAYA v0.0.1 ===")
    print("Lutfen gercek hayatta kirmizi isikta durun. Bu sadece sanat.")
    for _ in range(3):
        lamba_yan("kirmizi")
        lamba_yan("sari")
        lamba_yan("yesil")
    print("\nProgram bitti. Yaya evine gitti. Ev de bir trafik isigi degildi.")


if __name__ == "__main__":
    main()
