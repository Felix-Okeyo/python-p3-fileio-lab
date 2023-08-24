def write_file(file_name, file_content):
    """
    Write the given content to a file with the provided name.

    Args:
        file_name (str): The name of the file to be written.
        file_content (str): The content to be written to the file.
    """
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as file:   
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Append the given content to an existing file with the provided name.

    Args:
        file_name (str): The name of the file to which content will be appended.
        append_content (str): The content to be appended to the file.
    """
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Read and return the content of the file with the provided name.

    Args:
        file_name (str): The name of the file to be read.

    Returns:
        str: The content of the file.
    """
    with open(f'{file_name}.txt', mode='r', encoding='utf-8') as file:
        return file.read()
