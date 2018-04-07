drop database if exists soccer;
create database soccer;
use soccer;


CREATE TABLE team (
                        team_name CHAR(25) PRIMARY KEY,
                        salary_cap INTEGER NOT NULL DEFAULT 0,
                        wins INTEGER NOT NULL DEFAULT 0,
                        losses INTEGER NOT NULL DEFAULT 0,
                        home_wins INTEGER NOT NULL DEFAULT 0,
                        home_losses INTEGER NOT NULL DEFAULT 0,
                        road_wins INTEGER NOT NULL DEFAULT 0,
                        road_losses INTEGER NOT NULL DEFAULT 0,
                        no_of_players INTEGER NOT NULL DEFAULT 0
                   );
                    

CREATE TABLE team_captain (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            p_type CHAR(25) PRIMARY KEY
                          );
CREATE TABLE team_player (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            p_type CHAR(25) PRIMARY KEY
                          );
CREATE TABLE free_agent (
                            date_left DATE NOT NULL,
                            desired_salary INTEGER NOT NULL,
                            p_type CHAR(25) PRIMARY KEY
                        );
                          
                          
CREATE TABLE player (
                         SSN INTEGER PRIMARY KEY,
                         p_type CHAR(25) NOT NULL,
                         f_name CHAR(15) NOT NULL,
                         l_name CHAR(15) NOT NULL,
                         age INTEGER NOT NULL,
                         goals_scored INTEGER NOT NULL,
                         goals_stopped INTEGER NOT NULL,
                         yellow_cards INTEGER NOT NULL,
                         red_cards INTEGER NOT NULL,
                         minutes_played INTEGER NOT NULL,
                         player_id INTEGER NOT NULL,
                         team_name CHAR(25) NOT NULL,
                         player_status CHAR(15) NOT NULL,
                         FOREIGN KEY (team_name) REFERENCES team(team_name),
                         FOREIGN KEY (p_type) REFERENCES team_captain(p_type),
                         FOREIGN KEY (p_type) REFERENCES team_player(p_type),
                         FOREIGN KEY (p_type) REFERENCES free_agent(p_type)
                    );

                     
                     
CREATE TABLE coach_type (c_type CHAR(20) PRIMARY KEY);

INSERT INTO coach_type VALUES ('Manager');
INSERT INTO coach_type VALUES ('Assistant Manager');
INSERT INTO coach_type VALUES ('Physical Trainer');

CREATE TABLE coach (
                        SSN INTEGER PRIMARY KEY,
                        f_name CHAR(15) NOT NULL,
                        l_name CHAR(15) NOT NULL,
                        salary INTEGER NOT NULL,
                        c_type CHAR(20) NOT NULL,
                        check (type in ('Manager', 'Assistant Manager', 'Physical Trainer')),
                        FOREIGN KEY (c_type) REFERENCES coach_type(c_type)
                    );
                    

CREATE TABLE owner (
                        SSN INTEGER PRIMARY KEY,
                        f_name CHAR(15) NOT NULL,
                        l_name CHAR(15) NOT NULL,
                        net_worth INTEGER NOT NULL
                    );
                    
CREATE TABLE league (
                        league_name CHAR(20) PRIMARY KEY,
                        location CHAR(20) NOT NULL,
                        title_winners CHAR(25) NOT NULL,
                        participating_team_name CHAR(25) NOT NULL,
                        FOREIGN KEY (participating_team_name) REFERENCES team(team_name)
                    )