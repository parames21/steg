from PIL import Image
import numpy as np

def encrypt_message(img, message, password, output):
    """
    Encrypt a message into an image using steganography.
    
    Args:
        img: PIL Image object
        message: Message to encrypt
        password: Password for encryption
        output: BytesIO object for output
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

        # Calculate maximum message length
        max_length = (height * width * 3) // 8 - 20

        # Check message length
        if len(message) > max_length:
            raise ValueError(f"Message too long. Maximum {max_length} characters allowed.")

        # Add length of message at the beginning
        full_message = f"{len(message)}:{message}"

        # Initialize position trackers
        n, m, z = 0, 0, 0

        # Encrypt each character
        for char in full_message:
            if n >= height:
                raise ValueError("Message too long for this image")

            # Get ASCII value of character
            ascii_value = ord(char) & 0xFF
            
            # Modify pixel value
            img_array[n, m, z] = ascii_value

            # Update position
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1

        # Convert back to PIL Image and save to BytesIO
        encrypted_img = Image.fromarray(img_array.astype('uint8'))
        encrypted_img.save(output, format='PNG')
        
        return True

    except Exception as e:
        raise Exception(f"Encryption failed: {str(e)}")
