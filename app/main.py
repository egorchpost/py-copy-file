import os


def copy_file(command):
    list_com = command.split()

    if len(list_com) != 3:
        return

    com_, source, destination = list_com

    if (command == "" or source == "" or destination == "" or com_ != "cp"
            or not os.path.exists(source)):
        return

    if source == destination:
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
