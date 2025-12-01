# """
# Tiny Royale — a small battle-royale–style game in Tkinter with bots.
# Save as tiny_royale.py and run: python tiny_royale.py
# Controls:
#   - Move: W A S D
#   - Aim: Move the mouse (cursor)
#   - Shoot: Left mouse button
# Notes:
#   - No external assets required.
#   - Simple bot AI: wander, pursue player if close, and shoot sometimes.
#   - Safe zone shrinks over time; standing outside drains health.
# """

# import tkinter as tk
# import random
# import math
# import time

# WIDTH, HEIGHT = 900, 600
# PLAYER_RADIUS = 12
# BOT_RADIUS = 12
# BULLET_RADIUS = 3
# MAX_BULLETS = 5
# BULLET_SPEED = 10
# FPS = 30
# NUM_BOTS = 6
# SAFEZONE_SHRINK_INTERVAL = 6.0  # seconds between shrink steps
# SAFEZONE_SHRINK_AMOUNT = 0.75   # multiplier to radius each step
# DAMAGE_BULLET = 25
# OUTSIDE_DAMAGE_PER_SEC = 8

# class Entity:
#     def __init__(self, x, y, r, color, name="Entity"):
#         self.x = x
#         self.y = y
#         self.r = r
#         self.color = color
#         self.name = name

# class Player(Entity):
#     def __init__(self, x, y):
#         super().__init__(x, y, PLAYER_RADIUS, "blue", "Player")
#         self.angle = 0
#         self.speed = 4.2
#         self.health = 100
#         self.bullets = []
#         self.last_shot = 0
#         self.shot_cooldown = 0.25  # seconds

# class Bot(Entity):
#     def __init__(self, x, y, idnum):
#         super().__init__(x, y, BOT_RADIUS, "red", f"Bot{idnum}")
#         self.health = 100
#         self.speed = 2.3 + random.random()*1.2
#         self.state = "wander"  # wander | pursue
#         self.wander_target = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
#         self.last_shot = 0
#         self.shot_cooldown = 0.8 + random.random()*0.8

# class Bullet:
#     def __init__(self, x, y, vx, vy, owner):
#         self.x = x
#         self.y = y
#         self.vx = vx
#         self.vy = vy
#         self.owner = owner
#         self.r = BULLET_RADIUS

# class TinyRoyale:
#     def __init__(self, master):
#         self.master = master
#         master.title("Tiny Royale (battle-royale inspired)")
#         self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="lightgrey")
#         self.canvas.pack()
#         self.player = Player(WIDTH//2, HEIGHT//2)
#         self.bots = []
#         self.bullets = []
#         self.mouse_pos = (self.player.x, self.player.y)
#         self.pressed = set()
#         self.running = True
#         self.last_time = time.time()
#         self.safezone_center = (WIDTH//2, HEIGHT//2)
#         self.safezone_radius = min(WIDTH, HEIGHT) * 0.45
#         self.last_shrink_time = time.time() + SAFEZONE_SHRINK_INTERVAL
#         self.game_over = False

#         # spawn bots
#         for i in range(NUM_BOTS):
#             x = random.randint(40, WIDTH-40)
#             y = random.randint(40, HEIGHT-40)
#             # ensure not too close to player
#             if abs(x-self.player.x) < 80 and abs(y-self.player.y) < 80:
#                 x += 120 if x < WIDTH//2 else -120
#                 y += 80 if y < HEIGHT//2 else -80
#             self.bots.append(Bot(x,y,i+1))

#         # bindings
#         master.bind("<KeyPress>", self.on_key_press)
#         master.bind("<KeyRelease>", self.on_key_release)
#         master.bind("<Motion>", self.on_mouse_move)
#         master.bind("<Button-1>", self.on_mouse_click)

#         # HUD
#         self.info_text = self.canvas.create_text(10,10, anchor="nw", text="", font=("Arial",12), fill="black")

#         # start game loop
#         self.loop()

#     def on_key_press(self, event):
#         self.pressed.add(event.keysym.lower())

#     def on_key_release(self, event):
#         self.pressed.discard(event.keysym.lower())

#     def on_mouse_move(self, event):
#         self.mouse_pos = (event.x, event.y)

#     def on_mouse_click(self, event):
#         self.shoot(self.player, event.x, event.y)

#     def shoot(self, shooter, tx, ty):
#         now = time.time()
#         if now - shooter.last_shot < shooter.shot_cooldown:
#             return
#         shooter.last_shot = now
#         dx = tx - shooter.x
#         dy = ty - shooter.y
#         dist = math.hypot(dx, dy) or 1
#         vx = dx/dist * BULLET_SPEED
#         vy = dy/dist * BULLET_SPEED
#         b = Bullet(shooter.x + dx/dist*(shooter.r+4), shooter.y + dy/dist*(shooter.r+4), vx, vy, shooter)
#         self.bullets.append(b)

#     def loop(self):
#         if not self.running:
#             return
#         now = time.time()
#         dt = now - self.last_time
#         if dt > 0.5: dt = 1/FPS  # clamp if paused
#         self.last_time = now

#         if not self.game_over:
#             self.update_player(dt)
#             self.update_bots(dt)
#             self.update_bullets(dt)
#             self.update_safezone(now, dt)
#             self.check_collisions()
#             self.check_end_condition()

#         self.draw()
#         self.master.after(int(1000/FPS), self.loop)

#     def update_player(self, dt):
#         dx = dy = 0
#         if 'w' in self.pressed: dy -= 1
#         if 's' in self.pressed: dy += 1
#         if 'a' in self.pressed: dx -= 1
#         if 'd' in self.pressed: dx += 1
#         if dx or dy:
#             norm = math.hypot(dx, dy) or 1
#             self.player.x += dx/norm * self.player.speed
#             self.player.y += dy/norm * self.player.speed
#             self.player.x = max(0, min(WIDTH, self.player.x))
#             self.player.y = max(0, min(HEIGHT, self.player.y))
#         # aim angle
#         mx, my = self.mouse_pos
#         self.player.angle = math.degrees(math.atan2(my - self.player.y, mx - self.player.x))

#         # outside safezone damage
#         if not self.point_in_safezone(self.player.x, self.player.y):
#             self.player.health -= OUTSIDE_DAMAGE_PER_SEC * dt
#             if self.player.health < 0: self.player.health = 0

#     def update_bots(self, dt):
#         for bot in list(self.bots):
#             if bot.health <= 0:
#                 continue
#             # distance to player
#             dx = self.player.x - bot.x
#             dy = self.player.y - bot.y
#             dist = math.hypot(dx, dy)
#             # decide state
#             if dist < 220:
#                 bot.state = "pursue"
#             else:
#                 bot.state = "wander"

#             if bot.state == "pursue":
#                 tx, ty = self.player.x, self.player.y
#                 # move towards player
#                 nx, ny = tx - bot.x, ty - bot.y
#                 nd = math.hypot(nx, ny) or 1
#                 bot.x += nx/nd * bot.speed
#                 bot.y += ny/nd * bot.speed
#                 # occasionally shoot
#                 if now_seconds() - bot.last_shot > bot.shot_cooldown and dist < 380:
#                     bot.last_shot = now_seconds()
#                     # lead a bit
#                     target_x = self.player.x + self.player.speed * (nx/nd) * 6
#                     target_y = self.player.y + self.player.speed * (ny/nd) * 6
#                     self.shoot(bot, target_x, target_y)
#             else:
#                 # wander — move towards wander_target; if reached, pick new target
#                 tx, ty = bot.wander_target
#                 nx, ny = tx - bot.x, ty - bot.y
#                 nd = math.hypot(nx, ny) or 1
#                 if nd < 10:
#                     bot.wander_target = (random.randint(40, WIDTH-40), random.randint(40, HEIGHT-40))
#                 else:
#                     bot.x += nx/nd * bot.speed
#                     bot.y += ny/nd * bot.speed

#             # small boundary clamp
#             bot.x = max(8, min(WIDTH-8, bot.x))
#             bot.y = max(8, min(HEIGHT-8, bot.y))

#             # outside safezone damage
#             if not self.point_in_safezone(bot.x, bot.y):
#                 bot.health -= OUTSIDE_DAMAGE_PER_SEC * dt
#                 if bot.health < 0: bot.health = 0

#     def update_bullets(self, dt):
#         new_bullets = []
#         for b in self.bullets:
#             b.x += b.vx
#             b.y += b.vy
#             # off-screen?
#             if b.x < -10 or b.x > WIDTH+10 or b.y < -10 or b.y > HEIGHT+10:
#                 continue
#             new_bullets.append(b)
#         self.bullets = new_bullets

#     def update_safezone(self, now, dt):
#         # shrink safezone at intervals
#         if now > self.last_shrink_time:
#             self.last_shrink_time = now + SAFEZONE_SHRINK_INTERVAL
#             self.safezone_radius *= SAFEZONE_SHRINK_AMOUNT
#             # move center slightly to add challenge
#             cx, cy = self.safezone_center
#             cx += random.randint(-40,40)
#             cy += random.randint(-40,40)
#             cx = max(100, min(WIDTH-100, cx))
#             cy = max(80, min(HEIGHT-80, cy))
#             self.safezone_center = (cx, cy)

#     def point_in_safezone(self, x, y):
#         cx, cy = self.safezone_center
#         return (x-cx)**2 + (y-cy)**2 <= self.safezone_radius**2

#     def check_collisions(self):
#         # bullets vs entities
#         for b in list(self.bullets):
#             # player hit by bot bullet
#             if isinstance(b.owner, Bot) or isinstance(b.owner, Player):
#                 # check player
#                 if b.owner is not self.player:
#                     if circle_collision(b.x, b.y, b.r, self.player.x, self.player.y, self.player.r):
#                         self.player.health -= DAMAGE_BULLET
#                         try: self.bullets.remove(b)
#                         except: pass
#                         continue
#                 # check bots
#                 for bot in self.bots:
#                     if bot is b.owner or bot.health <= 0: 
#                         continue
#                     if circle_collision(b.x, b.y, b.r, bot.x, bot.y, bot.r):
#                         bot.health -= DAMAGE_BULLET
#                         try: self.bullets.remove(b)
#                         except: pass
#                         break

#         # Remove dead bots from active list after marking
#         # (We keep them in list but they won't act if health<=0)
#         # nothing more needed here.

#     def check_end_condition(self):
#         alive = [e for e in ([self.player] + self.bots) if getattr(e,'health',0) > 0]
#         alive_count = len(alive)
#         if self.player.health <= 0:
#             self.game_over = True
#             self.show_game_over("You died — Game Over")
#         elif alive_count == 1 and alive[0] is self.player:
#             self.game_over = True
#             self.show_game_over("You won! Last one standing!")
#         elif alive_count == 0:  # weird fallback
#             self.game_over = True
#             self.show_game_over("No survivors — Game Over")

#     def draw(self):
#         self.canvas.delete("all")
#         # draw safezone (semi-transparent ring effect)
#         cx, cy = self.safezone_center
#         r = self.safezone_radius
#         # background dim
#         self.canvas.create_rectangle(0,0,WIDTH,HEIGHT, fill="lightgrey", outline="")
#         # outside darken
#         self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="", outline="black")
#         # safe circle
#         self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, dash=(4,4))

#         # draw bullets
#         for b in self.bullets:
#             self.canvas.create_oval(b.x-b.r, b.y-b.r, b.x+b.r, b.y+b.r, fill="black")

#         # draw bots
#         for bot in self.bots:
#             if bot.health <= 0:
#                 # dead bot
#                 self.canvas.create_oval(bot.x-bot.r, bot.y-bot.r, bot.x+bot.r, bot.y+bot.r, fill="darkred", stipple="gray50")
#                 self.canvas.create_text(bot.x, bot.y, text="X", fill="white", font=("Arial",10,"bold"))
#             else:
#                 self.canvas.create_oval(bot.x-bot.r, bot.y-bot.r, bot.x+bot.r, bot.y+bot.r, fill=bot.color)
#                 # health bar
#                 self.draw_health_bar(bot.x, bot.y - bot.r - 8, bot.health)

#         # draw player
#         if self.player.health > 0:
#             x,y = self.player.x, self.player.y
#             self.canvas.create_oval(x-self.player.r, y-self.player.r, x+self.player.r, y+self.player.r, fill=self.player.color)
#             # draw aim direction line
#             mx,my = self.mouse_pos
#             dx,dy = mx-x, my-y
#             nd = math.hypot(dx,dy) or 1
#             ex = x + dx/nd * (self.player.r + 18)
#             ey = y + dy/nd * (self.player.r + 18)
#             self.canvas.create_line(x, y, ex, ey, width=2)
#             self.draw_health_bar(x, y - self.player.r - 10, self.player.health)

#         # HUD text
#         alive_bots = sum(1 for b in self.bots if b.health > 0)
#         hud = f"HP: {int(self.player.health)}   Bots alive: {alive_bots}   Bullets: {len(self.bullets)}"
#         self.canvas.create_text(12, 12, anchor="nw", text=hud, font=("Arial", 12, "bold"))
#         # safezone info
#         self.canvas.create_text(12, 34, anchor="nw", text=f"Safe zone center: ({int(cx)},{int(cy)})  radius: {int(r)}", font=("Arial", 10))

#         if self.game_over:
#             self.canvas.create_text(WIDTH//2, HEIGHT//2-20, text=self.end_message, font=("Arial", 26, "bold"), fill="black")
#             self.canvas.create_text(WIDTH//2, HEIGHT//2+18, text="Press R to restart", font=("Arial", 14))

#         # key to restart
#         self.master.bind("<r>", self.on_restart)

#     def draw_health_bar(self, x, y, health):
#         w = 34
#         h = 6
#         left = x - w//2
#         right = left + w
#         self.canvas.create_rectangle(left, y, right, y+h, fill="black", outline="")
#         fill_w = max(0, w * (health/100.0))
#         self.canvas.create_rectangle(left+1, y+1, left+1+fill_w, y+h-1, fill="green", outline="")

#     def on_restart(self, event=None):
#         if not self.game_over:
#             return
#         # reset game (simple: create a new instance state)
#         self.__init__(self.master)

#     def show_game_over(self, message):
#         self.end_message = message

# def circle_collision(x1,y1,r1,x2,y2,r2):
#     return (x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2

# def now_seconds():
#     return time.time()

# if __name__ == "__main__":
#     root = tk.Tk()
#     game = TinyRoyale(root)
#     root.mainloop()
# very_simple_battle.py
# Tiny 1-vs-bots shooter made with Tkinter (beginner-friendly)
# Controls:
#  - Move: W A S D
#  - Aim: move mouse
#  - Shoot: left mouse click

import tkinter as tk
import math
import random
import time

WIDTH, HEIGHT = 640, 420

# --- Simple entity classes ---
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 12
        self.speed = 4
        self.hp = 100

class Bot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 12
        self.speed = 2
        self.hp = 60

class Bullet:
    def __init__(self, x, y, vx, vy, owner):
        self.x = x; self.y = y
        self.vx = vx; self.vy = vy
        self.owner = owner
        self.r = 4

# --- Helper functions ---
def dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

def circle_collide(x1,y1,r1,x2,y2,r2):
    return (x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2

# --- Main game ---
class SimpleGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()
        # create player in center
        self.player = Player(WIDTH//2, HEIGHT//2)
        # spawn 3 simple bots
        self.bots = [Bot(random.randint(40, WIDTH-40), random.randint(40, HEIGHT-40)) for _ in range(3)]
        self.bullets = []
        self.keys = set()
        self.mouse = (self.player.x, self.player.y)
        self.last_time = time.time()

        # input
        root.bind("<KeyPress>", self.on_key)
        root.bind("<KeyRelease>", self.on_key_release)
        root.bind("<Motion>", self.on_mouse)
        root.bind("<Button-1>", self.on_click)

        self.update()

    def on_key(self, e):
        self.keys.add(e.keysym.lower())

    def on_key_release(self, e):
        self.keys.discard(e.keysym.lower())

    def on_mouse(self, e):
        self.mouse = (e.x, e.y)

    def on_click(self, e):
        # shoot: create a bullet towards mouse
        dx = e.x - self.player.x
        dy = e.y - self.player.y
        d = math.hypot(dx, dy) or 1
        speed = 10
        vx = dx/d * speed
        vy = dy/d * speed
        bx = self.player.x + (self.player.r + 4) * (dx/d)
        by = self.player.y + (self.player.r + 4) * (dy/d)
        self.bullets.append(Bullet(bx, by, vx, vy, self.player))

    def update(self):
        now = time.time()
        dt = now - self.last_time
        self.last_time = now
        self.handle_input(dt)
        self.update_bots(dt)
        self.update_bullets(dt)
        self.check_collisions()
        self.draw()
        # loop ~60fps
        self.root.after(16, self.update)

    def handle_input(self, dt):
        dx = dy = 0
        if 'w' in self.keys: dy -= 1
        if 's' in self.keys: dy += 1
        if 'a' in self.keys: dx -= 1
        if 'd' in self.keys: dx += 1
        if dx or dy:
            n = math.hypot(dx, dy) or 1
            self.player.x += dx/n * self.player.speed
            self.player.y += dy/n * self.player.speed
            # keep inside window
            self.player.x = max(self.player.r, min(WIDTH - self.player.r, self.player.x))
            self.player.y = max(self.player.r, min(HEIGHT - self.player.r, self.player.y))

    def update_bots(self, dt):
        for bot in self.bots:
            if bot.hp <= 0: continue
            # simple AI: move toward player
            dx = self.player.x - bot.x
            dy = self.player.y - bot.y
            d = math.hypot(dx, dy) or 1
            bot.x += dx/d * bot.speed
            bot.y += dy/d * bot.speed
            # bot occasionally shoots (very simple)
            if random.random() < 0.01:
                tx = self.player.x + random.uniform(-20,20)
                ty = self.player.y + random.uniform(-20,20)
                ddx = tx - bot.x; ddy = ty - bot.y; dd = math.hypot(ddx, ddy) or 1
                vx = ddx/dd * 8; vy = ddy/dd * 8
                bx = bot.x + (bot.r+4) * (ddx/dd)
                by = bot.y + (bot.r+4) * (ddy/dd)
                self.bullets.append(Bullet(bx, by, vx, vy, bot))

    def update_bullets(self, dt):
        new = []
        for b in self.bullets:
            b.x += b.vx; b.y += b.vy
            if 0 <= b.x <= WIDTH and 0 <= b.y <= HEIGHT:
                new.append(b)
        self.bullets = new

    def check_collisions(self):
        # bullets vs bots/player
        for b in list(self.bullets):
            # bullet hits player (only if from bot)
            if isinstance(b.owner, Bot):
                if circle_collide(b.x, b.y, b.r, self.player.x, self.player.y, self.player.r):
                    self.player.hp -= 15
                    try: self.bullets.remove(b)
                    except: pass
            # bullet hits bot (only if from player)
            elif isinstance(b.owner, Player):
                for bot in self.bots:
                    if bot.hp > 0 and circle_collide(b.x, b.y, b.r, bot.x, bot.y, bot.r):
                        bot.hp -= 30
                        try: self.bullets.remove(b)
                        except: pass
                        break

        # bots touching player deal damage
        for bot in self.bots:
            if bot.hp > 0 and dist(bot, self.player) < (bot.r + self.player.r):
                self.player.hp -= 0.6  # continuous small damage

        # clamp HP
        self.player.hp = max(0, self.player.hp)

    def draw(self):
        self.canvas.delete("all")
        # draw bullets
        for b in self.bullets:
            self.canvas.create_oval(b.x-b.r, b.y-b.r, b.x+b.r, b.y+b.r, fill="black")
        # draw bots
        for bot in self.bots:
            color = "red" if bot.hp>0 else "gray"
            self.canvas.create_oval(bot.x-bot.r, bot.y-bot.r, bot.x+bot.r, bot.y+bot.r, fill=color)
            # health text for bot
            self.canvas.create_text(bot.x, bot.y-18, text=str(int(bot.hp)), font=("Arial", 8))
        # draw player
        self.canvas.create_oval(self.player.x-self.player.r, self.player.y-self.player.r,
                                self.player.x+self.player.r, self.player.y+self.player.r, fill="blue")
        # HUD
        self.canvas.create_text(10, 10, anchor="nw", text=f"HP: {int(self.player.hp)}", font=("Arial", 12, "bold"))
        alive = sum(1 for b in self.bots if b.hp>0)
        self.canvas.create_text(10, 28, anchor="nw", text=f"BOTS: {alive}", font=("Arial", 10))
        if self.player.hp <= 0:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="YOU DIED", font=("Arial", 24), fill="black")
        elif alive == 0:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="YOU WIN!", font=("Arial", 24), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Very Simple Battle")
    game = SimpleGame(root)
    root.mainloop()
