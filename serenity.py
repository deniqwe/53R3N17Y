# -*- coding: utf-8 -*- 
"""
     _-----_
    |       |    .------------------------.
    |--(o)--|    |   Welcome to 53R3N17Y  |
   `---------´   |       abaykan.com      |
    ( _´U`_ )    '------------------------'
    /___A___\

     |  ~  |
   __'.___.'__
 ´   `  |° ´ Y `
"""

from insides import *
from sys     import argv
import requests, json
import optparse
import os, re
from lxml import html
import sys

################################  Banner   ################################

os.system('clear') 
print(Banner)

################################ Functions ################################

def reverseViaHT(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def geoip(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/geoip/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def httpheaders(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/httpheaders/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def hostsearch(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/hostsearch/?q="
    combo = "{url}{website}".format(url=url, website=website)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def whois(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/whois/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def dnslookup(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/dnslookup/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def findshareddns(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/findshareddns/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def heading(heading, website, color, afterWebHead):
    space = " " * 10
    var = str(heading + " '" + website + "'" + str(afterWebHead))
    length = len(var) + 1; print "" # \n
    print("\n\n{color}" + var).format(color=color)
    print("{white}" + "-" * length + "--").format(white=w); print "" # \n

################################  Args  ################################ 

_usage      = w + "python " + w + argv[0] + w + " --all hack.me" + w
parser      = optparse.OptionParser(usage=_usage, conflict_handler="resolve")
general     = optparse.OptionGroup(parser, c + 'Basic Help' + w)
general.add_option( '-h', '--help', action='help', dest='help', help='Shows the help for program.')

reverse_ip  = optparse.OptionGroup(parser, c + "IP Tools" + w)
reverse_ip.add_option( "-1", "--revht",  action='store_true', dest='hackertarget', help="Reverse IP")
reverse_ip.add_option( "-2", "--geo",  action='store_true', dest='geoip', help="Geo IP Lookup")
reverse_ip.add_option( "-3", "--whois",  action='store_true', dest='whois', help="Whois Lookup")
reverse_ip.add_option( "-4", "--host",  action='store_true', dest='hostsearch', help="Searching Host")
reverse_ip.add_option( "-5", "--dns",  action='store_true', dest='dnslookup', help="Show HTTP Header")
reverse_ip.add_option( "-6", "--sdns",  action='store_true', dest='findshareddns', help="Find Shared DNS")
reverse_ip.add_option( "-7", "--http",  action='store_true', dest='httpheaders', help="Show HTTP Header")

grouped_scanning = optparse.OptionGroup(parser, c + "Grouped Results" + w)
grouped_scanning.add_option( "-a", "--all",  action='store_true', dest='all', help="All Things at Once!")



parser.add_option_group(general)
parser.add_option_group(reverse_ip)
parser.add_option_group(grouped_scanning)

(options, args) = parser.parse_args()
try: website = addHTTP(args[0])
except: pass

try:
    if options.geoip:
        heading(heading="Geo IP Lookup",  color=c, website=website, afterWebHead="")
        geoip(website)

    elif options.hackertarget:
        heading(heading="Reversing IP", color=c, website=website, afterWebHead="")
        reverseViaHT(website)

    elif options.whois:
        heading(heading="Whois Lookup", color=c, website=website, afterWebHead="")
        whois(website)

    elif options.hostsearch:
        heading(heading="Searching Host", color=c, website=website, afterWebHead="")
        hostsearch(website)

    elif options.dnslookup:
        heading(heading="DNS Lookup", color=c, website=website, afterWebHead="")
        dnslookup(website)

    elif options.findshareddns:
        heading(heading="Find Shared DNS", color=c, website=website, afterWebHead="")
        findshareddns(website)

    elif options.hostsearch:
        heading(heading="HTTP Header Host", color=c, website=website, afterWebHead="")
        httpheaders(website)

    elif options.all:
        heading(heading="Geo IP Lookup", color=c, website=website, afterWebHead="")
        geoip(website)

        heading(heading="Reversing IP", color=c, website=website, afterWebHead="")
        reverseViaHT(website)

        heading(heading="Whois Lookup", color=c, website=website, afterWebHead="")
        whois(website)

        heading(heading="Searching Host", color=c, website=website, afterWebHead="")
        hostsearch(website)

        heading(heading="DNS Lookup", color=c, website=website, afterWebHead="")
        dnslookup(website)

        heading(heading="Find Shared DNS", color=c, website=website, afterWebHead="")
        findshareddns(website)

        heading(heading="HTTP Header Host", color=c, website=website, afterWebHead="")
        httpheaders(website)

    else:
        write(var="~", color=c, data="Usage: " + w + "python " + w + argv[0] + c + " --help")

except KeyboardInterrupt:
    write(var="~", color=r, data="Error: User Interrupted!")

except Exception, e:
    write(var="#", color=r, data="Error: Kindly Report the error below to me :) (If Your Internet's Working ;)\n\"\"\"\n" + str(e) + "\n\"\"\"")
