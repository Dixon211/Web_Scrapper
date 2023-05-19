from bs4 import BeautifulSoup
import requests
import tkinter as tk
from PIL import ImageTk, Image

class Window:
    def __init__(self, root):
        self.root = root
        root.geometry("500x300") #measured in pixels
        root.attributes('-fullscreen', True)
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

    def submit_action(self):
        input_text = self.entry.get()
        url = input_text
        http_response = requests.get(url)

        if http_response.status_code == 200:
            html_content = http_response.text

            #With this we have written to the webpage_testing.html all the html code for the site and now we can work on it locally to avoid overscraping
            with open('Scraped_site.html', 'r+', encoding='utf-8') as local_file:
                local_file.write(html_content)
                local_file.seek(0) # moves the pointer to the beginning
                content = local_file.read()
                soup = BeautifulSoup(content, 'lxml')
                display_text = "Scraping successful!"
                self.message_label.config(text=display_text)
        

        else:
            display_text =  f'failed to connect, Error Code:{http_response.status_code}'
            #uses the .config to change the text of the message_label
            self.message_label.config(text=display_text)



    
#the event variable must be there to have the esc key work in the window.
    def close_win(self, event=None):
        self.root.destroy()



#when program starts, run the following
if __name__ == '__main__':
    root = tk.Tk()
    new_win = Window(root)
    root.mainloop()
