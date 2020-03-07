import PySimpleGUI as s
import todo_db as n

s.ChangeLookAndFeel('BluePurple')
n.createTable()
n.createUsers()
lis,completed = [],[]
llayout = [                         #login layout
        [s.Text("LOGIN",pad= ((200,100),(0,0)))],
        [s.Text('Username : '),s.InputText('',key = 'lusername')],
        [s.Text('Password : '),s.InputText('',key = 'lpassword',password_char = '*')],
        [s.Button('Login',pad = ((100,10),(0,0))),s.Text('Not a member?'),s.Button('Sign up')],
        [s.Exit()],
        [s.Text("", auto_size_text=False, key="tell")]

]
slayout = [                         #sign up layout  s- sign up
        [s.Text("SIGN UP",pad= ((200,100),(0,0)))],
        [s.Text("NAME : "),s.InputText('', key = 'sname',do_not_clear=False)],
        [s.Text('E-mail : '),s.InputText('',key = 'semail',do_not_clear=False)],
        [s.Text('Username : '),s.InputText('',key = 'susername',do_not_clear=False)],
        [s.Text('Password : '),s.InputText('',key = 'spassword',password_char = '*',do_not_clear=False)],
        [s.Button('Sign up'),s.Button('Back'),s.Exit()],
        [s.Text("", auto_size_text=False, key="tell")]

]

selayout = [                           #select layout se - select
        [s.Image(r'logo1.png', pad = ((90,0),(0,0)))],
        #[s.Text("OPTION WINDOW",pad = ((250,0),(0,0)))],
        [s.Button("ADD TASK", pad =((140,0),(0,10))),s.Button("EDIT STATUS", pad =((140,140),(0,10)))],
        [s.Button("VIEW MODE", pad = ((140,0),(0,10))),s.Button("EDIT TASK", pad =((128,140),(0,10)))],
        [s.Button("DELETE TASK",pad =((140,0),(0,10))),s.Button("DELETE COMPLETED",pad =((116,140),(0,10)))],
        [s.Button("LOG OUT"),s.Exit()]

]


alayout = [                             #add layout a - add task
    #[s.Text("TODO LIST ",pad= ((200,100),(0,0)))],
    [s.Text("New Entry : "),s.InputText("",key = "entry",do_not_clear=False)],
    [s.CalendarButton("Choose Date", target="dateDisp", key='date'),s.InputText("",key = "dateDisp", disabled=True ,do_not_clear=False)],
    [s.Slider(range=(5,1,-1),default_value=5,orientation="horizontal",key="priority")],
    [s.Button("ADD")],
    [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True)],
    [s.Button("PRIORITIZE"),s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]

dtlayout = [                            #delete layout dt - delete task
    [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True)],
    [s.Button("DELETE"),s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]

dclayout = [                            #delete completed  layout dc - delete completed
    [s.Listbox(values = completed,key = "complete",size=(40,6), enable_events=True)],
    [s.Button("DELETE"),s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]

eslayout = [        
    [s.Text("TODO LIST ",pad= ((150,100),(0,0)))],
    [s.Listbox(values = lis,key = "list",size=(40,6), enable_events=True)],
    [s.Button("MARK COMPLETED"),s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]

vtlayout = [
    [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True)],
    [s.Button("PRIORITIZE"),s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]

vclayout = [
    [s.Listbox(values=completed ,key = "complete",size=(40,6), enable_events=True)],
    [s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]

etlayout = [
    [s.Text("EDIT TASK ",pad= ((200,100),(0,0)))],[s.Text("New Entry : "),s.InputText("",key = "entry",do_not_clear=False)],
    [s.CalendarButton("Choose Date", target="dateDisp", key='date'),s.InputText("",key = "dateDisp", disabled=True ,do_not_clear=False)],
    [s.Slider(range=(5,1,-1),default_value=5,orientation="horizontal",key="priority")],
    [s.Button("EDIT")],
    [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True)],
    [s.Button("PRIORITIZE"),s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]

]
vslayout = [
    [s.Button("VIEW TASKS",pad = ((140,0),(0,0))),s.Button("VIEW COMPLETED",pad =((125,140),(0,0)))],
    [s.Button("BACK"),s.Exit()],
    [s.Text("", auto_size_text=False, key="tell")]
]

#swindow = s.Window("Sign Up", slayout)

def selectWindow(u):
    swindow = s.Window("SELECT PAGE", selayout).Finalize()
    sevent,sentries = swindow.Read()
    print(sevent,sentries)
    if(sevent == "ADD TASK"):
        swindow.Close()
        awindow = s.Window("ADD TODO", alayout).Finalize()
        i = 1
        while(True):
            if(i==1):
                lis = n.readIncomplete(u)
                i=2
            awindow.FindElement("list").Update(lis)
            aevent, aentries = awindow.Read()
            print(aevent, aentries)
            if (aevent == "ADD"):
                if(aentries["dateDisp"] == "" or aentries["entry"] == ""):
                    awindow.Element("tell").Update("Please provide data in all fields")
                    continue
                x = aentries["entry"]+" "+aentries["dateDisp"]+" "+str(int(aentries["priority"]))
                lis.append(x)
                awindow.FindElement("list").Update(lis)
                awindow.Element("tell").Update("item added")
                n.addEvent(lis,u)
            elif (aevent == "PRIORITIZE"):
                lis = n.prioritizeEvents(u)
                awindow.Element("list").Update(lis)
            elif (aevent == "BACK"):
                awindow.Close()
                selectWindow(u)
            elif (aevent == "Exit" or aevent == None):
                awindow.Close()
                print("exited")
                exit(1)
                
    elif (sevent == 'DELETE TASK'):
        swindow.Close()
        dtwindow = s.Window("Delete Task",dtlayout).Finalize()
        lis = n.readIncomplete(u)
        dtwindow.FindElement("list").Update(lis)
        while(True):
            devent,dentries = dtwindow.Read()
            lis = n.readIncomplete(u)
            dtwindow.Element("tell").Update('')
            if (devent == 'DELETE'): 
                if(lis == []):
                    dtwindow.Element("tell").Update("No Tasks assigned yet")
                    continue

                print("delete pass argument : ",''.join(dentries["list"]))
                lis.remove(''.join(dentries["list"]))
                dtwindow.FindElement("list").Update(lis)
                dtwindow.Element("tell").Update("item deleted")
                n.deleteEvent(''.join(dentries["list"]),u) #working

            elif (devent == 'BACK'):
                dtwindow.Close()
                selectWindow(u)

            elif (devent == 'Exit' or devent == None):
                dtwindow.Close()
                exit(1)

    elif (sevent == 'EDIT STATUS'):
        swindow.Close()
        eswindow = s.Window("Edit Status",eslayout).Finalize()
        lis = n.readIncomplete(u)
        eswindow.FindElement("list").Update(lis)
        while(True):
            esevent,esentries = eswindow.Read()
            lis = n.readIncomplete(u)
            completed = n.readCompleted(u)
            eswindow.Element('tell').Update('')
            if( esevent == "MARK COMPLETED"):
                if(lis == []):
                    eswindow.Element("tell").Update("No Tasks assigned yet")
                    continue
                lis.remove(''.join(esentries["list"]))
                completed.append(''.join(esentries["list"]))
                eswindow.FindElement("list").Update(lis)
                #dcwindow.FindElement("complete").Update(completed)
                eswindow.Element("tell").Update("item completed")
                n.completedEvent(''.join(esentries["list"]),u) #working
            elif ( esevent == "BACK"):
                eswindow.Close()
                selectWindow(u)
            elif ( esevent == "Exit" or esevent == None ):
                eswindow.Close()
                exit(1)

    elif (sevent == 'EDIT TASK'):
        swindow.Close()
        etwindow = s.Window("EDIT TASK", etlayout).Finalize()
        i = 1
        while(True):
            if(i==1):
                lis = n.readIncomplete(u)
                i=2
            etwindow.FindElement("list").Update(lis)
            etevent, etentries = etwindow.Read()
            print(etevent, etentries)
            if (etevent == "EDIT"):
                if(lis == []):
                    etwindow.Element("tell").Update("No Tasks assigned yet")
                    continue
                elif(etentries["dateDisp"] == "" or etentries["entry"] == ""):
                    etwindow.Element("tell").Update("Please provide data in all fields")
                    continue
                print("delete pass argument : ",''.join(etentries["list"]))
                lis.remove(''.join(etentries["list"]))
                etwindow.FindElement("list").Update(lis)
                n.deleteEvent(''.join(etentries["list"]),u)          #deletion part
                x = etentries["entry"]+" "+etentries["dateDisp"]+" "+str(int(etentries["priority"]))
                lis.append(x)
                etwindow.FindElement("list").Update(lis)
                etwindow.Element("tell").Update("item modified")
                n.addEvent(lis,u)                                   #addition part
            elif (etevent == "PRIORITIZE"):
                lis = n.prioritizeEvents(u)
                etwindow.Element("list").Update(lis)
            elif (etevent == "BACK"):
                etwindow.Close()
                selectWindow(u)
            elif (etevent == "Exit" or etevent == None):
                etwindow.Close()
                print("exited")
                exit(1)
    
    elif (sevent == 'VIEW MODE'):
        swindow.Close()
        while(True):
            vswindow = s.Window("View Mode",vslayout).Finalize()
            vevents,evntries =  vswindow.Read()
            if (vevents == 'VIEW TASKS'):
                i=1
                while(True):
                    vswindow.Close()
                    vtwindow = s.Window("View Tasks",vtlayout).Finalize()
                    if(i == 1):
                        lis = n.readIncomplete(u)
                        i = 2
                    vtwindow.FindElement("list").Update(lis)
                    vtevent,vtentries = vtwindow.Read()
                    #window = sg.Window('ToDo').Layout(layout).Finalize()
                    if(vtevent == "BACK"):
                        vtwindow.Close()
                        break
                    elif (vtevent == "PRIORITIZE"):
                        lis = n.prioritizeEvents(u)
                        vtwindow.Element("list").Update(lis)
                        vtwindow.Close()
                        continue
                    elif(vtevent == "Exit" or vtevent == None):
                        vtwindow.Close()
                        exit(1)
                    vtwindow.Close()
        
            elif (vevents == 'VIEW COMPLETED'):
                vswindow.Close()
                vcwindow = s.Window("View completed",vclayout).Finalize()
                i=1
                while(True):
                    if(i == 1):
                        completed = n.readCompleted(u)
                        i=2
                    vcwindow.FindElement("complete").Update(completed)
                    vcevent,vcentries = vcwindow.Read()
                    #window = sg.Window('ToDo').Layout(layout).Finalize()
                    if(vcevent == "BACK"):
                        vcwindow.Close()
                        break
                    elif(vcevent == "Exit" or vcevent == None):
                        vcwindow.Close()
                        exit(1)
                    vcwindow.Close()
            
            elif(vevents == 'BACK'):
                vswindow.Close()
                selectWindow(u)
            
            elif(vevents == 'Exit' or vevents == None):
                vswindow.Close()
                exit(1)

    elif (sevent == 'DELETE COMPLETED'):
        swindow.Close()
        dcwindow = s.Window("Delete Completed",dclayout).Finalize()
        completed = n.readCompleted(u)
        dcwindow.FindElement("complete").Update(completed)
        while(True):
            devent,dentries = dcwindow.Read()
            completed = n.readCompleted(u)
            dcwindow.Element("tell").Update('')
            if (devent == 'DELETE'): 
                if(completed == []):
                    dcwindow.Element("tell").Update("No Tasks assigned yet")
                    continue

                print("delete pass argument : ",''.join(dentries["complete"]))
                completed.remove(''.join(dentries["complete"]))
                dcwindow.FindElement("complete").Update(completed)
                dcwindow.Element("tell").Update("item deleted")
                n.deleteEvent(''.join(dentries["complete"]),u) #working

            elif (devent == 'BACK'):
                dcwindow.Close()
                selectWindow(u)

            elif (devent == 'Exit' or devent == None):
                dcwindow.Close()
                exit(1)
    
    elif (sevent == 'LOG OUT'):
        swindow.Close()
        login()

    elif (sevent == 'Exit' or sevent == None):
        print('exited')
        exit(1)


def login():
    while (True):
        #login
        lwindow = s.Window("LOGIN PAGE",llayout)
        levent,llogin = lwindow.Read()
        print(levent , llogin)
        if (levent == "Exit" or levent == None) :           # not needed  levent is None or
            lwindow.Close()
            exit(1)
        if(levent == "Login"):
            print(llogin["lusername"],llogin["lpassword"])
            t = llogin['lusername']
            res = n.searchUsers(llogin['lusername'],llogin['lpassword'])
            if(res == 0):
                s.Popup('Enter valid credentials')
                lwindow.Close()
                continue
            else:
                lwindow.Close()
                selectWindow(t)
                #swindow = s.Window("SIGN UP",slayout)
        elif(levent == "Sign up"):
            lwindow.Close()
            swindow = s.Window("SIGN UP",slayout)
            while(True):
                sevent,sentry = swindow.Read()
                print(sevent,sentry)
                x = ['@','.']
                if (sevent == "Exit" or sevent == None):
                    swindow.Close()
                    exit(1)

                elif sevent == "Back":
                    #goto login
                    swindow.Close()
                    #lwindow = s.Window("LOGIN PAGE",llayout)
                    login()
                else:
                    print(sentry)
                    #l = sentry.values()
                    l = list(sentry.values())
                    print(l)
                    if(x[0] in sentry['semail'] and x[1] in sentry['semail']):
                        n.addUser(l)
                        swindow.Close()
                        #lwindow = s.Window("LOGIN PAGE",llayout)
                        login()
                    else:
                        s.Popup('Enter Valid credentials')
                        continue

login()
