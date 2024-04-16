class InputData:
    with open("api.txt", "r") as f:
        data = f.readlines()
    Base_url = data[0].strip()
    Key_id = data[1].strip()
    secret_key1 = data[2].strip()