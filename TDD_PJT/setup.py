import pytest

@pytest.fixture()
def resource():
    print('setup')
    yield 'resource'
    print('teardown')


class TestResource:
    def test_that_depends_on_resource(self, resource):
        print('resource1')
class TestResource2:
    def test_that_depends_on_resource(self):
        print('resource2')