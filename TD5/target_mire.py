import tkinter as tk
from random import randint
from math import sqrt
from random import choice


class Target:
    def __init__(self):
        self.__score = 0

        def create_circle(x, y, r, color="red"):  # center coordinates, radius
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            return self.__canvas.create_oval(x0, y0, x1, y1, outline=color)

        def draw_target():
            # Efface tout contenu précédent
            self.__canvas.delete("all")

            self.__canvas.create_oval(
                200 - 170, 200 - 170, 200 + 170, 200 + 170, outline="red", fill="white"
            )

            self.__canvas.create_oval(
                200 - 50, 200 - 50, 200 + 50, 200 + 50, outline="red", fill="red"
            )

            self.__canvas.create_oval(
                200 - 20, 200 - 20, 200 + 20, 200 + 20, outline="red", fill="white"
            )
            # Dessine les cercles concentriques
            for i in range(5):
                # color = "red" if i != 4 else "white"
                # self.__canvas.create_oval(200 - 30*(i+1), 200 - 30*(i+1), 200 + 30*(i+1), 200 + 30*(i+1), outline="red", fill=color)
                create_circle(200, 200, 200 - 30 * (i))

            # Dessine les axes
            self.__canvas.create_line(200, 0, 200, 400, fill="red", width=1)
            self.__canvas.create_line(0, 200, 400, 200, fill="red", width=1)

            # Dessine les chiffres
            n = 7
            for i in range(1, n):
                color = "red" if i != 2 else "white"
                self.__canvas.create_text(
                    200,
                    200 - 30 * (i - 1),
                    text=str(n - i),
                    fill=color,
                    font=("Helvetica", 14),
                )

        # Création de la fenêtre principale
        self.__root = tk.Tk()
        self.__root.title("Cible")
        self.__root.geometry("400x640")

        # Création du Canvas
        self.__canvas = tk.Canvas(self.__root, width=400, height=400, bg="red")
        self.__canvas.pack()

        # Bouton "Dessiner"
        draw_target()

        self.__mire = create_circle(200, 200, 10, color="black")

        # Bouton "Quitter"
        quit_button = tk.Button(
            self.__root, text="Quitter", command=self.__root.destroy
        )
        quit_button.pack(side=tk.RIGHT)


        self.__sample_text = tk.Label(self.__root, text=f"Score : {self.__score}")
        self.__sample_text.pack(side=tk.LEFT)

    def move_mire(self) : 
        dx = choice([-10,10,0])
        dy = choice([-10,10,0])
        self.__canvas.move(self.__mire, dx, dy)
        self.__root.after(100, self.move_mire)


    def check_hit_mire(self, event):
        (x1, y1, x2, y2) = self.__canvas.coords(self.__mire)
        x = (x2 + x1) / 2
        y = (y2 + y1) / 2
        if sqrt((x-200)**2 + (y - 200)**2) < 30:
            self.__sample_text.config(text="Touché !")
        else:
            self.__sample_text.config(text="Raté !")


    def execute(self):
        self.__root.after(100, self.move_mire)
        self.__root.bind("f", self.check_hit_mire)
        self.__root.mainloop()


if __name__ == "__main__":
    target = Target()
    target.execute()
