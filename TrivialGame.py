
from tkinter import *
from tkinter import messagebox as mb
import pyodbc
guiWindow = Tk()
guiWindow.geometry("1400x850")
guiWindow.title("Trivail Quiz")
class Db:
    def final_resultF(self):
        link = pyodbc.connect \
            ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P10URGCA\MSSQLSERVER01;DATABASE=Northwind;"
             "Trusted_connection=yes")
        # print("Done......")
        cursor = link.cursor()
        cursor.execute("SELECT question FROM Quiz")
        ques = cursor.fetchall()
        final_result = [list(i) for i in ques]

        flat_list = [x for xs in final_result for x in xs]
        return flat_list


class Option:
    def option(self):
        link = pyodbc.connect \
            ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P10URGCA\MSSQLSERVER01;DATABASE=Northwind;"
             "Trusted_connection=yes")
        cursor = link.cursor()
        cursor.execute("SELECT opta FROM Quiz")
        opta = cursor.fetchall()
        final2_result = [list(i) for i in opta]
        flat_list1 = [x for xs in final2_result for x in xs]

        cursor.execute("SELECT optb FROM Quiz")
        optb = cursor.fetchall()
        final3_result = [list(i) for i in optb]
        flat_list2 = [x for xs in final3_result for x in xs]

        cursor.execute("SELECT optc FROM Quiz")
        optc = cursor.fetchall()
        final4_result = [list(i) for i in optc]
        flat_list3 = [x for xs in final4_result for x in xs]

        cursor.execute("SELECT optd FROM Quiz")
        optd = cursor.fetchall()
        final5_result = [list(i) for i in optd]
        flat_list4 = [x for xs in final5_result for x in xs]

        newEmagin = []
        newEmagin.append(flat_list1[0]), newEmagin.append(flat_list2[0]), newEmagin.append(flat_list3[0])
        newEmagin.append(flat_list4[0])
        newEmagin1 = []
        newEmagin1.append(flat_list1[1])
        newEmagin1.append(flat_list2[1])
        newEmagin1.append(flat_list3[1])
        newEmagin1.append(flat_list4[1])
        newEmagin2 = []
        newEmagin2.append(flat_list1[2])
        newEmagin2.append(flat_list2[2])
        newEmagin2.append(flat_list3[2])
        newEmagin2.append(flat_list4[2])
        newEmagin3 = []
        newEmagin3.append(flat_list1[3])
        newEmagin3.append(flat_list2[3])
        newEmagin3.append(flat_list3[3])
        newEmagin3.append(flat_list4[3])
        newEmagin3 = []
        newEmagin3.append(flat_list1[3])
        newEmagin3.append(flat_list2[3])
        newEmagin3.append(flat_list3[3])
        newEmagin3.append(flat_list4[3])
        newEmagin4 = []
        newEmagin4.append(flat_list1[4])
        newEmagin4.append(flat_list2[4])
        newEmagin4.append(flat_list3[4])
        newEmagin4.append(flat_list4[4])
        newEmagin5 = []
        newEmagin5.append(flat_list1[5])
        newEmagin5.append(flat_list2[5])
        newEmagin5.append(flat_list3[5])
        newEmagin5.append(flat_list4[5])

        all_list = []
        all_list.append(newEmagin), all_list.append(newEmagin1), all_list.append(newEmagin2), all_list.append(
            newEmagin3), all_list.append(
            newEmagin4), all_list.append(newEmagin5)

        return all_list


class Answer:
    def answer(self):
        link = pyodbc.connect \
            ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P10URGCA\MSSQLSERVER01;DATABASE=Northwind;"
             "Trusted_connection=yes")
        cursor = link.cursor()
        cursor.execute("SELECT answer FROM Quiz")
        ans = list(cursor.fetchall())
        final1_result = [list(i) for i in ans]
        flat_list0 = [x for xs in final1_result for x in xs]
        return flat_list0


class MyQuiz(Db, Option, Answer):

    def __init__(self):
        self.quesNumber = 0

        self.displayTitle()
        self.displayQuestion()

        self.optSelected = IntVar()

        self.options = self.radioButtons()

        self.displayOptions()

        self.buttons()
        self.dataSize = len(self.final_resultF())

        self.rightAnswer = 0

    def displayResult(self):
        wrongCount = self.dataSize - self.rightAnswer
        rightAnswer = f"Correct: {self.rightAnswer}"
        wrongAnswer = f"Wrong: {wrongCount}"

        the_score = int(self.rightAnswer / self.dataSize * 100)
        the_result = f"Score: {the_score}%"

        mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")

    def checkAnswer(self, quesNumber):
        self.final_resultF()

        self.answer()

        if self.optSelected.get() == self.answer()[quesNumber]:
            return True

    def nextButton(self):

        if self.checkAnswer(self.quesNumber):
            self.rightAnswer += 1

        self.quesNumber += 1

        if self.quesNumber == self.dataSize:

            self.displayResult()

            guiWindow.destroy()
        else:
            self.displayQuestion()
            self.displayOptions()

    def buttons(self):

        next_button = Button(
            guiWindow,
            text="Next",
            command=self.nextButton,
            width=10,
            bg="blue",
            fg="white",
            font=("ariel", 16, "bold")
        )

        next_button.place(x=350, y=380)

        quit_button = Button(
            guiWindow,
            text="Quit",
            command=guiWindow.destroy,
            width=5,
            bg="black",
            fg="white",
            font=("ariel", 16, " bold")
        )
        quit_button.place(x=700, y=50)

    def displayOptions(self):
        self.final_resultF()
        self.option()
        val = 0

        self.optSelected.set(0)

        for opt in self.option()[self.quesNumber]:
            self.options[val]['text'] = opt
            val += 1

    def displayQuestion(self):
        self.final_resultF()

        quesNumber = Label(
            guiWindow,
            text=self.final_resultF()[self.quesNumber],
            width=60,
            font=('ariel', 16, 'bold'),
            anchor='w',

        )

        quesNumber.place(x=70, y=100)

    def displayTitle(self):

        myTitle = Label(
            guiWindow,
            text="Trivial QUIZ",
            width=50,
            bg="blue",
            fg="white",
            font=("ariel", 19, "bold")
        )

        myTitle.place(x=0, y=2)

    def radioButtons(self):

        qList = []

        y_pos = 150

        while len(qList) < 4:
            radio_button = Radiobutton(
                guiWindow,
                text=" ",
                variable=self.optSelected,
                value=len(qList) + 1,
                font=("ariel", 14)
            )
            qList.append(radio_button)

            radio_button.place(x=100, y=y_pos)

            y_pos += 40

        return qList


quiz = MyQuiz()
guiWindow.mainloop()
