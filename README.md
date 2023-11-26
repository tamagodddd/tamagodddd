text = "Hello, I am Bayu!;\n\
an Undergraduate of Biomedical Engineering Student at Universitas Airlangga;\n\
Currently looking for an internship.;\n\
Feel free to hit me up on my email:;\n\
bayu28.wb@gmail.com"

rows = text.split(';')
for row in rows:
    print(row.strip())
