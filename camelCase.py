user = raw_input("Type a sentence.")

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]

print(camelCase(user))