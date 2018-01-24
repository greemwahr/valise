import boto3
import zipfile
import StringIO
import mimetypes

s3 = boto3.resource('s3')

valise_bucket = s3.Bucket('valise.sherifolanrewaju.be')
build_bucket = s3.Bucket('valisebuild.sherifolanrewaju.be')

valise_zip = StringIO.StringIO()
build_bucket.download_fileobj('valisebuild.zip', valise_zip)

with zipfile.ZipFile(valise_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        valise_bucket.upload_fileobj(obj, nm,
            ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        valise_bucket.Object(nm).Acl().put(ACL='public-read')