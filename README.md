# dinner-collation-telebot
## Background

As one of my chores is to cook dinner for my family. I have to know how many of my family members are coming back to eat dinner, so i can prepare the amount of food correctly and reduce wastage and effort.

I created this bot to help solve this hassle of checking my family members on who is coming back for dinner.

## Problem
My family members do not always notified the chat group that they are coming back for dinner or they are not.

Thus, i have to call them and ask them which is a hassle.

# User Stories

/help

/start
 - run /settings

1. let the user choose which day to monitor, MONDAY, TUES, WED ETC
2. let the user choose which time to start monitoring, 6pm onwards
3. let the user choose which time to stop monitoring, 7.30pm onwards ---- 6pm to 7.30pm

/poll
- run 2 polls at the start of monitoring
- notify the user that have not poll yet in a fixed interval?? before the time stop 

## poll 1 
who is coming back for dinner? coming back for dinner | not me | im cooking dinner 

## give conclusion
at the end of time stop, 
### scenario
1. if no one is cooking dinner - THERE IS NO DINNER AT HOME, GO EAT OUTSIDE
2. if 1 or 2 is cooking dinner at home, give the total number of people eating dinner  - THERE IS DINNER AT HOME, COME BACK EAT  
# TODO

refactor the code into folders, helper, service and app.py