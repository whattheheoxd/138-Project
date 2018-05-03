import sqlite3
import add
import view

def Admin():       #table1
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS admin (username VARCHAR(20) NOT NULL, password VARCHAR(100) NOT NULL)")
    cur.execute("INSERT INTO admin VALUES('user 1', '482c811da5d5b4bc6d497ffa98491e38')")
    data.commit()
    data.close()

def team():       #table1
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS team (team_name VARCHAR(25) PRIMARY KEY, salary_cap FLOAT NOT NULL DEFAULT 0, wins INTEGER NOT NULL DEFAULT 0,losses INTEGER NOT NULL DEFAULT 0,home_wins INTEGER NOT NULL DEFAULT 0,home_losses INTEGER NOT NULL DEFAULT 0,road_wins INTEGER NOT NULL DEFAULT 0,road_losses INTEGER NOT NULL DEFAULT 0)")
    data.commit()
    data.close()

def player():           #table2
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS player (SSN CHAR(9) primary key,f_name VARCHAR(15) NOT NULL,l_name VARCHAR(15) NOT NULL,age INTEGER NOT NULL,goals_scored INTEGER NOT NULL,goals_stopped INTEGER NOT NULL,yellow_cards INTEGER NOT NULL,red_cards INTEGER NOT NULL,minutes_played INTEGER NOT NULL,player_id INTEGER)")
    data.commit()
    data.close()

def team_captain():           #table 3
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS team_captain (date_joined DATE NOT NULL,salary INTEGER NOT NULL,jersey_number INTEGER NOT NULL,player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE,team_name VARCHAR(25) REFERENCES team(team_name) ON DELETE CASCADE)")
    data.commit()
    data.close()

def team_player():           #table 4
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS team_player (date_joined DATE NOT NULL,salary INTEGER NOT NULL,jersey_number INTEGER NOT NULL,player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE,team_name VARCHAR(25) REFERENCES team(team_name) ON DELETE CASCADE)")
    data.close()

def free_agent():           #table5
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS free_agent (date_left DATE NOT NULL,desired_salary INTEGER NOT NULL,player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE)")
    data.commit()
    data.close()

def coach():           #table 6
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS coach (SSN CHAR(9) PRIMARY KEY,f_name VARCHAR(15) NOT NULL,l_name VARCHAR(15) NOT NULL,salary INTEGER NOT NULL,c_type_no integer ,coaches VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL, FOREIGN KEY (c_type_no) REFERENCES coach_type(S_no) ON DELETE CASCADE ON UPDATE CASCADE)") # added on update constraint-aakash
    data.commit()
    data.close()

def coach_type():           #table 7
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS coach_type (S_no integer primary key, c_type VARCHAR(20))")
    data.commit()
    data.close()

def owner():               #table 8
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS owner (SSN VARCHAR(9) PRIMARY KEY,f_name VARCHAR(15) NOT NULL,l_name VARCHAR(15) NOT NULL,net_worth FLOAT NOT NULL,owns VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL)")
    data.commit()
    data.close()

def league():               #table 9
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS league (league_name VARCHAR(20) ,location VARCHAR(20) NOT NULL,title_winners VARCHAR(25),participating_team_names VARCHAR(25) NOT NULL,primary key (league_name, participating_team_names),FOREIGN KEY (participating_team_names) REFERENCES team(team_name) ON DELETE CASCADE)")
    data.commit()
    data.close()

def fixtures():          #table 10
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS fixture ( fixture_date_time datetime not null,location varchar(50) not null,winner VARCHAR(25) ,loser VARCHAR(25), home_team VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL,away_team VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL,primary key (fixture_date_time, location))")
    data.commit()
    data.close()

def match_officials():              #table 11
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS match_officials (SSN CHAR(9) primary key,match_official_name VARCHAR(20) not null,works_for VARCHAR(45) REFERENCES league(league_name) ON DELETE SET NULL)")
    data.commit()
    data.close()

def stadium():                      #table 12
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    data.commit()
    data.close()

def away_team():                      #table 13
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    data.commit()
    data.close()

def home_team():                      #table 14
    data = sqlite3.connect("Soccer.db")
    cur = data.cursor()
    data.commit()
    data.close()
