import sys

sys.path.append("C://Users//Mykhailo//Desktop//Python//BeetRoot-education//lesson_8//homework")

def creating_of_file(name):
    with open(name, "w") as file:
        file.write("Hello Hello Hello\n")
        file.write("Hello\n")


def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
    return len(lines)


def count_chars(name):
    with open(name, 'r') as file:
        content = file.read()
    return len(content)


def test(name):
    creating_of_file(name)
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Number of lines: {lines}")
    print(f"Number of characters: {chars}")


input_user = input("Create name of file: ")
test(input_user)


"""
-m : http://dl4.joxi.net/drive/2023/05/16/0045/0626/2949746/46/213bbb05a9.jpg
console import I cant fix error: http://dl4.joxi.net/drive/2023/05/16/0045/0626/2949746/46/884aed9269.jpg
http://dl3.joxi.net/drive/2023/05/16/0045/0626/2949746/46/154e22d3d2.jpg
"""
