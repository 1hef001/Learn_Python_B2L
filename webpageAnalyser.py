import PySimpleGUI as s
import analyzerFns
import test_spell as p

s.ChangeLookAndFeel('BluePurple')
lst = []
lis = []
layout = [[s.Text("Enter URL"), s.InputText("", key = "url")],
          [s.Text('The number of unique words required:'),s.Slider(range=(1, 100), default_value=1,
                     orientation="horizontal", key="val")],
          [s.Multiline(key="data",size=(30, 10),disabled=True)],
          [s.Button("SUBMIT"), s.Exit()]]


window = s.Window('Web Page Analyser and spell checker', layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event is None or event == "Exit":
        break
    elif(event == "SUBMIT"):
        url = values["url"]
        text = analyzerFns.url(url)
        txt = "The web page consists of the following information: \n \n"
        sentences = str(analyzerFns.sentences(text))
        res = analyzerFns.dictionary(text)
        n = int(values["val"])
        print(n)
        txt += sentences + " sentences \n" + str(sum(res.values())) + " words \n"
        txt += str(len(res)) + " unique words \n \n"
        txt += "The top words are : \n"
        lst = analyzerFns.sortDictionary(res, n)
        for i in lst:
            txt += i + "\n"
        e,su = [], [] 
        t,e,su = p.spellCheck(txt)
        x = t + '\n\n' + str(len(e)) + ' spelling mistakes found\n'
        for i in range (len(e)):
            x= x + '\n\nErrors : '
            x = x + str(e[i]) + '\n'
            x = x + 'Suggestions : ' 
            for q in su[i]:
                x = x + q + ' '
        lis.append(x)
        print(lis)
        txt = txt + '\n'
        window.FindElement("data").Update(txt)
        window.FindElement("data").Update(" ".join(lis))
