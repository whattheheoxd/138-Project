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
                        road_losses INTEGER NOT NULL DEFAULT 0,
                        no_of_players INTEGER NOT NULL DEFAULT 0
                   );
                    

CREATE TABLE team_captain (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            player_id char(9) REFERENCES player(SSN)
                          );
CREATE TABLE team_player (
                            date_joined DATE NOT NULL,
                            salary INTEGER NOT NULL,
                            jersey_number INTEGER NOT NULL,
                            player_id char(9) REFERENCES player(SSN)
                          );
CREATE TABLE free_agent (
                            date_left DATE NOT NULL,
                            desired_salary INTEGER NOT NULL,
                            player_id char(9) REFERENCES player(SSN)
                        );
                          
                          
CREATE TABLE player (
                         SSN CHAR(9) primary key,
                         p_type VARCHAR(25) NOT NULL,
                         f_name VARCHAR(15) NOT NULL,
                         l_name VARCHAR(15) NOT NULL,
                         age INTEGER NOT NULL,
                         goals_scored INTEGER NOT NULL,
                         goals_stopped INTEGER NOT NULL,
                         yellow_cards INTEGER NOT NULL,
                         red_cards INTEGER NOT NULL,
                         minutes_played INTEGER NOT NULL
                    );

                     
                     
CREATE TABLE coach_type (c_type VARCHAR(20) PRIMARY KEY);

INSERT INTO coach_type VALUES ('Manager');
INSERT INTO coach_type VALUES ('Assistant Manager');
INSERT INTO coach_type VALUES ('Physical Trainer');

CREATE TABLE coach (
                        SSN CHAR(9) PRIMARY KEY,
                        f_name VARCHAR(15) NOT NULL,
                        l_name VARCHAR(15) NOT NULL,
                        salary INTEGER NOT NULL,
                        c_type VARCHAR(20) NOT NULL,
                        check (type in ('Manager', 'Assistant Manager', 'Physical Trainer')),
                        FOREIGN KEY (c_type) REFERENCES coach_type(c_type)
                    );
                    

CREATE TABLE owner (
                        SSN VARCHAR(9) PRIMARY KEY,
                        f_name CHAR(15) NOT NULL,
                        l_name CHAR(15) NOT NULL,
                        net_worth FLOAT NOT NULL
                    );
                    
CREATE TABLE league (
                        league_name VARCHAR(20) ,
                        location VARCHAR(20) NOT NULL,
                        title_winners VARCHAR(25) NOT NULL,
                        participating_team_names VARCHAR(25) NOT NULL,
                        FOREIGN KEY (participating_team_names) REFERENCES team(team_name)
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
                        location varchar(20) not null,
                        team_name1 VARCHAR(25) REFERENCES team(team_name),
                        team_name2 VARCHAR(25) REFERENCES team(team_name)
					);
                    

create table match_officials (
                              SSN CHAR(9) primary key,
                              match_official_name VARCHAR(20) not null,
                              works_for VARCHAR(20),
                              FOREIGN KEY (works_for) REFERENCES league(league_name)
                             );

create table stadium (  
                        stadium_id char(4) primary key,
                        owning_team varchar(25),
                        location varchar(20) not null,
                        capacity integer not null,
                        FOREIGN KEY (owning_team) REFERENCES team(team_name)
                     );
                     
Insert into team (team_name, salary_cap, wins, losses, home_wins, home_losses, road_wins, road_losses, no_of_players)
values ('team_a', 10000, 1,2, 1, 1, 0, 1, 11);

Insert into team (team_name, salary_cap, wins, losses, home_wins, home_losses, road_wins, road_losses, no_of_players)
values ('team_b', 12000, 1,4, 8, 3, 2, 1, 21);

Insert into team (team_name, salary_cap, wins, losses, home_wins, home_losses, road_wins, road_losses, no_of_players)
values ('team_c', 14000, 1,6, 5, 8, 1, 5, 18);

Insert into team (team_name, salary_cap, wins, losses, home_wins, home_losses, road_wins, road_losses, no_of_players)
values ('team_d', 16000, 1,2, 4, 5, 7, 9, 17);

Insert into team (team_name, salary_cap, wins, losses, home_wins, home_losses, road_wins, road_losses, no_of_players)
values ('team_e', 18000, 1,1, 0, 0, 0, 0, 14);

insert into team_captain (date_joined, salary, jersey_number, player_id)
values (curdate(), 15000, 1, 000000001);

insert into team_captain (date_joined, salary, jersey_number, player_id)
values (curdate(), 17000, 2, 000000002);

insert into team_captain (date_joined, salary, jersey_number, player_id)
values (curdate(), 19000, 3, 000000003);

insert into team_captain (date_joined, salary, jersey_number, player_id)
values (curdate(), 21000, 4, 000000004);

insert into team_captain (date_joined, salary, jersey_number, player_id)
values (curdate(), 23000, 5, 000000005);

insert into team_player (date_joined, salary, jersey_number, player_id)
values (curdate(), 25000, 6, 000000006);

insert into team_player (date_joined, salary, jersey_number, player_id)
values (curdate(), 27000, 7, 000000001);

insert into team_player (date_joined, salary, jersey_number, player_id)
values (curdate(), 29000, 8, 000000003);

insert into team_player (date_joined, salary, jersey_number, player_id)
values (curdate(), 31000, 9, 000000002);

insert into team_player (date_joined, salary, jersey_number, player_id)
values (curdate(), 33000, 10, 000000010);

insert into free_agent (date_left, desired_salary, player_id)
values (curdate(), 35000, 000000001);

insert into free_agent (date_left, desired_salary, player_id)
values (curdate(), 37000, 000000012);

insert into free_agent (date_left, desired_salary, player_id)
values (curdate(), 39000, 000000003);

insert into free_agent (date_left, desired_salary, player_id)
values (curdate(), 41000, 000000002);

insert into free_agent (date_left, desired_salary, player_id)
values (curdate(), 43000, 000000015);

insert into player (SSN, p_type, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played)
values (000000006, 'p_type_1', 'f_name_1', 'l_name_1', 10, 1,2,3,4,5);

insert into player (SSN, p_type, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played)
values (000000001, 'p_type_2', 'f_name_2', 'l_name_2', 11, 2,3,4,5,6);

insert into player (SSN, p_type, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played)
values (000000003, 'p_type_3', 'f_name_3', 'l_name_3', 12, 4,3,4,5,7);

insert into player (SSN, p_type, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played)
values (000000019, 'p_type_4', 'f_name_4', 'l_name_4', 13, 5,3,4,6,5);

insert into player (SSN, p_type, f_name, l_name, age, goals_scored, goals_stopped, yellow_cards, red_cards, minutes_played)
values (000000002, 'p_type_5', 'f_name_5', 'l_name_5', 14, 9,0,1,5,5);

insert into coach (SSN, f_name, l_name, salary, c_type)
values (000000022, 'coach_1', 'coach_l_1',40000, 'Manager');

insert into coach (SSN, f_name, l_name, salary, c_type)
values (000000023, 'coach_2', 'coach_l_1',45000, 'Physical Trainer');

insert into coach (SSN, f_name, l_name, salary, c_type)
values (000000024, 'coach_3', 'coach_l_1',50000, 'Assistant Manager');

insert into coach (SSN, f_name, l_name, salary, c_type)
values (000000025, 'coach_1', 'coach_l_1',55000, 'Physical Trainer');

insert into coach (SSN, f_name, l_name, salary, c_type)
values (000000026, 'coach_1', 'coach_l_1',60000, 'Manager');

insert into owner (SSN, f_name, l_name, net_worth)
values (000000026, 'un', 'one', 50000);

insert into owner (SSN, f_name, l_name, net_worth)
values (000000027, 'un', 'two', 55000);

insert into owner (SSN, f_name, l_name, net_worth)
values (000000028, 'dos', 'three', 560000);

insert into owner (SSN, f_name, l_name, net_worth)
values (000000029, 'tres', 'four', 570000);

insert into owner (SSN, f_name, l_name, net_worth)
values (000000030, 'quatro', 'five', 580000);

insert into user (user_id, user_name, birth_date, sex, age)
values (12345, 'username.one', curdate(), 'M', 10);

insert into user (user_id, user_name, birth_date, sex, age)
values (12346, 'username.two', curdate(), 'F', 20);

insert into user (user_id, user_name, birth_date, sex, age)
values (12347, 'username.three', curdate(), 'M', 30);

insert into user (user_id, user_name, birth_date, sex, age)
values (12348, 'username.four', curdate(), 'F', 40);

insert into user (user_id, user_name, birth_date, sex, age)
values (123459, 'username.five', curdate(), 'M', 50);

insert into fixture (fixture_date_time, location, team_name1, team_name2)
values (current_timestamp(), 'location_one', 'team_one', 'team_five');

insert into fixture (fixture_date_time, location, team_name1, team_name2)
values (current_timestamp(), 'location_two', 'team_two', 'team_four');

insert into fixture (fixture_date_time, location, team_name1, team_name2)
values (current_timestamp(), 'location_three', 'team_three', 'team_one');

insert into fixture (fixture_date_time, location, team_name1, team_name2)
values (current_timestamp(), 'location_four', 'team_four', 'team_two');

insert into fixture (fixture_date_time, location, team_name1, team_name2)
values (current_timestamp(), 'location_five', 'team_five', 'team_three');

insert into stadium (stadium_id, owning_team, location, capacity)
values (1234, 'team_a', 'location_one', 500);

insert into stadium (stadium_id, owning_team, location, capacity)
values (5678, 'team_b', 'location_two', 600);

insert into stadium (stadium_id, owning_team, location, capacity)
values (9101, 'team_c', 'location_three', 700);

insert into stadium (stadium_id, owning_team, location, capacity)
values (1112, 'team_d', 'location_four', 800);

insert into stadium (stadium_id, owning_team, location, capacity)
values (1314, 'team_e', 'location_five', 900);

insert into league (league_name, location, title_winners, participating_team_names)
values ('league_a', 'location_a', 'team_one', 'team_one');

insert into league (league_name, location, title_winners, participating_team_names)
values ('league_a', 'location_a', 'team_one', 'team_two');

insert into match_officials (SSN, match_official_name, works_for)
values (000000001, 'first_name', 'league_a');

insert into match_officials (SSN, match_official_name, works_for)
values (000000002, 'second_name', 'league_a');

insert into match_officials (SSN, match_official_name, works_for)
values (000000003, 'third_name', 'league_a');


