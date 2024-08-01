import cv2
import numpy as np
import pyautogui as pg
import tkinter as tk
import threading
import time
from PIL import Image, ImageTk
import customtkinter as ctk

class MainApp:

    def __init__(self, root):
        self.root = root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        screen_height=screen_height-80
        self.root.title("Valorant Manager")
        self.root.iconbitmap('ima/logo.ico')
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.agent_lock_event = threading.Event()
        self.stop_agent_lock_process = False

        self.streamermode_var = ctk.StringVar(value="off")

        self.top_frame = ctk.CTkFrame(self.root, width=1900, height=470, border_width=2, corner_radius=10)
        self.top_frame.pack(side="top", expand=True, padx=10, pady=10)

        self.login_frame = ctk.CTkFrame(self.top_frame, width=955, height=480, border_width=2, corner_radius=10)
        self.login_frame.pack(side="left", anchor="ne", expand=True, padx=10, pady=10)

        self.crosshair_frame = ctk.CTkFrame(self.top_frame, width=955, height=480, border_width=2, corner_radius=10)
        self.crosshair_frame.pack(side="top", anchor="nw", expand=True, padx=10, pady=10)

        self.agentlock_frame = ctk.CTkFrame(self.root,width=1910, height=480, border_width=2, corner_radius=10)
        self.agentlock_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        #agent lock
        self.create_button_frame(self.agentlock_frame)
        self.create_cancel_button_frame(self.agentlock_frame)
        self.create_text_output_frame(self.agentlock_frame)
        #valorant login
        self.id_input_frame = ctk.CTkFrame(self.login_frame, border_width=2, corner_radius=10)
        self.id_input_frame.pack(side="left", padx=20, pady=20)
        # Create the ID number label and input box
        self.id_no_label = ctk.CTkLabel(self.id_input_frame, text="ID Number:")
        self.id_no_label.pack(side="top", padx=10, pady=10)
        self.id_no_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_no_entry.pack(side="top", padx=10, pady=10)
        # Create the ID name label and input box
        self.id_name_label = ctk.CTkLabel(self.id_input_frame, text="ID Name:")
        self.id_name_label.pack(side="top", padx=10, pady=10)
        self.id_name_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_name_entry.pack(side="top", padx=10, pady=10)
        # Create the ID username label and input box
        self.id_username_label = ctk.CTkLabel(self.id_input_frame, text="ID Username:")
        self.id_username_label.pack(side="top", padx=10, pady=10)
        self.id_username_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_username_entry.pack(side="top", padx=10, pady=10)
        # Create the ID password label and input box
        self.id_password_label = ctk.CTkLabel(self.id_input_frame, text="ID Password:")
        self.id_password_label.pack(side="top", padx=10, pady=10)
        self.id_password_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_password_entry.pack(side="top", padx=10, pady=10)
        # Create the ID view box
        self.id_view_box = ctk.CTkScrollableFrame(self.login_frame, width=400, height=300, border_width=2, corner_radius=10)
        self.id_view_box.pack(side="left", padx=20, pady=20)
        # Create the buttons frame
        self.buttons_frame = ctk.CTkFrame(self.login_frame, border_width=2, corner_radius=10)
        self.buttons_frame.pack(side="right", padx=20, pady=20)
        self.titles = ["Add IDs", "View ID", "Update ID", "Delete ID", "Login to Valorant"]
        self.functions = [self.addvaloid, self.viewvaloid, self.editvaloid, self.deletevaloid, self.login]
        for i in range(len(self.titles)):
            button = ctk.CTkButton(self.buttons_frame, text=self.titles[i], command=self.functions[i], width=120, height=40, border_width=2, corner_radius=10)
            button.grid(row=i, column=0, padx=15, pady=15)
        # Create the Hide and un hide checkbox
        self.hide_unhide_checkbox = ctk.CTkSwitch(self.buttons_frame, text="Streamer mode",command=self.viewvaloid,variable=self.streamermode_var, onvalue="on", offvalue="off")
        self.hide_unhide_checkbox.grid(row=5, column=0, padx=15, pady=15)

        self.cross_input_frame = ctk.CTkFrame(self.crosshair_frame, border_width=2, corner_radius=10)
        self.cross_input_frame.pack(side="left", padx=20, pady=20)
        # Create the Crosshair number label and input box
        self.crosshair_no_label = ctk.CTkLabel(self.cross_input_frame, text="Crosshair Number:")
        self.crosshair_no_label.pack(side="top",  padx=10, pady=10)
        self.crosshair_no_entry = ctk.CTkEntry(self.cross_input_frame)
        self.crosshair_no_entry.pack(side="top",  padx=10, pady=10)
        # Create the Crosshair name label and input box
        self.crosshair_name_label = ctk.CTkLabel(self.cross_input_frame, text="Crosshair Name:")
        self.crosshair_name_label.pack(side="top",  padx=10, pady=10)
        self.crosshair_name_entry = ctk.CTkEntry(self.cross_input_frame)
        self.crosshair_name_entry.pack(side="top",  padx=10, pady=10)
        # Create the Crosshair code label and input box
        self.crosshair_code_label = ctk.CTkLabel(self.cross_input_frame, text="Crosshair Code:")
        self.crosshair_code_label.pack(side="top",  padx=10, pady=10)
        self.crosshair_code_entry = ctk.CTkEntry(self.cross_input_frame)
        self.crosshair_code_entry.pack(side="top",  padx=10, pady=10)
        # Create the Crosshair view box
        self.cross_view_box = ctk.CTkScrollableFrame(self.crosshair_frame, width=400, height=300, border_width=2, corner_radius=10)
        self.cross_view_box.pack(side="left", padx=20, pady=50)
        # Create the buttons frame
        self.cbuttons_frame = ctk.CTkFrame(self.crosshair_frame, border_width=2, corner_radius=10)
        self.cbuttons_frame.pack(side="right", padx=20, pady=20)
        self.ctitles = ["Add Crosshair", "View Crosshairs", "Delete Crosshair", "Input Crosshair"]
        self.cfunctions = [self.crossadd, self.crossview, self.crossdele, self.input]
        for i in range(len(self.ctitles)):
            button = ctk.CTkButton(self.cbuttons_frame, text=self.ctitles[i], command=self.cfunctions[i] ,width=120, height=40, border_width=2, corner_radius=10)
            button.grid(row=i, column=0, padx=15, pady=15)
    def create_button_frame(self, parent):
        button_frame = ctk.CTkFrame(master=parent, width=840, height=480, border_width=2, corner_radius=10)
        button_frame.pack(expand=True, fill="x", padx=5, pady=5)
        agents = [
            ("Astra", 'ima/astra.png'),
            ("Breach", 'ima/breach.png'),
            ("Brimstone", 'ima/brimstone.png'),
            ("Chamber", 'ima/chamber.png'),
            ("Clove", 'ima/clove.png'),
            ("Cypher", 'ima/cypher.png'),
            ("Deadlock", 'ima/deadlock.png'),
            ("Fade", 'ima/fade.png'),
            ("Gekko", 'ima/gekko.png'),
            ("Harbor", 'ima/harbor.png'),
            ("Iso", 'ima/iso.png'),
            ("Jett", 'ima/jett.png'),
            ("Kay/O", 'ima/kayo.png'),
            ("Killjoy", 'ima/killjoy.png'),
            ("Neon", 'ima/neon.png'),
            ("Omen", 'ima/omen.png'),
            ("Phoenix", 'ima/phoenix.png'),
            ("Raze", 'ima/raze.png'),
            ("Reyna", 'ima/reyna.png'),
            ("Sage", 'ima/sage.png'),
            ("Skye", 'ima/skye.png'),
            ("Sova", 'ima/sova.png'),
            ("Viper", 'ima/viper.png'),
            ("Yoru", 'ima/yoru.png')
        ]

        for i, (agent_name, original_image_path) in enumerate(agents):
            row, col = divmod(i, 15)
            self.create_agent_button(button_frame, agent_name, original_image_path, row, col)

    def create_agent_button(self, parent, agent_name, original_image_path, row, col):
        blurred_image_path = original_image_path.replace("ima/", "ima/stickers/")
        image = Image.open(blurred_image_path)
        image.thumbnail((100, 100))
        photo = ImageTk.PhotoImage(image)

        image_button = ctk.CTkButton(master=parent, image=photo, text=agent_name, height=150, width=102,
                                      font=("Helvetica", 14), hover_color="#000080", compound='top')
        image_button.image = photo
        image_button.grid(row=row, column=col, padx=5, pady=5)
        image_button.bind("<Button-1>", lambda event, name=agent_name, path=original_image_path: self.thread_agent_lock(name, path))

    def create_cancel_button_frame(self, parent):
        cancel_button_frame = ctk.CTkFrame(master=parent, width=170, height=50, border_width=2, corner_radius=10)
        cancel_button_frame.pack(padx=5, pady=5)
        cancel_label = ctk.CTkButton(master=cancel_button_frame, text="Cancel Agent Selection",
                                     command=self.cancel_agent_lock,
                                     height=40, width=12, font=("Helventica", 14), hover_color="#008080")
        cancel_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        cancel_label.bind("<Button-1>", lambda event: self.cancel_agent_lock())

    def create_text_output_frame(self, parent):
        text_output_frame = ctk.CTkFrame(parent, width=850, height=80, border_width=2, corner_radius=10)
        text_output_frame.pack(side="bottom", expand=True, fill="x", padx=5, pady=5)
        # rest of the code...
        self.text_output = ctk.CTkLabel(master=text_output_frame, text="Select your agent ")
        self.text_output.pack(padx=10, pady=10)
        self.text_output.configure(state="disabled")

    def thread_agent_lock(self, agent_name, original_image_path):
        # If a previous thread is still running, signal it to stop
        self.agent_lock_event.set()

        # Wait for a short period of time to ensure the previous thread has a chance to stop
        time.sleep(0.2)

        # Reset the event and start a new thread
        self.agent_lock_event.clear()
        threading.Thread(target=self.on_agent_button_click, args=(agent_name, original_image_path)).start()

    def on_agent_button_click(self, agent_name, original_image_path):
        self.stop_agent_lock_process = False
        self.update_output(f"Selected agent: {agent_name}")
        template_image = cv2.imread(original_image_path, cv2.IMREAD_COLOR)
        li = cv2.imread('ima/lock_in.png', cv2.IMREAD_COLOR)
        while not self.agent_lock_event.is_set() and not self.stop_agent_lock_process:
            screen_np = np.array(pg.screenshot(region=(0, 0, pg.size()[0]//2, pg.size()[1])))
            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
            result = cv2.matchTemplate(screen, template_image, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            result2 = cv2.matchTemplate(screen, li, cv2.TM_CCOEFF_NORMED)
            _, max_val2, _, max_loc2 = cv2.minMaxLoc(result2)
            if max_val >= 0.8 and max_val2 >= 0.8:
                for i in range (2):
                    pg.click(x=max_loc[0] + 41, y=max_loc[1] + 30, button='left')
                    time.sleep(0.01)
                    pg.click(x=max_loc2[0] + 30, y=max_loc2[1] + 30, button='left')
                self.update_output(f"{agent_name} locked successfully")
                break
        cv2.destroyAllWindows()

    def cancel_agent_lock(self):
        self.stop_agent_lock_process = True
        self.update_output("Agent lock canceled")

    def update_output(self, msg):
        self.text_output.configure(text=msg)

    def viewvaloid(self):
            # Clear the ID view box
            for widget in self.id_view_box.winfo_children():
                widget.destroy()
            if self.streamermode_var.get() == "off":
                # Read the ID, username, and password files
                with open('id.txt', 'r') as id_file:
                    id_lines = id_file.readlines()

                with open('username.txt', 'r') as username_file:
                    username_lines = username_file.readlines()

                with open('pass.txt', 'r') as password_file:
                    password_lines = password_file.readlines()

                # Display the IDs, usernames, and passwords in numerical order
                for i in range(len(id_lines)):
                    id_num = i + 1
                    id_text = f"ID No. {id_num}: {id_lines[i].strip()}"
                    username_text = f"Username: {username_lines[i].strip()}"
                    password_text = f"Password: {password_lines[i].strip()}\n"

                    label = ctk.CTkLabel(self.id_view_box, text=id_text)
                    label.pack(pady=5)

                    label = ctk.CTkLabel(self.id_view_box, text=username_text)
                    label.pack(pady=5)

                    label = ctk.CTkLabel(self.id_view_box, text=password_text)
                    label.pack(pady=5)

            elif self.streamermode_var.get() == "on":
                # Read the ID files
                with open('id.txt', 'r') as id_file:
                    id_lines = id_file.readlines()

                # Display the IDs in numerical order
                for i in range(len(id_lines)):
                    id_num = i + 1
                    id_text = f"ID No. {id_num} :- {id_lines[i].strip()}"

                    label = ctk.CTkLabel(self.id_view_box, text=id_text)
                    label.pack(pady=5)


    def addvaloid(self):
        # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Get the ID information from the entry widgets
        id_name = self.id_name_entry.get()
        id_username = self.id_username_entry.get()
        id_password = self.id_password_entry.get()

        # Check if the inputs are not empty
        if id_name and id_username and id_password:
            # Open the ID, username, and password files for appending
            with open('id.txt', 'a') as id_file:
                with open('username.txt', 'a') as username_file:
                    with open('pass.txt', 'a') as password_file:

                        # Write the ID information to the files
                        id_file.write(id_name + '\n')
                        username_file.write(id_username + '\n')
                        password_file.write(id_password + '\n')

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.id_view_box, text="Your ID is successfully being added.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text="Error: All fields must be filled.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_name_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def editvaloid(self):
            # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Get the serial number from the ID number entry widget
        serial_number_str = self.id_no_entry.get()

        # Check if the serial number string is not empty
        if not serial_number_str:
            error_label = ctk.CTkLabel(self.id_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        serial_number = int(serial_number_str)
        serial_number = serial_number - 1

        id_path = 'id.txt'
        username_path = 'username.txt'
        password_path = 'pass.txt'

        with open(id_path, 'r') as id_file, open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
            id_lines = id_file.readlines()
            username_lines = username_file.readlines()
            password_lines = password_file.readlines()

        if 0 <= serial_number < len(id_lines):
            # Get the new ID, username, and password from the entry widgets
            new_id = self.id_name_entry.get()
            new_username = self.id_username_entry.get()
            new_password = self.id_password_entry.get()

            id_lines[serial_number] = new_id + '\n'
            username_lines[serial_number] = new_username + '\n'
            password_lines[serial_number] = new_password + '\n'

            with open(id_path, 'w') as id_file, open(username_path, 'w') as username_file, open(password_path,'w') as password_file:
                id_file.writelines(id_lines)
                username_file.writelines(username_lines)
                password_file.writelines(password_lines)

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.id_view_box, text="Your Valorant ID is successfully updated.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_no_entry.delete(0, tk.END)
        self.id_name_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def deletevaloid(self):
        # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Get the serial number from the ID number entry widget
        serial_number_str = self.id_no_entry.get()

        # Check if the serial number string is not empty
        if not serial_number_str:
            error_label = ctk.CTkLabel(self.id_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        serial_number = int(serial_number_str)
        serial_number = serial_number - 1

        id_path = 'id.txt'
        username_path = 'username.txt'
        password_path = 'pass.txt'

        with open(id_path, 'r') as id_file, open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
            id_lines = id_file.readlines()
            username_lines = username_file.readlines()
            password_lines = password_file.readlines()

        if 0 <= serial_number < len(id_lines):
            # Delete the specified entries
            del id_lines[serial_number]
            del username_lines[serial_number]
            del password_lines[serial_number]

            with open(id_path, 'w') as id_file, open(username_path, 'w') as username_file, open(password_path,'w') as password_file:
                id_file.writelines(id_lines)
                username_file.writelines(username_lines)
                password_file.writelines(password_lines)

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.id_view_box, text=f"Entry with serial number {serial_number+1} has been deleted.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_no_entry.delete(0, tk.END)
        self.id_name_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def login(self):
            # Get the serial number from the ID number entry widget
            serial_number_str = self.id_no_entry.get()

            # Check if the serial number string is not empty
            if not serial_number_str:
                error_label = ctk.CTkLabel(self.id_view_box, text="Error: ID Number field must not be empty.")
                error_label.pack(side="top", padx=5, pady=5)
                return

            serial_number = int(serial_number_str)
            serial_number = serial_number - 1

            id_path = 'id.txt'
            username_path = 'username.txt'
            password_path = 'pass.txt'

            with open(id_path, 'r') as id_file, open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
                id_lines = id_file.readlines()
                username_lines = username_file.readlines()
                password_lines = password_file.readlines()

            if 0 <= serial_number < len(id_lines):
                x = username_lines[serial_number].strip()
                y = password_lines[serial_number].strip()

                time.sleep(1)
                pg.press("win")
                time.sleep(1)
                pg.write("valorant")
                pg.press("enter")
                UN_image_path = r'ima\un.png'
                PW_image_path = r'ima\pw.png'

                UN_image = cv2.imread(UN_image_path, cv2.IMREAD_COLOR)
                PW_image = cv2.imread(PW_image_path, cv2.IMREAD_COLOR)

                while True:
                    screen_pil = pg.screenshot()
                    screen_np = np.array(screen_pil)
                    screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

                    result = cv2.matchTemplate(screen, UN_image, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                    result2 = cv2.matchTemplate(screen, PW_image, cv2.TM_CCOEFF_NORMED)
                    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)

                    threshold = 0.8
                    if max_val >= threshold:
                        un_x, un_y = max_loc
                        pw_x, pw_y = max_loc2

                        pg.moveTo(un_x + 41, un_y + 32, 0.00000000000001)
                        pg.click(button='left')
                        pg.write(x)
                        pg.moveTo(pw_x + 41, pw_y + 32, 0.00000000000001)
                        pg.click(button='left')
                        pg.write(y)
                        pg.press("enter")
                        break
                cv2.destroyAllWindows()
            else:
                # Display an error message in the viewbox
                error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
                error_label.pack(side="top", padx=5, pady=5)

            # Clear the entry widgets
            self.id_no_entry.delete(0, tk.END)
            self.id_name_entry.delete(0, tk.END)
            self.id_username_entry.delete(0, tk.END)
            self.id_password_entry.delete(0, tk.END)
    def crossadd(self):
        # Clear the Crosshair view box
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()

        # Get the Crosshair information from the entry widgets
        crosshair_name = self.crosshair_name_entry.get()
        crosshair_code = self.crosshair_code_entry.get()

        # Check if the inputs are not empty
        if crosshair_name and crosshair_code:
            # Open the Crosshair name and code files for appending
            with open('crossname.txt', 'a') as chn_file, open('crosscode.txt', 'a') as ch_file:
                # Write the Crosshair information to the files
                chn_file.write(crosshair_name + '\n')
                ch_file.write(crosshair_code + '\n')

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.cross_view_box, text="Crosshair added successfully.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.cross_view_box, text="Error: All fields must be filled.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.crosshair_no_entry.delete(0, tk.END)
        self.crosshair_name_entry.delete(0, tk.END)
        self.crosshair_code_entry.delete(0, tk.END)

    def crossview(self):
        # Clear the Crosshair view box
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()

        chn_path = 'crossname.txt'
        ch_path = 'crosscode.txt'

        with open(chn_path, 'r') as chn_file, open(ch_path, 'r') as ch_file:
            chn_lines = chn_file.readlines()
            ch_lines = ch_file.readlines()

        for i in range(len(chn_lines)):
            crosshair_name = chn_lines[i].strip()
            crosshair_label = ctk.CTkLabel(self.cross_view_box, text=f"S.no -> {i+1}\nCrosshair -> {crosshair_name}")
            crosshair_label.pack(side="top", padx=5, pady=5)

    def crossdele(self):
        # Clear the Crosshair view box
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()

        # Get the serial number from the ID number entry widget
        serial_number_str = self.crosshair_no_entry.get()

        # Check if the serial number string is not empty
        if not serial_number_str:
            error_label = ctk.CTkLabel(self.cross_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        serial_number = int(serial_number_str)
        serial_number = serial_number - 1

        chn_path = 'crossname.txt'
        ch_path = 'crosscode.txt'

        with open(chn_path, 'r') as chn_file, open(ch_path, 'r') as ch_file:
            chn_lines = chn_file.readlines()
            ch_lines = ch_file.readlines()

        if 0 <= serial_number < len(chn_lines):
            del chn_lines[serial_number]
            del ch_lines[serial_number]

            with open(chn_path, 'w') as chn_file, open(ch_path, 'w') as ch_file:
                chn_file.writelines(chn_lines)
                ch_file.writelines(ch_lines)

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.cross_view_box, text=f"Entry with serial number {serial_number+1} has been deleted.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.cross_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.crosshair_no_entry.delete(0, tk.END)
        self.crosshair_name_entry.delete(0, tk.END)
        self.crosshair_code_entry.delete(0, tk.END)

    def input(self):
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()
        text_label = ctk.CTkLabel(self.cross_view_box,text=f"!!!!!!!! Works only in home screen of valorant !!!!!!!!")
        text_label.pack(side="top", padx=5, pady=5)
        chn = open('crosscode.txt', 'r')
        text_label = ctk.CTkLabel(self.cross_view_box, text=f"Enter the s.no of crosshair ")
        text_label.pack(side="top", padx=5, pady=5)
        chno_str = self.crosshair_no_entry.get()
        l = 1
        if not chno_str:
            error_label = ctk.CTkLabel(self.cross_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        chno = int(chno_str)
        while l <= chno:
            c = chn.readline()
            l = l + 1
        sett_image = cv2.imread('ima/sett.png', cv2.IMREAD_COLOR)
        setl_image = cv2.imread('ima/setl.png', cv2.IMREAD_COLOR)
        croha_image = cv2.imread('ima/croha.png', cv2.IMREAD_COLOR)
        impo_image = cv2.imread('ima/impo.png', cv2.IMREAD_COLOR)
        ok_image = cv2.imread('ima/ok.png', cv2.IMREAD_COLOR)
        pypch_image = cv2.imread('ima/pypch.png', cv2.IMREAD_COLOR)

        time.sleep(5)

        while True:
            screen_pil = pg.screenshot()
            screen_np = np.array(screen_pil)
            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

            # xyz = cv2.matchTemplate(screen, xyz_image, cv2.TM_CCOEFF_NORMED)
            # xyz_min_val, xyz_max_val, xyz_min_loc, xyz_max_loc = cv2.minMaxLoc(xyz)

            sett = cv2.matchTemplate(screen, sett_image, cv2.TM_CCOEFF_NORMED)
            sett_min_val, sett_max_val, sett_min_loc, sett_max_loc = cv2.minMaxLoc(sett)

            setl = cv2.matchTemplate(screen, setl_image, cv2.TM_CCOEFF_NORMED)
            setl_min_val, setl_max_val, setl_min_loc, setl_max_loc = cv2.minMaxLoc(setl)

            threshold = 0.8

            if setl_max_val >= threshold:
                match_x, match_y = setl_max_loc
                # print("Template found at:", match_x, match_y)
                pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                pg.click(button='left')
                if sett_max_val >= threshold:
                    match_x, match_y = sett_max_loc
                    pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                    pg.click(button='left')
                    time.sleep(0.5)
                    cv2.destroyAllWindows()

                    screen_pil = pg.screenshot()
                    screen_np = np.array(screen_pil)
                    screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                    croha = cv2.matchTemplate(screen, croha_image, cv2.TM_CCOEFF_NORMED)
                    croha_min_val, croha_max_val, croha_min_loc, croha_max_loc = cv2.minMaxLoc(croha)
                    if croha_max_val >= threshold:
                        match_x, match_y = croha_max_loc
                        pg.moveTo(match_x + 15, match_y + 15, 0.00000000000001)
                        pg.click(button='left')
                        time.sleep(0.5)
                        cv2.destroyAllWindows()

                        screen_pil = pg.screenshot()
                        screen_np = np.array(screen_pil)
                        screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                        impo = cv2.matchTemplate(screen, impo_image, cv2.TM_CCOEFF_NORMED)
                        impo_min_val, impo_max_val, impo_min_loc, impo_max_loc = cv2.minMaxLoc(impo)
                        if impo_max_val >= threshold:
                            match_x, match_y = impo_max_loc
                            pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                            pg.click(button='left')
                            time.sleep(0.5)
                            cv2.destroyAllWindows()
                            screen_pil = pg.screenshot()
                            screen_np = np.array(screen_pil)
                            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                            pypch = cv2.matchTemplate(screen, pypch_image, cv2.TM_CCOEFF_NORMED)
                            pypch_min_val, pypch_max_val, pypch_min_loc, pypch_max_loc = cv2.minMaxLoc(pypch)
                            if pypch_max_val >= threshold:
                                match_x, match_y = pypch_max_loc
                                pg.moveTo(match_x + 90, match_y + 140, 0.00000000000001)
                                pg.click(button='left')
                                pg.write(c)
                                pg.press("backspace")
                                pg.moveTo(match_x + 97, match_y + 300, 0.00000000000001)
                                pg.click(button='left')
                                cv2.destroyAllWindows()
                                time.sleep(1)
                                screen_pil = pg.screenshot()
                                screen_np = np.array(screen_pil)
                                screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                                ok = cv2.matchTemplate(screen, ok_image, cv2.TM_CCOEFF_NORMED)
                                ok_min_val, ok_max_val, ok_min_loc, ok_max_loc = cv2.minMaxLoc(ok)
                                if ok_max_val >= threshold:
                                    match_x, match_y = ok_max_loc
                                    pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                                    pg.click(button='left')
                                    text_label = ctk.CTkLabel(self.cross_view_box,text=f"Crosshair has been added successfully!")
                                    text_label.pack(side="top", padx=5, pady=5)
                                    break
                                else:
                                    text_label = ctk.CTkLabel(self.cross_view_box,text=f"Crosshair code is incorrect .Please correct it from previous menu")
                                    text_label.pack(side="top", padx=5, pady=5)
                                    break
                            else:
                                text_label = ctk.CTkLabel(self.cross_view_box,text=f"Your all Crosshair slots are full")
                                text_label.pack(side="top", padx=5, pady=5)
                                break
            cv2.destroyAllWindows()

    #def crf(self):


root = ctk.CTk()
app = MainApp(root)
root.mainloop()
