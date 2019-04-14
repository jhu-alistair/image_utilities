def get_config(key):
    import yaml
    configs = []
    with open('config.yaml', 'r') as stream:
        try:
            configs = yaml.safe_load(stream)
            return configs[key]
        except yaml.YAMLError as exc:
            print(exc)

def confirm_config(key):
    print('\n\nUsing ' + key +':')
    print(get_config(key)+'\n')
    path_ok  = input('OK to proceed? Y/N?: ')
    if path_ok.lower().strip() == 'y':
        return True
    else:
        return

def get_template():
    try:
        with open('template.txt', 'r') as template:
                return template.read().splitlines()
    except IOError as e:
       print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
       print("Unexpected error:", sys.exc_info()[0])


def confirm_template():
    lines = []
    lines = get_template()
    print('\n\nUsing file template:\n')
    for ln in lines:
        print(ln)
    template_ok = input('\nOK to proceed? Y/N: ')
    if template_ok.lower().strip() == 'y':
        return True
    else:
        return False
