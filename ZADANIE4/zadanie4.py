from tkinter import Label, StringVar, Button, Entry, filedialog, Canvas, Scrollbar
import tkinter as tk
from PIL import Image, ImageTk


class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Atrybuty
        self.image_fp = None  # Ścieżka do otwartego pliku obrazu
        self.image = None  # Oryginalny obraz
        self.photo_image = None  # Obraz do wyświetlania na Canvas

        # UI
        self.setup_ui()

    def setup_ui(self):
        """Ustawia interfejs użytkownika"""
        # Panel narzędziowy
        toolbar_frame = tk.Frame(self.root)
        toolbar_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Przyciski i pola tekstowe
        Button(toolbar_frame, text="Open", command=self.open_handler).pack(side=tk.LEFT, padx=5, pady=5)

        Label(toolbar_frame, text="Width:").pack(side=tk.LEFT, padx=5)
        self.width_entry_str = StringVar()
        self.width_entry = Entry(toolbar_frame, textvariable=self.width_entry_str, width=10)
        self.width_entry.pack(side=tk.LEFT, padx=5)
        self.width_entry.bind("<KeyRelease>", self.width_modified)

        Label(toolbar_frame, text="Height:").pack(side=tk.LEFT, padx=5)
        self.height_entry_str = StringVar()
        self.height_entry = Entry(toolbar_frame, textvariable=self.height_entry_str, width=10)
        self.height_entry.pack(side=tk.LEFT, padx=5)
        self.height_entry.bind("<KeyRelease>", self.height_modified)

        # Przyciski Resize i Save
        Button(toolbar_frame, text="Resize", command=self.resize_handler).pack(side=tk.LEFT, padx=5)
        Button(toolbar_frame, text="Save", command=self.save_handler).pack(side=tk.LEFT, padx=5)

        # Canvas do wyświetlania obrazu
        canvas_frame = tk.Frame(self.root)
        canvas_frame.grid(row=1, column=0, sticky="nsew")

        self.canvas = Canvas(canvas_frame, bg="gray")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Paski przewijania do Canvas
        self.scroll_x = Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scroll_y = Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)

        # Połącz paski przewijania z Canvas
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # **DO NAPISANIA**: Umieść paski przewijania w siatce (grid)
        # np. self.scroll_x.grid(...)
        # np. self.scroll_y.grid(...)

        # Dynamiczne skalowanie elementów
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_columnconfigure(0, weight=1)

    def open_handler(self):
        """Obsługuje otwieranie pliku obrazu"""
        self.image_fp = filedialog.askopenfilename(
            initialdir=".", filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*"))
        )
        if self.image_fp:
            try:
                self.image = Image.open(self.image_fp)
                self.display_image(self.image)
                self.width_entry_str.set(str(self.image.width))
                self.height_entry_str.set(str(self.image.height))
            except Exception as e:
                print(f"Error opening image: {e}")

    def width_modified(self, event):
        """Automatyczne wyliczenie wysokości przy zmianie szerokości"""
        if self.image:
            try:
                w = int(self.width_entry.get())
                height_set_to = int(self.image.height * (w / self.image.width))
                self.height_entry_str.set(str(height_set_to))
            except ValueError:
                pass

    def height_modified(self, event):
        """Automatyczne wyliczenie szerokości przy zmianie wysokości"""
        if self.image:
            try:
                h = int(self.height_entry.get())
                width_set_to = int(self.image.width * (h / self.image.height))
                self.width_entry_str.set(str(width_set_to))
            except ValueError:
                pass

    def resize_handler(self):
        """Zmiana rozmiaru obrazu"""
        # **DO NAPISANIA**:
        # Upewnij się, że wczytano obraz i wartości `width` i `height` są liczbami.
        # Następnie zmień rozmiar obrazu i wyświetl go na Canvas.
        pass

    def save_handler(self):
        """Zapisanie zmienionego obrazu"""
        # **DO NAPISANIA**:
        # Zapisz obraz do nowego pliku z rozmiarem ustawionym przez użytkownika.
        # Wykorzystaj `filedialog.asksaveasfilename` do wyboru lokalizacji zapisu.
        pass

    def display_image(self, image):
        """Wyświetla obraz na Canvasie"""
        self.canvas.delete("all")
        self.photo_image = ImageTk.PhotoImage(image)

        # Wyświetl obraz na Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        # **DO NAPISANIA**:
        # Skonfiguruj `scrollregion` Canvas w oparciu o rozmiar obrazu.
        # np. self.canvas.config(scrollregion=(0, 0, image.width, image.height))


# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()
