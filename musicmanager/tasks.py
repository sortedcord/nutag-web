from celery import shared_task

# -- Tutorial / Demo Tasks --
# To be removed when writing actual code
@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)
