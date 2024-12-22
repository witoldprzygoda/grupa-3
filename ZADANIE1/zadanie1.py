import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar

okno = tk.Tk()
# tytuł, rozmiar, blokada wielkości

# utwórz StringVar()

def update_date_time():
	# dzien = i tak dalej... miesiac, rok, czas, dzien
	# czytamy datetime.today().strftime('%A')
	# kody https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
	
	# dt = dzien + ... + "\n" + ...
	# ustaw za pomocą .set dt dla StringVar zrobinego powyżej
	# ważne: rekurencyjne odświeżanie etykiety - patrz poniżej
	date_time.after(1000, update_date_time)

# widget Label ustawiony na StringVar zrobiony na początku, rozmiar, czcionki, tło - wg uznania 
# date_time = Label(...
date_time.pack(anchor="center")

current_time = datetime.now()
# przyda się do kalendarza
# day = odczytaj przez .strftime('%d')
# month = 
# year = 

# utwórz cal = Calendar(...
# wstaw przez .pack poniżej zegara

update_date_time()

okno.mainloop()