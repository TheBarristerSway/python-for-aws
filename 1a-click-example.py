import click
def greeter(**kwargs):
    output = '{0}, {1}!'.format(kwargs['greeting'],
                                kwargs['name'])
    if kwargs['caps']:
        output = output.upper()
    print(output)

@click.group()
def greet():
    pass

@greet.command()
@click.argument('name')
# add an option with 'Hello' as the default
@click.option('--greeting', default='Hello')
# add a flag (is_flag=True)
@click.option('--caps', is_flag=True)
# the application logic has been refactored into a single function
def hello(**kwargs):
    greeter(**kwargs)

@greet.command()
@click.argument('name')
@click.option('--greeting', default='Goodbye')
@click.option('--caps', is_flag=True)
def goodbye(**kwargs):
    greeter(**kwargs)

if __name__ == '__main__':
    greet()