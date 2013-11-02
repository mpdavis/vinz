import os

from flask.ext.script import Manager, Command, Option

from app import app
from app.settings import PROJECT_NAME


class Test(Command):
    """
    Starts unit tests
    """

    start_discovery_dir = "tests"

    def get_options(self):
        return [
            Option('--start_discover', '-s', dest='start_discovery',
                help='Pattern to search for features',
                default=self.start_discovery_dir),
        ]

    def run(self, start_discovery):
        import unittest

        if os.path.exists(start_discovery):
            argv = [PROJECT_NAME, "discover"]
            argv += ["-s", start_discovery]

            unittest.main(argv=argv)
        else:
            print("Directory '%s' was not found in project root." % start_discovery)


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("test", Test())
    manager.run()