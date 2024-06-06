# "variant15.xml"
def findersomeone(fil):
    with open(fil, "r", encoding="utf-8") as file:
        data = file.readlines()
    out = ""
    suspect = "0"
    for i in data:
        # print(i)
        if i.find("<w:spacing") != -1:
            suspect = "1"

        mem = i.find("</w:t>")
        if mem != -1:
            kek = i.find(">")
            out = out + suspect * len(i[kek + 1:mem])
            # out + i[kek+1:mem]
            # print(suspect)
            suspect = "0"
        if i.find("</w:r>") != -1:
            suspect = "0"

    return out


def atomikos(fil):
    with open(fil, "r", encoding="utf-8") as file:
        data = file.readlines()
    out = ""
    suspect = "0"
    for i in data:
        # print(i)
        if i.find("<w:w w:val") != -1:
            suspect = "1"

        temp = i.find("</w:t>")
        if temp != -1:
            tempcount = i.find(">")
            out = out + suspect * len(i[tempcount + 1:temp])  # out + i[tempcount+1:temp]
            # print(suspect)
            suspect = "0"
        if i.find("</w:r>") != -1:
            suspect = "0"
    return out


# somik("variant15.xml")
print(atomikos("variant15.xml"))
