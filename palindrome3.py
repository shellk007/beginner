print ('*****************')
print ('**HELLO THERE!***')
print ('*****************')
print ('\nWelcome the the Python Palindrome Prober!\n')

def palindrome():

    print ('''Please enter the word you would like to check
                              for example: racecar''')
  
    prompt = '>'
  
    word = raw_input(prompt)
  
    if word == word[::-1]:
        print ('Yes, your word is a palindrome!')
    else:
        print ("Sorry this word isn't a palindrome :(")
  
    while(1):  
        re_play = raw_input("Want to play again (y/n)? ")
        if re_play.lower() == "y" or re_play.lower() == "n":
            break
        else:
            print "Wrong Choice!!! Please enter y/n"
    if re_play.lower() == "y":
        palindrome()
    else:
        print ('\nHave a nice day!')
  
palindrome()   
