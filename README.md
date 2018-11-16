Psql Dump
====================

#### Overview

Performs a psql dump, compresses it, and drops it into a folder of your choosing.  Everything is specified in the settings.ini file.

#### Compatibility

Python 3.4+

#### Getting Started

Just run it first and it will generate a stock settings file.  From there it will exit and you can set up the settings.ini file with your information.  Then just re-run it and it will do its thing.

```
[psql]
host = somehost.com
port = 5432
user = some_user
destination = /mnt/data/backups/psql/current/
file_name = output_file.sql
db_name = some_db
```

#### Caveats

The script is designed to be run remotely against another server hosting the psql instance you wish to back up.  It also relies on having a pgpass file (see https://www.postgresql.org/docs/8.3/libpq-pgpass.html for details).

And make sure the user has permission to run a mysqldump on the instance.

Enjoy!