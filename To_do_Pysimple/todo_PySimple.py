import PySimpleGUI as s
import fileModule


lis = []
completed = []
lis = fileModule.readFile()
completed = fileModule.readCompleted()
layout = [
            [s.Text("TODO LIST ")],[s.Text("New Entry : "),s.InputText("",key = "entry")],[s.Text("TODO"),s.Text("COMPLETED")],
            [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True), s.Listbox(values=completed,key = "complete",size=(40,6), enable_events=True)],
            [s.CalendarButton("Choose Date", target="dateDisp", key='date'),s.InputText("",key = "dateDisp", disabled=True ,do_not_clear=False)],
            [s.Text("Priority meter : "),s.Slider(range=(5,1,-1),default_value=5,orientation="horizontal",key="priority")],
            [s.Button("add"),s.Button("delete"),s.Button("prioritize"),s.Button("completed")],[s.Exit()],
            [s.Text("", auto_size_text=False, key="tell")]
            
         ]

window = s.Window("my first GUI ", layout)

while True:
    event, entries = window.Read()
    print(event, entries)
    if event is None or event == "Exit":
        break

    elif (event == "add"):
        if(entries["dateDisp"] == ""):
            window.Element("tell").Update("Please input a date")
            continue

        x = entries["entry"]+" "+entries["dateDisp"]+" "+str(int(entries["priority"]))
        lis.append(x)
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item added")
        fileModule.writeToFile(lis) #working

    elif( event == "delete"):
        lis.remove(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item deleted")
        fileModule.writeToFile(lis) #working

    elif( event == "prioritize"):
        for i in range(len(lis)):
            min = i
            for j in range(i+1, len(lis)):
                if(lis[min][-1] > lis[j][-1]):
                    min = j
            lis[i],lis[min] = lis[min],lis[i]
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("prioritized")
        fileModule.writeToFile(lis) #working

    elif( event == "completed"):
        lis.remove(''.join(entries["list"]))
        completed.append(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.FindElement("complete").Update(completed)
        window.Element("tell").Update("item completed")
        fileModule.writeToCompleted(completed) #working



window.Close()
