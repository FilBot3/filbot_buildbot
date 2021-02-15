"""Master Configuration
"""


# from buildbot.plugins import changes
from buildbot.plugins import schedulers
from buildbot.plugins import steps
from buildbot.plugins import util
# from buildbot.plugins import worker


def bb_builders() -> list:
    """Buildbot Factories and Builders for Jobs.
    """
    bb_builds: list = []

    factory = util.BuildFactory()
    factory.addStep(steps.ShellCommand(command=["echo", "Hello,", "World!"]))

    bb_builds.append(util.BuilderConfig(name="helloworld",
                                        workernames=["local-worker"],
                                        factory=factory))

    return bb_builds


def bb_schedulers() -> list:
    """Buildbot Schedulers to run the Builders.
    """
    bb_schedules: list = []

    bb_schedules.append(schedulers.ForceScheduler(
        name="force",
        builderNames=["helloworld"]))

    return bb_schedules
