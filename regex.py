import re
import sys

regexEmail = re.compile(r'''(([a-zA-Z0-9._%+-])+
                        \@+([a-zA-Z])+
                        (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

regexPhone = re.compile(r'''((\d{2}|\(\d{2}\))?
                        (\s|-|\.)?
                        \d{5}(\s|-|\.)?
                        \d{4})''', re.VERBOSE)


phoneSearch = regexPhone.search(str(sys.argv))
emailSearch = regexEmail.search(str(sys.argv))

if phoneSearch != None:
    print(phoneSearch.group())

if emailSearch != None:
    print(emailSearch.group())
