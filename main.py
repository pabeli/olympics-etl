from utils.extract_data import extract_data
from utils.transformation import check_if_no_empty_data
from utils.load import load_data
import logging

# Logger initialization
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

if __name__ == '__main__':
    # The extract process
    logging.info('Starting data extract...')
    dfs = extract_data()
    # Transformation process
    logging.info('Starting validation process...')
    dfs = check_if_no_empty_data(dfs)
    # Loading into database
    logging.info('Starting load process...')
    load_data(dfs)
