def convert(input_str):
    faces_str = input_str.replace(":)","🙂").replace(":(", "🙁")
    print(faces_str)

sentence = input("What is your string: ")
convert(sentence)