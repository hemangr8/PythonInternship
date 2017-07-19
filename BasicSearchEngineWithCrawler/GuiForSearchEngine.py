from tkinter import *
from SearchEngine import *


class SearchEngineUI:

    @staticmethod
    def bind_results(text_results, entry_keyword):
        count = 1
        text_results.delete('1.0', END)
        results = SearchEngine.search(entry_keyword.get())
        for result in results:
            if results[result] is not None:
                text = "Result {} \n\nTitle :  {}\n\nLink  :  {}\n--------------------------------------------------------------------------------\n".format(count, str(results[result]), str(result))
            else:
                text = "Result {} \n\nTitle :  {}\n\nLink  :  {}\n--------------------------------------------------------------------------------\n".format(count, entry_keyword.get(), str(result))
            text_results.insert(END, text)
            text_results.see(END)
            count += 1

    @staticmethod
    def callback(text_results, entry_keyword):
        return lambda: SearchEngineUI.bind_results(text_results, entry_keyword)

    def __init__(self, master):
        text_results = Text(master)
        text_results.grid(row=2)
        text_results.insert(END, "Results will be displayed here")
        entry_keyword = Entry(master)
        entry_keyword.grid(row=0)
        label = Label(master, text="Enter keyword here:")
        label.grid(row=0, column=0, sticky=W)
        button_search = Button(master, text="Search", command=SearchEngineUI.callback(text_results, entry_keyword))
        button_search.grid(row=0, sticky=E)
        Button(master, text="Exit", command=root.destroy).grid(row=3)


root = Tk()
root.title("Search Engine")
SearchEngineUI(root)
root.mainloop()
