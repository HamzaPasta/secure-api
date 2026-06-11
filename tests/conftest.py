import pytest


@pytest.fixture(scope="session")
def anyio_backend():
    #Set default backend for async test execution
    return "asyncio"