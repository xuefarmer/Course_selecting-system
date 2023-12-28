drop table STUDENTS cascade;
drop table TEACHERS cascade ;
drop table COURSES;
drop table CHOICES;
CREATE TABLE STUDENTS(
	sid char(9) NOT NULL PRIMARY KEY,
	sname varchar(30) NOT NULL,
	email varchar(30) NULL,
	grade int NULL,
	password varchar(30));
	

CREATE TABLE TEACHERS(
	tid char(9) NOT NULL PRIMARY KEY,
	tname varchar(30) NOT NULL,
	email varchar(30) NULL,
	salary int NULL);
	
	
CREATE TABLE COURSES(
	cid char(5) NOT NULL PRIMARY KEY,
	cname varchar(30) NOT NULL,
	hour int NULL);
	
CREATE TABLE CHOICES(
	no int NOT NULL PRIMARY KEY,
	sid char(9) NOT NULL,
	tid char(9) NOT NULL,
	cid char(5) NOT NULL,
	score int NULL,
CONSTRAINT FK_CHOICES_COURSES FOREIGN KEY(cid) REFERENCES COURSES (cid),
CONSTRAINT FK_CHOICES_STUDENTS FOREIGN KEY(sid) REFERENCES STUDENTS (sid),
CONSTRAINT FK_CHOICES_TEACHERS FOREIGN KEY(tid) REFERENCES TEACHERS (tid));









