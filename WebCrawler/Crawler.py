import os


def create_directory(directory):
    if not os.path.exists(directory):
        print("Creating Directory :" + directory)
        os.makedirs(directory)


def create_files(dir_name, base_url):
    toCrawl = os.path.join(dir_name,"toCrawl.txt")
    crawled = os.path.join(dir_name,"crawled.txt")
    if not os.path.isfile(toCrawl):
        write_to_file(toCrawl, base_url)
    if not os.path.isfile(crawled):
        write_to_file(crawled, '')


def write_to_file(path, data):
    with open(path, 'w') as file:
        file.write(data)


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data+"\n")


def delete_file_data(path):
    open(path, 'w').close()


def file_to_set(file_name):
    result = set()
    with open(file_name,'rt') as file:
        for i in file:
            result.add(i.replace('\n', ''))
    return result


def set_to_file(data, file_name):
    with open(file_name, 'w') as file:
        for i in sorted(data):
            file.write(i + "\n")
