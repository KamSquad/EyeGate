from schema import SchemaError, Schema, And, Use

answer_codes = {'success': 200,  # OK. Успешный запрос.
                                 # Ответ в виде успешного запроса.
                'object_created': 201,  # Успешный запрос. Был создан объект.
                                        # Используется, если были проведены действия на стороне сервера(добавлен объект)
                'failed': 400,  # Запрос отклонен. Запрос отклонен по причине какой-то ошибки. Смотри тело ответа.
                'login_failed': 401,  # Ошибка авторизации. Если авториз. провален.
                                      # Актуально при проверке токенов.
                'bad_url': 404,  # Ошибка написания URL. Такого адреса не существует. Если указал неправильный адрес.
                }


def make_answer_json(answer_code, body):
    ans_json = {'code': answer_code,
                'body': body}  # form answer as json
    return ans_json


def check_schema(inp_conf_schema, dict_object):
    try:
        inp_conf_schema.validate(dict_object)
        return True
    except SchemaError:
        return False


save_token_request_schema = Schema({
    'request': And(Use(str)),
    'body': {
        'auth': And(Use(str)),
        'push': And(Use(str)),
        'univer': And(Use(str)),
        'fak': And(Use(str)),
        'state': And(Use(str))
    }
})


def check_token_save_request_struct(dict_obj):
    check_res = check_schema(inp_conf_schema=save_token_request_schema,
                             dict_object=dict_obj)
    return check_res
