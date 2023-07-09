import json



def read_json(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())
def write_json(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

def main():
    d = {'fileroot': 'g:/program_code/PY/TODO_tools/todolist/', 'filename': 'todo.json'}
    write_json(d['fileroot']+d['filename'], d)
if __name__ == '__main__':
    main()

