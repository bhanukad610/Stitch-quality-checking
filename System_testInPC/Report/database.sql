use  id9694301_centralserver;

create table if not exists log(
    user varchar(10),
    date varchar(20),
    numOfFrames decimal(15,2),
    primary key (user,date)
);
