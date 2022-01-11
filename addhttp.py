with open('1.txt','r',encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        line = line.strip("\n")
        if line[0:5] == "https":
            l1 = line
            l1 =l1.strip()
            print(l1)
            with open('url2.txt','a') as a:
                a.write(l1+"\n")
        if line[0:5] != "https":
            l = 'http://' + line
            l =l.strip()
            print(l)
            with open('url2.txt','a') as a:
                a.write(l+"\n")
