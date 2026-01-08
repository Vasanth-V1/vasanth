n=int(input("Enter number of books: "))
books=[]
author=[]
for i in range(n):
    books.append(input("Enter book name: "))
    author.append(input("Enter Author name: "))
print("Book", '', 'Author')
for i in range(n):
    print(books[i]," ", authpr[i], end="\n") 