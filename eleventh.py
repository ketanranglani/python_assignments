
def unique(A):
   # intilize a null list
   uniquevalues = []

   # traversing the list
   for i in A:
   # check unique valueis present or not
    if i not in uniquevalues:
      uniquevalues.append(i)
      # print (A)
      for i in uniquevalues:
        print(i),

      # Driver code
      A=list()
      n=int(input("Enter the size of the List ::"))
      print("Enter the Element of List ::")
      for i in range(int(n)):
        k=int(input(""))
        A.append(k)

print("The unique values from the List is ::>")
unique(A)