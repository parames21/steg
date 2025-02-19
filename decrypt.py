from PIL import Image
import numpy as np

def decrypt_message(img, password):
    """
    Decrypt a message from an image using steganography.
    
    Args:
        img: PIL Image object
        password: Password for decryption
    
    Returns:
        str: Decrypted message if successful
        
    Raises:
        ValueError: If image cannot be loaded or message format is invalid
    """
    try:
        # Convert PIL Image to numpy array
        img_array = np.array(img)
        
        # Convert to RGB if image is in RGBA mode
        if img_array.shape[-1] == 4:  # If image has alpha channel
            img = img.convert('RGB')
            img_array = np.array(img)

        # Get image dimensions
        height, width = img_array.shape[:2]
        
        # Initialize position trackers
        n, m, z = 0, 0, 0
        
        # First, extract the message length
        length_str = ""
        while True:
            if n >= height:
                raise ValueError("Invalid message format")
                
            # Get ASCII value from pixel
            ascii_value = img_array[n, m, z]
            char = chr(ascii_value)
            
            if char == ':':
                break
                
            length_str += char
            
            # Update position
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1
        
        # Move to next position after colon
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= width:
                m = 0
                n += 1
        
        try:
            message_length = int(length_str)
        except ValueError:
            raise ValueError("Invalid message length format")

        # Extract the message
        message = ""
        for _ in range(message_length):
            if n >= height:
                raise ValueError("Message length exceeds image bounds")
                
            # Get ASCII value from pixel
            ascii_value = img_array[n, m, z]
            message += chr(ascii_value)
            
            # Update position
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1
        
        # Validate password (you might want to implement a more secure validation)
        if not message:
            raise ValueError("No message found in image")
            
        return message

    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
