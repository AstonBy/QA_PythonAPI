import os.path

for files in os.walk("main"):
    if '.py ' in " ".join(files[-1]):
        a = files[0]
        print(a.replace('\\','/'))





