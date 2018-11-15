import pytest
from scheduler import Task

@pytest.fixture
def task_init():
    arg = ('7:00', '8:00', 'have breakfast', 'tomato,milk,bread', 5, 0.85,
        {'qxc', 'daidai'})
    return Task(*arg)

def test_task_init(task_init):
    task2 = Task()
    assert task_init['id'] == 1
    assert task_init['s_time'] == '7:00'
    assert task_init['e_time'] == '8:00'
    assert task_init['title'] == 'have breakfast'
    assert task_init['content'] == 'tomato,milk,bread'
    assert task_init['level'] == 5
    assert task_init['percent'] == 0.85
    assert task_init['users'] == {'qxc', 'daidai'}
    assert task2['id'] == 2
    print(task_init, task2)

def test_task_match(task_init):
    assert task_init.match('have') == True
    assert task_init.match('tomato') == True
    assert task_init.match('milks') == False

