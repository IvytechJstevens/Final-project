from breezypythongui import EasyFrame
  
class BookingSynthopath(EasyFrame):
 
        def __init__(self):
            EasyFrame.__init__(self, background = "gray", resizable = True)
            self.addLabel(text = "Booking Synthopath", row = 0, column = 0, background = "red")
            self.addLabel(text = "Book a show with DJ Synthopath by sending an email!", row = 1, column = 1, background = "gray")
            self.addTextArea(text = "", row = 2, column = 1)
            self.addButton(text = "Send", row = 3, column = 2)

BookingSynthopath().mainloop()