"""Master Configuration
"""


from buildbot.plugins import changes
from buildbot.plugins import schedulers
from buildbot.plugins import steps
from buildbot.plugins import util
from buildbot.plugins import worker


def print_hello():
    """Print hello
    """
    print("Hello, World!")


def builders() -> list:
    """Buildbot Factories and Builders for Jobs.
    """
    bb_builders: list = []

    factory = util.BuildFactory()
    factory.addStep(steps.ShellCommand(command=["echo", "Hello,", "World!"]))

    bb_builders.append(util.BuilderConfig(name="helloworld",
                                          workernames=["local-worker"],
                                          factory=factory))

    return bb_builders
