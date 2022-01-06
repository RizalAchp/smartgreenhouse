from configparser import ConfigParser


def read_db_config(filename='database.ini', section='mysql'):
    """ Membaca configurasi database menjadi object
    :param filename: nama file dari configurasi database `(path)`
    :param section: bagian configurasi dari object file `[section]`
    :return: return ke dalam parameter database
    """
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(
            '{0} not found in the {1} file'.format(section, filename))

    return db
