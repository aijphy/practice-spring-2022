#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt","r") as name_file:
    name_list = name_file.read().split("\n")
#    print(name_list)


with open("Input/Letters/starting_letter.txt","r") as input_file:
    str = input_file.read()
    for name in name_list:
        new_filename = "Output/ReadyToSend/letter_for_" + name.replace(" ","_") + ".txt"
        with open(new_filename,"w") as output_file:
            new_email = str.replace('[name]',name)
            output_file.write(new_email)

