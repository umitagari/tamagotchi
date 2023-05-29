import time
import curses

class Tamagotchi:
    def __init__(self):
        self.hambre = 0
        self.sueño = 0
        self.aburrimiento = 0
        self.limpieza = 0

    def incrementar_hambre(self):
        self.hambre = min(self.hambre + 1, 100)

    def incrementar_sueño(self):
        self.sueño = min(self.sueño + 1, 100)

    def incrementar_aburrimiento(self):
        self.aburrimiento = min(self.aburrimiento + 1, 100)

    def incrementar_limpieza(self):
        self.limpieza = min(self.limpieza + 1, 100)

    def disminuir_estadisticas(self, key):
        if key == ord('h'):
            self.hambre = max(self.hambre - 8, 0)
        if key == ord('s'):
            self.sueño = max(self.sueño - 6, 0)
        if key == ord('a'):
            self.aburrimiento = max(self.aburrimiento - 9, 0)
        if key == ord('l'):
            self.limpieza = max(self.limpieza - 8, 0)

    def mostrar_estadisticas(self, stdscr):
        stdscr.addstr(1, 0, f"Hambre: {self.hambre}")
        stdscr.addstr(2, 0, f"Sueño: {self.sueño}")
        stdscr.addstr(3, 0, f"Aburrimiento: {self.aburrimiento}")
        stdscr.addstr(4, 0, f"Limpieza: {self.limpieza}")

    def mostrar_tamagotchi(self, stdscr, frame):
        if frame == 1:
            stdscr.addstr(6, 0, " /~~~\\ ")
            stdscr.addstr(7, 0, "( o _ o )")
            stdscr.addstr(8, 0, " \\~~~/ ")
        elif frame == 2:
            stdscr.addstr(6, 0, " /~~~\\ ")
            stdscr.addstr(7, 0, "( o . o )")
            stdscr.addstr(8, 0, " \\~~~/ ")
        elif frame == 3:
            stdscr.addstr(6, 0, " /~~~\\ ")
            stdscr.addstr(7, 0, "( o - o )")
            stdscr.addstr(8, 0, " \\~~~/ ")

    def mostrar_mensaje(self, stdscr, mensaje):
        stdscr.clear()
        stdscr.addstr(6, 0, mensaje)
        stdscr.addstr(8, 0, "Presiona 2 para salir.")
        stdscr.refresh()

    def animar_tamagotchi(self, stdscr):
        stdscr.nodelay(False)
        curses.halfdelay(1)  

        frame = 1
        tamagotchi_alive = True

        while tamagotchi_alive:
            stdscr.clear()

            self.mostrar_estadisticas(stdscr)

            stdscr.addstr(9, 0, "Presiona 'h' para disminuir hambre")
            stdscr.addstr(10, 0, "Presiona 's' para disminuir sueño")
            stdscr.addstr(11, 0, "Presiona 'a' para disminuir aburrimiento")
            stdscr.addstr(12, 0, "Presiona 'l' para disminuir limpieza")

            self.mostrar_tamagotchi(stdscr, frame)

            key = stdscr.getch()


            self.disminuir_estadisticas(key)

            self.incrementar_hambre()
            self.incrementar_sueño()
            self.incrementar_aburrimiento()
            self.incrementar_limpieza()

            if self.hambre >= 100 and self.sueño >= 100 and self.aburrimiento >= 100 and self.limpieza >= 100:
                tamagotchi_alive = False
                self.mostrar_mensaje(stdscr, "Tu Tamagotchi ha muerto.")

            stdscr.refresh()
            frame = (frame % 3) + 1  

        while True:
            key = stdscr.getch()
            if key == ord('1'):
                self.revivir = True
                break
            elif key == ord('2'):
                break

        stdscr.clear()
        stdscr.refresh()

tamagotchi = Tamagotchi()
curses.wrapper(tamagotchi.animar_tamagotchi)