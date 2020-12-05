from socket import *
from variables import *
import json


def get_message(message_in_bytes):
    encode_message = message_in_bytes.recv(MAX_PACKAGE_LENGTH)

    if isinstance(encode_message, bytes):
        c_decode_message = encode_message.decode(ENCODING)
        client_message = json.loads(c_decode_message)
        if isinstance(client_message, dict):
            return client_message
        raise ValueError
    raise ValueError


def send_message(message_in_dict):
    for section, commands in client_message.items():
        if "presence" in commands:
            successful_message = {
                "response": 200,
                "error": "ОК"
            }

            encode_successful_message = json.dumps(successful_message).encode(ENCODING)
            s_socket.send(encode_successful_message)

        else:
            error_message = {
                "response": 400,
                "error": "неправильный запрос"
            }

            encode_error_message = json.dumps(error_message).encode(ENCODING)
            s_socket.send(encode_error_message)
