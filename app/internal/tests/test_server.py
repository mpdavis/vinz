
from app.models.server import Server
from app import internal


class TestInternalServer:

    def setup(self):
        self.server1 = Server(name='server1', hostname='server1.test.com')
        self.server1.save()
        self.server2 = Server(name='server2', hostname='server2.test.com')
        self.server2.save()

    def teardown(self):
        Server.drop_collection()

    def test_get_servers(self):
        servers = internal.server.get_servers()
        assert len(servers) == 2
        assert self.server1 in servers
        assert self.server2 in servers

    def test_get_server(self):
        server = internal.server.get_server(self.server1.id)
        assert server.hostname == 'server1.test.com'

    def test_delete_server(self):
        internal.server.delete_server(self.server1.id)
        servers = list(Server.objects.all())
        assert len(servers) == 1
        assert self.server1 not in servers