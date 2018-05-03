import sqlite3
import create
import view
import hashlib

def hashedFunction(user_id,password):
    pH = hashlib.md5(password.encode('utf-8'))
    pH = pH.hexdigest()
    pH = str(pH)
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * from admin WHERE username =?",(user_id,))
    U = cur.fetchall()
    data.commit()
    data.close()
    if U == []:
        Error = 'Incorrect ADMIN ID'
        return Error
    else:
        if U[0][1] == pH:
            return True
        else:
            Error = 'Incorrect Password'
            return Error

def admin_add(new_user_id,new_password):
    pH = hashlib.md5(new_password.encode('utf-8'))
    pH = pH.hexdigest()
    pH = str(pH)
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO admin VALUES (?,?)",(new_user_id,pH,))
    data.commit()
    data.close()

def Add_table1(team_name, salary_cap, wins, losses, home_wins, home_losses,road_wins,road_losses):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO team VALUES (?,?,?,?,?,?,?,?)",(team_name, salary_cap, wins, losses, home_wins, home_losses,road_wins,road_losses))
    data.commit()
    data.close()

def Add_table2(SSN, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played, player_id):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO player VALUES (?,?,?,?,?,?,?,?,?,?)",(SSN, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played, player_id))
    data.commit()
    data.close()

def Add_table3(date_joined, salary, jersey_number, player_ssn, team_name):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO team_captain VALUES (?,?,?,?,?)",(date_joined, salary, jersey_number, player_ssn, team_name))
    data.commit()
    data.close()

def Add_table4(date_joined, salary, jersey_number, player_ssn, team_name):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO team_player VALUES (?,?,?,?,?)",(date_joined, salary, jersey_number, player_ssn, team_name))
    data.commit()
    data.close()

def Add_table5(date_left, desired_salary, player_ssn):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO free_agent VALUES (?,?,?)",(date_left, desired_salary, player_ssn))
    data.commit()
    data.close()

def Add_table6(SSN,f_name,l_name,salary,c_type,coaches):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO coach VALUES (?,?,?,?,?,?)",(SSN,f_name,l_name,salary,c_type,coaches))
    data.commit()
    data.close()

def Add_table7(c_type):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO coach_type VALUES (?)",(c_type))
    data.commit()
    data.close()

def Add_table8(SSN,f_name,l_name,net_worth):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO owner VALUES (?,?,?,?)",(SSN,f_name,l_name,net_worth))
    data.commit()
    data.close()

def Add_table9(league_name,location,title_winners,participating_team_names):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO league VALUES (?,?,?,?)",(league_name,location,title_winners,participating_team_names))
    data.commit()
    data.close()

def Add_table10(fixture_date, location,winner,loser,home_team,away_team):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO fixture VALUES (?,?,?,?,?,?)",(fixture_date, location,winner,loser,home_team,away_team))
    data.commit()
    data.close()

def Add_table11(SSN,match_official_name,works_for):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO match_officials VALUES (?,?,?)",(SSN,match_official_name,works_for))
    data.commit()
    data.close()

def Add_table12(stadium_id,owning_team,location,capacity):  #parameters
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("INSERT INTO stadium VALUES (?,?,?,?)",(stadium_id,owning_team,location,capacity))
    data.commit()
    data.close()

def Delete_table1(team_name):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM team WHERE team_name=?",(team_name,))
    data.commit()
    data.close()

def Delete_table2(SSN):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM player WHERE SSN=?",(SSN,))
    data.commit()
    data.close()

def Delete_table3(SSN):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM team_captain WHERE player_ssn=?",(SSN,))
    data.commit()
    data.close()

def Delete_table4(SSN):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM team_player WHERE player_ssn=?",(SSN,))
    data.commit()
    data.close()

def Delete_table5(SSN):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM free_agent WHERE player_ssn=?",(SSN,))
    data.commit()
    data.close()

def Delete_table6(SSN):             # Table Coach
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM coach WHERE SSN=?",(SSN,))
    data.commit()
    data.close()

def Delete_table7(coach_type):          #Table Coach Types
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM coach_type WHERE c_type=?",(coach_type,))
    data.commit()
    data.close()

def Delete_table8(SSN):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM owner WHERE SSN=?",(SSN,))
    data.commit()
    data.close()

def Delete_table9(league_name):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM league WHERE league_name=?",(league_name,))
    data.commit()
    data.close()

def Delete_table10(location,fixture_date_time):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM fixtures WHERE location =?, fixture_date_time=?",(location,fixture_date_time,))
    data.commit()
    data.close()

def Delete_table11(SSN):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM match_officials WHERE SSN=?",(SSN,))
    data.commit()
    data.close()

def Delete_table12(ID):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("DELETE FROM stadium WHERE stadium_id=?",(ID,))
    data.commit()
    data.close()


def Update_table1(team_name, salary_cap, wins, losses, home_wins, home_losses,road_wins,road_losses):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE team SET salary_cap=? ,wins =?, losses =?, home_wins =?, home_losses =?, road_wins =?, road_losses =? WHERE team_name=?",(salary_cap, wins, losses, home_wins, home_losses,road_wins,road_losses, team_name) )
    data.commit()
    data.close()
     # After the admin chooses the team table to be updated, he types in the name of the team to direct to the row. Asks the user for team_name, salary_cap, wins, losses, home_wins, home_losses,road_wins,road_losses and then updates it.

def Update_table2(SSN, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played, player_id):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE player SET f_name=? ,l_name =?, age =?, goals_scored =?, goals_stopped =?, yellow_cards =?, red_cards =?, minutes_played =?, player_id =? WHERE SSN=?",(f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played, player_id, SSN) )
    data.commit()
    data.close()

    # After the admin chooses the player table to be updated, he types in the SSN of the player to direct to the row. Asks the user for SSN, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played, player_id and then updates it.

def Update_table3(date_joined, salary, jersey_number, player_ssn, team_name):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE team_captain SET date_joined=? ,salary =?, jersey_number =?, team_name =? WHERE player_ssn=?",(date_joined, salary, jersey_number, team_name, player_ssn))
    data.commit()
    data.close()

 # After the admin chooses the team_captain table to be updated, he types in the player_ssn of the player to direct to the row. Asks the user for date_joined, salary, jersey_number, player_ssn, team_name and then updates it.

def Update_table4(date_joined, salary, jersey_number, player_ssn, team_name):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE team_player SET date_joined=? ,salary =?, jersey_number =?, team_name =? WHERE player_ssn=?",(date_joined, salary, jersey_number, team_name, player_ssn))
    data.commit()
    data.close()

    # After the admin chooses the free_agent table to be updated, he types in the player_ssn of the player to direct to the row. Asks the user for date_left, desired_salary, player_ssn and then updates it.

def Update_table5(date_left, desired_salary, player_ssn):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE free_agent SET date_left=? ,desired_salary =? WHERE player_ssn=?",(date_left, desired_salary, player_ssn))
    data.commit()
    data.close()

    # After the admin chooses the team_captain table to be updated, he types in the player_ssn of the player to direct to the row. Asks the user for date_joined, salary, jersey_number, player_ssn, team_name and then updates it.

def Update_table6(SSN,f_name,l_name,salary,c_type,coaches):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE coach SET f_name=? ,l_name =?, salary =?, c_type =?, coaches =? WHERE SSN=?",(f_name, l_name,salary, c_type, coaches, SSN))
    data.commit()
    data.close()

def Update_table7(c_type, c_new):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE coach_type SET c_type=? WHERE c_type=?",(c_new,c_type))
    data.commit()
    data.close()
 # There could be some errors in this update function

def Update_table8(SSN,f_name,l_name,net_worth):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE owner SET f_name=? ,l_name =?, net_worth =? WHERE SSN=?",(f_name,l_name,net_worth, SSN))
    data.commit()
    data.close()

def Update_table9(league_name,location,title_winners,participating_team_names):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE league SET location=? ,title_winners =?, participating_team_names =? WHERE league_name=?",(location,title_winners,participating_team_names, league_name))
    data.commit()
    data.close()

def Update_table10(fixture_date, location,winner,loser,home_team,away_team):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE fixtures SET winner=? ,loser =?, home_team =?, away_team =? WHERE location=? AND fixture_date_time =?",(winner,loser,home_team,away_team, location, fixture_date))
    data.commit()
    data.close()

def Update_table11(SSN,match_official_name,works_for):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE match_officials SET match_official_name =? , works_for =? WHERE SSN =? ",(match_official_name,works_for, SSN))
    data.commit()
    data.close()

def Update_table12(stadium_id,owning_team,location,capacity):
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute ("PRAGMA foreign_keys =1")
    cur.execute("UPDATE stadium SET owning_team =? , location =?, capacity =? WHERE stadium_id =? ",(owning_team,location,capacity, stadium_id))
    data.commit()
    data.close()
