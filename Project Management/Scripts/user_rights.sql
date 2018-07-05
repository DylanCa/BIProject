CREATE USER C##generator IDENTIFIED BY OraclePassword;
CREATE ROLE  C##role_generator;

GRANT SELECT ANY TABLE TO C##role_generator;
GRANT UPDATE, INSERT ON Orders TO  C##role_generator;
GRANT UPDATE, INSERT ON CandyReferences TO  C##role_generator;
GRANT UPDATE, INSERT ON Stock TO  C##role_generator;

GRANT  C##role_generator TO C##generator;

CREATE USER C##talend IDENTIFIED BY password2;


CREATE ROLE C##role_talend;
GRANT SELECT ANY TABLE TO C##talend;
GRANT C##role_talend TO C##talend;
