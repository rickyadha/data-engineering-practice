import requests
import os

path ='/home/syncopy/funlab/de/py/prct01/de-prct/Exercises/Exercise-01/download'

check_path = os.path.exists(path)

if check_path==True:
    pass
else:
    os.makedirs(path,exist_ok=False)

# download_uris = [
#     'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
#     'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
#     'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
#     'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
#     'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
#     'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
#     'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
# ]


# def main():
#     # your code here
#     pass


# if __name__ == '__main__':
#     main()
