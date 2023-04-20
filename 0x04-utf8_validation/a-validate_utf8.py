def validUTF8(data):
    """
    Determine if the given data set represents a valid UTF-8 encoding.
    
    Args:
        data (List[int]): A list of integers representing the data to be checked.
    
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0  # Number of bytes in the current character
    for byte in data:
        # Check if the byte is a continuation byte
        if num_bytes > 0 and (byte >> 6) == 0b10:
            num_bytes -= 1
        # Check if the byte is the start of a new character
        elif num_bytes == 0:
            if (byte >> 7) == 0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        # If the byte is not a continuation byte and not the start of a new character, it's invalid
        else:
            return False
    # If there are still bytes left in a character, it's invalid
    return num_bytes == 0
