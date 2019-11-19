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
            file_list[i] = file_list[i][0:len(file_list[i])-1]
        return file_list
def UpdateString(change_str,character,location):
    change_list = []
    for i in range(len(change_str)):
        change_list.append(change_str[i:i+1])
    change_list[location] = character
    string_output = ''.join(change_list)
    PrintOutput(string_output)
