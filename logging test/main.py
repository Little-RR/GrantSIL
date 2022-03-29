import json

def temp():
    try:
        with open("log.json", "r") as logging:
            content = json.loads(logging.read())
            return content
    except:
        newdict = {
            "id": 69,
            "hasroles": 1,
            "welcome": 1,
            "moderation": 1,
            "blacklists": []
        }

        data = [newdict]

        save(data)

        with open("log.json", "r") as logging:
            content = json.loads(logging.read())
            return content

def new_server(inid=int):

    newdict = {
        "id": int(inid),
        "hasroles": 1,
        "welcome": 1,
        "moderation": 1,
        "blacklists": []
    }
    data = temp()
    data.append(newdict)
    save(data)

def query(server, request=None):
    data = temp()
    ids = []
    serv = {}
    for d in data:
        s = d.get("id")
        ids.append(s)

    if server not in ids:
        new_server(int(server))
        pass
    else:
        for d in data:
            if d.get('id') == server:
                serv = d

    if request is not None:
        v = serv.get(str(request))
        return v
    else:
        return serv


def delete_server(inid):
    data = temp()
    for d in data:
        serv = d.get('id')
        if inid == serv:
            data.remove(d)
        else:
            pass

    save(data)


def write(target=int, existing=bool, term=None, value=None):
    data = temp()
    if existing is False:
        query(int(target))
        return
    else:
        for d in data:
            dID = d.get('id')
            if term != "blacklists":
                if dID == target:
                    d[term] = value
            elif term == "blacklists":
                if dID == target:
                    if list(value)[0] == "x":
                        value = str(value)[1:]
                        d['blacklists'].remove(int(value))
                    else:
                        d['blacklists'].append(int(value))


    save(data)

def save(data):
    with open("log.json", "w") as logging:
        json.dump(data, logging)


print(query(69, 'moderation'))