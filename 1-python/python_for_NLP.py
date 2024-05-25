# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:18:51 2023

@author: icon
"""

#Regex101
#nlp has advance=chatbot , and basic 
#extracting information from text,voice,video

""" Extracting information from text """

#tesal filling,
########### to display indian number ##############

import re
text ='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern=r"\d\d\d\d\d\d\d\d\d\d"

matches=re.findall(pattern,text)
########
matches
text1 ='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern1=r"\d{10}"

matches=re.findall(pattern1,text1)
matches


############### to display US number ##############


import re
text ='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''
pattern1=r"\d{10}"
pattern=r"\(\d{3}\)\-\d{3}-\d{4}"
matches=re.findall(pattern,text)
matches


############# to display US as well as american number

import re
text ='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern=r"\(\d{3}\)-\d{3}-\d{4} | \d{10}"
matches=re.findall(pattern,text)
matches


################ remove - ; ###################

"""  let us try:
A protracted; legal battle; over a 32-carat;
 Golconda diamond-
 we want any character except ;-
 pattern will be [^;-]
 """
text="""A protracted; legal battle; over a 32-carat;
 Golconda diamond-"""
pattern=r"[^;-]"
except1=re.findall(pattern,text)
except1


###############  extract Notes to Consolidated Financial Statements  ###########

text3=""" Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods."""

pattern=r"Note \d - [^\n]+"

matches=re.findall(pattern,text3)
matches

















from PyPDF2 import PdfFileReader
#importing required module
from PyPDF2 import PdfReader

reader=PdfReader("c:/1-python/python_tutorial.pdf")

#print number of pages
print(len(reader.pages))

#getting a specific page from pdf file
page=reader.pages[10]
page

#extracting page from text
text=page.extract_text()
print(text)

################################################################

import re
chat1="Hi I have problem with all my order number : 412456787"
pattern=r"order [^\d]*(\d*)"
check=re.findall(pattern,chat1)
check


import re
chat3="Hi I have problem with all my order number : 412456787 and i am having issue with my order number # 423534654 and i was charged 300 "
pattern=r"order [^\d]*(\d*)"
check=re.findall(pattern,chat3)
check

###########################################################

def get_pattren_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattren_match("order [^\d]*(\d*)",chat1)


#########################################################

######### Retrive email id and number  ##################
# if dot than take \
#^ not


at1="hi you ask a lot of questions 1233543523 abc3@gmail.com"
at2="hello my email is jrgj67@dkg.kih"
pattern=r"[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*"
check=re.findall(pattern,at1)
check


########################################################

import re
text=""" Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family"""


def get_pattren_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
"""
get_pattren_match(r"age (\d+)",text)
get_pattren_match(r"Born(.*)\n",text).strip()
get_pattren_match(r"Born .*\n(.*)\(age",text).strip()
get_pattren_match(r"\(age.*\n(.*)",text).strip()
"""
def extract_personal_info(text):
    age=get_pattren_match(r"age (\d+)",text)
    full_name=get_pattren_match(r"Born(.*)\n",text).strip()
    birth_date=get_pattren_match(r"Born .*\n(.*)\(age",text)
    birth_place=get_pattren_match(r"\(age.*\n(.*)",text)
    return{
        "age":int(age),
        "name":full_name,
        "birth_date":birth_date,
        "birth_place":birth_place

    }
extract_personal_info(text)


#############################################################

text=""" Born Dhirajlal Hirachand Ambani
28 December 1932
Chorwad, Junagadh State, British India
(present-day Gujarat, India)
Died	6 July 2002 (aged 69)
Mumbai, Maharashtra, India
Citizenship	British India (1932–1947)
Dominion of India (1947–1950)
India(1950–2002)
Occupation	Businessman
Organization(s)	Reliance Industries
Reliance Capital
Reliance Infrastructure
Reliance Power
Spouse	Kokila Dhirubhai Ambani
​
​(m. 1955)​
Children	4, including Mukesh Ambani and Anil Ambani
Awards	Padma Vibhushan (2016) (posthumously)"""

def extract_personal_info(text):
    age=get_pattren_match(r"aged (\d+)",text)
    full_name=get_pattren_match(r"Born(.*)\n",text)
    birth_date=get_pattren_match(r"Born .*\n(.*)",text)
    birth_place=get_pattren_match(r"\(aged.*\n(.*)",text)
    return{
        "age":int(age),
        "name":full_name,
        "birth_date":birth_date,
        "birth_place":birth_place

    }

extract_personal_info(text)

###############################################################

#####################  Tokanization  ##################

txt="welcome to new year 2023"
x=txt.split()
print(x)

import re
def remove_special_char(text):
    pat=r'[^a-zA-Z0-9.,?!/:;\"\'\s]'
    return re.sub(pat,'',text)


remove_special_char("0215 hatdf % kugewik kjhkffdg")

#####  remove number

import re
def remove_number(text):
    pat=r'[^a-zA-Z.,?!/:;\"\'\s]'
    return re.sub(pat,'',text)


remove_number("345 hatdf ? 7656 kugewik kjhkffdg")

txt="welcome , to the ; yera!"
x=re.split(r"(?:,|:|\s)\s*",txt)
print(x)

##################################################

######### remove punctuation ###############

import string
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text

remove_punctuation("Artical: @ first semtence of some {important} artical lots of ~ punctuation and another one ;!")

#################################################

##################  stemming  ##################

#convert word into base word
#nltk  natural language tool kit
#it has drawback
import nltk
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text

get_stem("we are eating and swimming; we have been eating and swimming he eats and swims; he ate and swam ")

#########################################################
#matching text at start or end of string
filename="spam.txt"
filename.endswith(".txt")

area_name="6 th lane west andheri"
area_name.endswith("west andheri")

choices=("http","ftp")
url="http://www.python.org"
url.startswith(choices)

################################################

#slicing of string
s="ABCDEFGHI"
print(s[2:5])#CDE
print(s[-6:-2])#DEFG
print(s[2:-1])
print(s[1:6:2])
print(s[6:1:-2])#reverse i step of 2 (-) is compulsory
print(s[:4])
print(s[1:])
#slice last three character
print(s[6:])
#reversing string
print(s[::-1])

# similar operation can be done by slicing

filename="spam.txt"
filename[-4:]==".txt"

url="http://www.python.org"
url[:5]=="http:"or url[:6]=="https:"or url[:4]=="ftp:"

##############################################################

###important ####
from fnmatch import fnmatch,fnmatchcase
names=["Dot1.csv","Dot2.csv","config.ini","foo.py"]
[name for name in names if fnmatch(name,"Dot*.csv")]

addresses=[
    "5412 N CLARK ST",
    '1060 W ADDISON ST',
     "1039 W GRANVILLE AVE",
     "2122 N CLARK ST",
     "4802 N BROADWAY"]
from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr,"*ST")]

################################################

text="yeah but no but yeah but no but yeah"
text=="yeah"
text.startswith("yeah")
text.endswith("no")
text.find("no")

text1="11/27/2012"
text2="Nov 27,2012"

##### whether date pattren matches or not  ######

import re

if re.match(r"\d+/\d+/\d+",text1):
    print("yes")
#herewe need front slash so / is given and \ is given we we need that 
#element over there
else:
    print("no")

if re.match(r"\d+/\d+/\d+",text2):
    print("yes")
else:
    print("no")

### same using ()  ###
dat=re.compile(r"(\d+)/(\d+)/(\d+)")
if re.match(dat,text1):
    print("yes")
else:
    print("no")

if re.match(dat,text2):
    print("yes")
else:
    print("no")

############################################################

#search and replace text

text="yeah but no but yeah but no but yeah"
text.replace("yeah","yup")


text="today is 11/12/2012,pycan starts 3/13/2013"
import re
re.sub(r"(\d+)/(\d+)/(\d+)",r"\3-\1-\2",text)# change the position of dates
                                            # 3-1st group,13-2nd group,2013-3rd group

################################################################

# if you want to know how many substitution are made in text

newtext, n=dat.subn(r"\3-\1-\2",text)
newtext
n

### replace python with snake

text ="UPPER PYTHON ,lower python,Mixesd PYthon"
re.findall("python",text,flags=re.IGNORECASE)
re.sub("python","snake",text,flags=re.IGNORECASE)

###################################################################

import re
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return  word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
text3=re.sub("python",matchcase("snake"),text,flags=re.IGNORECASE)
text3

#######################################################

#print "no."
str_ppt=re.compile(r'\"(.*)\"')
text1='Computer says "no."'
str_ppt.findall(text1)


text2='Coumputer says "no" phone says "yes"'
str_ppt=re.compile(r'\"(.*)\"')
str_ppt.findall(text2) #but here phone says also get printed 

text2='Coumputer says "no" phone says "yes"'
str_ppt=re.compile(r'\"(.*?)\"')
str_ppt.findall(text2) # here phone says don't get printed 

comment=re.compile(r"/\*(.*?)\*/")
text1='/* this is comment */'
comment.findall(text1)

text2='''/*this is
    multi line comment*/'''
comment.findall(text2)

comment=re.compile(r"/\*(.*?)\*/",re.DOTALL)
comment.findall(text2)

###########################################################

#normalizing unicode text to standard representation 

s1="spicy jalapse\u00f10"
s2="spicy jalapse\u0303o"
print(s1)
print(s2)
s1==s2

import unicodedata
t1=unicodedata.normalize("NFC",s1)
t2=unicodedata.normalize("NFC",s2)
t1==t2

"""unicode defines code points , i.e a number which represent charachter
"""
#UTF unicode transformation formate and '8' means 8bit are used for
#encoding it is one of most efficient and convenient encoding formats
#among various encodings

string1="apple"
string2="jee123"
string3="098123"
string4="uyfg@443"

string1.encode(encoding="UTF-8",errors="strict")
string2.encode(encoding="UTF-8",errors="strict")
string3.encode(encoding="UTF-8",errors="strict")
string4.encode(encoding="UTF-8",errors="strict")

text="one 🐘 and three 🐋"
print(text)
print(len(text))

e=text.encode("utf8")
print(e)
print(len(e))

"""
we encode the string into a bytes type using the utf8 encoding and print the bytes.
we count the number of bytes in this encoding type
"""

#############################################################

fname="data.txt"
with open(fname,mode="rb")as f:
    #by default it encode with utf-8
    contents=f.read()
    
    print(type(contents))
    print(contents)
    print(contents.decode("utf8"))

fname="data.txt"
with open(fname,mode="rb")as f:
    #by default it encode with utf-8
    contents=f.read()
    
    print(type(contents))
    print(contents)
    print(contents.decode("utf16"))

#NFD and NFC 
#there is no differnce between NFD nand NFC intended for generating code compatible to the platform

###########################################################

########## whitespace strapping  ###########

### strip()

s="  hello world  \n"
s.strip()
s.lstrip()#left side white space will be reduce
s.rstrip()#right side white space will be reduce

#character striping
t="--------hello====="
t.strip("-")
t.strip("-=")

s="  hello world   \n"
s.strip()

### replace()

s.replace(" ","")

import re
re.sub("\s+"," ",s)

#########################################################################

#Aliging the text string
text="hello world"
text.ljust(20)
text.rjust(20)
text.center(20)

   ###########

text.rjust(20,"=")
text.ljust(20,"*")
text.center(20,"$")

   ############
   
format(text,">20")  #right align
format(text,"<20")  #left align
format(text,"^20")  #center align

format(text,"=>20")
format(text,"*<20")
format(text,".^20")

#these formate code can also be used in formate ()method
"{:>10s}{:10s}".format("hello","world")

#benefits of formate() is that it is not spexific to string
#making it more geberal purpose 

x=1.2334
format(x,">10")

format(x,"^10.2f")

#################################

parts=["Is","chicago","Not","Chicago?"]
"".join(parts)
#IschicagoNotChicago?
",".join(parts)
#Is,chicago,Not,Chicago?
" ".join(parts)
#Is chicago Not Chicago?

















