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
                   
INSERT INTO team VALUES('Barcelona', 507.5, 25, 8, 14, 2, 11, 6);
INSERT INTO team VALUES('Real Madrid', 499.3, 20, 13, 12, 6, 8, 7);
INSERT INTO team VALUES('Atletico Madrid', 237.8, 21, 13, 12, 6, 9, 7);
CREATE TABLE team_captain (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE,
                            team_name VARCHAR(25) REFERENCES team(team_name) ON DELETE CASCADE
                          );
INSERT INTO team_captain VALUES('2004-10-16', 30, 10, '000000009', 'Barcelona');
INSERT INTO team_captain VALUES('2009-07-01', 32, 7, '000000010', 'Real Madrid');
INSERT INTO team_captain VALUES('2012-06-11', 12, 2, '000000011', 'Atletico Madrid');
                          
CREATE TABLE team_player (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE,
                            team_name VARCHAR(25) REFERENCES team(team_name) ON DELETE CASCADE
                          );
                          
INSERT INTO team_player VALUES('2012-04-16', 10, 11, '000000000', 'Barcelona');
INSERT INTO team_player VALUES('2013-11-11', 11, 12, '000000001', 'Barcelona');
INSERT INTO team_player VALUES('2014-06-19', 12, 13, '000000002', 'Barcelona');
INSERT INTO team_player VALUES('2011-07-13', 18, 8, '000000003', 'Real Madrid');
INSERT INTO team_player VALUES('2013-03-09', 14, 9, '000000004', 'Real Madrid');
INSERT INTO team_player VALUES('2015-12-26', 13, 10, '000000005', 'Real Madrid');
INSERT INTO team_player VALUES('2015-06-30', 16, 3, '000000006', 'Atletico Madrid');
INSERT INTO team_player VALUES('2015-04-24', 20, 4, '000000007', 'Atletico Madrid');
INSERT INTO team_player VALUES('2015-09-18', 15, 5, '000000008', 'Atletico Madrid');
                          
CREATE TABLE free_agent (
                            date_left DATE NOT NULL,
                            desired_salary INTEGER NOT NULL,
                            player_ssn char(9) REFERENCES player(SSN) ON DELETE CASCADE
                        );
                          
INSERT INTO free_agent VALUES('2018-01-02', 25, '000000012');
INSERT INTO free_agent VALUES('2018-02-03', 19, '000000013');
                          
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
                    
INSERT INTO player VALUES('000000000', 'Anon0', 'Last0', 20, 5, 0, 2, 0, 40, 9999);
INSERT INTO player VALUES('000000001', 'Anon1', 'Last1', 21, 10, 10, 4, 1, 60, 9998);
INSERT INTO player VALUES('000000002', 'Anon2', 'Last2', 22, 15, 1, 8, 2, 80, 9997);
INSERT INTO player VALUES('000000003', 'Anon3', 'Last3', 23, 20, 0, 9, 0, 50, 9996);
INSERT INTO player VALUES('000000004', 'Anon4', 'Last4', 24, 39, 0, 15, 2, 3958, 9995);
INSERT INTO player VALUES('000000005', 'Anon5', 'Last5', 22, 48, 0, 36, 3, 2650, 9994);
INSERT INTO player VALUES('000000006', 'Anon6', 'Last6', 23, 0, 125, 8, 0, 4080, 9993);
INSERT INTO player VALUES('000000007', 'Anon7', 'Last7', 21, 87, 0, 21, 1, 6109, 9992);
INSERT INTO player VALUES('000000008', 'Anon8', 'Last8', 28, 0, 483, 9, 0, 8482, 9991);
INSERT INTO player VALUES('000000009', 'Lionel', 'Messi', 30, 608, 0, 71, 1, 54789, 1);
INSERT INTO player VALUES('000000010', 'Christiano', 'Ronaldo', 33, 652, 0, 103, 5, 64791, 2);
INSERT INTO player VALUES('000000011', 'Thiago', 'Silva', 33, 40, 0, 38, 1, 33910, 3);
INSERT INTO player VALUES('000000012', 'Jan', 'Oblak', 25, 0, 569, 9, 0, 17058, 4);
INSERT INTO player VALUES('000000013', 'David', 'De Gea', 27, 0, 643, 9, 0, 22764, 5);
                     
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
                    
INSERT INTO coach VALUES('111111111', 'Coach1', 'Name1', 10, 'Manager', 'Barcelona');
INSERT INTO coach VALUES('222222222', 'Coach2', 'Name2', 5, 'Assistant Manager', 'Barcelona');
INSERT INTO coach VALUES('333333333', 'Coach3', 'Name3', 3, 'Physical Trainer', 'Barcelona');
INSERT INTO coach VALUES('444444444', 'Coach4', 'Name4', 8, 'Manager', 'Real Madrid');
INSERT INTO coach VALUES('555555555', 'Coach5', 'Name5', 4, 'Assistant Manager', 'Real Madrid');
INSERT INTO coach VALUES('666666666', 'Coach6', 'Name6', 4, 'Physical Trainer', 'Real Madrid');
INSERT INTO coach VALUES('777777777', 'Coach7', 'Name7', 9, 'Manager', 'Atletico Madrid');
INSERT INTO coach VALUES('888888888', 'Coach8', 'Name8', 6, 'Assistant Manager', 'Atletico Madrid');
INSERT INTO coach VALUES('999999999', 'Coach9', 'Name9', 3, 'Physical Trainer', 'Atletico Madrid');
CREATE TABLE owner (
                        SSN VARCHAR(9) PRIMARY KEY,
                        f_name VARCHAR(15) NOT NULL,
                        l_name VARCHAR(15) NOT NULL,
                        net_worth FLOAT NOT NULL,
                        owns VARCHAR(25) REFERENCES team(team_name) ON DELETE SET NULL
                    );
                    
INSERT INTO owner VALUES('101010101', 'Owner1', 'Name1', 483, 'Barcelona');
INSERT INTO owner VALUES('202020202', 'Owner2', 'Name2', 952, 'Real Madrid');
INSERT INTO owner VALUES('303030303', 'Owner3', 'Name3', 569, 'Barcelona');
INSERT INTO owner VALUES('404040404', 'Owner4', 'Name4', 819, 'Atletico Madrid');
                    
CREATE TABLE league (
                        league_name VARCHAR(20) ,
                        location VARCHAR(20) NOT NULL,
                        title_winners VARCHAR(25),
                        participating_team_names VARCHAR(25) NOT NULL,
                        primary key (league_name, participating_team_names),
                        FOREIGN KEY (participating_team_names) REFERENCES team(team_name) ON DELETE CASCADE
                    );
                    
INSERT INTO league VALUES ('La Liga', 'Spain', NULL, 'Barcelona');
INSERT INTO league VALUES ('La Liga', 'Spain', NULL, 'Real Madrid');
INSERT INTO league VALUES ('La Liga', 'Spain', NULL, 'Atletico Madrid');
                    
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
                             
INSERT INTO match_officials VALUES ('123456789', 'Official', 'La Liga');
create table stadium (  
                        stadium_id char(4) primary key,
                        owning_team varchar(25),
                        location varchar(50) not null,
                        capacity integer not null,
                        FOREIGN KEY (owning_team) REFERENCES team(team_name) ON DELETE CASCADE
                     );
                     
INSERT INTO stadium VALUES ('1111', 'Barcelona', 'C. d Aristides Maillol', 99354);
INSERT INTO stadium VALUES ('2222', 'Real Madrid', 'Av. de Concha Espina', 81044);
INSERT INTO stadium VALUES ('3333', 'Atletico Madrid', 'Av. de Luis Aragones', 67703);


insert into fixture (fixture_date_time, location, team_name1, team_name2)
values ('2018-01-02', 'C. d Aristides Maillol', 'Barcelona', 'Real Madrid'), 
('2018-05-01', 'Av. de Luis Aragones', 'Atletico Madroid', 'Real Madrid'),
('2018-05-06', 'Av. de Concha Espina', 'Barcelona', 'Atletico Madrid');
