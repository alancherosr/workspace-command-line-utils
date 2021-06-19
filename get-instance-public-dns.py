#!/usr/bin/env python3
import boto3
import json
import sys
import argparse

def main(argv):

  parser = argparse.ArgumentParser(description='Get public dns for given instance')
  parser.add_argument('--instance-id', action="store", dest="instance_id", help="EC2 instance id")
  parser.add_argument('--profile', action="store", dest="profile", 
      help="local aws profile stored in ~/.aws/config file", default="default")

  arguments = parser.parse_args()

  if arguments.instance_id == None:
    parser.error('--instance-id argument is required')

  # Set configuration for this script
  profile = arguments.profile 
  instance_id = arguments.instance_id

  # Set custom profile to use in this script
  boto3.setup_default_session(profile_name=profile)

  ec2 = boto3.client('ec2')

  response = ec2.describe_instances(
      InstanceIds=[
          instance_id,
      ],
  )

  print(response['Reservations'][0]['Instances'][0]['PublicDnsName'])

# Call main function
if __name__ == '__main__':
  main(sys.argv[1:])

