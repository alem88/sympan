from sympan.handlers import S3Handler

from credentials import (AWS_ACCESS_KEY_ID,
                         AWS_SECRET_ACCESS_KEY,
                         REGION_NAME)

from config import (
    S3_URL,
    DESTINATION_FOLDER_PATH
)

if __name__ == '__main__':
    s3 = S3Handler(aws_access_key_id=AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                   region_name=REGION_NAME)

    s3.download_locally(s3_url= S3_URL,
                        destination_folder=DESTINATION_FOLDER_PATH,
                        n_jobs=2)
