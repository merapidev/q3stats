import click

from processes.factory import ProcessFactory


def factory():
    return ProcessFactory()


@click.group()
def main():
    pass


@main.command()
def loader():
    process = factory().get(ProcessFactory.LOADER)
    process.run()


@main.command()
def parser():
    process = factory().get(ProcessFactory.PARSER)
    process.run()


if __name__ == "__main__":
    main()
