#
# リクエストメッセージがJSONかどうか判断するデコレータ
#
from flask import Flask, request, make_response, jsonify
import functools

def contentType(typeValue):
    def validateContentType(func):
        # 引数はそのまま渡す
        # requestのheaderを読んで、jsonでなければデコレータ内でレスポンスしてしまう
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not request.headers.get("Content-Type") == typeValue:
                error_message = {
                    'error': 'not supported Content-Type'
                }
                return make_response(jsonify(error_message), 400)

            return func(*args, **kwargs)
        
        return wrapper

    return validateContentType