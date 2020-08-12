
f = open('text.txt', mode ='r', encoding = 'UTF-8')
names = f.read().replace('"', '').replace(",", ' ')
names = names.lower()
listOfNames = names.split(' ')
listOfNames.sort()# aaron ...
listofNumbers = []
listCortej = [('a', 1), ('b',2), ('c',3), ('d',4), ('e',5), ('f',6), ('g', 7), ('h', 8), ('i', 9), ('j',10), ('k',11), ('l',12), ('m',13),
                ('n',14), ('o',15), ('p',16), ('q',17), ('r', 18), ('s', 19), ('t',20), ('u',21), ('v',22), ('w',23), ('x',24), ('y',25), ('z',26)]
intNum = 0
for i in listOfNames: # находим имя в списке
    for j in i: # находим букву в имени (слове)
        for k in listCortej:
            if j == k[0]:
                intNum += k[1]
    listofNumbers.append(intNum)
    intNum = 0

finalList = [] # новый лист
for i in range(len(listofNumbers)):
    sum = listofNumbers[i] * (i+1)
    finalList.append(sum)
    sum = 0

del listOfNames, listofNumbers, listCortej, names # удалены за ненадобностью

finalsum = 0 # финальная сумма всех чисел из finalList
for i in finalList:
    finalsum += i
print(finalsum)
