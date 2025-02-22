# Image Steganography Web Application

A web-based application that allows users to hide secret messages within images using steganography techniques. The application provides both encryption and decryption capabilities through a user-friendly interface.

## Features

- Encrypt messages into images without visible changes
- Decrypt hidden messages from processed images
- Support for various image formats (automatically converted to PNG)
- Password protection for message security
- Web-based interface for easy access
- Real-time error handling and validation

## Technical Details

The application uses the following technologies:
- Python 3.x
- Flask (Web Framework)
- PIL/Pillow (Image Processing)
- NumPy (Array Operations)
- HTML/CSS (Frontend)

## Installation

1. Clone the repository:
```bash
git clone [<repository-url>](https://github.com/parames21/steg.git)
cd steg
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

### Encrypting a Message

1. Navigate to the encryption page
2. Upload an image file
3. Enter your secret message
4. Set a password
5. Click "Encrypt" to download the processed image

### Decrypting a Message

1. Navigate to the decryption page
2. Upload the processed image
3. Enter the password
4. Click "Decrypt" to reveal the hidden message

## Technical Implementation

The steganography implementation works by:
- Storing message length at the beginning of the image data
- Using RGB color channels to store ASCII values
- Implementing basic password protection
- Maintaining image quality while hiding data

## Limitations

- Maximum message length depends on image dimensions
- Only supports RGB and RGBA images (automatically converted to RGB)
- Messages are encoded using ASCII (no extended character support)

## Security Considerations

This implementation is for educational purposes and demonstrates basic steganography concepts. For sensitive data, consider:
- Using more sophisticated encryption methods
- Implementing stronger password hashing
- Adding additional security layers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License


## Author

Parameswaran S
