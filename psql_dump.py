# __author__ = 'Chris Eby'

from configparser import ConfigParser
from os import path
from subprocess import Popen, PIPE
import shlex


def main():
    config_file = 'settings.ini'

    # Check if the ini file exists, create if not
    if not path.isfile(config_file):
        create_ini(config_file)
        print(config_file, ' not found, a default one has been created.  Set it up and then re-run.')
        quit()

    # Read in all the settings
    config = ConfigParser()
    config.read(config_file)
    host = config.get('psql', 'host')
    port = config.get('psql', 'port')
    user = config.get('psql', 'user')
    destination = config.get('psql', 'destination')
    file_name = config.get('psql', 'file_name')
    db_name = config.get('psql', 'db_name')

    print('Running psql_dump')
    cmd = 'pg_dump -h ' + host + ' -p ' + port + ' -U ' + user + ' -f ' + file_name + ' ' + db_name
    print(cmd)
    run_cmd(cmd)

    print('Creating tarball')
    run_cmd('tar -cf ' + file_name + '.tar ' + file_name)

    print('Zipping tarball')
    run_cmd('gzip -f ' + file_name + '.tar')

    print('Removing dump file')
    run_cmd('rm ' + file_name)

    print('Moving zipped tarball to destination')
    run_cmd('mv ' + file_name + '.tar.gz ' + destination)


def run_cmd(cmd):
    process = Popen(shlex.split(cmd), stdout=PIPE)
    dump_output = process.communicate()[0]
    exit_code = process.wait()
    if exit_code != 0:
        print(dump_output)
        raise Exception(str(exit_code) + ' - Error executing command.  Please review output.')


def create_ini(config_file):
    config = ConfigParser()
    config['psql'] = {
        'host': 'somehost.com',
        'user': 'some_user',
        'port': '5432',
        'destination': '/mnt/data/backups/psql/current/',
        'file_name': 'output_file.sql',
        'db_name': 'some_db'
    }
    with open(config_file, 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    main()