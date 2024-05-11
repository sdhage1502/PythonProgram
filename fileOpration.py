#file=open('Library.txt',"w+")
with open('Library1.txt',"w+")as file:
      BookTitle =input(" enter book title ")
      BookAuthor=input(" enter aurthr name ")
      file.writelines([f" book title name  {BookTitle}\nbook author name {BookAuthor}"])
