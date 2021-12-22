import os
import sqlalchemy
import pandas as pd
from sqlalchemy import Table, Column, String, MetaData, Integer
from sqlalchemy.orm import sessionmaker
import sqlite3
import logging

# Logger initialization
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

# Env variables
from dotenv import load_dotenv

# Recover env variables
load_dotenv()

# Database Location
DATABASE_LOCATION = os.getenv('DATABASE_LOCATION')

def load_data(dfs):
    """
    Function that allows loading data into the database
    """
    
    # Create the database
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    # Create the connection
    conn = sqlite3.connect('data.sqlite')
    # Create the pointer to direct to specific rows into the database
    cursor = conn.cursor()
    # Metadata object that will hold the table
    meta = MetaData(engine)
    # If the table does not exist
    insp = sqlalchemy.inspect(engine)
    # We need to extract each dataset
    athletes = dfs['athletes']
    coaches = dfs['coaches']
    gender = dfs['gender']
    medals = dfs['medals']
    teams = dfs['teams']

    print(medals)
    print(teams)

    if not insp.has_table('athletes'):
        # Create the table
        sql_create_athletes_table = Table(
            'athletes',
            meta,
            Column('id', Integer),
            Column('Name', String),
            Column('Country', String),
            Column('Discipline', String)
            )
    if not insp.has_table('coaches'):
        sql_create_coaches_table = Table(
            'coaches',
            meta,
            Column('id', Integer),
            Column('Name', String),
            Column('Country', String),
            Column('Discipline', String),
            Column('Event', String)
            )
    if not insp.has_table('gender'):
        sql_create_gender_table = Table(
            'gender',
            meta,
            Column('id', Integer),
            Column('Discipline', String),
            Column('Female', Integer),
            Column('Male', Integer),
            Column('Total', Integer)
            )
    if not insp.has_table('medals'):
        sql_create_medals_table = Table(
            'medals',
            meta,
            Column('id', Integer),
            Column('Rank', Integer),
            Column('Team/NOC', String),
            Column('Gold', Integer),
            Column('Silver', Integer),
            Column('Bronze', Integer),
            Column('Total', Integer),
            Column('Rank by Total', Integer),
            )
    if not insp.has_table('teams'):
        sql_create_teams_table = Table(
            'teams',
            meta,
            Column('id', Integer),
            Column('Name', String),
            Column('Discipline', String),
            Column('Country', String),
            Column('Event', String),
            )
    
    meta.create_all()
        
    try:
        athletes.to_sql('athletes', engine, if_exists='append')
        coaches.to_sql('coaches', engine, if_exists='append')
        gender.to_sql('gender', engine, if_exists='append')
        medals.to_sql('medals', engine, if_exists='append')
        teams.to_sql('teams', engine, if_exists='append')
    except:
        logging.info('Data already exists in the database')
    
    conn.close()

    logging.info('Close database successfully')