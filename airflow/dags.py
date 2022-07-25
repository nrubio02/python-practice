# To define a DAG:
import time

from airflow import DAG
from datetime import datetime, timedelta
# Operator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
# Sensor
from airflow.contrib.sensors.file_sensor import FileSensor
# Branching
from airflow.operators.python_operator import BranchPythonOperator

# attributes to components of DAG
default_arguments = {
    'owner': 'jdoe',
    'email': 'j́doe@data.com',
    'start_date': datetime(2020, 1, 20),
    'sla': timedelta(seconds=30)  # DAG-wide SLA
}

with DAG('etl_workflow', default_args=default_arguments) as etl_dag:
    # OPERATORS
    # These represent a single task in a workflow

    # # BashOperator
    example_task = BashOperator(task_id='bash_ex',
                                bash_command='echo 1',
                                dag=etl_dag)


    # # PythonOperator
    # Let's define the function to call:
    def printme():
        print("This goes in the logs!")


    python_task = PythonOperator(task_id='simple_print',
                                 python_callable=printme,
                                 dag=etl_dag)


    def sleep(length_of_time):
        time.sleep(length_of_time)


    # When the function has keyword parameters,
    # you can use the op_kwargs dictionary to pass the arguments to the function
    sleep_task = PythonOperator(task_id='sleep',
                                python_callable=sleep,
                                op_kwargs={'length_of_time': 5},
                                dag=etl_dag)

    # Task dependencies
    task1 = BashOperator(task_id='first_task',
                         bash_command='echo 1',
                         dag=etl_dag)

    task2 = BashOperator(task_id='second_task',
                         bash_command='echo 2',
                         dag=etl_dag)

    # Set first_task to run before second_task
    task1 >> task2  # or task2 << task1

    # SENSORS
    # special type of operator, can be also bitshift
    # FileSensor checks for existence of a file
    file_sensor_task = FileSensor(task_id='file_sense',
                                  filepath='salesdata.csv',
                                  poke_interval=300,  # in seconds
                                  dag=etl_dag)

    # SLAs
    # Using the 'sla' argument on the task:
    task1 = BashOperator(task_id='sla_task',
                         bash_command='runcode.sh',
                         sla=timedelta(seconds=30),
                         dag=etl_dag)

    # Or can be set for the whole DAG in the default_args dictionary. (See the dict definition at the top)
    # You can also configure email notification on success, failure and retry from the default_args dictionary.

    # TEMPLATES
    # Define the templated command:
    templated_command = """
    echo "Reading {{ params.filename }}"
    """

    # Pass a params dictionary with the
    templated_task = BashOperator(task_id="templatedTask",
                                  bash_command=templated_command,
                                  params={'filename': 'file1.txt'},
                                  dag=etl_dag)

    # Templates with looping
    templated_command = """
      <% for filename in params.filenames %>
      bash cleandata.sh {{ ds_nodash }} {{ filename }};
      <% endfor %>
    """

    filelist = [f'file{x}.txt' for x in range(30)]

    # Modify clean_task to use the templated command
    clean_task = BashOperator(task_id='cleandata_task',
                              bash_command=templated_command,
                              params={'filenames': filelist},
                              dag=etl_dag)

    # Branching
    # Define the python_callable that returns the next task:
    def branch_test(**kwargs):
        if int(kwargs['ds_nodash']) % 2 == 0:
            return 'even_day_task'
        else:
            return 'odd_day_task'

    branch_task = BranchPythonOperator(task_id='branch_task',
                                       dag=etl_dag,
                                       provide_context=True,  # This tells airflow to provide access to the runtime
                                                              # variables and macros to the function
                                       python_callable=branch_test)

    # assuming the tasks are already created, we define dependencies like:
    # start_task >> branch_task >> even_day_task >> even_day_task_2
    # branch_task >> odd_day_task >> odd_day_task_2

    # Apparently, you can also group tasks in a list when defining dependencies for branching operators:
    # python_task >> branch_task >> [email_report_task, no_email_task]