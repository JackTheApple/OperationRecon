import re

killswitch = 2
access = 0
print("Access Granted")
print("Search help to see a list of what you can search for.")
Rawaccess = open("User.txt", "r")
refineaccess = Rawaccess.read()
if refineaccess == "Limited":
  access=-3
elif refineaccess == "Unlimited":
  access=+3
elif refineaccess == "SuperUnlimited":
  access=+10
print()
while killswitch<3:
  a = None
  b = None
  c = None
  d = None
  e = None
  f = None
  g = None
  h = None
  i = None
  j = None
  k = None
  l = None
  m = None
  n = None
  o = None
  p = None
  Op = None
  print(" ")
  ask_pls = input("What do you want to search?\n").lower()
  a = re.search("expect", ask_pls)
  b = re.search("job", ask_pls)
  c = re.search("servant", ask_pls)
  d = re.search("user", ask_pls)
  e = re.search("spy", ask_pls)
  f = re.search("writer", ask_pls)
  g = re.search("^k$", ask_pls)
  h = re.search("tipper", ask_pls)
  i = re.search("term", ask_pls)
  j = re.search("history", ask_pls)
  k = re.search("jeeva", ask_pls)
  l = re.search("eric", ask_pls)
  m = re.search("monique", ask_pls)
  n = re.search("greta", ask_pls)
  o = re.search("ella", ask_pls)
  p = re.search("help", ask_pls)
  if a:
    if a == None:
      continue
    else:
      print("Opening Expectations. Please wait.\n ")
      print('')
      Op = open("Expectations.txt", "r")
      print(Op.read())
      Op.close()
  elif b:
    if b == None:
      continue
    else:
      print("Opening All Job documents. Please wait.\n ")
      print('')
      Op = open("Masse Spy.txt", "r")
      Opa = open("Servant.txt", "r")
      Opb = open("Tipper.txt", "r")
      Opc = open("Writer.txt", "r")
      print(Op.read())
      print('')
      print(Opa.read())
      print('')
      print(Opb.read())
      print('')
      print(Opc.read())
      Op.close()
      Opa.close()
      Opb.close()
      Opc.close()
  elif c:
    if c == None:
      continue
    else:
      print("Opening Servant. Please wait.")
      Op = open("Servant.txt", "r")
      print(Op.read())
      Op.close()
  elif d:
    if d == None:
      continue
    else:
      if access < 2:
        print("Sorry, but you are not an admin account and cannot access this. (Basically everybody who is not Ella, Eric, or the programmers don't have an admin account.)If you think that this is a mistake than contact Eric or Ella.(Which is stupid, cause only Eric and Ella are supposed to have admin accounts) Otherwise, log in with a admin account, or continue browsing.")
      elif access > 2:
        print('Opening Usernames. Please wait.')
        Op = open("People.txt", "r")
        print(Op.read())
        Op.close()
  elif e:
    if e == None:
      continue
    else:
      print('Opening Masse Spy. Please wait.')
      Op = open("Masse Spy.txt", "r")
      print(Op.read())
      Op.close()
  elif f:
    if f == None:
      continue
    else:
      print('Opening Writer. Please wait.')
      Op = open("Writer.txt", "r")
      print(Op.read())
      Op.close
  elif g:
    if g == None:
      continue
    else:
      killswitch =+ 10
      print('Killswitch activated. You are now logged out.')
  elif h:
    if h == None:
      continue
    else:
      print('Opening Tipper. Please wait.')
      Op = open("Tipper.txt", "r")
      print(Op.read())
      Op.close
  elif i:
    if i == None:
      continue
    else:
      print('Opening terminology. Please wait.')
      Op = open("Terminology You Should Know.txt")
      print(Op.read())
      Op.close
  elif j:
    if j == None:
      continue
    else:
      print('Opening history. Please wait')
      Op = open("History of Stop the Masse Order.txt")
      print(Op.read())
      Op.close
  elif ask_pls == 'star chamber':
    if access < 4:
      print('YOU DO NOT HAVE ACCESS, SCRAM UNDERLINGS')
    elif access > 4:
      print('Opening Star Chamber Please wait.')
      username = input('Sorry, but we need you to log in again just in case you are nasty supervillain in disguise.\nUsername:')
      password = input('Password:')
      if username == "superuser" and password == "shimmersparkle2021superusernoonecanknow":
        Op = open("Star Chamber.txt", "r")
        print(Op.read())
        Op.close
  elif k:
    if k == None:
      continue
    else:
      print('Opening the file on Jeeva Karthy.')
      Op = open("JeevaKarthy.txt", "r")
      print(Op.read())
      Op.close
  elif l:
    if l == None:
      continue
    else:
      print('Opening the file on Eric Mo')
      Op = open("EricMo.txt", "r")
      print(Op.read())
      Op.close
  elif m:
    if m == None:
      continue
    else:
      print('Opening the file on Monique Botelho.')
      Op = open("MoniqueBotelho.txt", "r")
      print(Op.read())
      Op.close
  elif n:
    if n == None:
      continue
    else:
      print('Opening Files On Greta Sharma.')
      if access < 2:
        Op = open("GretaSharma.txt", "r")
        print(Op.read())
        Op.close
      elif access > 2:
        Op = open("TSGretaSharma.txt", "r")
        print(Op.read())
        Op.close
  elif o:
    if o == None:
      continue
    else:
      print('Opening Files on Ella Dumars')
      Op = open("EllaDumars.txt", "r")
      print(Op.read())
      Op.close
  elif p:
    if p == None:
      continue
    else:
      print('Opening all commands.')
      Op = open("Commands.txt", "r")
      print(Op.read())
      Op.close
  else:
    print("No results found sorry.")