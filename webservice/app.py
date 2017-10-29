"""
Entry point for our webservice
"""
import settings
from database_client.create_database import create_database


if __name__ == '__main__':
    create_database(settings.db_path, settings.db_name)
    print('Lets build some webservices')
