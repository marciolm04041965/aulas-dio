import hashlib

def calculate_sha1(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()

input_text = "28170800156225000131650110000151341562040824|2|1|1SEU-CODIGO-CSC-CONTRIBUINTE-36-CARACTERES"
sha1_hash = calculate_sha1(input_text)
print("SHA-1 Hash:", sha1_hash)