import tkinter as tk

from matematika import (
    secti, odecti, vynasob, vydel, cele_deleni, zbytek,
    mocnina, odmocnina, faktorial, absolutni_hodnota, logaritmus
)
from historie import (
    nacti_historii,
    uloz_vypocet,
    smaz_historii
)
from nastaveni import nacti_nastaveni, uloz_nastaveni


class Kalkulacka:
    def __init__(self, okno):
        self.okno = okno
        self.prvni_cislo = None
        self.zvolena_operace = None
        
        self.desetinna_mista = nacti_nastaveni()
        self.historie = nacti_historii()

        self.okno.title("Kalkulačka v2.0.0")
        self.okno.geometry("350x530")
        self.okno.resizable(False, False)

        # Horní lišta pro mini tlačítko historie
        self.horni_lista = tk.Frame(self.okno)
        self.horni_lista.pack(fill="x", padx=20, pady=(10, 0))

        self.btn_historie = tk.Button(
            self.horni_lista,
            text="📜 Historie",
            font=("Arial", 9),
            command=self.zobrazit_historii
        )
        self.btn_historie.pack(side="right")

        self.btn_nastaveni = tk.Button(
            self.horni_lista,
            text="⚙️ Nastavení",
            font=("Arial", 9),
            command=self.zobrazit_nastaveni
        )
        self.btn_nastaveni.pack(side="right", padx=(0, 10))

        self.displej = tk.Entry(
            self.okno,
            font=("Arial", 24),
            justify="right"
        )

        self.displej.pack(
            padx=20,
            pady=(5, 20),
            fill="x"
        )

        self.ramecek_tlacitka = tk.Frame(self.okno)
        self.ramecek_tlacitka.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        self.vytvorit_tlacitka()

    def vytvorit_tlacitka(self):
        tlacitka = [
            [("7", lambda: self.pridat_cislo("7")), ("8", lambda: self.pridat_cislo("8")), ("9", lambda: self.pridat_cislo("9")), ("/", lambda: self.zvolit_operaci("/"))],
            [("4", lambda: self.pridat_cislo("4")), ("5", lambda: self.pridat_cislo("5")), ("6", lambda: self.pridat_cislo("6")), ("*", lambda: self.zvolit_operaci("*"))],
            [("1", lambda: self.pridat_cislo("1")), ("2", lambda: self.pridat_cislo("2")), ("3", lambda: self.pridat_cislo("3")), ("-", lambda: self.zvolit_operaci("-"))],
            [("0", lambda: self.pridat_cislo("0")), (".", lambda: self.pridat_cislo(".")), ("C", self.vymazat_vse),                ("+", lambda: self.zvolit_operaci("+"))],
            [("//", lambda: self.zvolit_operaci("//")), ("%", lambda: self.zvolit_operaci("%")), ("^", lambda: self.zvolit_operaci("^")), ("log", lambda: self.zvolit_operaci("log"))],
            [("√", lambda: self.jednoducha_operace("√")), ("!", lambda: self.jednoducha_operace("!")), ("|x|", lambda: self.jednoducha_operace("|x|")), ("=", self.spocitat)]
        ]

        for radek_idx, radek in enumerate(tlacitka):
            for sloupec_idx, (text, prikaz) in enumerate(radek):
                btn = tk.Button(
                    self.ramecek_tlacitka,
                    text=text,
                    font=("Arial", 16),
                    command=prikaz
                )
                btn.grid(row=radek_idx, column=sloupec_idx, padx=4, pady=4, sticky="nsew")

        for i in range(4):
            self.ramecek_tlacitka.columnconfigure(i, weight=1)
        for i in range(6):
            self.ramecek_tlacitka.rowconfigure(i, weight=1)

    def pridat_cislo(self, cislo):
        self.displej.insert(tk.END, cislo)

    def vymazat_displej(self):
        self.displej.delete(0, tk.END)

    def vymazat_vse(self):
        self.vymazat_displej()
        self.prvni_cislo = None
        self.zvolena_operace = None

    def nacist_cislo(self):
        hodnota = float(self.displej.get())
        return int(hodnota) if hodnota.is_integer() else hodnota

    def zvolit_operaci(self, operace):
        try:
            self.prvni_cislo = self.nacist_cislo()
            self.zvolena_operace = operace
            self.vymazat_displej()
        except ValueError:
            self.zobrazit_chybu()

    def spocitat(self):
        if self.prvni_cislo is None or not self.zvolena_operace:
            return

        operace_mapa = {
            "+": secti, "-": odecti, "*": vynasob, "/": vydel,
            "//": cele_deleni, "%": zbytek, "^": mocnina, "log": logaritmus
        }

        try:
            druhe_cislo = self.nacist_cislo()
            funkce = operace_mapa[self.zvolena_operace]
            vysledek = funkce(self.prvni_cislo, druhe_cislo)

            if self.zvolena_operace == "log":
                vypocet = f"log_{druhe_cislo}({self.prvni_cislo})"
            else:
                vypocet = f"{self.prvni_cislo} {self.zvolena_operace} {druhe_cislo}"

            self.zpracovat_a_zobrazit_vysledek(vypocet, vysledek)

        except (ValueError, ZeroDivisionError, KeyError):
            self.zobrazit_chybu()

    def jednoducha_operace(self, operace):
        mapa_operaci = {
            "√": (odmocnina, lambda c: f"√{c}"),
            "!": (faktorial, lambda c: f"{c}!"),
            "|x|": (absolutni_hodnota, lambda c: f"|{c}|")
        }

        try:
            cislo = self.nacist_cislo()
            funkce, format_vypoctu = mapa_operaci[operace]
            vysledek = funkce(cislo)
            vypocet = format_vypoctu(cislo)
            
            self.zpracovat_a_zobrazit_vysledek(vypocet, vysledek)

        except (ValueError, KeyError):
            self.zobrazit_chybu()

    def zpracovat_a_zobrazit_vysledek(self, vypocet, vysledek):
        vysledek = round(vysledek, self.desetinna_mista)
        if isinstance(vysledek, float) and vysledek.is_integer():
            vysledek = int(vysledek)

        self.vymazat_displej()
        self.displej.insert(0, str(vysledek))

        self.prvni_cislo = None
        self.zvolena_operace = None

        zaznam = f"{vypocet} = {vysledek}"
        self.historie.append(zaznam)
        uloz_vypocet(zaznam)

    def zobrazit_historii(self):
        okno_historie = tk.Toplevel(self.okno)
        okno_historie.title("Historie výpočtů")
        okno_historie.geometry("280x350")
        okno_historie.resizable(False, False)

        scrollbar = tk.Scrollbar(okno_historie)
        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(
            okno_historie,
            font=("Arial", 11),
            yscrollcommand=scrollbar.set
        )
        listbox.pack(
            padx=10, 
            pady=10, 
            fill="both", 
            expand=True
        )
        scrollbar.config(
            command=listbox.yview
        )

        if not self.historie:
            listbox.insert(
                tk.END, "Historie je prázdná"
            )
        else:
            for zaznam in self.historie:
                listbox.insert(
                    tk.END, zaznam
                )

    def zobrazit_nastaveni(self):
        okno_nastaveni = tk.Toplevel(self.okno)

        okno_nastaveni.title("Nastavení")
        okno_nastaveni.geometry("300x200")
        okno_nastaveni.resizable(False, False)

        label = tk.Label(
            okno_nastaveni,
            text="Počet desetinných míst:",
            font=("Arial", 12)
        )
        label.pack(pady=(20, 5))

        desetinna_mista = tk.Entry(
            okno_nastaveni,
            font=("Arial", 12),
            justify="center"
        )
        desetinna_mista.pack()

        desetinna_mista.insert(
            0,
            str(self.desetinna_mista)
        )

        def ulozit():
            try:
                hodnota = int(desetinna_mista.get())

                if hodnota < 0:
                    raise ValueError

                self.desetinna_mista = hodnota
                uloz_nastaveni(hodnota)

                okno_nastaveni.destroy()

            except ValueError:
                chyba = tk.Label(
                    okno_nastaveni,
                    text="Zadej celé číslo 0 nebo větší!",
                    font=("Arial", 9)
                )
                chyba.pack(pady=5)

        tlacitko = tk.Button(
            okno_nastaveni,
            text="Uložit",
            font=("Arial", 12),
            command=ulozit
        )
        tlacitko.pack(pady=20)

    def zobrazit_chybu(self):
        self.vymazat_vse()
        self.displej.insert(0, "Chyba!")


if __name__ == "__main__":
    okno = tk.Tk()
    aplikace = Kalkulacka(okno)
    okno.mainloop()