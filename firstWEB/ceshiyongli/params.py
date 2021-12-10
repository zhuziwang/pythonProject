import yaml

datas = None
#读取数据驱动的数据
with open('./lib/cases.yaml',encoding='utf8') as f:
    datas = yaml.safe_load(f)

print(datas)