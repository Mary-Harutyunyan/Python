#--------------------- dictionary ---------------------------
# ------------------- N1 ------------------------------------
# data = {'a': 77,'b': 124,'c': 59, 'd': 1,'e': -36}
# keys = sorted(data, key= data.get )
# print(data.values())

#------------------- N2 -------------------------------------
# data = {'a': 77,'b': 124,'c': 59, 'd': 1,'e': -36}
# data['f']= 47
# print(data)

#------------------- N3 --------------------------------------
# data = {'a': 77,'b': 124,'c': 59, 'd': 1,'e': -36}
# print(data.get('a', 'ka'))
# print(data.get( 'r', 'chka'))

#------------------- N4--------------------------------------
# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)

#------------------- N5---------------------------------------
# mydict = {'a':1,'b':2,'c':12}
# summ = 1 
# for i in mydict:
#     summ *= mydict[i]
#     print(summ)

# -------------------- N6 ------------------------------------
# d = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(d, key=d.get, reverse=True)[:3]
# test = {}
# for i in keys: 
#     test[i] = d[i]
# print(test)
#
#
#---------------------- Exercises----------------------------
#----------------------- N1-----------------------------------
# students = {
#   'Anna': 5,
#   'Varduhi': 3,
#   'Arman': 9,
#   'Artur': 1,
#   'Karen': 4,
#   'Artak': 2,
#   'Davit': 8,
#   'Meri': 7,
#   'Ani': 6,
#   'Arpine': 10,
# }
#---------------------- N2--------------------------
# x = 0
# sum = 0
# for i in students:
#     sum += students [i]
#     x += 1
#     average = (sum/x)
# print(average)
#--------------------- N4-----------------------------
# good = []
# for i in students:
#     if students[i] > 5:
#         good.append(i)
# print('good students : ', good)
#--------------------- N5--------------------------
# bad = []
# for i in students:
#     if students[i] <= 5:
#         bad.append(i)
# print('bad students: ', bad)
# --------------------- N7 ----------------------------

# s = 'a,7,b,3,c,9,d,1,a,8,e,36'
# s = s.split(',')
# data = {}
# for i in range(0, len(s) - 1, 2):
#     if s[i] in data:
#         data[s[i]] += int(s[i + 1])
#     else:
#         data[s[i]] = int(s[i + 1])
# print(data)

# ---------------------- N8 ---------------------------
# s = 'exercises'
# data = {}
# for i in s :
#     if i in data:
#         data[i] += 1
#     else:
#         data[i] = 1
# print(data)

# ----------------------- N9 ---------------------------------------------
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []
# for i in old_list:
#     if  i not  in new_list :
#         new_list.append(i)
# print (new_list)
        
