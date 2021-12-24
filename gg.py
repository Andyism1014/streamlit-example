def to_dic(x):
  dic={}
  for i in range(len(x)):
    if i in range(0,len(x),2):
      dic[x[i+1]]=x[i]
  print("=",dic)

to_dic(Transactions)