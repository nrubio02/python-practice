# Defining context managers:
import contextlib
import os
import time


# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    # Write the initialization code
    start = time.time()

    # Send control back to the context block with the 'yield' keyword
    # You can send control back with or without a value. If you send a value, you can assign that value with the 'as'
    # statement in the context block definition
    yield

    # This will get executed when the context block finishes execution
    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))


with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)


@contextlib.contextmanager
def in_dir(directory):
    """Change current working directory to `directory`,
    allow the user to run some code, and change back.

    Args:
      directory (str): The path to a directory to work in.
    """
    current_dir = os.getcwd()
    os.chdir(directory)

    # Add code that lets you handle errors
    try:
        yield
    # Ensure the directory is reset,
    # whether there was an error or not
    finally:
        os.chdir(current_dir)


with in_dir('/home'):
    print(os.getcwd())

