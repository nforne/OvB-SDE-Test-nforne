import json

print("Place the input_file.json file in the same working directory as this script")
print("You must not replace or mutilate the output file herein in any way. It's a part of this script. Copy it at the "
      "end of your run if need be")
while True:
    try:
        print("The input file must be named 'input_file.json'")
        input_f = input("Enter the input file name: ")
        if input_f != "input_file.json":
            print("The input file must be named 'input_file.json'")
        elif input_f == "input_file.json":
            break
    except Exception as e:
        print(e)

fi = open(input_f, "r")
xi = json.loads(fi.read())
db_set_ip = xi["data"]

spread_l = []
opl = []
op_s2b = 0
for i in db_set_ip:
    if i["type"] == "corporate":
        for j in db_set_ip:
            if j["type"] == "government":
                if type(i['yield']) != 'NoneType' and type(j['yield']) != 'NoneType':
                    spread = float(i['yield'].replace('%', '')) - float(j['yield'].replace('%', ''))
                    spread_l.append(spread)
                else:
                    pass
            else:
                pass
    else:
        pass
for i in db_set_ip:
    if i["type"] == "corporate":
        for j in db_set_ip:
            if j["type"] == "government":
                if type(i['yield']) != 'NoneType' and type(j['yield']) != 'NoneType':
                    spread = float(i['yield'].replace('%', '')) - float(j['yield'].replace('%', ''))
                    if spread == min(spread_l):
                        opl.append(i["id"])
                        opl.append(j["id"])
                        op_s2b += spread
                    else:
                        pass
                else:
                    pass
            else:
                pass
    else:
        pass


print(spread_l)
print(min(spread_l))

fo = open("output_file.json", "r")
xo = json.loads(fo.read())
db_set_op = xo["data"]

db_set_op[0]["corporate_bond_id"] = opl[0]
db_set_op[0]["government_bond_id"] = opl[1]
db_set_op[0]["spread_to_benchmark"] = f'{int(round(float(op_s2b), 0)) * 100}bps'

print(db_set_op)
