# **Shooter Game**

This is explanation of how this code works.

## **1. Importing Libraries**
```python
from random import randint
import pygame
```
- `randint` (from the `random` module) is used to **randomly position the alien** along the x-axis.
- `pygame` is the game development library that provides functions for:
  - Displaying graphics
  - Handling user input (keyboard/mouse events)
  - Managing game loops
  - Rendering text and images

### **Why do we use Pygame?**
Pygame simplifies the process of making 2D games. It provides built-in functions for:
- Drawing images (`blit`)
- Handling player input (`KEYDOWN`, `KEYUP`)
- Managing game state (`event.get()`, `display.update()`)


## **2. Initializing Pygame**
```python
pygame.init()
```
- **This must be called before using Pygame features.**
- It sets up internal modules like sound, display, fonts, etc.


## **3. Defining Colors and Fonts**
```python
WHITE = (255, 255, 255)  # RGB format
game_font = pygame.font.Font(None, 50)  
score_font = pygame.font.Font(None, 30)
```
- **Why use RGB values?**  
  - Pygame uses `(R, G, B)` values for colors, where `255, 255, 255` is white.
- **`Font(None, size)`**:
  - `None` means the default font is used.
  - The size determines the text size.


## **4. Setting Up the Game Window**
```python
WIDTH, HEIGHT = 800, 600
screen_color = (32, 52, 71)  # Dark blue background
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game!")
```
- **Creates a game window of size `800x600`.**
- **Why set a caption?**  
  - It makes the game look polished and professional.


## **5. Fighter (Spaceship) Setup**
```python
FIGHTER_STEP = 0.8  # Speed of fighter movement
fighter = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter.get_size()
fighter_x, fighter_y = WIDTH / 2 - fighter_width / 2, HEIGHT - fighter_height
fighter_move_left, fighter_move_right = False, False
```
- **Loads an image (`fighter.png`)** and gets its size.
- **Positions the fighter in the middle-bottom of the screen.**
- **Booleans (`fighter_move_left`, `fighter_move_right`)** track movement.
  
### **Why use `FIGHTER_STEP = 0.8`?**
- It defines the **speed** of movement.
- A lower value makes movement smooth.
- If it were `10`, the fighter would move **too fast**.


## **6. Ball (Bullet) Setup**
```python
BALL_STEP = 0.3  # Speed of the bullet
ball = pygame.image.load('images/ball.png')
ball_width, ball_height = ball.get_size()
ball_x, ball_y = 0, 0
ball_fired = False
```
- **Loads the bullet image.**
- **Starts off-screen (`(0,0)`) and is repositioned when fired.**
- **`ball_fired = False`** means the bullet isn't currently on the screen.

### **Why track `ball_fired`?**
- Prevents **multiple bullets** from being on screen at once.
- Ensures the bullet disappears when it leaves the screen.


## **7. Alien (Enemy) Setup**
```python
ALIEN_STEP = 0.1
alien_speed = ALIEN_STEP  # Speed of falling alien
alien = pygame.image.load('images/alien.png')
alien_width, alien_height = alien.get_size()
alien_x, alien_y = randint(0, WIDTH - alien_width), 0
```
- **The alien starts at the top of the screen at a random `x` position.**
- **Why use `randint(0, WIDTH - alien_width)`?**  
  - Ensures the alien spawns within screen boundaries.
- **`alien_speed` increases when an alien is hit, making the game harder.**


## **8. Game Loop**
```python
run = True
game_score = 0
while run:
```
- The game **keeps running until `run = False`**.
- **`game_score = 0`** keeps track of the player’s points.


## **9. Handling User Input**
### **a) Detecting Key Presses (`KEYDOWN`)**
```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        fighter_move_left = True
    if event.key == pygame.K_RIGHT:
        fighter_move_right = True
    if event.key == pygame.K_SPACE:
        ball_fired = True
        ball_x = fighter_x + fighter_width / 2 - ball_width / 2
        ball_y = fighter_y - ball_height
```
- **Pressing Left Arrow (`K_LEFT`) → Moves left.**
- **Pressing Right Arrow (`K_RIGHT`) → Moves right.**
- **Pressing Spacebar (`K_SPACE`) → Fires the bullet.**
  - The bullet appears **in the middle of the fighter**.

### **b) Detecting Key Release (`KEYUP`)**
```python
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT:
        fighter_move_left = False
    if event.key == pygame.K_RIGHT:
        fighter_move_right = False
```
- **Releasing a key stops movement.**


## **10. Updating Positions**
Got it! Let's break down **section 10** in a more detailed, logical way.

---

### **10. Updating Positions**
This section ensures the movement of different game elements (fighter, alien, and bullet) based on user input and game logic.

---

### **a) Moving the Fighter**
```python
if fighter_move_left and fighter_x >= FIGHTER_STEP:
    fighter_x -= FIGHTER_STEP
if fighter_move_right and fighter_x <= WIDTH - fighter_width - FIGHTER_STEP:
    fighter_x += FIGHTER_STEP
```
#### **How This Works:**
1. **Checking `fighter_move_left`:**  
   - If `fighter_move_left` is `True`, it means the left arrow key is being pressed.  
   - The condition `fighter_x >= FIGHTER_STEP` ensures the fighter **doesn’t go off the left edge**.
   - If both conditions are true, `fighter_x -= FIGHTER_STEP` moves the fighter **left** by reducing its `x` position.

2. **Checking `fighter_move_right`:**  
   - If `fighter_move_right` is `True`, it means the right arrow key is being pressed.  
   - The condition `fighter_x <= WIDTH - fighter_width - FIGHTER_STEP` ensures the fighter **doesn’t go off the right edge**.  
   - If both conditions are true, `fighter_x += FIGHTER_STEP` moves the fighter **right** by increasing its `x` position.

#### **Why These Conditions Are Important:**
- **Prevents the fighter from going off the screen.**  
- **Ensures smooth movement** by only moving when necessary.  
- **Uses `FIGHTER_STEP` to control speed**, allowing fine-tuning of movement speed.

---

### **b) Moving the Alien**
```python
alien_y += alien_speed
```
#### **How This Works:**
1. `alien_y += alien_speed` increases the alien’s **y-coordinate**, making it move **downward**.
2. `alien_speed` is initially set to `ALIEN_STEP` but increases when an alien is hit, making the game progressively harder.

#### **Why This Works:**
- **Each frame, the alien moves down slightly.**  
- **The alien speed can increase**, making it fall faster over time.

---

### **c) Moving the Bullet**
```python
if ball_fired and ball_y + ball_height < 0:
    ball_fired = False
```
#### **How This Works:**
1. The condition `ball_fired` ensures that this code **only runs if the bullet is currently on the screen**.
2. The condition `ball_y + ball_height < 0` checks if the bullet has **gone past the top edge** of the screen.
3. If both conditions are true, `ball_fired = False` **removes the bullet from the screen**.

#### **Why This Works:**
- **Prevents bullets from staying off-screen forever.**
- **Allows firing a new bullet after the previous one disappears.**

---

```python
if ball_fired:
    ball_y -= BALL_STEP
```
#### **How This Works:**
1. If `ball_fired` is `True`, meaning a bullet is on screen, `ball_y -= BALL_STEP` moves the bullet **upward**.
2. `BALL_STEP` controls how fast the bullet moves.

#### **Why This Works:**
- **Moves the bullet up smoothly** while it's active.
- **Keeps the bullet moving until it either hits an alien or disappears.**

---

### **Summary of How Everything Moves**
- **Fighter moves left/right** when the respective key is pressed and stops when the key is released.
- **Alien continuously moves downward** at a speed that increases when hit.
- **Bullet moves upward** if fired and disappears if it leaves the screen.

Would you like an explanation for another part in more detail? 😊


## **11. Drawing Everything**
```python
screen.fill(screen_color)
screen.blit(fighter, (fighter_x, fighter_y))
screen.blit(alien, (alien_x, alien_y))
```
- **Clears screen** (`fill(screen_color)`) to remove old frames.
- **Draws the fighter, alien, and ball**.
```python
if ball_fired:
    screen.blit(ball, (ball_x, ball_y))
```
- This condition checks if `ball_fired` is `True`.
- `ball_fired` becomes `True` when the spacebar is pressed (in **event handling**).
- If `ball_fired` is `False`, this block **does nothing**, meaning the bullet is **not drawn** on the screen.
```python
screen.blit(ball, (ball_x, ball_y))
```
- This line **draws the bullet** (`ball`) on the screen at position `(ball_x, ball_y)`.
- `blit()` is a Pygame function that **renders an image onto another surface (the screen)**.
- Since `ball_y` decreases over time (from the movement logic in **section 10**), the bullet appears to move **upward**.


## **12. Displaying the Score**
```python
score_text = score_font.render(f"Your score is: {game_score}", True, 'white')
screen.blit(score_text, (20, 20))
```
- **Creates a text surface (`render()`)**
- **Displays score at the top left.**


## **13. Checking for Game Over**
```python
if alien_y + alien_height > fighter_y:
    run = False
```
- If the **alien reaches the fighter**, the game ends.


## **14. Checking for Bullet Collision**
This section detects if the bullet hits the alien. If a collision happens, the following things occur:
1. The bullet disappears.
2. The alien resets to the top of the screen at a new random position.
3. The alien's speed increases, making the game harder.
4. The player's score increases.

Here’s the code:
```python
if ball_fired and alien_x < ball_x < alien_x + alien_width - ball_width and alien_y < ball_y < alien_y + alien_height - ball_height:
    ball_fired = False
    alien_x, alien_y = randint(0, WIDTH - alien_width), 0
    alien_speed += ALIEN_STEP / 2
    game_score += 1
```


#### **Step 1: Checking if the Bullet is Fired**
```python
if ball_fired
```
- This ensures the check **only happens if there’s an active bullet**.
- If `ball_fired` is `False` (meaning no bullet is on screen), this block is **skipped**.
- This prevents unnecessary collision checks when no bullet exists.

---

#### **Step 2: Checking if the Bullet is Inside the Alien’s X-Range**
```python
alien_x < ball_x < alien_x + alien_width - ball_width
```
- **`alien_x < ball_x`** → This checks if the bullet's `x` coordinate is **to the right** of the alien’s left edge.
- **`ball_x < alien_x + alien_width - ball_width`** → This checks if the bullet's `x` coordinate is **to the left** of the alien’s right edge.
- **If both conditions are true**, it means the bullet is horizontally **inside the alien**.

---

#### **Step 3: Checking if the Bullet is Inside the Alien’s Y-Range**
```python
alien_y < ball_y < alien_y + alien_height - ball_height
```
- **`alien_y < ball_y`** → This checks if the bullet's `y` coordinate is **below** the alien’s top edge.
- **`ball_y < alien_y + alien_height - ball_height`** → This checks if the bullet's `y` coordinate is **above** the alien’s bottom edge.
- **If both conditions are true**, it means the bullet is vertically **inside the alien**.

---

### **Step 4: What Happens When a Collision is Detected**
If **all the above conditions are true**, it means the bullet **hit the alien**, and we execute the following actions:

#### **1. Remove the Bullet**
```python
ball_fired = False
```
- **This makes the bullet disappear**.
- Prevents multiple hits from a single bullet.

---

#### **2. Respawn the Alien at the Top**
```python
alien_x, alien_y = randint(0, WIDTH - alien_width), 0
```
- **Randomizes the alien’s `x` position** so it appears in a different location.
- **Resets `alien_y = 0`** to move the alien back to the top of the screen.

---

#### **3. Increase the Alien’s Speed**
```python
alien_speed += ALIEN_STEP / 2
```
- **Gradually makes the game harder** by increasing the falling speed of the alien.
- Uses `ALIEN_STEP / 2` to increase speed **slowly**, so difficulty ramps up smoothly.

#### **4. Increase the Player’s Score**
```python
game_score += 1
```
- **Adds 1 point to the player’s score**.
- This score is later displayed on the screen.

### **Final Summary**
1. **Checks if the bullet is active.**  
2. **Checks if the bullet’s x and y positions overlap with the alien’s position.**  
3. **If a collision happens:**  
   - **The bullet disappears.**  
   - **The alien moves back to the top at a new random position.**  
   - **The alien’s speed increases.**  
   - **The player earns points.**  

This creates **progressively increasing difficulty**, making the game more engaging.

Would you like me to explain any other part in detail? 😊


## **15. Game Over Message**
```python
game_over_text = game_font.render("Game Over!", True, 'white')
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()
```
- Displays **"Game Over!"** in the center.
- Waits **5 seconds** before closing.


## **Final Thoughts**
- **This game is simple yet effective**:  
  - Moving player  
  - Shooting bullets  
  - Enemy movement  
  - Collision detection