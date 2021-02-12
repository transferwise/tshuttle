import socket

from unittest.mock import Mock, patch, call

import tshuttle.sdnotify


@patch('tshuttle.sdnotify.os.environ.get')
def test_notify_invalid_socket_path(mock_get):
    mock_get.return_value = 'invalid_path'
    assert not tshuttle.sdnotify.send(tshuttle.sdnotify.ready())


@patch('tshuttle.sdnotify.os.environ.get')
def test_notify_socket_not_there(mock_get):
    mock_get.return_value = '/run/valid_nonexistent_path'
    assert not tshuttle.sdnotify.send(tshuttle.sdnotify.ready())


@patch('tshuttle.sdnotify.os.environ.get')
def test_notify_no_message(mock_get):
    mock_get.return_value = '/run/valid_path'
    assert not tshuttle.sdnotify.send()


@patch('tshuttle.sdnotify.socket.socket')
@patch('tshuttle.sdnotify.os.environ.get')
def test_notify_socket_error(mock_get, mock_socket):
    mock_get.return_value = '/run/valid_path'
    mock_socket.side_effect = socket.error('test error')
    assert not tshuttle.sdnotify.send(tshuttle.sdnotify.ready())


@patch('tshuttle.sdnotify.socket.socket')
@patch('tshuttle.sdnotify.os.environ.get')
def test_notify_sendto_error(mock_get, mock_socket):
    message = tshuttle.sdnotify.ready()
    socket_path = '/run/valid_path'

    sock = Mock()
    sock.sendto.side_effect = socket.error('test error')
    mock_get.return_value = '/run/valid_path'
    mock_socket.return_value = sock

    assert not tshuttle.sdnotify.send(message)
    assert sock.sendto.mock_calls == [
        call(message, socket_path),
    ]


@patch('tshuttle.sdnotify.socket.socket')
@patch('tshuttle.sdnotify.os.environ.get')
def test_notify(mock_get, mock_socket):
    messages = [tshuttle.sdnotify.ready(), tshuttle.sdnotify.status('Running')]
    socket_path = '/run/valid_path'

    sock = Mock()
    sock.sendto.return_value = 1
    mock_get.return_value = '/run/valid_path'
    mock_socket.return_value = sock

    assert tshuttle.sdnotify.send(*messages)
    assert sock.sendto.mock_calls == [
        call(b'\n'.join(messages), socket_path),
    ]
