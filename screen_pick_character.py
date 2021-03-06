import tkinter

class Screen_character_selector (tkinter.Frame):
    def __init__ (self, master, char_list, call_on_selected):
        super(Screen_character_selector, self).__init__(master)
        
        # Save the list of characters 
        self.char_list = char_list
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_selected
        
        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        
        The radio buttons on this page must use the variable "self.character".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character has been instantiated for your convenience below.
        
        Here is sample code for including an image on a page:   (char is a Character object)
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall

            w.grid (ADD PARAMETERS HERE) hi
        '''


        self.font = ("Apple Chancery", 18)

        tkinter.Label(self, text="Ability", font=self.font).grid(row=1, column=0, sticky=tkinter.W)
        tkinter.Label(self, text = "Hit Points", font=self.font).grid(row = 2, column = 0, sticky = tkinter.W)
        tkinter.Label(self, text="Dexterity", font=self.font).grid(row = 3, column = 0, sticky = tkinter.W)
        tkinter.Label(self, text="Strength",font=self.font).grid(row = 4, column = 0, sticky = tkinter.W)


        self.character = tkinter.StringVar()
        self.character.set(None)

        column = 1
        value = 0
        otherthing = 0
        anotherthing = 1
        for c in self.char_list.character_list:
            tkinter.Radiobutton(self, text = c.name, variable=self.character, value=value, font=self.font).grid(row = 0, column = otherthing, sticky = tkinter.E)
            imageSmall = tkinter.PhotoImage(file="images/"+ c.small_image)
            w = tkinter.Label(self, image=imageSmall,)
            w.photo = imageSmall
            w.grid(row = 0, column = anotherthing, sticky = tkinter.W)
            tkinter.Label(self, text=c.ability, font=self.font).grid(row=1, column=anotherthing)
            tkinter.Label(self, text = c.hit_points, font=self.font).grid(row = 2, column = anotherthing)
            tkinter.Label(self, text = c.dexterity,font=self.font).grid(row = 3, column = anotherthing)
            tkinter.Label(self, text = c.strength, font=self.font).grid(row = 4, column = anotherthing)

            column += 1
            value += 1
            otherthing +=2
            anotherthing +=2
        tkinter.Button(self, text = "Continue to Battle!", command = self.continue_clicked, fg = "red", bg = "black").grid(row = 7, column = 9)
 
    def continue_clicked(self):
        ''' This method is called when the Next button is clicked. 
            Notice that it passes self.character back to the callback method. '''         
        self.call_on_selected(self.character.get())
            
        