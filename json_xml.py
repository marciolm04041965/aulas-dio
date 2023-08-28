import json
import xmltodict

# Carregar o arquivo JSON
with open('nfce.json', 'r') as json_file:
    data = json.load(json_file)

# Converter o dicionário JSON em XML
xml_data = xmltodict.unparse(data, pretty=True)

# Salvar o XML em um arquivo
with open('dados.xml','w') as xml_file:
    xml_file.write(xml_data)

print("Arquivo XML gerado com sucesso.")