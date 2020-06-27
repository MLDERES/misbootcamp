# Holds all the tests for the various challenges presented in the challenges notebook.
from termcolor import colored

def assert_equal(a, b, test_name='', hint=''):
    result = a==b
    if (result):
        status = 'pass'
        msg_color = 'green'
    else:
        status = 'fail'
        msg_color = 'red'
    msg = colored(f'Test {test_name}: {status}'
                  f'\tResult: {a}. Expected {b}.', msg_color)
    if not result:
        msg += '\t'+colored(f'{hint}','red','on_white', attrs=['bold'])
    print(msg)
    
def Test_Relationships():
    family_a = [("Enid", "Susan"), ("Susan", "Deborah")]
    family_b = [('Enid', 'Susan'), ('Susan', 'Deborah'), ('Enid', 'Dianne'), ('Dianne', 'Judy'), ('Dianne', 'Fern')]

    relations(family_a,('Enid','Susan'))
    relations(family_b,('Enid','Judy'))