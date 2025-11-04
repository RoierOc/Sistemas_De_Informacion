import json
import boto3

s3 = boto3.client("s3")


def handler(event, context):
    """
    Lambda que lee un objeto en S3
    event debe enviar: bucket y key
    {
        "bucket": "nombre-bucket",
        "key": "archivo.txt"
    }
    """
    bucket = event.get("bucket")
    key = event.get("key")

    if not bucket or not key:
        return {
            "statusCode": 400,
            "body": json.dumps("Falta bucket o key en el evento.")
        }

    try:
        # Obtiene el objeto de S3
        response = s3.get_object(Bucket=bucket, Key=key)

        # Lee el contenido
        contenido = response["Body"].read().decode("utf-8")
        print("Contenido del archivo:")
        print(contenido)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Archivo leído correctamente",
                "content": contenido
            })
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps("Error leyendo el archivo")
        }
