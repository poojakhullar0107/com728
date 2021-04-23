import sqlite3


def setup():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
    BEGIN TRANSACTION;
    CREATE TABLE countries (
        id   INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE organisations (
        id   INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL,
        location_id  INTEGER NOT NULL,
        FOREIGN KEY("location_id") REFERENCES "locations"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE  events (
        id   INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL,
        type TEXT NOT NULL CHECK("type" IN ("presentation", "workshop", "seminar")),
        host_id  INTEGER NOT NULL,
        FOREIGN KEY("host_id") REFERENCES "organisations"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE presenters (
        id   INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL,
        organisation_id  INTEGER NOT NULL,
        FOREIGN KEY("organisation_id") REFERENCES "organisations"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE locations (
        id   INTEGER NOT NULL UNIQUE,
        city TEXT NOT NULL,
        country_id   INTEGER NOT NULL,
        FOREIGN KEY("country_id") REFERENCES "countries"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE event_presenters (
        event_id INTEGER NOT NULL,
        presenter_id INTEGER NOT NULL,
        FOREIGN KEY("presenter_id") REFERENCES "presenters"("id"),
        FOREIGN KEY("event_id") REFERENCES "events"("id"),
        PRIMARY KEY("event_id","presenter_id")
    );
    INSERT INTO "countries" ("id","name") VALUES (1,'United Kingdom');
    INSERT INTO "organisations" ("id","name","location_id") VALUES (1,'Solent University',1);
    INSERT INTO "events" ("id","name","type","host_id") VALUES (1,'Ai Workshop','workshop',1);
    INSERT INTO "presenters" ("id","name","organisation_id") VALUES (1,'pooja',1);
    INSERT INTO "locations" ("id","city","country_id") VALUES (1,'Southampton',1);
    INSERT INTO "event_presenters" ("event_id","presenter_id") VALUES (1,1);
    COMMIT;
    """
    cursor.executescript(sql)
    db.commit()

