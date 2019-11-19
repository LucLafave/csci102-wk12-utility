#https://github.com/LucLafave/csci102-wk12-utility
#Luc Lafave
#​CSCI 102 – Section C
#Week 11 - Part B

def PrintOutput(input_string):
    print('OUTPUT %s' % (input_string))
def LoadFile(file_name):
    with open(file_name) as file_in:
        file_list = file_in.readlines()
        for i in range(len(file_list)):
            if i == (len(file_list) - 1):
                file_list[i] = file_list[i][0:len(file_list[i])]
            else:
                file_list[i] = file_list[i][0:len(file_list[i])-1]
        return file_list
def UpdateString(change_str,character,location):
    change_list = []
    for i in range(len(change_str)):
        change_list.append(change_str[i:i+1])
    change_list[location] = character
    string_output = ''.join(change_list)
    PrintOutput(string_output)
def FindWordCount(list_find,string_find):
    count = 0
    for i in range(len(list_find)):
        count += list_find[i].count(string_find)
    return count
def ScoreFinder(players_list,scores_list,find_player):
    score = 0
    Is_in = False
    for i in range(len(players_list)):
        if players_list[i].lower() == find_player.lower():
            Is_in = True
            break
    if Is_in:
        PrintOutput("%s got a score of %d" % (players_list[i],scores_list[i]))
    else:
        PrintOutput("player not found")
def Union(list1,list2):
    return list1+list2
def Intersection(list1, list2):
    out_list=[]
    for i in range(len(list1)):
        for z in range(len(list2)):
            if list1[i].lower() == list2[z].lower():
                out_list.append(list1[i])
    return out_list
def NotIn(list1,list2):
    out_list =[]
    for i in range(len(list1)):
        if list1[i] in list2:
            continue
        else:
            out_list.append(list1[i])
    return out_list
            
