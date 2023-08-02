import os
import sys
import select
import time
import subprocess

if "OPENAI_API_KEY" not in os.environ:
  print("You must set an OPENAI_API_KEY using the Secrets tool",
        file=sys.stderr)
else:

  print("== OPENAI + REPLIT CUSTOM BOT==")
  print("You have five seconds to select an option")
  print()
  print("1: Train Model\n2: Talk to your Bot\n3: Prompt Injection CTF MODE\n4: AISafety Bypass CTF MODE\n>",end="")

  i, o, e = select.select([sys.stdin], [], [], 10)
  print()

  if (i):
    choice = sys.stdin.readline().strip()
    time.sleep(0.5)
    os.system('clear')
    if choice == "1":
      print("BOT TRAINING MODE")
      import process
      process.train()
    elif choice == "2":
      print("BOT CONVERSATION MODE")
      import process
      process.runPrompt()
    elif choice == "3":
      print("Prompt Injection CTF MODE")
      import level2
      level2.runPrompt()
    elif choice == "4":
      print("AISafety Bypass CTF MODE")
      import level3
      level3.runPrompt()
    else:
      print("Booting into API Server…")
      time.sleep(1)
      os.system('clear')
      print("BOT API SERVER RUNNING")
      p = subprocess.Popen([sys.executable, 'server.py'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
      while True:
        line = p.stdout.readline()
        if not line: break

  else:
    time.sleep(0.5)
    os.system('clear')
    print("Booting into API Server…")
    time.sleep(1)
    os.system('clear')
    print("BOT API SERVER RUNNING")
    p = subprocess.Popen([sys.executable, 'server.py'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    while True:
      line = p.stdout.readline()
      if not line: break

