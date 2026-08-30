import tkinter as tk


class Kalkulacka:
    def __init__(self, okno):
        self.okno = okno
        self.prvni_cislo = None
        self.zvolena_operace = None

        self.okno.title("Kalkulačka v2.0.0")
        self.okno.geometry("350x500")
        self.okno.resizable(False, False)

        self.displej = tk.Entry(
            self.okno,
            font=("Arial", 24),
            justify="right"
        )

        self.displej.pack(
            padx=20,
            pady=20,
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
            [("7", lambda: self.pridat_cislo("7")), ("8", lambda: self.pridat_cislo("8")), ("9", lambda: self.pridat_cislo("9")), ("/", None)],
            [("4", lambda: self.pridat_cislo("4")), ("5", lambda: self.pridat_cislo("5")), ("6", lambda: self.pridat_cislo("6")), ("*", None)],
            [("1", lambda: self.pridat_cislo("1")), ("2", lambda: self.pridat_cislo("2")), ("3", lambda: self.pridat_cislo("3")), ("-", None)],
            [("0", lambda: self.pridat_cislo("0")), (".", lambda: self.pridat_cislo(".")), ("C", self.vymazat_vse), ("+", None)],
            [("//", None), ("%", None), ("^", None), ("log", None)],
            [("√", None), ("!", None), ("|x|", None), ("=", None)]
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


if __name__ == "__main__":
    okno = tk.Tk()
    aplikace = Kalkulacka(okno)
    okno.mainloop()