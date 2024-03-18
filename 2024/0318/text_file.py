# f = open("text.txt")
# print(f.read())

# letter = open("letter.txt", "w")
# letter.write("Dear Father,")
# letter.close()

letter = open("txt_file/letter.txt", "a+")
letter.write("\n\nHow are you?")
letter.close()
