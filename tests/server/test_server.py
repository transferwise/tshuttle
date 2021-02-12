import io
import socket

from unittest.mock import patch, Mock

import tshuttle.server


def test__ipmatch():
    assert tshuttle.server._ipmatch("1.2.3.4") is not None
    assert tshuttle.server._ipmatch("::1") is None   # ipv6 not supported
    assert tshuttle.server._ipmatch("42 Example Street, Melbourne") is None


def test__ipstr():
    assert tshuttle.server._ipstr("1.2.3.4", 24) == "1.2.3.4/24"
    assert tshuttle.server._ipstr("1.2.3.4", 32) == "1.2.3.4"


def test__maskbits():
    netmask = tshuttle.server._ipmatch("255.255.255.0")
    tshuttle.server._maskbits(netmask)


@patch('tshuttle.server.which', side_effect=lambda x: x == 'netstat')
@patch('tshuttle.server.ssubprocess.Popen')
def test_listroutes_netstat(mock_popen, mock_which):
    mock_pobj = Mock()
    mock_pobj.stdout = io.BytesIO(b"""
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG        0 0          0 wlan0
192.168.1.0     0.0.0.0         255.255.255.0   U         0 0          0 wlan0
""")
    mock_pobj.wait.return_value = 0
    mock_popen.return_value = mock_pobj

    routes = tshuttle.server.list_routes()

    assert list(routes) == [
        (socket.AF_INET, '192.168.1.0', 24)
    ]


@patch('tshuttle.server.which', side_effect=lambda x: x == 'ip')
@patch('tshuttle.server.ssubprocess.Popen')
def test_listroutes_iproute(mock_popen, mock_which):
    mock_pobj = Mock()
    mock_pobj.stdout = io.BytesIO(b"""
default via 192.168.1.1 dev wlan0  proto static
192.168.1.0/24 dev wlan0  proto kernel  scope link  src 192.168.1.1
""")
    mock_pobj.wait.return_value = 0
    mock_popen.return_value = mock_pobj

    routes = tshuttle.server.list_routes()

    assert list(routes) == [
        (socket.AF_INET, '192.168.1.0', 24)
    ]
