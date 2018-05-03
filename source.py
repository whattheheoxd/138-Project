import add
import view
import create
import datetime
from tabulate import tabulate
import os

first = 0

l = []
for fname in os.listdir('.'):
    l.append(fname)

if 'Soccer.db' in l:
    pass
else:
    create.team()
    create.player()
    create.team_captain()
    create.team_player()
    create.free_agent()
    create.coach_type()
    create.coach()
    create.owner()
    create.league()
    create.fixtures()
    create.match_officials()
    create.stadium()
    create.Admin()
    create.away_team()
    create.home_team()


while first >-2:
    first = input('\n'+ 'Enter a number from the following options'+'\n'+'1. Admin'+'\n'+ '2. User' + '\n' + '-1 Exit'+'\n')
    try:
        first = int(first)
    except:
        print('Enter a digit')
        first = 0
        print('\n')
    if first == 1:
        user_id = input('Enter Login ID :- ' +'\n')
        password = input('Enter password :-' + '\n')
        check = add.hashedFunction(user_id,password)
        if check == True:
            admin_loop = 1
            while admin_loop == 1:
                option = int(input("Select one of the following Admin command:- "+'\n'+'1. Add'+'\n'+'2. Update' +'\n'+'3. Delete' +'\n' +'4. Add Admin'+'\n' +'5. View'+'\n' '-1 GO BACK' +'\n'))
                if option == 1:

                    T_add = int(input('Select the table to which you want to add content'+'\n'+'1: Team'+'\n'+'2: Player'+'\n'+'3: Team Captain'+'\n'+'4: Team Player'+'\n'+ '5: Free Agent'+'\n'+'6: Coach'+'\n'+'7: Coach Type'+'\n'+'8: Owner'+'\n'+'9: League'+'\n'+'10: Fixture'+'\n'+'11: Match Officials'+'\n'+'12: Stadium'+'\n'))
                    if T_add == 1:                             #team
                        T = input('Team Name: ')
                        S = float(input('Salary Cap: '))
                        W = int(input('Wins: '))
                        L = input('Losses: ')
                        HW= int(input('Home Wins: '))
                        HL= int(input('Home Losses: '))
                        RW= int(input('Road Wins: '))
                        RL= int(input('Road Losses: '))
                        add.Add_table1(T,S,W,L,HW,HL,RW,RL)

                    elif T_add == 2:                              #player
                        SSN = input('SSN: ')
                        F = input('First Name: ')
                        L = input('Last Name: ')
                        A = int(input('Age: '))
                        GS= int(input('Goals Scored: '))
                        GT= int(input('Goals Stopped: '))
                        Y = int(input('Yellow Cards: '))
                        R = int(input('Red Cards: '))
                        M = int(input('Minutes Played: '))
                        I = int(input('Player ID: '))
                        add.Add_table2(SSN,F,L,A,GS,GT,Y,R,M,I)

                    elif T_add == 3:                              #team captain
                        print('Input format :- 2018-05-24')
                        D = input('Date Joined: ')
                        year, month, day = map(int, D.split('-'))
                        D = datetime.date(year, month, day)
                        S = int(input('Salary: '))
                        J = int(input('Jersey #: '))
                        SSN = input('Player SSN: ')
                        T = input('Team Name: ')
                        add.Add_table3(D,S,J,SSN,T)

                    elif T_add == 4:                               #team player
                        print('Input format :- year-month-date')
                        D = input('Date Joined: ')
                        year, month, day = map(int, D.split('-'))
                        D = datetime.date(year, month, day)
                        S = int(input('Salary: '))
                        J = int(input('Jersey #: '))
                        SSN = input('Player SSN: ')
                        T = input('Team Name: ')
                        add.Add_table4(D,S,J,SSN,T)

                    elif T_add == 5:                                #free agent
                        print('Input format :- year-month-date')
                        D = input('Date Left: ')
                        D = datetime()
                        S = int(input('Desired Salary: '))
                        SSN = input('Player SSN: ')
                        add.Add_table5(D,S,J,SSN,T)

                    elif T_add == 6:                             #coach
                        SSN = input('Player SSN: ')
                        F = input('First Name: ')
                        L = input('Last Name: ')
                        S = int(input('Salary: '))
                        C = input('Coaching Position: ')
                        T = input('Coaches: ')
                        add.Add_table6(SSN,F,L,S,C,T)

                    elif T_add == 7:                             #coach type
                        CT = input('Coaching Type: ')
                        add.Add_table7(CT)

                    elif T_add == 8:                             #owner
                        SSN = input('Owner SSN: ')
                        F = input('First Name: ')
                        L = input('Last Name: ')
                        N = float(input('Net Worth: '))
                        O = input('Owns: ')
                        add.Add_table8(SSN,F,L,N,O)

                    elif T_add == 9:                                   #League
                        L = input('League Name: ')
                        Lo= input('Location: ')
                        T = input('Title Winners: ')
                        P = input('Participating Team: ')
                        add.Add_table9(L,Lo,T,P)

                    elif T_add == 10:                                     #Fixture
                        print('Input format :- year-month-date')
                        F = input('Fixture Date: ')
                        year, month, day = map(int, F.split('-'))
                        F = datetime.date(year, month, day)
                        Lo= input('Location: ')
                        W = input('Winner: ')
                        L = input('Loser: ')
                        H = input('Home Team: ')
                        A = input('Away Team: ')
                        add.Add_table10(F,Lo,W,L,H,A)

                    elif T_add == 11:                                  #Match Officials
                        SSN = input('Official SSN: ')
                        N = input('Name: ')
                        W = input('Works For: ')
                        add.Add_table11(SSN, N, W)

                    elif T_add == 12:                                     #Stadium
                        S = input('Stadium ID: ')
                        O = input('Owning Team: ')
                        Lo= input('Location: ')
                        C = input('Capacity: ')
                        C = int(C)
                        add.Add_table12(S,O,Lo,C)

                    else:
                        print('Choose from above mentioned options')

                elif option == 2:
                    T_update = int(input('Select the table which you want to Update'+'\n'+'1: Team'+'\n'+'2: Player'+'\n'+'3: Team Captain'+'\n'+'4: Team Player'+'\n'+ '5: Free Agent'+'\n'+'6: Coach'+'\n'+'7: Coach Type'+'\n'+'8: Owner'+'\n'+'9: League'+'\n'+'10: Fixture'+'\n'+'11: Match Officials'+'\n'+'12: Stadium'+'\n'))

                    if T_update == 1:                             #team
                        print('Current Team Table')
                        a =view.view_team()
                        print(tabulate(a, headers = ['Team Name','Salary_cap','Wins','Losses','Home Wins','Home Losses','Away Wins','Away Losses']))
                        T = input('Team Name which you want to update: ')
                        print('Enter new data' +'\n')
                        S = float(input('Salary Cap: '))
                        W = int(input('Wins: '))
                        L = input('Losses: ')
                        HW= int(input('Home Wins: '))
                        HL= int(input('Home Losses: '))
                        RW= int(input('Road Wins: '))
                        RL= int(input('Road Losses: '))
                        add.Update_table1(T,S,W,L,HW,HL,RW,RL)
                        print('Updated Team Table')
                        a =view.view_team()
                        print(tabulate(a, headers = ['Team Name','Salary_cap','Wins','Losses','Home Wins','Home Losses','Away Wins','Away Losses']))

                    if T_update == 2:                              #player
                        print('Cureent Player Table')
                        b = view.view_players()
                        print(tabulate(b,headers = ['SSN','First Name','Last Name','Age', 'Goals Scored', 'Goals stopped','Yellow Cards','Red Cards','Minutes Played','Player Id']))
                        SSN = input('SSN of the player: ')
                        print('Enter new data' +'\n')
                        F = input('First Name: ')
                        L = input('Last Name: ')
                        A = int(input('Age: '))
                        GS= int(input('Goals Scored: '))
                        GT= int(input('Goals Stopped: '))
                        Y = int(input('Yellow Cards: '))
                        R = int(input('Red Cards: '))
                        M = int(input('Minutes Played: '))
                        I = int(input('Player ID: '))
                        add.Update_table2(SSN,F,L,A,GS,GT,Y,R,M,I)
                        print('Updated Player Table')
                        b = view.view_players()
                        print(tabulate(b,headers = ['SSN','First Name','Last Name','Age', 'Goals Scored', 'Goals stopped','Yellow Cards','Red Cards','Minutes Played','Player Id']))

                    if T_update == 3:                       #team captain
                        print('Current Team Captain Table')
                        c = view.view_team_captain()
                        print(tabulate(c, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))
                        SSN = input('Player SSN whom info you want to update: ')
                        print('Enter new data')
                        print('Input format :- 2018-05-24')
                        D = input('Date Joined: ')
                        year, month, day = map(int, D.split('-'))
                        D = datetime.date(year, month, day)
                        S = int(input('Salary: '))
                        J = int(input('Jersey #: '))
                        T = input('Team Name: ')
                        add.Update_table3(D,S,J,SSN,T)
                        print('Updated Team Captain Table')
                        c = view.view_team_captain()
                        print(tabulate(c, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))

                    if T_update == 4:                               #team player
                        print('Current Team Players Table')
                        d = view.view_team_player()
                        print(tabulate(d, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))
                        SSN = input('Player SSN whom info you want to update: ')
                        print('Enter new data')
                        print('Input format :- year-month-date')
                        D = input('Date Joined: ')
                        year, month, day = map(int, D.split('-'))
                        D = datetime.date(year, month, day)
                        S = int(input('Salary: '))
                        J = int(input('Jersey #: '))
                        T = input('Team Name: ')
                        add.Update_table4(D,S,J,SSN,T)
                        print('Updated Team Players Table')
                        d = view.view_team_player()
                        print(tabulate(d, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))

                    if T_update == 5:                                #free agent
                        print('Current Free agent Table')
                        e = view.view_free_agent()
                        print(tabulate(e,headers=('Date Left','Desired Salary', 'Player SSN')))
                        SSN = input('Player SSN whom info you want to update: ')
                        print('Enter new data')
                        print('Input format :- year-month-date')
                        D = input('Date Left: ')
                        D = datetime()
                        S = int(input('Desired Salary: '))
                        print('Updated Free Agent Table')
                        e = view.view_free_agent()
                        print(tabulate(e,headers=('Date Left','Desired Salary', 'Player SSN')))

                        add.Update_table5(D,S,J,SSN,T)

                    if T_update == 6:                             #coach
                        print('Current Coach Table')
                        f = view.view_coach()
                        print(tabulate(f,headers=('SSN','First Name','Last Name','Salary','Type','Team')))
                        SSN = input('Coach SSN whom info you want to update:  ')
                        print('Enter new data')
                        F = input('First Name: ')
                        L = input('Last Name: ')
                        S = int(input('Salary: '))
                        C = input('Coaching Position: ')
                        T = input('Coaches: ')
                        add.Update_table6(SSN,F,L,S,C,T)
                        print('Updated Coach Table')
                        f = view.view_coach()
                        print(tabulate(f,headers=('SSN','First Name','Last Name','Salary','Type','Team')))

                    if T_update == 7:                             #coach type
                        print('Curretn Coach Type table')
                        g = view.view_coach_type()
                        print(tabulate(g,headers=('Type')))
                        CT = input('Coaching Type you want to update: ')
                        CT_new = input('Enter the new coaching Type')
                        add.Update_table7(CT,CT_new)
                        print('Updated Coach Type Table')
                        g = view.view_coach_type()
                        print(tabulate(g,headers=('Type')))

                    if T_update == 8:                             #owner
                        pint('Current Owner Table')
                        h = view.view_owner()
                        print(tabulate(h,headers=('SSN','Owner F_Name','Owner L_Name','Net Worth','Team')))
                        SSN = input('Owner SSN whom info you want to update:  ')
                        print('Enter new data')
                        F = input('First Name: ')
                        L = input('Last Name: ')
                        N = float(input('Net Worth: '))
                        O = input('Owns: ')
                        add.Update_table8(SSN,F,L,N,O)
                        print('Updated Owner Table')
                        h = view.view_owner()
                        print(tabulate(h,headers=('SSN','Owner F_Name','Owner L_Name','Net Worth','Team')))

                    if T_update == 9:                                   #League
                        print('League Table :'+'\n')
                        i = view.view_league()
                        print(tabulate(i, headers=['League Name', 'Location', 'Title Winners', 'Participating Team Names']))
                        L = input('Enter League Name you want to update: ')
                        print('Enter new data')
                        Lo= input('Location: ')
                        T = input('Title Winners: ')
                        P = input('Participating Team: ')
                        add.Update_table9(L,Lo,T,P)
                        print('Updated League Table :'+'\n')
                        i = view.view_league()
                        print(tabulate(i, headers=['League Name', 'Location', 'Title Winners', 'Participating Team Names']))


                    if T_update == 10:

                        print('Enter the location and fixture date time you want to update')                                    #Fixture
                        print('Input format :- year-month-date')
                        F = input('Fixture Date: ')
                        year, month, day = map(int, F.split('-'))
                        F = datetime.date(year, month, day)
                        Lo= input('Location: ')
                        print('Enter new data')
                        W = input('Winner: ')
                        L = input('Loser: ')
                        H = input('Home Team: ')
                        A = input('Away Team: ')
                        add.Update_table10(F,Lo,W,L,H,A)

                    if T_update == 11:                                  #Match Officials
                        print('Match officials Table' +'\n')
                        k = view.view_match_officials()
                        print(tabulate(k, headers= ['SSN', 'Match Officials Name', 'Works For']))
                        SSN = input('Official SSN whom info you want to update:  : ')
                        print('Enter new data')
                        N = input('Name: ')
                        W = input('Works For: ')
                        add.Update_table11(SSN, N, W)
                        print('Updated Match officials Table' +'\n')
                        k = view.view_match_officials()
                        print(tabulate(k, headers= ['SSN', 'Match Officials Name', 'Works For']))

                    if T_update == 12:
                        print('Stadium Table')
                        l = view.view_stadiums()
                        print(tabulate(l, headers= ['Stadium Id','Owning Team', 'Location', 'Capacity']))                                    #Stadium
                        S = input('Enter Stadium ID: ')
                        print('Enter new data')
                        O = input('Owning Team: ')
                        Lo= input('Location: ')
                        C = input('Capacity: ')
                        C = int(C)
                        add.Update_table12(S,O,Lo,C)
                        print('Updated Stadium Table')
                        l = view.view_stadiums()
                        print(tabulate(l, headers= ['Stadium Id','Owning Team', 'Location', 'Capacity']))

                elif option == 3:
                    T_delte = int(input('Select the table from which you want to delete content'+'\n'+'1: Team'+'\n'+'2: Player'+'\n'+'3: Team Captain'+'\n'+'4: Team Player'+'\n'+ '5: Free Agent'+'\n'+'6: Coach'+'\n'+'7: Coach Type'+'\n'+'8: Owner'+'\n'+'9: League'+'\n'+'10: Fixture'+'\n'+'11: Match Officials'+'\n'+'12: Stadium'+'\n'))

                    if T_delte == 1:
                        a =view.view_team()
                        print(tabulate(a, headers = ['Team Name','Salary_cap','Wins','Losses','Home Wins','Home Losses','Away Wins','Away Losses']))
                        name = input('Enter team Name you want to Delete   ')
                        add.Delete_table1(name)

                    elif T_delte == 2:
                        b = view.view_players()
                        print(tabulate(b,headers = ['SSN','First Name','Last Name','Age', 'Goals Scored', 'Goals stopped','Yellow Cards','Red Cards','Minutes Played','Player Id']))
                        ssn = input('Enter Player SSN whom you want to delete   ')
                        add.Delete_table2(ssn)

                    elif T_delte == 3:
                        c = view.view_team_captain()
                        print(tabulate(c, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))
                        ssn = input('Enter Team Captain SSN whom you want to delete  ')
                        add.Delete_table3(ssn)

                    elif T_delte == 4:
                        d = view.view_team_player()
                        print(tabulate(d, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))
                        ssn = input('Enter Team Player SSN whom you want to delete  ')
                        add.Delete_table4(ssn)

                    elif T_delte == 5:
                        e = view.view_free_agent()
                        print(tabulate(e,headers=('Date Left','Desired Salary', 'Player SSN')))
                        ssn = input('Enter Free Agents SSN whom you want to delete  ')
                        add.Delete_table5(ssn)

                    elif T_delte == 6:
                        f = view.view_coach()
                        print(tabulate(f,headers=('SSN','First Name','Last Name','Salary','Type','Team')))
                        ssn = input('Enter Coach SSN whom you want to delete   ')
                        add.Delete_table6(ssn)

                    elif T_delte == 7:
                        g = view.view_coach_type()
                        print(tabulate(g,headers=['Type']))
                        typ = input('Enter Coach Typeyou want to delete   ')
                        add.Delete_table7(typ)

                    elif T_delte == 8:
                        h = view.view_owner()
                        print(tabulate(h,headers=('SSN','Owner F_Name','Owner L_Name','Net Worth','Team')))
                        ssn = input('Enter Owners SSN whom you want to delete   ')
                        add.Delete_table8(ssn)

                    elif T_delte == 9:
                        i = view.view_league()
                        print(tabulate(i, headers=['League Name', 'Location', 'Title Winners', 'Participating Team Names']))
                        l_name = input('Enter League Name you want to delete   ')
                        add.Delete_table9(l_name)

                    elif T_delte == 10:
                        j = view.view_fixtures()
                        print(tabulate(j, headers=['Date Time','Location','Winner','Loser','Home Team']))
                        location = input('Enter Location Name you want to delete   ')
                        print('Input format :- year-month-date')
                        dt = input('Enter Date Time   ')
                        add.Delete_table10(location, dt)

                    elif T_delte == 11:
                        k = view.view_match_officials()
                        print(tabulate(k, headers= ['SSN', 'Match Officials Name', 'Works For']))
                        ssn = input('Enter SSN of match_officials you want to delete   ')
                        add.Delete_table11(ssn)

                    elif T_delte == 12:
                        l = view.view_stadiums()
                        print(tabulate(l, headers= ['Stadium Id','Owning Team', 'Location', 'Capacity']))
                        s_id = input('Enter ID of Stadium you want to delete   ')
                        add.Delete_table12(s_id)

                    else:
                        print('Pick correct option')

                elif option == 4:
                    new_id = input('Enter the new user_id' +'\n')
                    new_password = input('Enter the new password'+'\n')
                    add.admin_add(new_id,new_password)

                elif option == 5:

                    T_view = int(input('Select the table you want to view'+'\n'+ '1: Team'+'\n'+'2: Player'+'\n'+'3: Team Captain'+'\n'+'4: Team Player'+'\n'+ '5: Free Agent'+'\n'+'6: Coach'+'\n'+'7: Coach Type'+'\n'+'8: Owner'+'\n'+'9: League'+'\n'+'10: Fixture'+'\n'+'11: Match Officials'+'\n'+'12: Stadium'+'\n'))

                    if T_view == 1:             #View Teams
                        a =view.view_team()
                        print(tabulate(a, headers = ['Team Name','Salary_cap','Wins','Losses','Home Wins','Home Losses','Away Wins','Away Losses']))

                    elif T_view == 2:            #View Players
                        b = view.view_players()
                        print(tabulate(b,headers = ['SSN','First Name','Last Name','Age', 'Goals Scored', 'Goals stopped','Yellow Cards','Red Cards','Minutes Played','Player Id']))

                    elif T_view == 3:             #Team Captain
                        c = view.view_team_captain()
                        print(tabulate(c, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))

                    elif T_view == 4:             #Team Players
                        d = view.view_team_player()
                        print(tabulate(d, headers=['Date Joined','Salary','Jersey Number','Player SSN','Team Name']))

                    elif T_view == 5:             #Free Agent
                        e = view.view_free_agent()
                        print(tabulate(e,headers=('Date Left','Desired Salary', 'Player SSN')))

                    elif T_view == 6:             #Coach
                        f = view.view_coach()
                        print(tabulate(f,headers=('SSN','First Name','Last Name','Salary','Type','Team')))

                    elif T_view == 7:             #Coach Type
                        g = view.view_coach_type()
                        print(tabulate(g,headers=['Type']))

                    elif T_view == 8:             #Owner
                        h = view.view_owner()
                        print(tabulate(h,headers=('SSN','Owner F_Name','Owner L_Name','Net Worth','Team')))
                    elif T_view == 9:             #League
                        i = view.view_league()
                        print(tabulate(i, headers=['League Name', 'Location', 'Title Winners', 'Participating Team Names']))

                    elif T_view == 10:               #Fixture
                        j = view.view_fixtures()
                        print(tabulate(j, headers=['Date Time','Location','Winner','Loser','Home Team']))

                    elif T_view == 11:                #Match Officials
                        k = view.view_match_officials()
                        print(tabulate(k, headers= ['SSN', 'Match Officials Name', 'Works For']))

                    elif T_view == 12:                #Stadium
                        l = view.view_stadiums()
                        print(tabulate(l, headers= ['Stadium Id','Owning Team', 'Location', 'Capacity']))

                    else:
                        print('Pick the right option')

                elif option == -1:
                    admin_loop = -1

                else:
                    print('Select from given options')
        else:
            print(check)

    # User section to view all tables
    elif first == 2:
        T_view = int(input('Select the table you want to view'+'\n'+ '1: Team'+'\n'+'2: Player'+'\n'+'3: Team Captain'+'\n'+'4: Team Player'+'\n'+ '5: Free Agent'+'\n'+'6: Coach'+'\n'+'7: Coach Type'+'\n'+'8: Owner'+'\n'+'9: League'+'\n'+'10: Fixture'+'\n'+'11: Match Officials'+'\n'+'12: Stadium'+'\n'))

        if T_view == 1:             #View Teams
            a =view.view_team()
            print(tabulate(a, headers = ['Team Name','Salary_cap','Wins','Losses','Home Wins','Home Losses','Away Wins','Away Losses']))

        if T_view == 2:            #View Players
            b = view.view_tablePlayer()
            print(tabulate(b,headers = ['First Name','Last Name','Age', 'Goals Scored', 'Goals stopped','Yellow Cards','Red Cards','Minutes Played','Player Id']))

        if T_view == 3:             #Team Captain
            c = view.view_tableCaptain()
            #print(c)
            print(tabulate(c, headers=['First Name', 'Last Name', 'Team Name', 'Jersey Number', 'Date Joined', 'Salary']))

        if T_view == 4:             #Team Players
            d = view.view_tableteamPlayer()
            print(tabulate(d, headers=['First Name', 'Last Name', 'Team Name', 'Jersey Number', 'Date Joined', 'Salary']))

        if T_view == 5:             #Free Agent
            e = view.view_tableFreeAgent()
            print(tabulate(e,headers=('First Name', 'Last Name', 'Date Left', 'Desired Salary')))

        if T_view == 6:             #Coach
            f = view.view_tableCoach()
            print(tabulate(f,headers=('First Name','Last Name','Salary','Type','Team')))

        if T_view == 7:             #Coach Type
            g = view.view_coach_type()
            print(tabulate(g,headers=['Type']))

        if T_view == 8:             #Owner
            h = view.view_tableOwner()
            print(tabulate(h,headers=('Owner F_Name','Owner L_Name','Net Worth','Team')))
        if T_view == 9:             #League
            i = view.view_league()
            print(tabulate(i, headers=['League Name', 'Location', 'Title Winners', 'Participating Team Names']))

        if T_view == 10:               #Fixture
            j = view.view_fixtures()
            print(tabulate(j, headers=['Date Time','Location','Winner','Loser','Home Team','Away Team']))

        if T_view == 11:                #Match Officials
            k = view.view_tableMatchofficials()
            print(tabulate(k, headers= ['Match Officials Name', 'Works For']))

        if T_view == 12:                #Stadium
            l = view.view_stadiums()
            print(tabulate(l, headers= ['Stadium Id','Owning Team', 'Location', 'Capacity']))

    elif first == -1:
        print('Bye')
        first = -10
    else:
        print('Enter a valid number')
