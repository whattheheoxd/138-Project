import sqlite3
import create
import add

def view_team():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM team")
    rows = cur.fetchall()
    data.close()
    return rows

def view_players():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM player")
    rows = cur.fetchall()
    data.close()
    return rows

def view_team_captain():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM team_captain")
    #select f_name as First_Name, l_name as Last_name, t.team_name  from team_captain c join team t join player p where c.team_name = t.team_name and c.player_ssn = p.SSN
    rows = cur.fetchall()
    data.close()
    return rows

def view_team_player():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM team_player")
    rows = cur.fetchall()
    data.close()
    return rows

def view_free_agent():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM free_agent")
    rows = cur.fetchall()
    data.close()
    return rows

def view_coach():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM coach")
    rows = cur.fetchall()
    data.close()
    return rows

def view_coach_type():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM coach_type")
    rows = cur.fetchall()
    data.close()
    return rows

def view_owner():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM owner")
    rows = cur.fetchall()
    data.close()
    return rows

def view_league():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM league")
    rows = cur.fetchall()
    data.close()
    return rows

def view_fixtures():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM fixture")
    rows = cur.fetchall()
    data.close()
    return rows

def view_match_officials():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM match_officials")
    rows = cur.fetchall()
    data.close()
    return rows

def view_stadiums():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM stadium")
    rows = cur.fetchall()
    data.close()
    return rows

def view_tableCaptain():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT f_name as First_Name, l_name as Last_name, team_name, jersey_number, date_joined, salary from team_captain AS c join player AS p WHERE c.player_ssn=p.SSN")
    rows = cur.fetchall()
    data.close()
    return rows

def view_tablePlayer():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played, player_id from player")
    rows = cur.fetchall()
    data.close()
    return rows

def view_tableteamPlayer():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT f_name as First_Name, l_name as Last_name, team_name, jersey_number, date_joined, salary from team_player AS c join player AS p WHERE c.player_ssn=p.SSN")
    rows = cur.fetchall()
    data.close()
    return rows

def view_tableFreeAgent():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT f_name as First_Name, l_name as Last_name, date_left, desired_salary from free_agent AS c join player AS p WHERE c.player_ssn=p.SSN")
    rows = cur.fetchall()
    data.close()
    return rows

def view_tableCoach():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT f_name, l_name, salary, c_type, coaches from coach")
    rows = cur.fetchall()
    data.close()
    return rows

def view_tableOwner():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT f_name, l_name, net_worth, owns from owner")
    rows = cur.fetchall()
    data.close()
    return rows


def view_tableMatchofficials():
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("SELECT match_official_name,works_for from match_officials")
    rows = cur.fetchall()
    data.close()
    return rows
