
from ansible.runner import Runner
from ansible.inventory import Inventory


def test():
    """
    Simple test to ping all of the hosts.
    """

    # Eventually, this will be need to be pulled out of the database.
    # Just need to make a list of hosts.  DNS names and IPv4 addresses.  No IPv6.
    hosts = ['test.example.com']

    inventory = Inventory(hosts)

    # TODO: We need to find a way to handle the private key file.
    runner = Runner(
        pattern='*',
        module_name='ping',
        inventory=inventory,
        remote_user='root',
        private_key_file='/path/to/key/id_rsa'
    )

    results = runner.run()
    print results
