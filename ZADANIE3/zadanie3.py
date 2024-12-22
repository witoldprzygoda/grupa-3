import fitz  # pip install pymupdf
import tkinter as tk
from tkinter import filedialog

okno = tk.Tk()
# dodać tytuł, rozmiar

# dodać widget Text i umieściś z jakimś marginesem

# Funkcja do czyszczenia zawartości Text
def clear_text():
   pass

# Funkcja do otwierania pliku PDF
def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file = fitz.open(file)  
      for page in pdf_file:  
         content = page.get_text()  
         text.insert(tk.END, content)

# Funkcja do zamknięcia aplikacji
def quit_app():
   pass

# utworzyć widget Menu i jego strukturę jak na rysunku
# Open powinno wołać open_pdf
# Clear powinno wołać clear_text
# Quit powinno wołać quit_app

okno.mainloop()
