import PySimpleGUI as s
import analyzerFns

lst = []
layout = [[s.Text("Enter URL"), s.InputText("", key = "url")],
          [s.Slider(range=(1, 100), default_value=1,
                     orientation="horizontal", key="val")],
          [s.Multiline(key="data",size=(30, 10),disabled=True)],
          [s.Button("GET"), s.Exit()]]


window = s.Window('Web Page Analyser', layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event is None or event == "Exit":
        break
    elif(event == "GET"):
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
        window.FindElement("data").Update(txt)
