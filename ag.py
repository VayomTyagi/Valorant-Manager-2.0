
import tkinter as tk
from tkinter import Label
import cv2
import numpy as np
import pyautogui as pg
import threading
from PIL import Image, ImageTk
stop_agent_lock_process = False
def on_agent_button_click(agent_name, original_image_path):
    global text_output, stop_agent_lock_process
    stop_agent_lock_process = False
    text_output.config(state="normal")
    text_output.insert("end", f"Selected agent: {agent_name}\n")
    text_output.see("end")
    text_output.config(state="disabled")
    template_image = cv2.imread(original_image_path, cv2.IMREAD_COLOR)
    li = cv2.imread('ima/lock_in.png', cv2.IMREAD_COLOR)
    while not stop_agent_lock_process:
        screen_pil = pg.screenshot(region=(0, pg.size()[1] // 2, pg.size()[0], pg.size()[1] // 2))
        screen_np = np.array(screen_pil)
        screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screen, template_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        result2 = cv2.matchTemplate(screen, li, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc2 = cv2.minMaxLoc(result2)
        if max_val >= 0.8:
            pg.click(x=max_loc[0] + 41, y=max_loc[1] + pg.size()[1] // 2 + 32, button='left')
            pg.click(x=max_loc2[0] + 30, y=max_loc2[1] + pg.size()[1] // 2 + 30, button='left')
            text_output.config(state="normal")
            text_output.insert("end", "Agent lock successful\n")
            text_output.see("end")
            text_output.config(state="disabled")
            break
    cv2.destroyAllWindows()
def cancel_agent_lock():
    global stop_agent_lock_process
    stop_agent_lock_process = True
    text_output.config(state="normal")
    text_output.insert("end", "Agent lock canceled\n")
    text_output.see("end")
    text_output.config(state="disabled")
def update_output(msg):
    text_output.config(state="normal")
    text_output.insert("1.0", msg + "\n")
    text_output.config(state="disabled")
def thread_agent_lock(agent_name, original_image_path):
    threading.Thread(target=on_agent_button_click, args=(agent_name, original_image_path)).start()
def close_application(event):
    root.destroy()
root = tk.Tk()
root.title("AGENT LOCK")
root.geometry("640x550")
#root.overrideredirect(True)
root.configure(bg="#333333")
# Create a close button using grid
close_image = Image.open('ima/close.png')
close_image.thumbnail((30, 30))
close_photo = ImageTk.PhotoImage(image=close_image)
close_button = tk.Label(root, image=close_photo,bg="black")
close_button.image = close_photo
close_button.grid(row=0, column=7, sticky="ne")  # Use grid manager for the close button
close_button.bind("<Button-1>", close_application)
agents = [("Astra", 'ima/astra.png'),("Breach", 'ima/breach.png'),("Brimstone", 'ima/brimstone.png'),("Chamber", 'ima/chamber.png'),("Cypher", 'ima/cypher.png'),("Deadlock", 'ima/deadlock.png'),("Fade", 'ima/fade.png'),("Gekko", 'ima/gekko.png'),("Harbor", 'ima/harbor.png'),("Iso", 'ima/iso.png'),("Jett", 'ima/jett.png'),("Kay/O", 'ima/kayo.png'),("Killjoy", 'ima/killjoy.png'),("Neon", 'ima/neon.png'),("Omen", 'ima/omen.png'),("Phoenix", 'ima/phoenix.png'),("Raze", 'ima/raze.png'),("Reyna", 'ima/reyna.png'),("Sage", 'ima/sage.png'),("Skye", 'ima/skye.png'),("Sova", 'ima/sova.png'),("Viper", 'ima/viper.png'),("Yoru", 'ima/yoru.png')]
def agent_button_click(agent_name, original_image_path):
    thread_agent_lock(agent_name, original_image_path)
image_buttons = []
for i, (agent_name, original_image_path) in enumerate(agents):
    row = i // 7
    col = i % 7
    blurred_image_path = original_image_path.replace("ima/", "ima/stickers/")
    image = Image.open(blurred_image_path)
    image.thumbnail((80, 80))
    photo = ImageTk.PhotoImage(image=image)
    image_button = Label(root, image=photo, text=agent_name, compound="top", bg="black", fg="white",
                         font=("Helvetica", 10))
    image_button.image = photo
    image_button.grid(row=row+1, column=col+1)
    image_buttons.append(image_button)
    image_button.bind("<Button-1>",lambda event, name=agent_name, path=original_image_path: agent_button_click(name, path))
cancel_image = Image.open('ima/cancel.png')
cancel_image.thumbnail((120, 120))
cancel_photo = ImageTk.PhotoImage(image=cancel_image)
def on_cancel_label_click(event):
    cancel_agent_lock()
cancel_label = Label(root, image=cancel_photo, bg="black")
cancel_label.image = cancel_photo
cancel_label.grid(row=row + 2, columnspan=11)
cancel_label.bind("<Button-1>", on_cancel_label_click)
text_output = tk.Text(root, wrap="word", bg="#333333", fg="white", height=2)
text_output.grid(row=row + 3, columnspan=11, sticky="nsew")
text_output.config(state="disabled")
root.mainloop()
root.mainloop()