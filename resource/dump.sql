BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone txst, website test, regdate test);
INSERT INTO "users" VALUES(1,'kim','kim@naver.com','010-000-0000','kim.com','2022-04-22 08:10:13');
INSERT INTO "users" VALUES(2,'park','park@daum.net','010-1111-1111','Park.com','2022-04-22 08:10:13');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2022-04-22 08:10:13');
INSERT INTO "users" VALUES(4,'cho','Cho@daum.net','010-3333-3333','Cho.com','2022-04-22 08:10:13');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@google.com','010-4444-4444','Yoo.net','2022-04-22 08:10:13');
COMMIT;
