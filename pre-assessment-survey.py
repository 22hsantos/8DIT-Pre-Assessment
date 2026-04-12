
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

        #frame1 will be used for 'Collecting Person Data'
        #'Collecting Person Data' label will added, with 'Show All' button to the right
        frame1 = Frame(
            parent, 
            bg="pink"
            )
        frame1.grid(row=0, column=0, sticky=NSEW)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(1, weight=1)


        #Collecting Person Data label
        lbl_person_data =Label(
            frame1,
            text="Collecting Person Data",
            bg="pink"
        )
        lbl_person_data.grid(row=0,column=0)

        #Show All button
        btn_person_data = Button(
            frame1,
            text="Show All",
            bg="lightgrey",
            padx=10,
            pady=5
        )
        btn_person_data.grid(row=0, column=1)


        """
        planned layout for frame2:
        +------------------------------------------------------+
        |  First name:              |  Entry  |                |
        |  Age:                     |  Entry  |                |
        | Do you have a mobile phone? o                        |
        |                             o                        |
        |           [Enter Data]                               |
        |                                                      |
        +------------------------------------------------------+
        """
        frame2 = Frame(parent,bg="lightblue")
        frame2.grid(row=1, column=0, sticky=NSEW)

        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)

        lbl_first_name = Label(
            frame2,
            text="First name:",
            bg="lightblue",
            padx=20,
        )
        lbl_first_name.grid(row=0, column=0, sticky=W)
        # make an entry for the first name

        lbl_age = Label(
            frame2,
            text="Age:",
            bg="lightblue",
            padx=20,
        )
        lbl_age.grid(row=1, column=0, sticky=W)
        # make an entry for the age

        lbl_mobile_phone = Label(
            frame2,
            text="Do you have a mobile phone?",
            bg="lightblue",
            padx=20,
        )
        lbl_mobile_phone.grid(row=2, column=0, sticky=W)
        # make two radio buttons (Yes/No) for the mobile phone question

        btn_enter_data = Button(
            frame2,
            text="Enter Data",
            bg="lightgrey",
            padx=10,
            pady=5
        )
        btn_enter_data.grid(row=3, column=0)

if __name__ == "__main__":
    root = Tk()
    root.title("Pre-assessment survey")
    root.geometry("400x400")
    main = SurveyGUI(root)
    root.mainloop()