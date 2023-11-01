import boto3
import os

def generate_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def upload_to_s3(filename, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket_name, filename)
    print(f"File {filename} uploaded to {bucket_name}")

if __name__ == '__main__':
    file_name = "sample.txt"
    content = "Hello, this is a sample content for S3 upload. v.2"
    
    generate_file(file_name, content)
    upload_to_s3(file_name, "mi-nuevo-bucket-unico")  # reemplaza 'your-bucket-name' con el nombre de tu bucket

    # Limpiar: eliminar el archivo generado (opcional)
    os.remove(file_name)
