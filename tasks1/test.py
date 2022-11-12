def service_center(clients_list: list, file_name):
    owners_list = []
    f = open(file_name, 'w')
    for item in clients_list:
        item_owner = item[2]
        owner_number = item[3]
        str_person = ""
        if item_owner not in owners_list:
            str_person = str_person + item_owner + " " + owner_number + ": "
            owners_list.append(item_owner)
            for items in clients_list:
                if items[2] == item_owner:
                    str_person = str_person + items[0] + " - " + str(items[1]) + "; "
        result_string = str_person[:len(str_person)-2] + "\n"
        if result_string != "" and result_string != "\n":
            f.write(result_string)
    f.close()
