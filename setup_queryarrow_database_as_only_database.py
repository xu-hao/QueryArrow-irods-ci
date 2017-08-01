from __future__ import print_function

import os
import shutil

from irods.configuration import IrodsConfig
from irods import paths

def main():
#    shutil.copy(os.path.join(paths.config_directory(), 'core.py.template'), os.path.join(paths.config_directory(), 'core.py'))

    irods_config = IrodsConfig()
    irods_config.server_config['plugin_configuration']['database'] = {
            "postgres": {
                "db_host": "localhost",
                "db_name": "ICAT",
                "db_odbc_driver": "PostgreSQL ANSI",
                "db_password": "testpassword",
                "db_port": 5432,
                "db_username": "irods"
            }
        }
    irods_config.commit(irods_config.server_config, irods_config.server_config_path, make_backup=True)

if __name__ == '__main__':
    main()
