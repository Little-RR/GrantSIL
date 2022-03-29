import pip

with open("requirements.txt", "r") as f:
    g = f.readlines()
    for line in g:
        pip.main(["install", "--user", str(line)])


