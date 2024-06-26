import tkinter as tk
from random import randint
from math import sqrt


class Target:
    def __init__(self):
        self.__score = 0
        self.__shots_fired = 0

        def create_circle(x, y, r, color="red"):  # center coordinates, radius
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            return self.__canvas.create_oval(x0, y0, x1, y1, outline=color)

        def feu():
            for _ in range(5):
                self.create_shot()
            self.__sample_text.config(text=f"Score : {self.__score}")


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

        # Bouton "Quitter"
        quit_button = tk.Button(
            self.__root, text="Quitter", command=self.__root.destroy
        )
        quit_button.pack(side=tk.RIGHT)

        fire_button = tk.Button(self.__root, text="Feu !", command=feu)
        fire_button.pack(side=tk.LEFT)

        self.__sample_text = tk.Label(self.__root, text=f"Score : {self.__score}")
        self.__sample_text.pack(side=tk.LEFT)

    def score(self, x: int, y: int) -> int:
        """Returns the score of a position"""
        if x < 0 or x > 320 or y < 0 or y > 320:
            return 0
        distance_from_center = sqrt((x - 200) ** 2 + (y - 200) ** 2)
        if distance_from_center < 20:
            return 6
        elif distance_from_center < 50:
            return 5
        elif distance_from_center < 80:
            return 4
        elif distance_from_center < 110:
            return 3
        elif distance_from_center < 140:
            return 2
        elif distance_from_center < 170:
            return 1
        else:
            return 0

    def create_shot(self) : 
        if self.__shots_fired >= 5:
            return;
        x = randint(10, 390)
        y = randint(10, 390)
        self.__canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
        print(x, y, self.score(x, y))
        self.__score += self.score(x, y)
        self.__sample_text.config(text=f"Score : {self.__score}")
        self.__shots_fired += 1

    def shot_with_f(self, event):
        self.create_shot()

    def execute(self):
        self.__root.bind("f", self.shot_with_f)
        self.__root.mainloop()


if __name__ == "__main__":
    target = Target()
    target.execute()
