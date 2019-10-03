import json
import sys

def ParseInFile(filepath) :
    count = len(open(filepath).readlines(  ))

    fp = open(filepath , "r")
    writep = open("My.json" , "w")
    line = fp.readline()

    writep.write("[")
    line = line.rstrip()
    line += ',\n'
    writep.write(line)
    for i in range(count - 2) :
        line = fp.readline()
        line = line.rstrip()
        line += ',\n'
        writep.write(line)
    # last line
    lastline = fp.readline()
    lastline = lastline.rstrip()
    writep.write(lastline)
    writep.write("]")

    print(count)
    writep.close()
    fp.close()

def CountLang(lang, count_lang, string) :
    data_keys = string.keys()
    keys_list = list(data_keys)
    if 'lang' in keys_list :
        current_lang = string['lang']
        if current_lang in lang :
            current_index = lang.index(current_lang)
            count_lang[current_index] += 1
        else :
            lang.append(current_lang)
            count_lang.append(1)
    
    for i in range(len(keys_list)) :
        current_element = string[keys_list[i]]
        if current_element == None :
            continue
        if keys_list[i] == 'user' :
            continue
        if type(current_element) is dict :
            CountLang(lang, count_lang , current_element)
        
def ParseJson(filepath) :
    json_file = open(filepath)
    data = json.load(json_file)
    # Сколько твитов в наборе?
    number_twit = len(data)
    print('[ 1 ] КОЛИЧЕСТВО ТВИТОВ : ' + str(number_twit))
    # Какой процент твитов составляют удаленные записи? (помеченные как deleted)
    number_delete = 1
    for i in range(number_twit) :
        data_keys = data[i].keys()
        keys_list = list(data_keys)
        if 'delete' in keys_list :
            number_delete += 1
    print('[ 2 ] КОЛИЧЕСТВО УДАЛЕННЫХ ТВИТОВ : ' + str(number_delete))
    # Какие самые популярные языки твитов?
    lang = []
    count_lang = []
    for i in range(number_twit) :
        CountLang(lang, count_lang, data[i])
    print('[ 3 ] САМЫЕ ПОПУЛЯРНЫЕ ЯЗЫКИ \n')
    cum = 0
    for i in range(len(lang)) :
        print('[ ' + lang[i] + ' ] : ' + str(count_lang[i]))
        cum += count_lang[i]
    # print('[ + ] ВСЕГО ЯЗЫКОВ : ' + str(cum))

    # Есть ли твиты от одного и того же пользователя? Если да, то сколько таких пользователей?
    users = []
    count_twit = []
    for i in range(number_twit) :
        data_keys = data[i].keys()
        keys_list = list(data_keys)
        if 'user' in keys_list :
            current_user = data[i]['user']
            if 'id' in current_user :
                current_id = current_user['id']
                if current_id in users :
                    current_index = users.index(current_id)
                    count_twit[current_index] += 1
                else :
                    users.append(current_id)
                    count_twit.append(1)
    answer = 0
    for i in range(len(users)) :
        if count_twit[i] > 1 :
            answer += 1
    print('\n\n[ 4 ] ВСЕГО ПОЛЬЗОВАТЕЛЕЙ С БОЛЬШЕ ЧЕМ ОДНИМ ТВИТОМ : ' , answer)



def main():
    if len(sys.argv) < 3 :
        print("[ - ] Error then start program ! ")
        return
    
    if sys.argv[1] == 'parsefile' :
        ParseInFile(sys.argv[2])
    elif sys.argv[1] == 'parsejson' :
        ParseJson(sys.argv[2])
    else : 
        print("[ - ] Error then start program ! ")


if __name__ == "__main__":
    main()