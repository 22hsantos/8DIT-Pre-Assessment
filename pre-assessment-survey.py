
"""
-Make a GUI application which collects name, age and the answer to the survey question "Do you have a mobile phone?".

-When an Enter Data button is pressed, the information is collected from the GUI and used to construct an object for this person, stored in a list.

-When a Show All button is pressed, the data collection frame is removed and replaced by a frame in which each person's information is presented one by one using the Next/Previous buttons.

-An 'Add New Person' button will toggle the layout back to "data collection mode".
"""

from tkinter import *

class SurveyGUI:
    """
    GUI class for the survey interface.
    """
    def __init__(self, parent):
        """
        Initialises the GUI, contains two frames for collection and viewing.

        Args:
            parent: The root window of the GUI.
        """

        parent.grid_rowconfigure(0, weight=1)#configure the grid priority for frame1
        parent.grid_rowconfigure(1, weight=1)#configure the grid priority for frame2
        parent.grid_columnconfigure(0, weight=1)#configure the grid priority for column 0

        """
        Frame 4 will be used for displaying data. It is the bottom frame on the second screen.
        """
        #region for frame 4
        #frame 4 will contain name, age, and mobile phone information. and will have next adn previous buttons
        self.frame4 = Frame(parent,bg="lightgreen")
        frame4 = self.frame4
        self.frame4.grid(row=1, column=0, sticky=NSEW)

        #first name label output
        lbl_first_name2 = Label(
            frame4,
            text="First name:",
            bg="lightgreen",
            padx=20,
            pady=5
        )
        lbl_first_name2.grid(row=0, column=0, sticky=W)
        
        #placeholder label for name output
        entry_first_name = Label(frame4, text="John", bg="lightgreen")
        entry_first_name.grid(row=0, column=1, sticky=W)

        #age label output
        lbl_age2 = Label(
            frame4,
            text="Age:",
            bg="lightgreen",
            padx=20,
            pady=5
        )
        lbl_age2.grid(row=1, column=0, sticky=W)

        #placeholder label for age output
        entry_age = Label(frame4, text="25", bg="lightgreen")
        entry_age.grid(row=1, column=1, sticky=W)

        #mobile phone label output
        lbl_mobile_phone2 = Label(
            frame4,
            text="John has a mobile phone.",
            bg="lightgreen",
            padx=20,
            pady=5
        )
        lbl_mobile_phone2.grid(row=2, column=0, sticky=W)

        previous_button = Button(
            frame4,
            text="Previous",
            bg="lightgrey",
            padx=10,
            pady=5
        )
        previous_button.grid(row=3, column=0)

        next_button = Button(
            frame4,
            text="Next",
            bg="lightgrey",
            padx=10,
            pady=5
        )
        next_button.grid(row=3, column=1)
        #endregion for frame 4

        """
        Frame 2 will be used for data collection. It is the bottom frame on the first screen.
        It will collect name, age, and the answer to the survey question "Do you have a mobile phone?".
        This frame overlays frame 4.
        """
        #region for frame 2
        #Frame 2
        self.frame2 = Frame(parent,bg="lightblue")
        frame2 = self.frame2
        self.frame2.grid(row=1, column=0, sticky=NSEW)

        #first name label
        lbl_first_name = Label(
            frame2,
            text="First name:",
            bg="lightblue",
            padx=20,
            pady=5
        )
        lbl_first_name.grid(row=0, column=0, sticky=W)
        
        #entry field for first name
        entry_first_name = Entry(frame2)
        entry_first_name.grid(row=0, column=1, sticky=W)

        #age label
        lbl_age = Label(
            frame2,
            text="Age:",
            bg="lightblue",
            padx=20,
            pady=5
        )
        lbl_age.grid(row=1, column=0, sticky=W)

        #entry field for age
        entry_age = Entry(frame2)
        entry_age.grid(row=1, column=1, sticky=W)

        #mobile phone label
        lbl_mobile_phone = Label(
            frame2,
            text="Do you have a mobile phone?",
            bg="lightblue",
            padx=20,
            pady=5
        )
        lbl_mobile_phone.grid(row=2, column=0, sticky=W)

        self.phone_var = StringVar()
        self.phone_var.set("No") # default value
        rb_yes = Radiobutton(
            frame2,
            text="Yes",
            variable=self.phone_var,
            value="Yes",
            bg="lightblue"
        )
        rb_yes.grid(row=2, column=1, sticky=W)
        rb_no = Radiobutton(
            frame2,
            text="No",
            variable=self.phone_var,
            value="No",
            bg="lightblue"
        )
        rb_no.grid(row=2, column=1, sticky=E)

        btn_enter_data = Button(
            frame2,
            text="Enter Data",
            bg="lightgrey",
            padx=10,
            pady=5
        )
        btn_enter_data.grid(row=3, column=1)
        #endregion for frame 2
        
        """
        Frame 3 will be used for display person data and add new person button. It is the top frame on the second screen.
        """
        #region for frame 3
        #frame 3
        self.frame3 = Frame(
            parent, 
            bg="pink"
            )
        self.frame3.grid(row=0, column=0, sticky=NSEW)
        self.frame3.grid_rowconfigure(0, weight=1)
        self.frame3.grid_columnconfigure(0, weight=1)
        self.frame3.grid_columnconfigure(1, weight=1)
        frame3 = self.frame3

        #displaying person data label
        lbl_person_data =Label(
            frame3,
            text="Displaying person data",
            bg="pink"
        )
        lbl_person_data.grid(row=0,column=0)

        #Add New Person button
        btn_person_data = Button(
            frame3,
            text="Add New Person",
            bg="lightgrey",
            padx=10,
            pady=5
        )
        btn_person_data.grid(row=0, column=1)
        #endregion for frame 3
        
        """
        Frame 1 will be used for the title and show all button. It is the top frame on the first screen.
        Frame one overlays frame 3.
        """
        #region for frame 1
        #frame 1
        self.frame1 = Frame(
            parent, 
            bg="#FFFA9E"
            )
        frame1 = self.frame1
        self.frame1.grid(row=0, column=0, sticky=NSEW)
        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(1, weight=1)

        #Collecting Person Data label
        lbl_person_data =Label(
            frame1,
            text="Collecting Person Data",
            bg="#FFFA9E"
        )
        lbl_person_data.grid(row=0,column=0)

        #Show All button
        btn_person_data = Button(
            frame1,
            text="Show All",
            bg="lightgrey",
            padx=10,
            pady=5,
            command=self.switch_to_display
        )
        btn_person_data.grid(row=0, column=1)
        #endregion for frame 1

    #when the show all button is pressed, frames 1 and 2 will be removed and frames 3 and 4 will be displayed, showing results
    def switch_to_display(self):
        self.frame1.grid_remove()
        self.frame2.grid_remove()
        self.frame3.grid()
        self.frame4.grid()

if __name__ == "__main__":
    root = Tk()
    root.title("Pre-assessment survey: Gather information")
    root.geometry("400x400")
    main = SurveyGUI(root)
    root.mainloop()