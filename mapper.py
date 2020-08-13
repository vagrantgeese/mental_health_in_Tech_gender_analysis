import sys
import csv

oFile = open("mapOutput.txt", "w")

with open('survey.csv') as f:
    readf = csv.reader(f, delimiter=',')

    #treatment/gender key value pair variables
    treatedMales = 0
    untreatedMales = 0
    treatedFemales = 0
    untreatedFemales = 0
    treatedGQ = 0
    untreatedGQ = 0

    #treatment/age key value pair variables
    treatedTwenties = 0;
    untreatedTwenties = 0;
    treatedThirties = 0;
    untreatedThirties = 0;
    treatedForties = 0;
    untreatedForties = 0;
    treatedFifties = 0;
    untreatedFifties = 0;

    #treatment/gender/workInterfere key value pair variables
    treatedMalesOften = 0
    treatedMalesSometimes = 0
    treatedMalesRarely = 0
    treatedMalesNever = 0
    untreatedMalesOften = 0
    untreatedMalesSometimes = 0
    untreatedMalesRarely = 0
    untreatedMalesNever = 0
    treatedFemalesOften = 0
    treatedFemalesSometimes = 0
    treatedFemalesRarely = 0
    treatedFemalesNever = 0
    untreatedFemalesOften = 0
    untreatedFemalesSometimes = 0
    untreatedFemalesRarely = 0
    untreatedFemalesNever = 0
    treatedGQOften = 0
    treatedGQSometimes = 0
    treatedGQRarely = 0
    treatedGQNever = 0
    untreatedGQOften = 0
    untreatedGQSometimes = 0
    untreatedGQRarely = 0
    untreatedGQNever = 0
    
    for row in readf:
        gender = "N"; #a value of n represesnts anyone who is not strictly cis male or cis female(includes entries like "male leaning androgynous" and "Genderqueer")

        #determine missspellings and synonyms for "male" and assign gender to record (makes data consistent)
        if (row[2] == "male" or row[2] == "Male" or row[2] == "M" or row[2] == "m" or row[2] == "maile" or row[2] == "Cis Male" or row[2] == "Mal" or row[2] == "Male (CIS)" or row[2] == "Make" or row[2] == "Man" or row[2] == "Mail" or row[2] == "Malr" or row[2] == "Cis Man"):
            gender = "M"

        #determine misspellings and synonyms for "female" and assign gender to record (makes data consistent)
        if (row[2] == "female" or row[2] == "Female" or row[2] == "F" or row[2] == "f" or row[2] == "Cis Female" or row[2] == "Woman" or row[2] == "Femake" or row[2] == "cis-female/femme" or row[2] == "Female (cis)" or row[2] == "femail"):
            gender = "F"

        #link age and gender for those who have had treatment in the past for mental health issues 
        if (row[7] == "Yes"):
        
            if ((int(row[1]) >= 20 and int(row[1]) < 30)):
                oFile.write("treatedTwenties 1 \n");

            if ((int(row[1]) >= 30 and int(row[1]) < 40)):
                oFile.write("treatedThirties 1 \n");

            if ((int(row[1]) >= 40 and int(row[1]) < 50)):
                oFile.write("treatedForties 1 \n");

            if ((int(row[1]) >= 50 and int(row[1]) < 60)):
                oFile.write("treatedFifties 1 \n");

            #determine relationship between gender treatment and work interuptions caused by mental illnes for Males
            if (gender == "M"):
                oFile.write("treatedMales 1 \n");
                if(row[8] == "Often"):
                    oFile.write("treatedMalesOften 1 \n");
                if(row[8] == "Sometimes"):
                    oFile.write("treatedMalesSometimes 1 \n");
                if(row[8] == "Rarely"):
                    oFile.write("treatedMalesRarely 1 \n");
                if(row[8] == "Never"):
                    oFile.write("treatedMalesNever 1 \n");

            #determine relationship between gender treatment and work interuptions caused by mental illnes for Females
            if (gender == "F"):
                oFile.write("treatedFemales 1 \n");
                if(row[8] == "Often"):
                    oFile.write("treatedFemalesOften 1 \n");
                if(row[8] == "Sometimes"):
                    oFile.write("treatedFemalesSometimes 1 \n");
                if(row[8] == "Rarely"):
                    oFile.write("treatedFemalesRarely 1 \n");
                if(row[8] == "Never"):
                    oFile.write("treatedFemalesNever 1 \n");
                
            #determine relationship between gender treatment and work interuptions caused by mental illnes for GQ
            if (gender == "N"):
                oFile.write("treatedGQ 1 \n");
                if(row[8] == "Often"):
                    oFile.write("treatedGQOften 1 \n");
                if(row[8] == "Sometimes"):
                    oFile.write("treatedGQSometimes 1 \n");
                if(row[8] == "Rarely"):
                    oFile.write("treatedGQRarely 1 \n");
                if(row[8] == "Never"):
                    oFile.write("treatedGQNever 1 \n");

        #link age and gender for those who have not had treatment in the past for mental health issues
        if (row[7] == "No"):
            if ((int(row[1]) >= 20 and int(row[1]) < 30)):
                oFile.write("untreatedTwenties 1 \n");

            if ((int(row[1]) >= 30 and int(row[1]) < 40)):
                oFile.write("untreatedThirties 1 \n");

            if ((int(row[1]) >= 40 and int(row[1]) < 50)):
                oFile.write("untreatedForties 1 \n");

            if ((int(row[1]) >= 50 and int(row[1]) < 60)):
                oFile.write("untreatedFifties 1 \n");

            #determine relationship between gender treatment and work interuptions caused by mental illnes for Males
            if (gender == "M"):
                oFile.write("untreatedMales 1 \n");
                if(row[8] == "Often"):
                    oFile.write("untreatedMalesOften 1 \n");
                if(row[8] == "Sometimes"):
                    oFile.write("untreatedMalesSometimes 1 \n");
                if(row[8] == "Rarely"):
                    oFile.write("untreatedMalesRarely 1 \n");
                if(row[8] == "Never"):
                    oFile.write("untreatedMalesNever 1 \n");

            #determine relationship between gender treatment and work interuptions caused by mental illnes for Females
            if (gender == "F"):
                oFile.write("untreatedFemales 1 \n");
                if(row[8] == "Often"):
                    oFile.write("untreatedFemalesOften 1 \n");
                if(row[8] == "Sometimes"):
                    oFile.write("untreatedFemalesSometimes 1 \n");
                if(row[8] == "Rarely"):
                    oFile.write("untreatedFemalesRarely 1 \n");
                if(row[8] == "Never"):
                    oFile.write("untreatedFemalesNever 1 \n");

            #determine relationship between gender treatment and work interuptions caused by mental illnes for GQ
            if (gender == "N"):
                oFile.write("untreatedGQ 1 \n");
                if(row[8] == "Often"):
                    oFile.write("untreatedGQOften 1 \n");
                if(row[8] == "Sometimes"):
                    oFile.write("untreatedGQSometimes 1 \n");
                if(row[8] == "Rarely"):
                    oFile.write("untreatedGQRarely 1 \n");
                if(row[8] == "Never"):
                    oFile.write("untreatedGQNever 1 \n");

oFile.close();

#in-mapper combiner (I dont have a purpose for a real reducer because I only have one pc in my cluster, but the code would be pretty much the same)
#however the combiner would append combineOutput.txt instead of overwritting it and then the reducer would reduce the results on combineOutput.txt 
#and store those results in a third file. 
oFile = open("mapOutput.txt", "r")

#Goes through every line in the mapper output file and adds up all the key value pairs 
for line in oFile:
    pairType = 0
    pairCount = 0
    parseList = line.split(" ")
    pairType = parseList[0]
    pairCount = int(parseList[1]) 
     
    if(pairType == "treatedTwenties"):
        treatedTwenties = treatedTwenties + pairCount

    if(pairType == "treatedThirties"):
        treatedThirties = treatedThirties + pairCount

    if(pairType == "treatedForties"):
        treatedForties = treatedForties + pairCount

    if(pairType == "treatedFifties"):
        treatedFifties = treatedFifties + pairCount

    if(pairType == "untreatedTwenties"):
        untreatedTwenties = untreatedTwenties + pairCount

    if(pairType == "untreatedThirties"):
        untreatedThirties = untreatedThirties + pairCount

    if(pairType == "untreatedForties"):
        untreatedForties = untreatedForties + pairCount

    if(pairType == "untreatedFifties"):
        treatedForties = treatedForties + pairCount

    if(pairType == "treatedMales"):
        treatedMales = treatedMales + pairCount

    if(pairType == "untreatedMales"):
        untreatedMales = untreatedMales + pairCount

    if(pairType == "treatedFemales"):
        treatedFemales = treatedFemales + pairCount

    if(pairType == "untreatedFemales"):
        untreatedFemales = untreatedFemales + pairCount

    if(pairType == "treatedGQ"):
        treatedGQ = treatedGQ + pairCount

    if(pairType == "untreatedGQ"):
        untreatedGQ = untreatedGQ + pairCount

    if(pairType == "treatedMalesOften"):
        treatedMalesOften = treatedMalesOften + pairCount

    if(pairType == "treatedMalesSometimes"):
        treatedMalesSometimes = treatedMalesSometimes + pairCount

    if(pairType == "treatedMalesRarely"):
        treatedMalesRarely = treatedMalesRarely + pairCount

    if(pairType == "treatedMalesNever"):
        treatedMalesNever = treatedMalesNever + pairCount

    if(pairType == "untreatedMalesOften"):
        untreatedMalesOften = untreatedMalesOften + pairCount

    if(pairType == "untreatedMalesSometimes"):
        untreatedMalesSometimes = untreatedMalesSometimes + pairCount

    if(pairType == "untreatedMalesRarely"):
        untreatedMalesRarely = untreatedMalesRarely + pairCount

    if(pairType == "untreatedMalesNever"):
        untreatedMalesNever = untreatedMalesNever + pairCount

    if(pairType == "treatedFemalesOften"):
        treatedFemalesOften = treatedFemalesOften + pairCount

    if(pairType == "treatedFemalesSometimes"):
        treatedFemalesSometimes = treatedFemalesSometimes + pairCount

    if(pairType == "treatedFemalesRarely"):
        treatedFemalesRarely = treatedFemalesRarely + pairCount

    if(pairType == "treatedFemalesNever"):
        treatedFemalesNever = treatedFemalesNever + pairCount

    if(pairType == "untreatedFemalesOften"):
        untreatedFemalesOften = untreatedFemalesOften + pairCount

    if(pairType == "untreatedFemalesSometimes"):
        untreatedFemalesSometimes = untreatedFemalesSometimes + pairCount

    if(pairType == "untreatedFemalesRarely"):
        untreatedFemalesRarely = untreatedFemalesRarely + pairCount

    if(pairType == "untreatedFemalesNever"):
        untreatedFemalesNever = untreatedFemalesNever + pairCount

    if(pairType == "treatedGQOften"):
        treatedGQOften = treatedGQOften + pairCount

    if(pairType == "treatedGQSometimes"):
        treatedGQSometimes = treatedGQSometimes + pairCount

    if(pairType == "treatedGQRarely"):
        treatedGQRarely = treatedGQRarely + pairCount

    if(pairType == "treatedGQNever"):
        treatedGQNever = treatedGQNever + pairCount

    if(pairType == "untreatedGQOften"):
        untreatedGQOften = untreatedGQOften + pairCount

    if(pairType == "untreatedGQSometimes"):
        untreatedGQSometimes = untreatedGQSometimes + pairCount

    if(pairType == "untreatedGQRarely"):
        untreatedGQRarely = untreatedGQRarely + pairCount

    if(pairType == "untreatedGQNever"):
        untreatedGQNever = untreatedGQNever + pairCount
oFile.close()

#takes all the added up key-value pairs and writes them to another file ("combineOutput.txt")  
oFile = open("combineOutput.txt", "w")

oFile.write("treatedTwenties " + str(treatedTwenties) +" \n");
oFile.write("treatedThirties " + str(treatedThirties) +" \n");
oFile.write("treatedForties " + str(treatedForties) +" \n");
oFile.write("treatedFifties " + str(treatedFifties) +" \n");
oFile.write("treatedMales " + str(treatedMales) +" \n");
oFile.write("treatedFemales " + str(treatedFemales) +" \n");
oFile.write("treatedGQ " + str(treatedGQ) +" \n");
oFile.write("untreatedTwenties " + str(untreatedTwenties) +" \n");
oFile.write("untreatedThirties " + str(untreatedThirties) +" \n");
oFile.write("untreatedForties " + str(untreatedForties) +" \n");
oFile.write("untreatedFifties " + str(untreatedFifties) +" \n");
oFile.write("untreatedMales " + str(untreatedMales) +" \n");
oFile.write("untreatedFemales " + str(untreatedFemales) +" \n");
oFile.write("untreatedGQ " + str(untreatedGQ) +" \n");
oFile.write("treatedMalesOften " + str(treatedMalesOften) +" \n");
oFile.write("treatedMalesSometimes " + str(treatedMalesSometimes) +" \n");
oFile.write("treatedMalesRarely " + str(treatedMalesRarely) +" \n");
oFile.write("treatedMalesNever " + str(treatedMalesNever) +" \n");
oFile.write("untreatedMalesOften " + str(untreatedMalesOften) +" \n");
oFile.write("untreatedMalesSometimes " + str(untreatedMalesSometimes) +" \n");
oFile.write("untreatedMalesRarely " + str(untreatedMalesRarely) +" \n");
oFile.write("untreatedMalesNever " + str(untreatedMalesNever) +" \n");
oFile.write("treatedFemalesOften " + str(treatedFemalesOften) +" \n");
oFile.write("treatedFemalesSometimes " + str(treatedFemalesSometimes) +" \n");
oFile.write("treatedFemalesRarely " + str(treatedFemalesRarely) +" \n");
oFile.write("treatedFemalesNever " + str(treatedFemalesNever) +" \n");
oFile.write("untreatedFemalesOften " + str(untreatedFemalesOften) +" \n");
oFile.write("untreatedFemalesSometimes " + str(untreatedFemalesSometimes) +" \n");
oFile.write("untreatedFemalesRarely " + str(untreatedFemalesRarely) +" \n");
oFile.write("untreatedFemalesNever " + str(untreatedFemalesNever) +" \n");
oFile.write("treatedGQOften " + str(treatedGQOften) +" \n");
oFile.write("treatedGQSometimes " + str(treatedGQSometimes) +" \n");
oFile.write("treatedGQRarely " + str(treatedGQRarely) +" \n");
oFile.write("treatedGQNever " + str(treatedGQNever) +" \n");
oFile.write("untreatedGQOften " + str(untreatedGQOften) +" \n");
oFile.write("untreatedGQSometimes " + str(untreatedGQSometimes) +" \n");
oFile.write("untreatedGQRarely " + str(untreatedGQRarely) +" \n");
oFile.write("untreatedGQNever " + str(untreatedGQNever) +" \n");
oFile.close()
