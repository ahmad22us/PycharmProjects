with open("data.txt") as f_data:
    data_content = f_data.readlines()
    print(data_content)
    data_f = ""
    for data in data_content:
        if data.strip()[-1] != ".":
            data_f = data.strip() + ".\n"
        else:
            data_f = data
        print(data_f)
        with open("modified_data", mode="a") as data_write:
            data_write.write(data_f)

# data_cont = ['Licit definition, legal; lawful; legitimate; permissible.\n', 'She made some money by licit means.\n']
# data_f = [data for data in data_cont if data.strip()[-1] != "." data_f = data.strip() + ".\n" else ]
