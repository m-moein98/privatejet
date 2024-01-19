"""
Command-line interface for the package.
"""
import argparse
import os
import shutil


class CLI:
    """
    Class for the command-line interface.
    """

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="Command-line interface for the package."
        )
        self.subparsers = self.parser.add_subparsers(
            title="subcommands", dest="subcommand", help="Subcommand to run"
        )

        self.create_project_parser = self.subparsers.add_parser(
            "create_project", help="Create a create_project app"
        )
        self.create_project_parser.add_argument(
            "--name", required=True, help="Name of the app"
        )

    def create_project(self, args: argparse.Namespace) -> None:
        """
        Create a new project
        """
        if not os.path.exists(args.name):
            os.mkdir(args.name)
        shutil.copyfile(
            os.path.join(os.path.dirname(__file__), "boilerplates/main.py"),
            os.path.join(os.getcwd(), args.name, "main.py"),
        )

    def run(self) -> None:
        """
        Run the command-line interface.
        """
        args = self.parser.parse_args()

        if args.subcommand == "create_project":
            self.create_project(args)
        else:
            print("Unknown command. Use --help for usage information.")


if __name__ == "__main__":
    CLI().run()
