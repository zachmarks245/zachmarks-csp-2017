def mad_libs():
    array = [] #this will store the list of word the player gives
    print("We are going to play a game of Christmas Mad Libs!")
    #1st word
    category = raw_input("First I need you to give me a plural noun: ")
    print(category)
    array.append(category)
    #2nd word
    category = raw_input("Now I need the name of a person: ")
    print(category)
    array.append(category)
    #3rd word
    category = raw_input("Now give me a verb: ")
    print(category)
    array.append(category)
    #4th word
    category = raw_input("Now give me a plural noun: ")
    print(category)
    array.append(category)
    #5th word
    category = raw_input("Now give me a holiday: ")
    print(category)
    array.append(category)
    #6th word
    category = raw_input("Now give me a color: ")
    print(category)
    array.append(category)
    #7th word
    category = raw_input("Now give me an adjective: ")
    print(category)
    array.append(category)
    #8th word
    category = raw_input("Now give me a color: ")
    print(category)
    array.append(category)
    #9th word
    category = raw_input("Now give me an adjective: ")
    print(category)
    array.append(category)
    #10th word
    category = raw_input("Now give me a verb ending in ed: ")
    print(category)
    array.append(category)
    #11th word
    category = raw_input("Now give me a vegetable: ")
    print(category)
    array.append(category)
    #12th word
    category = raw_input("Now give me a verb ending in ed: ")
    print(category)
    array.append(category)
    #13th word
    category = raw_input("Now give me the name of a person: ")
    print(category)
    array.append(category)
    #14th word
    category = raw_input("Now give me a verb: ")
    print(category)
    array.append(category)
    #15th word
    category = raw_input("Now give me a verb: ")
    print(category)
    array.append(category)
    #16th word
    category = raw_input("Now give me a color: ")
    print(category)
    array.append(category)
    
    #print the story
    print("Ok, here is the story you helped write")
    print("Did you ever have one of those "+array[0]+"?")
    print("Well today "+array[1]+" did! Mom wanted to")
    print(array[2]+" "+array[3]+" up for "+array[4]+". Not")
    print("just any lights, "+array[5]+" lights. "+array[6])
    print(array[7]+" lights! "+array[8]+" bright red lights.")
    print("The only problem, they are a "+array[9]+" mess!")
    print("Not to mention that there are some "+array[10])
    print("yellow and green lights "+array[11]+" in.")
    print("''"+array[12]+"!'' I yell! This can't be done!")
    print("She could "+array[13]+" I was right and went out and")
    print(array[14]+" some new shiny "+array[15]+" lights!")
    
    