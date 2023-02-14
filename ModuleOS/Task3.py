"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os
import re

start = r'targer'
virus = r'\d+'

for var in os.listdir(start):
     contest = re.findall(virus,var)
     if int(contest[0]) %2 == 0:
        os.rename(start + '/' + contest[0], start + '/letsgo' + str(int(contest[0])*13))