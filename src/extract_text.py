from .log import logger

logger.info(__file__)

def extract_text(file):
    """
    Read the content of a text file and return it as a string.

    Parameters:
    - file: gr.File object (the uploaded file).

    Returns:
    - str: The content of the file.
    """
    # Check if the file is valid
    if not file :
        logger.error("File is not valid")
        return ""
    # Read the content of the file
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        logger.info("File content: " + content)
    # Return the content as a string
    return content