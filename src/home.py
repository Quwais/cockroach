from data.main import *

def Home():
    Banner()
    print("""
              \033[1;30m      COCKRO\033[1;31mACH
  \033[1;32m  ______________________________________
   | Version : {0}                      |
   | Author  : M{1}   |
    --------------------------------------
    \033[1;33m{2}\033[1;37m""".format(Cockroach.version,Cockroach.author,Cockroach.facebook))
