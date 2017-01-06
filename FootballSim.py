import sqlite3
import random
import math as m
import time

global verbose #A global printing variable, if Verbose=True, then all match and other data will be printed. Else, only the final standings of each season will be.
verbose = False
#verbose = True 

if verbose:
    print("Verbose is True, therefore all data will be printed.")
else:
    print("Verbose is False, therefore no data will be printed. Code is still running however.")

def sent_off(home_team, away_team, match_time,mult,home_s,away_s):
    num = random.random()
    #print num
    redspg=0.3
    if num < (redspg/90):
        if random.random() >= 0.50:
            #home team sending off
            if verbose: print ("{} has had a player sent off! ({}\')").format(home_team, match_time)
            home_s[9] = home_s[9] + 1
            if mult[0] > 0.2:
                mult[0] = mult[0] - 0.2
            #print ("{} mult = {}").format(home_team,mult[0])
        else:
            #away team sending off
            if verbose: print("{} has had a player sent off! ({}\')").format(away_team, match_time)
            away_s[9] = away_s[9] + 1
            if mult[0] > 0.2:
                mult[1] = mult[1] - 0.2
            #print ("{} mult = {}").format(away_team,mult[1])
    return mult


def chance(home_team, away_team, score, match_time, mult):
    num = random.random()
    #print num
    goalspg = 1.8 #2.79 apparent average
    if num < 0.65:
        #home team score
        num2 = random.random()
        if num2 < (goalspg*mult[0]/90):
            score[0] = score[0] + 1
            if verbose:
                print ("{} have scored! ({}\')").format(home_team, match_time)
                print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])

        else:
            pass

    else:
        #away team score
        num2 =random.random()
        if num2 < (goalspg*mult[1]*2/90):

            score[1] = score[1] + 1
            if verbose:
                print("{} have scored! ({}\')").format(away_team, match_time)
                print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])

        else:
            pass


    return score

def penalty(home_team, away_team, match_time, score, home_s, away_s):
    num = random.random()
    if random.random() < (0.6273):
        if verbose: print ("It's a penalty to {}! ({}\')").format(home_team, match_time)
        home_s[10] = home_s[10] + 1
        if num < (0.8443):
            score[0] = score[0] + 1
            if verbose:
                print("Wonderful penalty scored by {} - straight out of the top drawer! ({}\')").format(home_team, match_time)
                print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])
        elif num < 0.9617 and num > 0.8443:
            if verbose:
                print ("The keepers guessed right and saved it brilliantly down low!")
        elif num > 0.9617:
            if verbose:
                print ("That's a bad miss - he'll be kicking himself right now.")
                
    else:
        if verbose: print("It's a penalty to {}! ({}\')").format(away_team, match_time)
        away_s[10] = away_s[10] + 1
        if num < 0.8443:
            score[1] = score[1] + 1
            if verbose:
                print("Wonderful penalty scored by {} - straight out of the top drawer! ({}\')").format(away_team, match_time)
                print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])

        elif num < 0.9617 and num > 0.8443:
            if verbose:
                print ("The keeper's guessed right and saved it brilliantly down low!")
        else:
            if verbose:
                print ("That's a bad miss - he'll be kicking himself right now.")

    return score

def penalties(home_team, away_team):
    score = [0,0]
    for i in range(0,5):
        for j in range(0,2):
            num = random.random()
            if num < (0.8443):
                score[j] = score[j] + 1
                if verbose:
                    print("Wonderful penalty from - straight out of the top drawer!")
                    print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])
            elif (num < 0.9617 and num > 0.8443):
                if verbose:
                    print ("The keeper's guessed right and saved it brilliantly down low!")
                    print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])
                else:
                    pass
            elif (num > 0.9617):
                if verbose:
                    print ("That's a bad miss - he'll be kicking himself right now.")
                    print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])
                else:
                    pass

    if score[0] == score[1]:
        while score[0] == score[1]:
            for j in range(0,2):
                num = random.random()
                if num < (0.8443):
                    score[j] = score[j] + 1
                    if verbose:
                        print("Wonderful penalty - straight out of the top drawer!")
                        print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])

                elif num < 0.9617 and num > 0.8443:
                    if verbose:
                        print ("The keeper's guessed right and saved it brilliantly down low!")
                        print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])
                    else:
                        pass
                elif num > 0.9617:
                    if verbose:
                        print ("That's a bad miss - he'll be kicking himself right now.")
                        print "{} {}, {} {}".format(home_team, score[0], away_team, score[1])
                    else:
                        pass
    if verbose: print("Final score: {} {}, {} {}\n").format(home_team,score[0],away_team,score[1])

    return score




def matchday(home_team, away_team, minutes, league):
    try:
        con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+league+".db",timeout=11.0,check_same_thread=False)
        c = con.cursor()
    except error:
        print("Error, connection to TeamData database could not be made.\nPlease try again")



    h=(home_team,)
    a=(away_team,)

    c.execute('SELECT * FROM Teams WHERE Name=?',h)
    home_data = list(c.fetchone())
    c.execute('SELECT * FROM Teams WHERE Name=?',a)
    away_data = list(c.fetchone())

    c.execute('SELECT * FROM Standings WHERE Team=?',h)
    home_s = list(c.fetchone())
    c.execute('SELECT * FROM Standings WHERE Team=?',a)
    away_s = list(c.fetchone())


    #print home_data
    #print away_data
    if verbose:
        if minutes == 30:
            print("\nExtra time is needed!")
        else:
            print("\nTodays Match: {} vs {}").format(home_team, away_team)
            print("Attendance: {}").format(int(round(random.normalvariate(home_data[3], m.sqrt(home_data[3])))))

    match_time = 0
    score = [0]*2
    mult = [home_data[2],away_data[2]]
    extra_time = int(round(random.normalvariate(3,1.5)))

    if league != "\Cup":
        for i in home_data[4]:
            if i=="W":
                mult[0] = mult[0] + 0.15
            elif i=="D":
                pass
            elif i=="L":
                mult[0] = mult[0] - 0.12

        for i in away_data[4]:
            if i=="W":
                mult[1] = mult[1] + 0.15
            elif i=="D":
                pass
            elif i=="L":
                mult[1] = mult[1] - 0.12

    if league == "\Cup":
        if home_data[5] != away_data[5]:
            if home_data[5] == "Premier" and away_data[5] == "Championship":
                mult[1] = mult[1] - 0.35

            elif home_data[5] == "Championship" and away_data[5] == "Premier":
                mult[0] = mult[0] - 0.35



    while (match_time) <= minutes + extra_time:
        if match_time == 0:
            #print("Peep! And We're underway here at {}'s {}.\n").format(home_team,home_data[1])
            pass
        match_time = match_time + 1
        if match_time == minutes + extra_time:
            #print("That's the final whistle and it's all over!\n")
            break
        #print match_time
        mult = sent_off(home_team, away_team, match_time, mult, home_s, away_s)
        num = random.random()
        if num < (0.201/90):
            new_score = penalty(home_team, away_team, match_time, score, home_s, away_s)
        elif  num > (0.201/90):
            new_score = chance(home_team, away_team, score, match_time, mult)
        #print new_score
        score = new_score


    if verbose:
        if minutes == 30:
            pass
        else:
            print ("Final Score: {} {}, {} {}").format(home_team, score[0],away_team,score[1])

    if league != "\Cup1":
        k = (home_s[9],home_s[10],home_s[0])
        c.execute("""UPDATE Standings SET Reds = ?, Penalties = ? WHERE Team = ?""",k)

        l = (away_s[9],away_s[10],away_s[0])
        c.execute("""UPDATE Standings SET Reds = ?, Penalties = ? WHERE Team = ?""",l)

    con.commit()
    con.close()
    return score

def updater(home_team, away_team, score, league):
    try:
        con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+league+".db",timeout=11.0,check_same_thread=False)
        c = con.cursor()
    except error:
        print("Error, connection to TeamData database could not be made.\nPlease try again")

    h = (home_team,)
    a = (away_team,)
    c.execute("SELECT * FROM Standings WHERE Team = ?",h)
    home_s = list(c.fetchone())
    c.execute("SELECT * FROM Standings WHERE Team = ?",a)
    away_s = list(c.fetchone())

    f = (home_team,)
    d = (away_team,)
    c.execute("SELECT * FROM Teams WHERE Name = ?",f)
    home_d = list(c.fetchone())
    c.execute("SELECT * FROM Teams WHERE Name = ?",d)
    away_d = list(c.fetchone())

    #print home_s
    #print away_s

    home_s[1] = home_s[1] + 1 #update games played
    away_s[1] = away_s[1] + 1 #update games played

    home_s[5] = home_s[5] + score[0] #update home GF
    away_s[5] = away_s[5] + score[1] #update home GF
    home_s[6] = home_s[6] + score[1] #update away GA
    away_s[6] = away_s[6] + score[0] #update away GA

    if score[0] > score[1]:
        #home win
        home_s[2] = home_s[2] + 1 #update games won
        away_s[4] = away_s[4] + 1 #update games lost
        home_s[8] = home_s[8] + 3 #update points
        home_d[4] = home_d[4][:4] + "W" #update form
        away_d[4] = away_d[4][:4] + "L" #update form

    elif score[0] == score[1]:
        #draw
        home_s[8] = home_s[8] + 1 #update points
        away_s[8] = away_s[8] + 1 #update points
        home_s[3] = home_s[3] + 1 #update games drawn
        away_s[3] = away_s[3] + 1 #update games drawn
        home_d[4] = home_d[4][:4] + "D" #update form
        away_d[4] = away_d[4][:4] + "D" #update form

    else:
        #away win
        away_s[8] = away_s[8] + 3 #update points
        away_s[2] = away_s[2] + 1 #update games won
        home_s[4] = home_s[4] + 1 #update games lost
        away_d[4] = away_d[4][:4] + "W"
        home_d[4] = home_d[4][:4] + "L"

    home_s[7] = home_s[5] - home_s[6]
    away_s[7] = away_s[5] - away_s[6] #calculating goal difference

    k = (home_s[1],home_s[2],home_s[3],home_s[4],home_s[5],home_s[6],home_s[7],home_s[8],home_s[9],home_s[10],home_s[0])
    c.execute("""UPDATE Standings SET Played = ?, Won = ?, Drawn = ?, Lost = ?, GF = ?, GA = ?, GD = ?, Points = ?, Reds = ?, Penalties = ? WHERE Team = ?""",k)

    #time.sleep(2)

    l = (away_s[1],away_s[2],away_s[3],away_s[4],away_s[5],away_s[6],away_s[7],away_s[8],away_s[9],away_s[10],away_s[0])
    c.execute("""UPDATE Standings SET Played = ?, Won = ?, Drawn = ?, Lost = ?, GF = ?, GA = ?, GD = ?, Points = ?, Reds = ?, Penalties = ? WHERE Team = ?""",l)

    z = (home_d[4], home_d[0])
    c.execute("UPDATE Teams SET Form = ? WHERE Name = ?",z)

    x = (away_d[4],away_d[0])
    c.execute("UPDATE Teams SET Form = ? WHERE Name = ?",x)

    total_goals = []
    total_reds=[]
    total_pens=[]

    if verbose: print "\nTeam\tPlayed\tWon\tDrawn\tLost\tGF\tGA\tGD\tPoints\n-------------------------------------------------------------------------"
    for i, row in enumerate(c.execute("SELECT * FROM Standings ORDER BY Points DESC, GD DESC, GF DESC")):
        if verbose: print ("{}\t | {}\t{}\t{}\t{}\t{}\t{}\t{}\t{}").format(row[0][:5],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        total_goals.append(row[5])
        total_reds.append(row[9])
        total_pens.append(row[10])
        if league == "\Championship":
            if  i==1 or i==5 or i==20:
                if verbose: print ("-------------------------------------------------------------------------")
        elif league == "\Premier":
            if i==0 or i==3 or i==16:
                if verbose: print ("-------------------------------------------------------------------------")
        elif league == "\League_1":
            if i==1 or i==5 or i==19:
                if verbose: print ("-------------------------------------------------------------------------")
        elif league == "\League_2":
            if  i==2 or i==6 or i==20:
                if verbose: print ("-------------------------------------------------------------------------")

    if verbose: print "\n"

    con.commit()
    con.close()

    return sum(total_goals),sum(total_reds),sum(total_pens)

def season(league):
    try:
        con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+league+".db",timeout=11.0, check_same_thread=False)
        c = con.cursor()

    except error:
        print("Error, connection to TeamData database could not be made.\nPlease try again")

    data = (0,0,0,0,0,0,0,0,0,0)
    data2 = ("",)
    c.execute("""UPDATE Standings SET Played=?, Won=?, Drawn=?, Lost=?, GF=?, GA=?, GD=?, Points=?, Reds=?, Penalties=?;""",data)
    c.execute("""UPDATE Teams SET Form=?""",data2)


    c.execute("SELECT Name FROM Teams")
    team_column = c.fetchall()
    team_list=[]
    for row in team_column:
        team_list.append(list(row)[0])

    con.commit()
    con.close()

    match_list = []

    #print team_list
    counter = 0
    for i, item in enumerate(team_list):
        for j, jtem in enumerate(team_list):
            if item != jtem:
                match_list.append([item,jtem])
                #nothing = raw_input("Press \'Enter\' to continue to next matchday: ")
                #print ("{} vs {}").format(item,jtem)


    random.shuffle(match_list)
    for item in match_list:
        score = matchday(item[0],item[1],90,league)
        total_goals,total_reds,total_pens = updater(item[0],item[1],score,league)
        counter = counter + 1
        if (counter == 380 and league == "\Premier") or (counter == 552 and league != "\Premier"):
            if verbose: print ("""Average goals per game = {0:.2f}\nAverage reds per game = {1:.2f}\nAverage penalties per match = {2:.2f}\n""").format((total_goals*1.0/counter),(total_reds*1.0/counter),(total_pens*1.0/counter))


    try:
        con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+league+".db",timeout=11.0,check_same_thread=False)
        c = con.cursor()
    except sqlite3.OperationalError:
        print("Error, connection to TeamData database could not be made.\nPlease try again")


    final_standings = []
    rel_teams =[]
    pro_teams=[]

    for row in c.execute("SELECT * FROM Standings ORDER BY Points DESC, GD DESC, GF DESC"):
        final_standings.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]])

    print "\nTeam\tPlayed\tWon\tDrawn\tLost\tGF\tGA\tGD\tPoints\n-------------------------------------------------------------------------"
    for i, row in enumerate(c.execute("SELECT * FROM Standings ORDER BY Points DESC, GD DESC, GF DESC")):
        print ("{}\t | {}\t{}\t{}\t{}\t{}\t{}\t{}\t{}").format(row[0][:5],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        if league == "\Championship":
            if i==0 or i==1 or i==5 or i==20:
                print"-------------------------------------------------------------------------"

        elif league == "\Premier":
            if i==0 or i==3 or i==16:
                print"-------------------------------------------------------------------------"

        elif league == "\League_1":
            if i==0 or i==1 or i==5 or i==19:
                print"-------------------------------------------------------------------------"

        elif league == "\League_2":
            if i==0 or i==2 or i==6 or i==21:
                print"-------------------------------------------------------------------------"


    playoffs = []
    po_final =[]

    if league == "\Premier":
        po_winner=""
    if league != "\Premier":
        if verbose: print("It's time for the playoffs to determine the final team to be promoted!")
        po_start = 2
        po_end = 6
        if league == "\League_2":
            po_start = 3
            po_end = 7
        for i, item in enumerate(final_standings):
            if (i >= po_start) and (i < po_end):
                playoffs.append(item[0])
                #print "got here"

        for i in range(0,2,1):
            home_score = matchday(playoffs[i],playoffs[i+2],90,league)
            away_score = matchday(playoffs[i+2],playoffs[i],90,league)
            semi_score = [a + b for a, b in zip(home_score, away_score[::-1])]

            #print semi_score1, semi_score2

            if semi_score[0] > semi_score[1]:
                po_final.append(playoffs[i])
            elif semi_score[1] > semi_score[0]:
                po_final.append(playoffs[i+2])
            elif semi_score[0] == semi_score[1]:
                score = matchday(playoffs[i+2],playoffs[i],30,league)
                if score[1] > score[0]:
                    po_final.append(playoffs[i])
                elif score[1] < score[0]:
                    po_final.append(playoffs[i+2])
                elif score[1] == score[0]:
                    pens = penalties(playoffs[i],playoffs[i+2])
                    if pens[0] > pens[1]:
                        po_final.append(playoffs[i])
                    else:
                        po_final.append(playoffs[i+2])

        #print po_final

        po_winner = ""
        final_score = matchday(po_final[0],po_final[1],90,league)
        if final_score[0] > final_score[1]:
            po_winner = po_final[0]
        elif final_score[1] > final_score[0]:
            po_winner = po_final[1]
        elif final_score[0] == final_score[1]:
            score = matchday(po_final[0],po_final[1],30,league)
            if score[1] > score[0]:
                po_winner = po_final[0]
            elif score[1] < score[0]:
                po_winner = po_final[1]
            elif score[1] == score[0]:
                pens = penalties(po_final[0],po_final[1])
                if pens[0] > pens[1]:
                    po_winner = po_final[0]
                else:
                    po_winner = po_final[1]


    #print po_winner
    #
    # final_standings.append([po_winner,0])

    for i, item in enumerate(final_standings):
        c.execute("SELECT * FROM Teams WHERE Name=?",(item[0],))
        data = list(c.fetchone())
        if league == "\Premier":
            if i > 16:
                rel_teams.append(data)

        elif league == "\Championship":
            if (i>=0 and i < 2):
                pro_teams.append(data)
            elif item[0] == po_winner:
                pro_teams.append(data)
            elif i > 20:
                rel_teams.append(data)

        elif league == "\League_1":
            if (i>=0 and i < 2):
                pro_teams.append(data)
            elif item[0] == po_winner:
                pro_teams.append(data)
            elif i > 19:
                rel_teams.append(data)

        elif league == "\League_2":
            if (i>=0 and i < 3):
                pro_teams.append(data)
            elif item[0] == po_winner:
                pro_teams.append(data)


    con.commit()
    con.close()
    #print final_standings

    return final_standings, pro_teams, rel_teams

    #print counter


def cup():
    # make league database with all teams
    league = "\Cup"
    try:
        con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+league+".db",timeout=11.0, check_same_thread=False)
        c = con.cursor()

    except error:
        print("Error, connection to TeamData database could not be made.\nPlease try again")

    c.execute("SELECT Name FROM Teams")
    team_column = c.fetchall()
    con.commit()
    con.close()

    team_list=[]
    #odd_team=""
    for row in team_column:
        team_list.append(list(row)[0])

    random.shuffle(team_list)

    power = 0
    i = 0

    while i < len(team_list):
        i = 2**power
        power = power + 1

    bye_num = i - len(team_list)
    bye_teams = team_list[bye_num:]
    team_list = team_list[:bye_num]

    #print len(bye_teams),len(team_list)

    for item in range(0,len(bye_teams),2):
        score = matchday(bye_teams[item],bye_teams[item+1],90,league)
        if verbose: print"\n"
        if score[0] > score[1]:
            team_list.append(bye_teams[item])
        elif score[1] > score[0]:
            team_list.append(bye_teams[item+1])
        else:
            #print "Extra time needed."
            ET_score = matchday(bye_teams[item],bye_teams[item+1],30,league)
            score = [score[a]+ET_score[a] for a in xrange(len(score))]
            if verbose: print("Score after extra time: {} {}, {} {}\n").format(bye_teams[item],score[0],bye_teams[item+1],score[1])
            if score[0] > score[1]:
                team_list.append(bye_teams[item])
            elif score[1] > score[0]:
                team_list.append(bye_teams[item+1])
            else:
                if verbose: print("Scores even after ET - penalties needed!")
                score = penalties(bye_teams[item],bye_teams[item+1])
                if score[0] > score[1]:
                    team_list.append(bye_teams[item])
                elif score[1] > score[0]:
                    team_list.append(bye_teams[item+1])


    while len(team_list) > 1:
        winners=[]
        for item in range(0,len(team_list),2):
            score = matchday(team_list[item],team_list[item+1],90,league)
            if verbose: print"\n"
            if score[0] > score[1]:
                winners.append(team_list[item])
            elif score[1] > score[0]:
                winners.append(team_list[item+1])
            else:
                #print "Extra time needed."
                ET_score = matchday(team_list[item],team_list[item+1],30,league)
                score = [score[a]+ET_score[a] for a in xrange(len(score))]
                if verbose: print("Score after extra time: {} {}, {} {}\n").format(team_list[item],score[0],team_list[item+1],score[1])
                if score[0] > score[1]:
                    winners.append(team_list[item])
                elif score[1] > score[0]:
                    winners.append(team_list[item+1])
                else:
                    if verbose: print("Scores even after ET - penalties needed!")
                    score = penalties(team_list[item],team_list[item+1])
                    if score[0] > score[1]:
                        winners.append(team_list[item])
                    elif score[1] > score[0]:
                        winners.append(team_list[item+1])
        team_list = winners
        if len(team_list) == 2:
            if verbose: print("It's {} vs {} in the final of the FootballSim Cup at Wembley!\n").format(team_list[0],team_list[1])
        #print team_list
        #print("\nLength of team_list = {}\n").format(len(team_list))

    return team_list[0]

def league_updater():
    league_list = ["\Premier","\Championship","\League_1","\League_2"]
    for item in league_list:
        try:
            con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+item+".db",timeout=11.0, check_same_thread=False)
            c = con.cursor()

        except error:
            print("Error, connection to TeamData database could not be made.\nPlease try again")

        league_teams = []
        #print item
        for row in c.execute('SELECT Team FROM Standings'):
            league_teams.append((item[1:],row[0]))
        #print league_teams
        con.commit()
        con.close()

        try:
            con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim\Cup.db",timeout=11.0, check_same_thread=False)
            c = con.cursor()

        except error:
            print("Error, connection to TeamData database could not be made.\nPlease try again")

        for i in league_teams:
            c.execute("UPDATE Teams SET League = ? WHERE Name = ?",i)

        con.commit()
        con.close()

def league_changes(rel_prem, pro_cham, rel_cham, pro_lg1, rel_lg1, pro_lg2):
    league_list = ["\Premier","\Championship","\League_1", "League_2"]
    for item in league_list:
        try:
                con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+item+".db",timeout=11.0, check_same_thread=False)
                c = con.cursor()

        except error:
                print("Error, connection to TeamData database could not be made.\nPlease try again")

        if item == "\Premier":
            for i in pro_cham:
                k = (i[0],0,0,0,0,0,0,0,0,0,0)
                j = (i[0],i[1],i[2]-0.25 ,i[3])
                c.execute("""INSERT INTO Standings VALUES(?,?,?,?,?,?,?,?,?,?,?)""",k)
                c.execute("""INSERT INTO Teams VALUES(?,?,?,?,NULL)""",j)

        if item == "\Championship":
            for i in rel_prem:
                k = (i[0],0,0,0,0,0,0,0,0,0,0)
                j = (i[0],i[1],i[2]+0.25,i[3])
                c.execute("""INSERT INTO Standings VALUES(?,?,?,?,?,?,?,?,?,?,?)""",k)
                c.execute("""INSERT INTO Teams VALUES(?,?,?,?,NULL)""",j)
            for i in pro_lg1:
                k = (i[0],0,0,0,0,0,0,0,0,0,0)
                j = (i[0],i[1],i[2]-0.25,i[3])
                c.execute("""INSERT INTO Standings VALUES(?,?,?,?,?,?,?,?,?,?,?)""",k)
                c.execute("""INSERT INTO Teams VALUES(?,?,?,?,NULL)""",j)

        if item == "\League_1":
            for i in rel_cham:
                k = (i[0],0,0,0,0,0,0,0,0,0,0)
                j = (i[0],i[1],i[2]+0.25,i[3])
                c.execute("""INSERT INTO Standings VALUES(?,?,?,?,?,?,?,?,?,?,?)""",k)
                c.execute("""INSERT INTO Teams VALUES(?,?,?,?,NULL)""",j)
            for i in pro_lg2:
                k = (i[0],0,0,0,0,0,0,0,0,0,0)
                j = (i[0],i[1],i[2]-0.25,i[3])
                c.execute("""INSERT INTO Standings VALUES(?,?,?,?,?,?,?,?,?,?,?)""",k)
                c.execute("""INSERT INTO Teams VALUES(?,?,?,?,NULL)""",j)

        if item == "\League_2":
            for i in rel_lg1:
                k = (i[0],0,0,0,0,0,0,0,0,0,0)
                j = (i[0],i[1],i[2]+0.25,i[3])
                c.execute("""INSERT INTO Standings VALUES(?,?,?,?,?,?,?,?,?,?,?)""",k)
                c.execute("""INSERT INTO Teams VALUES(?,?,?,?,NULL)""",j)
 
        con.commit()
        con.close()

    for item in league_list:
        try:
                con = sqlite3.connect("C:\Users\Niall\Documents\Misc\Football Sim"+item+".db",timeout=11.0, check_same_thread=False)
                c = con.cursor()

        except error:
                print("Error, connection to TeamData database could not be made.\nPlease try again")

        if item == "\Premier":
            for i in rel_prem:
                k = (i[0],)
                c.execute("""DELETE FROM Standings WHERE Team=?""",k)
                c.execute("""DELETE FROM Teams WHERE Name=?""",k)

        if item == "\Championship":
            for i in pro_cham:
                k = (i[0],)
                c.execute("""DELETE FROM Standings WHERE Team=?""",k)
                c.execute("""DELETE FROM Teams WHERE Name=?""",k)
            for i in rel_cham:
                k = (i[0],)
                c.execute("""DELETE FROM Standings WHERE Team=?""",k)
                c.execute("""DELETE FROM Teams WHERE Name=?""",k)

        if item == "\League_1":
            for i in pro_lg1:
                k = (i[0],)
                c.execute("""DELETE FROM Standings WHERE Team=?""",k)
                c.execute("""DELETE FROM Teams WHERE Name=?""",k)
            for item in rel_lg1:
                k = (i[0],)
                c.execute("""DELETE FROM Standings WHERE Team=?""",k)
                c.execute("""DELETE FROM Teams WHERE Name=?""",k)

        if item == "\League_2":
            for i in pro_lg2:
                k = (i[0],)
                c.execute("""DELETE FROM Standings WHERE Team=?""",k)
                c.execute("""DELETE FROM Teams WHERE Name=?""",k)

        con.commit()
        con.close()



if __name__ == "__main__":
    begin = time.time()
    league_updater()

    winner = cup()
    final_standings_pr, pro_pr, rel_pr = season("\Premier")
    final_standings_ch, pro_ch, rel_ch = season("\Championship")
    final_stadnings_lg1, pro_lg1, rel_lg1 = season("\League_1")
    final_standings_lg2, pro_lg2, rel_lg2 = season("\League_2")
    
    print("Promoted from Championship: {}, {}, {}\n").format(pro_ch[0][0],pro_ch[1][0],pro_ch[2][0])
    print("Promoted from League 1: {}, {}, {}\n").format(pro_lg1[0][0],pro_lg1[1][0],pro_lg1[2][0])
    print("Promoted from League 2: {}, {}, {}, {}\n").format(pro_lg2[0][0],pro_lg2[1][0],pro_lg2[2][0], pro_lg2[3][0])
    print("Relegated from Premier League: {}, {}, {}\n").format(rel_pr[0][0],rel_pr[1][0],rel_pr[2][0])
    print("Relegated from Championship: {}, {}, {}\n").format(rel_ch[0][0],rel_ch[1][0],rel_ch[2][0])
    print("Relegated from League 1: {}, {}, {}, {}\n").format(rel_lg1[0][0],rel_lg1[1][0],rel_lg1[2][0], rel_lg1[3][0])

    #league_changes(rel_pr,pro_ch,rel_ch,pro_lg1,rel_lg1,pro_lg2)

    end = time.time()
    print("Winner of the 2016/17 FootballSim Cup is {}!").format(winner)
    print("Winner of the 2016/17 FootballSim Championship is {}!").format(final_standings_ch[0][0])
    print("Winner of the 2016/17 FootballSim Premier League is {}!").format(final_standings_pr[0][0])
    print("Winner of the 2016/17 FootballSim League 1 is {}!").format(final_stadnings_lg1[0][0])
    print("Winner of the 2016/17 FootballSim League 2 is {}!").format(final_standings_lg2[0][0])


    print("Seasons and cup took {} seconds to complete.").format(round(end-begin,2))


    
else:
    print("Called from import, code will not run until function directly called.")
