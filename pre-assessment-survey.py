
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
            width=200,
            height=200,
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

        #frame2 will be used for user input
        #'Name' and 'Age' labels will be added, with entry boxes to the right
        #'Do you have a mobile phone?' label will be added underneath, with 'Yes' and 'No' radio buttons to the right
        #'Enter Data' button will sit at the bottom of frame2
        frame2 = Frame(parent)
        frame2.grid(row=1, column=0, sticky=NSEW)

        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)

        label2 = Label(
            frame2,
            text="Frame 2",
            bg="lightblue"
        )
        label2.grid(row=0, column=0, sticky=NSEW)


if __name__ == "__main__":
    root = Tk()
    root.title("Pre-assessment survey")
    root.geometry("400x400")
    main = SurveyGUI(root)
    root.mainloop()