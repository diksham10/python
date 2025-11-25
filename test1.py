# # # snake.py
# # Simple Snake game using Tkinter
# # Run: python snake.py

# import tkinter as tk
# import random

# CELL_SIZE = 20     # size of one cell in pixels
# GRID_W = 30        # number of cells horizontally
# GRID_H = 20        # number of cells vertically
# INIT_LENGTH = 5
# BASE_DELAY = 140   # initial delay in ms between moves
# SPEED_STEP = 6     # how much to speed up (reduce delay) per food

# class SnakeGame(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.master = master
#         self.master.title("Snake — Tkinter")
#         self.pack()

#         self.canvas = tk.Canvas(self, width=GRID_W*CELL_SIZE, height=GRID_H*CELL_SIZE, bg="#111111")
#         self.canvas.pack(side=tk.TOP)

#         # Info / controls
#         self.info_frame = tk.Frame(self)
#         self.info_frame.pack(fill=tk.X, pady=6)
#         self.score_var = tk.StringVar(value="Score: 0")
#         self.score_label = tk.Label(self.info_frame, textvariable=self.score_var, font=("Consolas", 12))
#         self.score_label.pack(side=tk.LEFT, padx=8)

#         self.msg_var = tk.StringVar(value="Press arrows to move • P=pause • R=restart")
#         self.msg_label = tk.Label(self.info_frame, textvariable=self.msg_var, font=("Consolas", 10))
#         self.msg_label.pack(side=tk.RIGHT, padx=8)

#         # Bind keys
#         self.master.bind("<Up>", lambda e: self.change_direction("Up"))
#         self.master.bind("<Down>", lambda e: self.change_direction("Down"))
#         self.master.bind("<Left>", lambda e: self.change_direction("Left"))
#         self.master.bind("<Right>", lambda e: self.change_direction("Right"))
#         self.master.bind("p", lambda e: self.toggle_pause())
#         self.master.bind("P", lambda e: self.toggle_pause())
#         self.master.bind("r", lambda e: self.restart())
#         self.master.bind("R", lambda e: self.restart())

#         self.running = False
#         self.paused = False
#         self.after_id = None

#         self.reset_game()
#         self.start()

#     def reset_game(self):
#         # game state
#         self.direction = "Right"
#         self.next_direction = "Right"
#         mid_x = GRID_W // 2
#         mid_y = GRID_H // 2
#         self.snake = [(mid_x - i, mid_y) for i in range(INIT_LENGTH)]  # list of (x,y) from head to tail
#         self.score = 0
#         self.delay = BASE_DELAY
#         self.place_food()
#         self.redraw_all()
#         self.score_var.set(f"Score: {self.score}")
#         self.msg_var.set("Press arrows to move • P=pause • R=restart")

#     def start(self):
#         if not self.running:
#             self.running = True
#             self.paused = False
#             self.schedule_move()

#     def schedule_move(self):
#         if self.after_id:
#             self.after_cancel(self.after_id)
#             self.after_id = None
#         if not self.paused and self.running:
#             self.after_id = self.after(self.delay, self.game_step)

#     def toggle_pause(self):
#         if not self.running:
#             return
#         self.paused = not self.paused
#         if self.paused:
#             self.msg_var.set("Paused — press P to resume")
#             if self.after_id:
#                 self.after_cancel(self.after_id)
#                 self.after_id = None
#         else:
#             self.msg_var.set("Running")
#             self.schedule_move()

#     def restart(self):
#         if self.after_id:
#             self.after_cancel(self.after_id)
#             self.after_id = None
#         self.running = False
#         self.reset_game()
#         self.start()

#     def change_direction(self, new_dir):
#         # prevent reversing direction immediately
#         opposites = {"Up":"Down","Down":"Up","Left":"Right","Right":"Left"}
#         if opposites.get(new_dir) == self.direction:
#             return
#         # queue direction change for next step (prevents multi-key issues)
#         self.next_direction = new_dir

#     def place_food(self):
#         free_cells = {(x,y) for x in range(GRID_W) for y in range(GRID_H)} - set(self.snake)
#         if not free_cells:
#             self.food = None
#             return
#         self.food = random.choice(list(free_cells))

#     def game_step(self):
#         # apply queued direction
#         self.direction = self.next_direction

#         head_x, head_y = self.snake[0]
#         dx, dy = 0, 0
#         if self.direction == "Up":
#             dy = -1
#         elif self.direction == "Down":
#             dy = 1
#         elif self.direction == "Left":
#             dx = -1
#         elif self.direction == "Right":
#             dx = 1

#         new_head = (head_x + dx, head_y + dy)

#         # check wall collision
#         x, y = new_head
#         if not (0 <= x < GRID_W and 0 <= y < GRID_H):
#             self.game_over("Hit the wall!")
#             return

#         # check self collision
#         if new_head in self.snake:
#             self.game_over("You hit yourself!")
#             return

#         # move snake
#         self.snake.insert(0, new_head)

#         # check food
#         if self.food and new_head == self.food:
#             self.score += 1
#             self.score_var.set(f"Score: {self.score}")
#             # speed up
#             self.delay = max(30, BASE_DELAY - self.score * SPEED_STEP)
#             self.place_food()
#         else:
#             # remove tail
#             self.snake.pop()

#         self.redraw_all()
#         self.schedule_move()

#     def game_over(self, reason="Game Over"):
#         self.running = False
#         self.paused = False
#         if self.after_id:
#             self.after_cancel(self.after_id)
#             self.after_id = None
#         self.msg_var.set(f"{reason} — Press R to restart")
#         # draw Game Over text
#         self.canvas.create_rectangle(40, 40, GRID_W*CELL_SIZE-40, GRID_H*CELL_SIZE-40, fill="#000000", outline="#444444")
#         self.canvas.create_text(GRID_W*CELL_SIZE//2, GRID_H*CELL_SIZE//2 - 10, text="GAME OVER", fill="red", font=("Consolas", 28, "bold"))
#         self.canvas.create_text(GRID_W*CELL_SIZE//2, GRID_H*CELL_SIZE//2 + 24, text=f"Score: {self.score}", fill="white", font=("Consolas", 16))

#     def redraw_all(self):
#         self.canvas.delete("all")
#         # draw grid faint (optional)
#         #for i in range(GRID_W+1):
#         #    self.canvas.create_line(i*CELL_SIZE, 0, i*CELL_SIZE, GRID_H*CELL_SIZE, fill="#222222")
#         #for j in range(GRID_H+1):
#         #    self.canvas.create_line(0, j*CELL_SIZE, GRID_W*CELL_SIZE, j*CELL_SIZE, fill="#222222")

#         # draw food
#         if self.food:
#             x, y = self.food
#             self._draw_cell(x, y, "#e74c3c")  # red

#         # draw snake
#         if self.snake:
#             # head
#             hx, hy = self.snake[0]
#             self._draw_cell(hx, hy, "#2ecc71")  # head color
#             # body
#             for cell in self.snake[1:]:
#                 self._draw_cell(cell[0], cell[1], "#27ae60")

#     def _draw_cell(self, cx, cy, color):
#         x1 = cx * CELL_SIZE + 1
#         y1 = cy * CELL_SIZE + 1
#         x2 = x1 + CELL_SIZE - 2
#         y2 = y1 + CELL_SIZE - 2
#         self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#0f0f0f")

# def main():
#     root = tk.Tk()
#     game = SnakeGame(root)
#     root.resizable(False, False)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
import tkinter as tk
import random

# --------------------------------------
# CONFIG
# --------------------------------------
WIN_WIDTH = 500
WIN_HEIGHT = 600
GRAVITY = 0.5
FLAP_STRENGTH = -8
PIPE_SPEED = 4
PIPE_GAP = 160
PIPE_DISTANCE = 250


# --------------------------------------
# GAME CLASS
# --------------------------------------
class FlappyBird:
    def __init__(self, root):
        self.root = root
        self.root.title("Flappy Bird - Tkinter")

        self.canvas = tk.Canvas(root, width=WIN_WIDTH, height=WIN_HEIGHT, bg="skyblue")
        self.canvas.pack()

        # Bird
        self.bird = self.canvas.create_oval(50, 200, 80, 230, fill="yellow")
        self.velocity = 0

        # Pipes list
        self.pipes = []
        self.score = 0
        self.running = True

        # Score text
        self.score_text = self.canvas.create_text(
            250, 50, text="Score: 0", font=("Arial", 24, "bold"), fill="white"
        )

        # Bind space bar
        self.root.bind("<space>", self.flap)

        # Start game
        self.spawn_pipe()
        self.update_game()

    # --------------------------------------
    # BIRD JUMP
    # --------------------------------------
    def flap(self, event):
        if self.running:
            self.velocity = FLAP_STRENGTH

    # --------------------------------------
    # PIPE SPAWN
    # --------------------------------------
    def spawn_pipe(self):
        top_height = random.randint(100, 400)
        bottom_height = top_height + PIPE_GAP

        # Create top pipe
        top_pipe = self.canvas.create_rectangle(
            WIN_WIDTH, 0, WIN_WIDTH + 80, top_height, fill="green"
        )
        # Create bottom pipe
        bottom_pipe = self.canvas.create_rectangle(
            WIN_WIDTH, bottom_height, WIN_WIDTH + 80, WIN_HEIGHT, fill="green"
        )

        self.pipes.append((top_pipe, bottom_pipe))

        if self.running:
            self.root.after(1500, self.spawn_pipe)

    # --------------------------------------
    # MAIN GAME LOOP
    # --------------------------------------
    def update_game(self):
        if not self.running:
            return

        # 1. Bird physics
        self.velocity += GRAVITY
        self.canvas.move(self.bird, 0, self.velocity)

        # Get bird coords
        bx1, by1, bx2, by2 = self.canvas.coords(self.bird)

        # Bird hits the ground or top
        if by2 >= WIN_HEIGHT or by1 <= 0:
            self.end_game()

        # 2. Move and check pipes
        pipes_to_delete = []
        for top_pipe, bottom_pipe in self.pipes:
            self.canvas.move(top_pipe, -PIPE_SPEED, 0)
            self.canvas.move(bottom_pipe, -PIPE_SPEED, 0)

            tp = self.canvas.coords(top_pipe)
            bp = self.canvas.coords(bottom_pipe)

            # Scoring when bird passes pipe
            if tp[2] < 40 and tp[2] > 35:
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

            # Collision detection
            if self.check_collision((top_pipe, bottom_pipe)):
                self.end_game()

            # Remove pipes off-screen
            if tp[2] < 0:
                pipes_to_delete.append((top_pipe, bottom_pipe))

        # Clean old pipes
        for p in pipes_to_delete:
            self.canvas.delete(p[0])
            self.canvas.delete(p[1])
            self.pipes.remove(p)

        # Continue loop
        self.root.after(20, self.update_game)

    # --------------------------------------
    # COLLISION CLEAR CHECK
    # --------------------------------------
    def check_collision(self, pipe_pair):
        bx1, by1, bx2, by2 = self.canvas.coords(self.bird)
        for pipe in pipe_pair:
            px1, py1, px2, py2 = self.canvas.coords(pipe)

            if not (bx2 < px1 or bx1 > px2 or by2 < py1 or by1 > py2):
                return True
        return False

    # --------------------------------------
    # GAME OVER
    # --------------------------------------
    def end_game(self):
        self.running = False
        self.canvas.create_text(
            WIN_WIDTH / 2,
            WIN_HEIGHT / 2,
            text=f"GAME OVER\nScore: {self.score}",
            font=("Arial", 32, "bold"),
            fill="red",
        )


# --------------------------------------
# RUN
# --------------------------------------
root = tk.Tk()
game = FlappyBird(root)
root.mainloop()
