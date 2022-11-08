create database if not exists tourbooking;
use tourbooking;
create table if not exists BUS(
    location varchar(255) not null,
    price int not null,
    numBus int not null,
    numAvail int not null default 0,
    primary key(location)
);
create table if not exists HOTELS(
    location varchar(255)not null,
    price int not null,
    numRooms int not null,
    numAvail int not null default 0,
    primary key(location)
);
create table if not exists CUSTOMERS(
    custID int not null auto_increment,
    custName varchar(255) unique,
    custPassword varchar(255),
    primary key(custID)
);
create table if not exists RESERVATIONS(
    resvKey varchar(255) not null,
    custName varchar(255) not null,
    resvType int not null,
    primary key(resvKey,custName,resvType)
);
create table if not exists FLIGHTS(
    flightNum varchar(255) unique  not null,
    price int not null,
    numSeats int  not null,
    numAvail int default 0  not null,
    FromCity varchar(255)  not null,
    ArivCity varchar(255)  not null,
    primary key(flightNum)
);




