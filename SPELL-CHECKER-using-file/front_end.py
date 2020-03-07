import PySimpleGUI as s
import test_spell as p

s.ChangeLookAndFeel('BluePurple')

layout = [                             #add layout a - add task
    #[t.Text("TODO LIST ",pad= ((200,100),(0,0)))],
    [s.Text("Enter the file to be checked : "),s.InputText("",key = "entry",do_not_clear=True)], #(path if necessary) 
    [s.Button("CHECK")],
    [s.Multiline(size=(70,20),disabled=True,key = 'list')],
    [s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]
lis = []

def spell():
    window = s.Window("SPELL CHECKER", layout).Finalize()
    while(True):
        aevent, aentries = window.Read()
        print(aevent, aentries)
        if (aevent == "CHECK"):
            if(aentries["entry"] == ""):
                window.Element("tell").Update("Please provide data in all fields")
                continue
            e,su = [], [] 
            t,e,su = p.spellCheck(aentries['entry'])
            x = t + '\n\n' + str(len(e)) + ' spelling mistakes found\n'
            for i in range (len(e)):
                x= x + '\n\nErrors : '
                x = x + str(e[i]) + '\n'
                x = x + 'Suggestions : ' 
                for q in su[i]:
                    x = x + q + ' '
            lis.append(x)
            print(lis)
            window.FindElement("list").Update(" ".join(lis))
            

        elif (aevent == "Exit" or aevent == None):
            window.Close()
            print("exited")
            exit(1)

spell()