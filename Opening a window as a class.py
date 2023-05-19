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

        #setting python image
        self.image = Image.open('python.png')
        self.image = self.image.resize((300, 300))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label= tk.Label(self.root, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

         #creates an input field
        self.entry = tk.Entry(self.root, width=50)
        self.entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

         #creates a button
        self.submit_button = tk.Button(self.root, text="Site to Scrape", command = self.submit_action)
        self.submit_button.place(relx=0.5, rely=0.43, anchor=tk.CENTER)

        #message label
        self.message_label = tk.Label(self.root, text="")
        self.message_label.place(relx=0.5, rely=0.46, anchor=tk.CENTER)

        #text box, start invisible
        self.text_box = tk.Text(root)


    def submit_action(self):
        input_text = self.entry.get()
        url = input_text
        http_response = requests.get(url)

        if http_response.status_code == 200:
            html_content = http_response.text
            soup = BeautifulSoup(html_content, 'lxml')
            self.text_box.insert(INSERT, soup)

            display_text = "Scraping successful!"
            self.message_label.config(text=display_text)
            self.root.after(1500, self.transition_text) #adds a delay to the execution in milliseconds

        
        else:
            display_text =  f'failed to connect, Error Code:{http_response.status_code}'
            #uses the .config to change the text of the message_label
            self.message_label.config(text=display_text)

    def transition_text(self):
        #get rid of current elements
        self.image_label.place_forget()
        self.entry.place_forget()
        self.submit_button.place_forget()
        self.message_label.place_forget()

        self.text_frame = Frame(root, width=900, height=1200, bg="black")
        self.text_box.grid(row=0, column=0, padx=10, pady=5)


    
#the event variable must be there to have the esc key work in the window.
    def close_win(self, event=None):
        self.root.destroy()



#when program starts, run the following
if __name__ == '__main__':
    root = tk.Tk()
    new_win = Window(root)
    root.mainloop()
