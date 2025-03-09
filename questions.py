import random 
import pathlib as Path
import os
import random

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
for paperNum in range(1,36):
    
    #specify question number 
    paperNo = open(f'paper{paperNum}.txt','w')
    answerKey = open(f'answerKey{paperNum}.txt','w')

    paperNo.write('\n Name: \n\n Date: \n\n Period:\n\n')
    paperNo.write((' '*20)+f'State Capital Quiz{paperNum}')
    paperNo.write('\n\n')

    #write questions on each paper 
    key = list(capitals.keys())
    random.shuffle(key)
    counter = 0
    for states in key:
        counter +=1
        
        paperNo.write(f'\n\n\n{counter}. What is the capital of {states}?\n\n')

        correctAnswer = capitals[states]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        finalOptions = wrongAnswer+[correctAnswer]
        random.shuffle(finalOptions)

        options = 'ABCD'
        iterator = 0
        for option in options:
            if(finalOptions[iterator] == correctAnswer):
                answerKey.write(f'{counter}. {option}\n')
            paperNo.write(f'{option}. {finalOptions[iterator]}\n')
            iterator+=1
        
        





        

