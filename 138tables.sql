drop database if exists soccer;
create database soccer;
use soccer;
CREATE TABLE team (
                        team_name VARCHAR(25) PRIMARY KEY,
                        salary_cap FLOAT NOT NULL DEFAULT 0,
                        wins INTEGER NOT NULL DEFAULT 0,
                        losses INTEGER NOT NULL DEFAULT 0,
                        home_wins INTEGER NOT NULL DEFAULT 0,
                        home_losses INTEGER NOT NULL DEFAULT 0,
                        road_wins INTEGER NOT NULL DEFAULT 0,
                        road_losses INTEGER NOT NULL DEFAULT 0
                   );
                   
CREATE TABLE team_captain (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE,
                            team_name VARCHAR(25) REFERENCES team(team_name) ON DELETE CASCADE
                          );
                          
CREATE TABLE team_player (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE,
                            team_name VARCHAR(25) REFERENCES team(team_name) ON DELETE CASCADE
                          );

                          
CREATE TABLE free_agent (
                            date_left DATE NOT NULL,
                            desired_salary INTEGER NOT NULL,
                            player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE
                        );

CREATE TABLE player (
                         SSN CHAR(9) primary key,
                         f_name VARCHAR(15) NOT NULL,
                         l_name VARCHAR(15) NOT NULL,
                         age INTEGER NOT NULL,
                         goals_scored INTEGER NOT NULL,
                         goals_stopped INTEGER NOT NULL,
                         yellow_cards INTEGER NOT NULL,
                         red_cards INTEGER NOT NULL,
                         minutes_played INTEGER NOT NULL,
                         player_id INTEGER
                    );

CREATE TABLE coach_type (
                            c_type VARCHAR(20) PRIMARY KEY
                        );
INSERT INTO coach_type VALUES ('Manager');
INSERT INTO coach_type VALUES ('Assistant Manager');
INSERT INTO coach_type VALUES ('Physical Trainer');
CREATE TABLE coach (
                        SSN CHAR(9) PRIMARY KEY,
                        f_name VARCHAR(15) NOT NULL,
                        l_name VARCHAR(15) NOT NULL,
                        salary INTEGER NOT NULL,
                        c_type VARCHAR(20) REFERENCES coach_type(c_type) ON DELETE SET NULL,
                        check (type in ('Manager', 'Assistant Manager', 'Physical Trainer')),
                        coaches VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL
                    );
                    

CREATE TABLE owner (
                        SSN VARCHAR(9) PRIMARY KEY,
                        f_name VARCHAR(15) NOT NULL,
                        l_name VARCHAR(15) NOT NULL,
                        net_worth FLOAT NOT NULL,
                        owns VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL
                    );
                    
                    
CREATE TABLE league (
                        league_name VARCHAR(20) ,
                        location VARCHAR(20) NOT NULL,
                        title_winners VARCHAR(25),
                        participating_team_names VARCHAR(25) NOT NULL,
                        primary key (league_name, participating_team_names),
                        FOREIGN KEY (participating_team_names) REFERENCES team(team_name) ON DELETE CASCADE
                    );

                    
CREATE TABLE user (
                   user_id VARCHAR(20) PRIMARY KEY,
                   user_name VARCHAR (20) not null,
                   birth_date date not null,
                   sex varchar(1) not null,
                   age integer not null
                 );
                 
                 
create table fixture ( 
                        fixture_date_time datetime not null,
                        location varchar(50) not null,
                        winner VARCHAR(25),
                        loser VARCHAR(25), 
                        team_name1 VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL,
                        team_name2 VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL
                    );
                    
create table match_officials (
                              SSN CHAR(9) primary key,
                              match_official_name VARCHAR(20) not null,
                              works_for VARCHAR(45) REFERENCES league(league_name) ON DELETE SET NULL
                             );
                             

create table stadium (  
                        stadium_id char(4) primary key,
                        owning_team varchar(25),
                        location varchar(50) not null,
                        capacity integer not null,
                        FOREIGN KEY (owning_team) REFERENCES team(team_name) ON DELETE CASCADE
                     );

