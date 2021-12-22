import os
import pandas as pd
import logging

from dotenv import load_dotenv

# Logger initialization
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

# Recover env variables
load_dotenv()

# Database Location
DATABASE_LOCATION = os.getenv('DATABASE_LOCATION')

def extract_data():
    """
    Function that allows the extract data process
    """
    # Try to import datasets
    try:
        athletes = pd.read_excel('datasets/Athletes.xlsx')
        coaches = pd.read_excel('datasets/Coaches.xlsx')
        gender = pd.read_excel('datasets/EntriesGender.xlsx')
        medals = pd.read_excel('datasets/Medals.xlsx')
        teams = pd.read_excel('datasets/Teams.xlsx')
    except:
        raise Exception(f'Something happened in the extract process')
    
    ## Rename the NOC column ##
    column_rename = {'NOC': 'Country'}

    athletes.rename(columns=column_rename, inplace=True)
    coaches.rename(columns=column_rename, inplace=True)
    teams.rename(columns=column_rename, inplace=True)

    """
    If we wanted to select certain fields which we consider are the important
    ones, we could perform that task at this point
    """

    # We grab the different datasets into a dict, in order to be able
    # To add other datasets in the future

    df_dict = {
    'athletes': athletes,
    'coaches': coaches,
    'gender': gender,
    'medals': medals,
    'teams': teams
    }

    return df_dict

