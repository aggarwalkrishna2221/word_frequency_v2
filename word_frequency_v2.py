print("Option 1:- Do you want to upload file whose word you wanna count \n")
print("Option 2:- Do you want to enter the line whose word you wanna count \n ")

option_input = int(input("Enter the option number:- (Like 1 or 2) "))
if option_input == 1:
    file_input = input("Enter the name of the file:- ")
    count = dict()
    lst = list()
    newlst = list()
    try:
        file_handle = open(file_input, "r")
    except:
        print("Enter a valid file name. ")
        exit()

    for lines in file_handle:
        words = lines.split()
        for word in words:
            count[word] = count.get(word, 0) + 1
    
    for key, val in count.items():
        newt = (val, key)
        if val == 1:
            newlst.append(newt)
        else:
            lst.append(newt)
        
    lst = sorted(lst, reverse=True)

    print("Option:-1 Print all the words ")
    print("Option:-2 Print Specific number of words ")
    option2_input = int(input("Enter option number:- (Like 1 or 2) "))
    if option2_input == 1:
        print("------Word Frequency------")
        print(file_input)
        i = 0
        for val, key in lst:
            print(str(i + 1) + "." + key + "-" + str(val))
            i += 1
        print("Number of words which appeared only once:- ", len(newlst))
        exit()

    else:
        number_input = int(input("How many words do you want:- "))
        print("------Word Frequency------")
        print(file_input)
        i = 0
        for val, key in lst[:number_input]:
            print(str(i+1) + ". " + key + "- "+ str(val))
            i += 1
        exit()

if option_input == 2:
    count2 = dict()
    lst2 = list()
    newlst2 = list()
    line = input("Enter the line for which you want the word frequency:- ")

    for words in line.split():
        count2[words] = count2.get(words, 0) + 1
    
    for key, val in count2.items():
        newt2 = (val,key)
        if val == 1:
            newlst2.append(newt2)
        else:
            lst2.append(newt2)
    
    lst2 = sorted(lst2, reverse=True)
    print("Option 1:- Print all the words")
    print("Option 2:- Print specific number of words ")
    option_input3 = int(input("Enter the option number:- (Like 1 or 2) :- "))
    if option_input3 == 1:
        print("-----Word Frequency----")
        j = 1
        for val, key in lst2:
            print(str(j) +"." + key + "- " + str(val))
            j+=1
        print("Number of words that occured only once:- ", len(newlst2))
        exit()
    
    else:
        num_input = int(input("How many words do you want:- "))
        print("----Word Frequency----")
        j = 1
        for val, key in lst2[:num_input]:
            print(str(j) + ". " + key + "- " + str(val))
            j+=1
        exit()

    


        

        

    
        
