class ErrorMessage:

    BAD_REQUEST = "field missing"
    UNAUTHORIZED = "unauthorized"
    NOT_FOUND = "not found"
    INTERNAL_ERROR = "internal error"
    ALREADY_EXISTS = "already exists"

    

    DB_CONNECTION = "db connection error"
    DB_GET_CONNECTION_POOL = "db get connection from pool error"
    DB_CLOSE_CURSOR_CONNECTION = "db close cursor error"
    DB_PUT_CONNECTION_TO_POOL = "db put connection to pool error"
    DB_SELECT = "db select error"

    REDIS_CONNECTION = "redis connection error"
    REDIS_SISMEMBER = "redis membership error"
    REDIS_SET = "redis SET error"
    REDIS_GET = "redis GET error"

    INVESTOR_REPO_ERROR_LOGS = "investor repo error log"