import scratchapi
import getpass
scratch = scratchapi.ScratchUserSession(input("What's your username?  "), getpass.getpass("What's your password?  "))
proceed=input("Are you sure you would like to proceed? This will follow me and my 6 alternate account. Please answer Y/N   ")
if 'Y' == str.upper(proceed):
  scratch.users.follow('-Infinite-Code-')
  print("Followed -Infinite-Code-")
  scratch.users.follow('--Explosion--')
  print("Followed --Explosion--")
  scratch.users.follow('--ExpIosion--')
  print("Followed --ExpIosion--")
  scratch.users.follow('--Implosion--')
  print("Followed --Implosion--")
  scratch.users.follow('--ImpIosion--')
  print("Followed --ImpIosion--")
  scratch.users.follow('Exploding_Test')
  print("Followed Exploding_Test")
  scratch.users.follow('--EXPLOSlON--')
  print("Followed --EXPLOSlON--")
else: 
  print("That's okay! Thanks for looking at this program anyways!")