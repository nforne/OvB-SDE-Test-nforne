import json

fi = open("sample_input.json", "r")
xi = json.loads(fi.read())
db_set_ip = xi["data"]

spread_l = []
opl = []
for i in db_set_ip:
    q = 0
    i-id = []
    j-id = []
    if i["type"] == "corporate":
        for j in db_set_ip:
            if j["type"] == "government":
                if type(i['yield']) != 'NoneType' and type(j['yield']) != 'NoneType':
                    spread = (float(i['yield'].replace('%', '')) - float(j['yield'].replace('%', '')))
                    q += spread
                    spread_l.append(spread)
                else:
                    pass
            else:
                pass
    else:
        pass
    if q == min(spread_l):
        opl.append(i["id"])
        opl.append(j["id"])
    else:
        pass

print(spread_l)
spread_min = min(spread_l)
print(spread_min)

fo = open("sample_output.json", "r")
xo = json.loads(fo.read())
print(xo["data"])
db_set_op = xo["data"]

db_set_op[0]["corporate_bond_id"] = opl[0]
db_set_op[0]["government_bond_id"] = opl[1]
db_set_op[0]["spread_to_benchmark"] = f'{int(round((float(opl[0]) - float(opl[1])), 0)) * 100}bps'
