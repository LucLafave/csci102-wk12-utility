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
