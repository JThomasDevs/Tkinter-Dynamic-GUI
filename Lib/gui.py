import tkinter as tk
from PIL import Image, ImageTk
from functions import imgpath


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.scenes = {
            'art1': {'scene': imgpath('Art', 'art1.png'),
                     'name': 'art1',
                     'leftbutton': imgpath('Button', 'button2.png'),
                     'rightbutton': imgpath('Button', 'button3.png'),
                     'leftnext': 'art2',
                     'rightnext': 'art3'},
            'art2': {'scene': imgpath('Art', 'art2.png'),
                     'name': 'art2',
                     'leftbutton': imgpath('Button', 'button3.png'),
                     'rightbutton': imgpath('Button', 'button4.png'),
                     'leftnext': 'art3',
                     'rightnext': 'art4'},
            'art3': {'scene': imgpath('Art', 'art3.png'),
                     'name': 'art3',
                     'leftbutton': imgpath('Button', 'button4.png'),
                     'midbutton': imgpath('Button', 'button9.png'),
                     'rightbutton': imgpath('Button', 'button10.png'),
                     'leftnext': 'art4',
                     'midnext': 'art9',
                     'rightnext': 'art10'},
            'art4': {'scene': imgpath('Art', 'art4.png'),
                     'name': 'art4',
                     'topleftbutton': imgpath('Button', 'button5.png'),
                     'botleftbutton': imgpath('Button', 'button6.png'),
                     'toprightbutton': imgpath('Button', 'button7.png'),
                     'botrightbutton': imgpath('Button', 'button8.png'),
                     'topleftnext': 'art5',
                     'botleftnext': 'art6',
                     'toprightnext': 'art7',
                     'botrightnext': 'art8'},
            'art5': {'scene': imgpath('Art', 'art5.png'),
                     'name': 'art5'},
            'art6': {'scene': imgpath('Art', 'art6.png'),
                     'name': 'art6'},
            'art7': {'scene': imgpath('Art', 'art7.png'),
                     'name': 'art7'},
            'art8': {'scene': imgpath('Art', 'art8.png'),
                     'name': 'art8'},
            'art9': {'scene': imgpath('Art', 'art9.png'),
                     'name': 'art9'},
            'art10': {'scene': imgpath('Art', 'art10.png'),
                      'name': 'art10'}
        }
        self.current_scene = self.scenes['art1']
        self.previous_scene = None

        # Main window frames
        self.art_frame = tk.Frame(self, bd=0)
        self.art_frame.config(highlightthickness=0, highlightbackground='red')

        self.script_frame = tk.Frame(self, bd=0)
        self.script_frame.config(highlightthickness=0, highlightbackground='green')

        self.info_frame = tk.Frame(self, bd=0)
        self.info_frame.config(highlightthickness=0, highlightbackground='white')

        # Place the main window frames
        self.art_frame.place(relx=0, rely=0, relwidth=0.75, relheight=1)
        self.script_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=(2 / 3))
        self.info_frame.place(relx=0.75, rely=(2 / 3), relwidth=0.25, relheight=(1 / 3))

        # Labels for each main window frame
        self.art_label = tk.Label(self.art_frame)
        self.art_label.pack(fill='both', expand=True)

        self.script_label = tk.Label(self.script_frame)
        self.script_label.pack(fill='both', expand=True)

        self.info_label = tk.Label(self.info_frame)
        self.info_label.pack(fill='both', expand=True)

        # Load all images
        self.artimg = Image.open(imgpath('Art', 'art1.png'))
        self.scriptimg = Image.open(imgpath('Script', 'gamescript1.png'))
        self.infoimg = Image.open(imgpath('Info', 'gameinfo.png'))

        # Initialize buttons
        self.buttons = []
        self.create_buttons()

        # Bind all frames to <Configure> so they resize when the window resizes
        self.art_frame.bind('<Configure>', self.resize_artimg)
        self.script_frame.bind('<Configure>', self.resize_scriptimg)
        self.info_frame.bind('<Configure>', self.resize_infoimg)

    def create_buttons(self):
        # Remove any existing buttons
        for button in self.buttons:
            button.destroy()
        self.buttons = []

        if (self.current_scene['name'] != 'art1') and (self.previous_scene is not None):
            self.gobackimg = ImageTk.PhotoImage(Image.open(imgpath('Button', 'button1.png')))
            self.gobackbutton = tk.Button(self.art_label, image=self.gobackimg, bd=0, bg='black')
            self.gobackbutton.place(relx=0.02, rely=0.05, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.gobackbutton)
            self.gobackbutton.bind('<Configure>', self.resize_gobackbutton)
            self.gobackbutton.config(command=lambda: self.goback())

        if 'leftbutton' in self.current_scene:
            leftbtnimage = ImageTk.PhotoImage(Image.open(self.current_scene['leftbutton']))
            self.leftbutton = tk.Button(self.art_label, image=leftbtnimage, bd=0, bg='black')
            self.leftbutton.config(fg='pink')
            self.leftbutton.place(relx=0.15, rely=0.85, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.leftbutton)
            self.leftbutton.bind('<Configure>', self.resize_leftbutton)
            self.leftbutton.config(command=lambda: self.update_scene(self.current_scene['leftnext']))
        if 'midbutton' in self.current_scene:
            midbtnimage = ImageTk.PhotoImage(Image.open(self.current_scene['midbutton']))
            self.midbutton = tk.Button(self.art_label, image=midbtnimage, bd=0, bg='black')
            self.midbutton.config(fg='pink')
            self.midbutton.place(relx=0.4, rely=0.85, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.midbutton)
            self.midbutton.bind('<Configure>', self.resize_midbutton)
            self.midbutton.config(command=lambda: self.update_scene(self.current_scene['midnext']))
        if 'rightbutton' in self.current_scene:
            rightbtnimage = ImageTk.PhotoImage(Image.open(self.current_scene['rightbutton']))
            self.rightbutton = tk.Button(self.art_label, image=rightbtnimage, bd=0, bg='black')
            self.rightbutton.place(relx=0.65, rely=0.85, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.rightbutton)
            self.rightbutton.bind('<Configure>', self.resize_rightbutton)
            self.rightbutton.config(command=lambda: self.update_scene(self.current_scene['rightnext']))
        if 'topleftbutton' in self.current_scene:
            topleftbtnimage = ImageTk.PhotoImage(Image.open(self.current_scene['topleftbutton']))
            self.topleftbutton = tk.Button(self.art_label, image=topleftbtnimage, bd=0, bg='black')
            self.topleftbutton.place(relx=0.15, rely=0.75, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.topleftbutton)
            self.topleftbutton.bind('<Configure>', self.resize_topleftbutton)
            self.topleftbutton.config(command=lambda: self.update_scene(self.current_scene['topleftnext']))
        if 'botleftbutton' in self.current_scene:
            botleftbtnimage = ImageTk.PhotoImage(Image.open(self.current_scene['botleftbutton']))
            self.botleftbutton = tk.Button(self.art_label, image=botleftbtnimage, bd=0, bg='black')
            self.botleftbutton.place(relx=0.15, rely=0.85, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.botleftbutton)
            self.botleftbutton.bind('<Configure>', self.resize_botleftbutton)
            self.botleftbutton.config(command=lambda: self.update_scene(self.current_scene['botleftnext']))
        if 'toprightbutton' in self.current_scene:
            toprightbtnimage = ImageTk.PhotoImage(Image.open(self.current_scene['toprightbutton']))
            self.toprightbutton = tk.Button(self.art_label, image=toprightbtnimage, bd=0, bg='black')
            self.toprightbutton.place(relx=0.65, rely=0.75, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.toprightbutton)
            self.toprightbutton.bind('<Configure>', self.resize_toprightbutton)
            self.toprightbutton.config(command=lambda: self.update_scene(self.current_scene['toprightnext']))
        if 'botrightbutton' in self.current_scene:
            botrightbtnimage = ImageTk.PhotoImage(Image.open(self.current_scene['botrightbutton']))
            self.botrightbutton = tk.Button(self.art_label, image=botrightbtnimage, bd=0, bg='black')
            self.botrightbutton.place(relx=0.65, rely=0.85, relwidth=(103/720), relheight=(1/15))
            self.buttons.append(self.botrightbutton)
            self.botrightbutton.bind('<Configure>', self.resize_botrightbutton)
            self.botrightbutton.config(command=lambda: self.update_scene(self.current_scene['botrightnext']))

    def resize_rightbutton(self, event):
        rightbtnorig = Image.open(self.current_scene['rightbutton'])
        rightbtn_resized = rightbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.rightbtn_tk = ImageTk.PhotoImage(rightbtn_resized)
        self.rightbutton.config(image=self.rightbtn_tk)

    def resize_midbutton(self, event):
        midbtnorig = Image.open(self.current_scene['midbutton'])
        midbtn_resized = midbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.midbtn_tk = ImageTk.PhotoImage(midbtn_resized)
        self.midbutton.config(image=self.midbtn_tk)

    def resize_leftbutton(self, event):
        leftbtnorig = Image.open(self.current_scene['leftbutton'])
        leftbtn_resized = leftbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.leftbtn_tk = ImageTk.PhotoImage(leftbtn_resized)
        self.leftbutton.config(image=self.leftbtn_tk)

    def resize_topleftbutton(self, event):
        topleftbtnorig = Image.open(self.current_scene['topleftbutton'])
        topleftbtn_resized = topleftbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.topleftbtn_tk = ImageTk.PhotoImage(topleftbtn_resized)
        self.topleftbutton.config(image=self.topleftbtn_tk)

    def resize_botleftbutton(self, event):
        botleftbtnorig = Image.open(self.current_scene['botleftbutton'])
        botleftbtn_resized = botleftbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.botleftbtn_tk = ImageTk.PhotoImage(botleftbtn_resized)
        self.botleftbutton.config(image=self.botleftbtn_tk)

    def resize_toprightbutton(self, event):
        toprightbtnorig = Image.open(self.current_scene['toprightbutton'])
        toprightbtn_resized = toprightbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.toprightbtn_tk = ImageTk.PhotoImage(toprightbtn_resized)
        self.toprightbutton.config(image=self.toprightbtn_tk)

    def resize_botrightbutton(self, event):
        botrightbtnorig = Image.open(self.current_scene['botrightbutton'])
        botrightbtn_resized = botrightbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.botrightbtn_tk = ImageTk.PhotoImage(botrightbtn_resized)
        self.botrightbutton.config(image=self.botrightbtn_tk)

    def resize_gobackbutton(self, event):
        gobackbtnorig = Image.open(imgpath('Button', 'button1.png'))
        gobackbtn_resized = gobackbtnorig.resize((event.width, event.height), Image.LANCZOS)
        self.gobackbtn_tk = ImageTk.PhotoImage(gobackbtn_resized)
        self.gobackbutton.config(image=self.gobackbtn_tk)

    def resize_artimg(self, event):
        artimg = Image.open(self.current_scene['scene'])
        self.artimg_resized = artimg.resize((self.art_frame.winfo_width(), self.art_frame.winfo_height()))
        self.artimg_tk = ImageTk.PhotoImage(self.artimg_resized)
        self.art_label.config(image=self.artimg_tk)

    def resize_scriptimg(self, event):
        self.scriptimg_resized = self.scriptimg.resize((self.script_frame.winfo_width(),
                                                        self.script_frame.winfo_height()))
        self.scriptimg_tk = ImageTk.PhotoImage(self.scriptimg_resized)
        self.script_label.config(image=self.scriptimg_tk)

    def resize_infoimg(self, event):
        self.infoimg_resized = self.infoimg.resize((self.info_frame.winfo_width(), self.info_frame.winfo_height()))
        self.infoimg_tk = ImageTk.PhotoImage(self.infoimg_resized)
        self.info_label.config(image=self.infoimg_tk)

    def update_scene(self, scene):
        self.previous_scene = self.current_scene
        self.current_scene = self.scenes[scene]
        self.artimg = self.current_scene
        newart = Image.open(self.current_scene['scene'])
        newart_resized = newart.resize((self.art_frame.winfo_width(), self.art_frame.winfo_height()))
        newart_tk = ImageTk.PhotoImage(newart_resized)
        self.art_label.config(image=newart_tk)
        self.create_buttons()
        # The following lines keep the updated image from being garbage collected
        self.image1 = newart
        self.image1_resized = newart_resized
        self.image1_tk = newart_tk

    def goback(self):
        if self.previous_scene is not None:
            self.update_scene(self.previous_scene['name'])
            self.previous_scene = None
            self.create_buttons()


root = Game()
root.geometry('1280x720')
root.minsize(width=720, height=405)
root.configure(bg='black')
root.title(' ̵̙̓ ̴̖̈́͛ ̴͎̏ ̵̲͓̆̈́ ̴̗̤̌ ̶̡̈́̾ ̷̦̖̆̈S̷͔̈́̅ͅT̸̳͉̉Ù̸̢͠C̸̨̤̃̕K̸̢̦̏͆ ̴̖̺̓ ̴̳̹̆͝ ̷̢̺̄̋ ̵̛͖͎́ ̵͚̤͗͑ ̴͔͕̀͝ ̵̨̇')
root.iconbitmap(imgpath('Icon', 'stuckicon.ico'))
root.state('zoomed')
# root.attributes('-fullscreen', True)
root.update()
root.mainloop()
