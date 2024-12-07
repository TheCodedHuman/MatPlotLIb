# This program helps me in clearing the clutter from terminal
# its possible to use this file at multiple places without hardcoding this two lines, by sys module
# but, in my opinion, better to just paste these two lines in whatever code you using

import os
def klear(): os.system('cls' if os.name=='nt' else 'clear')

