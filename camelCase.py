user = input("Type a sentence.") #asks for user sentence input

def camelCase(st):
    #for camelCase, makes sentence title, removes space, lowers first word
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]

print(camelCase(user))