import os
import boto3
import tempfile
import zipfile
import uuid

# boto3.setup_default_session(profile_name='vivek-us-east-1')
s3 = boto3.resource('s3',  region_name='us-east-1')


def _zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), arcname=file)


def _random_filename():
    return "resumes_{}.zip".format(uuid.uuid4())


def download_and_upload(resumeUrls):
    with tempfile.TemporaryDirectory() as tmpdirname:
        for resumeUrl in resumeUrls:
            url = resumeUrl["resumeUrl"]
            filename = "{}_{}.pdf".format(
                resumeUrl["studentCollegeId"], resumeUrl["studentName"])
            print("Downloading resumeURL {}".format(url))
            output = '{}/{}'.format(tmpdirname, filename)
            s3.meta.client.download_file(
                os.environ['ATNP_STORAGE'], 'public/{}'.format(url),
                output)
            print("Downloaded")
        # Temporary file for writing zipped data
        temp_resumes = tempfile.TemporaryFile()
        filename = _random_filename()
        zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
        _zipdir(tmpdirname, zipf)
        zipf.close()
        s3.meta.client.upload_file(
            filename, os.environ['ATNP_STORAGE'], 'misc/{}'.format(filename))
        url = s3.meta.client.generate_presigned_url('get_object', Params={'Bucket': os.environ['ATNP_STORAGE'],
                                                                          'Key': 'misc/{}'.format(filename)})
        return url
