ListOfName = []

while True:
  vorname = input("First Name: ").strip().capitalize()
  nachname = input("Last Name: ").strip().capitalize()

  name = f"{vorname} {nachname}"
  if name not in ListOfName:
    ListOfName.append(name)
    for namen in ListOfName:
      print(namen)
  else:
    print(f"{name} is already on the list")
    for namen in ListOfName:
      print(namen)