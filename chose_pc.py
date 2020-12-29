import os.path


filepath = os.path.dirname(__file__)


def encrypting_save(text):

    pc_data = ""
    pc_data_x = ""
    end = len(text)
    for i in range(len(text)):
        pc_data += text[i] + text[end - 1]
        end -= 1

    for i in pc_data:
        if i == "n":
            pc_data_x += "x"
        elif i == "p":
            pc_data_x += "q"
        else:
            pc_data_x += i
    return pc_data_x


def create_file(pc_data_x):

    """ Create save file in PC """

    save_file = open(os.path.join(filepath, "data\\save\\pc_save.txt"), "w")
    save_file.write(pc_data_x)
    save_file.close()


def open_pc_file():

    """ Open pc_save file """

    file_pc = open(os.path.join(filepath, "data\\save\\pc_save.txt"), "r")
    pc_data_x = file_pc.read()
    file_pc.close()
    return pc_data_x

        
def decrypting_save(pc_data_x):

    pc_data_load = ""
    pc_data_load_x = ""

    for i in pc_data_x:
        if i == "x":
            pc_data_load_x += "n"
        elif i == "q":
            pc_data_load_x += "p"
        else:
            pc_data_load_x += i

    start = 0
    for i in range(len(pc_data_load_x)):
        if (i + start) < len(pc_data_load_x):
            pc_data_load += pc_data_load_x[i + start]
            if (i + start) >= len(pc_data_load_x):
                break
            else:
                start += 1
    return pc_data_load
