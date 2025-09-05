import qrcode

def generate_qr_code(data, filename):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code where L is about 7% or less errors can be corrected and M is about 15% or less and H is about 30% or less
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the instance
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

    print(f"QR Code generated and saved as {filename}")

n = input("Enter the data to encode in the QR Code: ")
generate_qr_code(n, "qrcode.png")