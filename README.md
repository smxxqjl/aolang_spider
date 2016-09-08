# A login spider for http://180.209.64.253:866/login.aspx
Usage: ` python3 aolangspieder.py id processnum sex(boy|girl) startpoint`

All arguments are optional, but one option requires last option to be specified

Written by python3 and requests library, base on the hypothesis that the default password for an account is last six digital of Identity Card Number.
Enumerate all possible code to login and print it out if spider login successfully.
