import tkinter as tk


class Kalkulacka:
    def __init__(self, okno):
        self.okno = okno
        self.prvni_cislo = None
        self.zvolena_operace = None

        # Základní nastavení okna
        self.okno.title("Kalkulačka v2.0.0")
        self.okno.geometry("350x500")
        self.okno.resizable(False, False)


if __name__ == "__main__":
    okno = tk.Tk()
    aplikace = Kalkulacka(okno)
    okno.mainloop()