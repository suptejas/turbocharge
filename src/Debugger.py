import click
from sys import platform

class Debugger:
    def debug(self, password: str, error: bytes):
        error = error.decode('utf-8')

        if 'sudo: 1 incorrect password attempt' in error:
            click.echo(
                click.style(
                    '✅ Successful Debugging! ✅ \n',
                    fg='green',
                    bold=True))
            click.echo(
                click.style(
                    f'Cause: Wrong Password Entered. Code: 001',
                    fg='yellow',
                    bold=True,
                    blink=True))

            return

        elif platform == 'darwin':
            click.echo(
                click.style(
                    '✅ Successful Debugging! ✅ \n',
                    fg='green',
                    bold=True))
            click.echo(
                click.style(
                    f'Cause: Incompatible Platform. Turbocharge doesn\'t support macOS yet. Code: 005',
                    fg='yellow',
                    bold=True,
                    blink=True))

            return

        elif platform == 'win32':
            click.echo(
                click.style(
                    '✅ Successful Debugging! ✅ \n',
                    fg='green',
                    bold=True))
            click.echo(
                click.style(
                    f'Cause: Incompatible Platform. Turbocharge doesn\'t support Windows 10/8/7/XP yet. Code: 010',
                    fg='yellow',
                    bold=True,
                    blink=True))

            return

        else:
            click.echo(click.style(':( Failed To Debug... :(', fg='red'))

            return
