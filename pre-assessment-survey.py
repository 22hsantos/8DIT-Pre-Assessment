"""
-Make a GUI application which collects name, age and the answer to the survey question "Do you have a mobile phone?".

-When an Enter Data button is pressed, the information is collected from the GUI and used to construct an object for this person, stored in a list.

-When a Show All button is pressed, the data collection frame is removed and replaced by a frame in which each person's information is presented one by one using the Next/Previous buttons.

-An 'Add New Person' button will toggle the layout back to "data collection mode".
"""

"""
-Make a GUI application which collects name, age and the answer to the survey question "Do you have a mobile phone?".

-When an Enter Data button is pressed, the information is collected from the GUI and used to construct an object for this person, stored in a list.

-When a Show All button is pressed, the data collection frame is removed and replaced by a frame in which each person's information is presented one by one using the Next/Previous buttons.

-An 'Add New Person' button will toggle the layout back to "data collection mode".
"""

from tkinter import *

class SurveyGUI:
    def __init__(self, parent):

        frame1 = Frame(parent, bg="pink")
        frame1.pack(side=TOP, expand=True, fill=BOTH)

        label1 = Label(
            frame1,
            text = "Frame 1",
            bg='pink',
            width=10,
        )  
        label1.pack(expand=True, fill=BOTH)

        frame2 = Frame(parent)
        frame2.pack(side=BOTTOM)

if __name__ == "__main__":
    root = Tk()
    root.title("Pre-assessment survey")
    root.geometry("400x400")
    main = SurveyGUI(root)
    root.mainloop()