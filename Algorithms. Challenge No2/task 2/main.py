def first(sentence):
    if input_word in s:
        count = sentence.count(input_word)
        return count
    else:
        return False

        
def second(sentence):
    sentence = sentence.split()
    if (input_word is item or input_word == item for item in sentence):
        count = sentence.count(input_word)
        return count


input_word = input('Input word: ')
input_file_path = input('Input file path: ')

try:
    with open(input_file_path, "r") as file:
        s = file.read()
        s = s.lower().replace(',', '').replace('.', '')

except:
    print("An exception occurred")
else:
    try:
        input_search_type = 0
        while input_search_type != '1' or input_search_type != '2':
            input_search_type = input('Input search type: ')
            if input_search_type == '1':
                print(first(s))
                break
            elif input_search_type == '2':
                print(second(s))
                break
            
    except: ("Wrong")


    




    
