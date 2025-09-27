try: 
    result = 10/0
except ZeroDivisionError:
    print ("see on ei okei nii kurat")

    text = ("SEE ON EI NUMBRID")

 #example 2
    try:
        text_to_int = int(text)
    except Exception as e:
        print ("an error happend ", e)

     # example 3

try: 
    result = 10/2
except ZeroDivisionError:
    print ("see on ei okei numbrid")
else:
    text = ("SEE ON EI NUMBRID")

    print (result)

