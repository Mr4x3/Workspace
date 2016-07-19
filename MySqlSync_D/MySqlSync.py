#!/usr/bin/python3
import re
import sys
import os
import logging
import datetime
import optparse
import syncdb
import utils
from info import *

try:
    import MySQLdb
except ImportError:
    print("Just Install MySQLdb For Python3")
    sys.exit(1)

try:
    import schemaobject
except ImportError:
    print("Error: Missing Required Dependency SchemaObject")
    sys.exit(1)

PATCH_TPL = """--
-- MySqlSync %(app_version)s %(type)s
-- Created: %(created)s
-- Server Version: %(server_version)s
-- Apply To: %(target_host)s/%(target_database)s
--

%(data)s"""

def schemamove():
    """create a simple revert back file"""
    port="revertback.sql"




def app(sourcedb='', targetdb='', version_filename=False,
        output_directory="./results/", log_directory="./results/",
        tag=None, sync_auto_inc=True, sync_comments=False,other=None):
    """Main Powering Application"""

    options = locals()

    if not os.path.isabs(output_directory):
        print("Error: Output directory must be an absolute path. Quiting.")
        return 1

    if not os.path.isdir(output_directory):
        print("Error: Output directory does not exist. Quiting.")
        return 1

    if not log_directory or not os.path.isdir(log_directory):
        if log_directory:
            print(("Log directory does not exist, writing log to %s" % output_directory))
        log_directory = output_directory

    logging.basicConfig(filename=os.path.join(log_directory, LOG_FILENAME),
                        level=logging.INFO,
                        format= '[%(levelname)s  %(asctime)s] %(message)s')

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logging.getLogger('').addHandler(console)

    if not sourcedb:
        logging.error("Source database URL not provided. Exiting.")
        return 1

    source_info = schemaobject.connection.parse_database_url(sourcedb)
    if not source_info:
        logging.error("Invalid source database URL format. Exiting.")
        return 1

    if not source_info['protocol'] == 'mysql':
        logging.error("Source database must be MySQL. Exiting.")
        return 1

    if 'db' not in source_info:
        logging.error("Source database name not provided. Exiting.")
        return 1

    if not targetdb:
        logging.error("Target database URL not provided. Exiting.")
        return 1

    target_info = schemaobject.connection.parse_database_url(targetdb)
    if not target_info:
        logging.error("Invalid target database URL format. Exiting.")
        return 1

    if not target_info['protocol'] == 'mysql':
        logging.error("Target database must be MySQL. Exiting.")
        return 1

    if 'db' not in target_info:
        logging.error("Target database name not provided. Exiting.")
        return 1

    source_obj = schemaobject.SchemaObject(sourcedb)
    target_obj = schemaobject.SchemaObject(targetdb)

    if source_obj.version < '5.0.0':
        logging.error("%s requires MySQL version 5.0+ (source is v%s)"
                        % (APPLICATION_NAME, source_obj.version))
        return 1

    if target_obj.version < '5.0.0':
        logging.error("%s requires MySQL version 5.0+ (target is v%s)"
                % (APPLICATION_NAME, target_obj.version))
        return 1

    # data transformation filters
    filters = (lambda d: utils.REGEX_MULTI_SPACE.sub(' ', d),
                lambda d: utils.REGEX_DISTANT_SEMICOLIN.sub(';', d))

    # Information about this run, used in the patch/revert templates
    ctx = dict(app_version=APPLICATION_VERSION,
               server_version=target_obj.version,
               target_host=target_obj.host,
               target_database=target_obj.selected.name,
               created=datetime.datetime.now().strftime(TPL_DATE_FORMAT))

    p_fname, r_fname = utils.create_pnames(target_obj.selected.name,
                                           tag=tag,
                                           date_format=DATE_FORMAT)

    ctx['type'] = "Patch Script"
    pBuffer = utils.PatchBuffer(name=os.path.join(output_directory, p_fname),
                                filters=filters, tpl=PATCH_TPL, ctx=ctx.copy(),
                                version_filename=version_filename)

    ctx['type'] = "Revert Script"
    rBuffer = utils.PatchBuffer(name=os.path.join(output_directory, r_fname),
                                filters=filters, tpl=PATCH_TPL, ctx=ctx.copy(),
                                version_filename=version_filename)

    db_selected = False
    for patch, revert in syncdb.sync_schema(source_obj.selected,
                                            target_obj.selected, options):
        if patch and revert:

            if not db_selected:
                pBuffer.write(target_obj.selected.select() + '\n')
                rBuffer.write(target_obj.selected.select() + '\n')
                db_selected = True

            pBuffer.write(patch + '\n')
            #rBuffer.write(revert + '\n')

    if not pBuffer.modified:
        logging.info(("No migration scripts written."
                     " mysql://%s/%s and mysql://%s/%s were in sync.") %
                    (source_obj.host, source_obj.selected.name,
                     target_obj.host, target_obj.selected.name))
    else:
        try:
            pBuffer.save()
            #rBuffer.save()
            logging.info("Migration scripts created for mysql://%s/%s\n"
                         "Patch Script: %s"
                         % (target_obj.host, target_obj.selected.name,
                            pBuffer.name, ))#rBuffer.name))
        except OSError as e:
            pBuffer.delete()
            #rBuffer.delete()
            logging.error("Failed writing migration scripts. %s" % e)
            return 1

    return 0

def parse_cmd_line(fn):
    """Parse the command line options and pass them to the application"""

    def processor(*args, **kwargs):
        usage = """
                %prog [options] <source> <target>
                source/target format: mysql://user:pass@host:port/database"""
        description = """
                       A MySQL Schema Synchronization Utility
                      """
        parser = optparse.OptionParser(usage=usage,
                                        description=description)

        parser.add_option("-V", "--version",
                          action="store_true",
                          dest="show_version",
                          default=False,
                          help=("show version and exit."))

        parser.add_option("-r", "--revision",
                        action="store_true",
                        dest="version_filename",
                        default=False,
                        help=("increment the migration script version number "
                              "if a file with the same name already exists."))

        parser.add_option("-a", "--sync-auto-inc",
                          dest="sync_auto_inc",
                          action="store_true",
                          default=False,
                          help="sync the AUTO_INCREMENT value for each table.")

        parser.add_option("-c", "--sync-comments",
                          dest="sync_comments",
                          action="store_true",
                          default=False,
                          help=("sync the COMMENT field for all "
                                "tables AND columns"))

        parser.add_option("--tag",
                         dest="tag",
                         help=("tag the migration scripts as <database>_<tag>."
                               " Valid characters include [A-Za-z0-9-_]"))

        parser.add_option("--output-directory",
                          dest="output_directory",
                          default=os.getcwd(),
                          help=("directory to write the migration scrips. "
                                 "The default is current working directory. "
                                 "Must use absolute path if provided."))

        parser.add_option("--log-directory",
                          dest="log_directory",
                          help=("set the directory to write the log to. "
                                "Must use absolute path if provided. "
                                "Default is output directory. "
                                "Log filename is {}".format(LOG_FILENAME)))

        options, args = parser.parse_args(sys.argv[1:])


        if options.show_version:
            print((APPLICATION_NAME, __version__))
            return 0

        if (not args) or (len(args) != 2):
            parser.print_help()
            return 0

        return fn(*args, **dict(version_filename=options.version_filename,
                                 output_directory=options.output_directory,
                                 log_directory=options.log_directory,
                                 tag=options.tag,
                                 sync_auto_inc=options.sync_auto_inc,
                                 sync_comments=options.sync_comments))
    return processor


def main():
    try:
        print("Creating SQL Files")
        sys.exit(parse_cmd_line(app)())
    except schemaobject.connection.DatabaseError as e:
        logging.error("MySQL Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    except KeyboardInterrupt:
        print("Sync Interrupted, Exiting.")
        sys.exit(1)


if __name__ == "__main__":
    main()
