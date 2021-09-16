# module == a function containing python code. May contain functions.classes etc
# used in modular programming(separate a program into parts)
# help('modules') == listing of available python modules

# method1
#import messages

#messages.hello()
#messages.bye()

# method 2
#import messages as msg  # reduce typing/import w/ different name

#msg.hello()
#msg.bye()

from messages import hello,bye  # imports specific functions
                                # import * for all functions

hello()  # no need to preceed w/module name
bye()

help('modules')