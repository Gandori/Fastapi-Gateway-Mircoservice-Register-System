class DatabaseFindError(Exception):
    pass


class DatabaseInsertError(Exception):
    pass


class DatabaseUpdateError(Exception):
    pass


class DatabaseDeleteError(Exception):
    pass


class DatabaseCreateIndexError(Exception):
    pass


class DatabaseDropIndexError(Exception):
    pass


class DatabaseDropError(Exception):
    pass


class DatabaseDuplicateKeyError(Exception):
    pass
