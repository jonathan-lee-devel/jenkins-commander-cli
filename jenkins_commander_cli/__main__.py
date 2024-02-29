"""Main import station for CLI command collections"""
import click

from jenkins_commander_cli.cli.jenkins.example.commands import jenkins_example_commands
from jenkins_commander_cli.cli.jenkins.yaml.commands import jenkins_yaml_commands
from jenkins_commander_cli.cli.jenkins.basic.commands import jenkins_basic_commands

# noinspection PyTypeChecker
cli = click.CommandCollection(sources=[
    jenkins_basic_commands,
    jenkins_example_commands,
    jenkins_yaml_commands,
])

if __name__ == '__main__':
    cli()
