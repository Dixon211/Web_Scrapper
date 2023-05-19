from bs4 import BeautifulSoup
import requests
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Frame
from tkinter import INSERT

class Window:
    def __init__(self, root):
        self.root = root
        root.title = "Scraping Practice"
        root.geometry("500x300") #measured in pixels
        root.attributes('-fullscreen', True)
        root.config(bg="#262624")
        root.bind('<Escape>', self.close_win) #binds close window to esc key
        self.create_page()
#create initial page
    def create_page(self):
        self.entry_frame = Frame(root)
        self.entry_frame.pack(side='top', expand=True)
        #setting python image
        self.image = Image.open('python.png')
        self.image = self.image.resize((300, 300))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label= tk.Label(self.entry_frame, image=self.photo)
        self.image_label.grid(column=0, row=0)

        #creates an input field
        self.entry = tk.Entry(self.entry_frame, width=50)
        self.entry.grid(column=0, row=1)

        #creates a button
        self.submit_button = tk.Button(self.entry_frame, text="Site to Scrape", command = self.submit_action)
        self.submit_button.grid(column=0, row=2)

        #message label
        self.message_label = tk.Label(self.entry_frame, text="")
        self.message_label.grid(column=0, row=3)
#submit the website
    def submit_action(self):
        input_text = self.entry.get()
        url = input_text
        http_response = requests.get(url)

        if http_response.status_code == 200:
            html_content = http_response.text
            self.soup = BeautifulSoup(html_content, 'lxml')
            

            display_text = "Scraping successful!"
            self.message_label.config(text=display_text)
            self.root.after(1500, self.transition_text) #adds a delay to the execution in milliseconds

        
        else:
            display_text =  f'failed to connect, Error Code:{http_response.status_code}'
            #uses the .config to change the text of the message_label
            self.message_label.config(text=display_text)
#create new window with editable textbox
    def transition_text(self):
        #get rid of current elements and set the new frames!
        self.entry_frame.forget()
        self.upper_frame = Frame(root)
        self.upper_frame.pack(side='top', expand=True)
        self.text_frame = Frame(root)
        self.text_frame.pack()


        self.text_box = tk.Text(self.text_frame, width=600, height=800)
        self.text_box.grid(row=0, column=0, padx=10, pady=5)
        self.text_box.insert(INSERT, self.soup)

        
        self.back_button = tk.Button(self.upper_frame, text="New Site", command = self.create_page)
        self.back_button.grid(row=1, column=0, padx=10, pady=5)
   
#the event variable must be there to have the esc key work in the window.
    def close_win(self, event=None):
        self.root.destroy()



#when program starts, run the following
if __name__ == '__main__':
    root = tk.Tk()
    new_win = Window(root)
    root.mainloop()
