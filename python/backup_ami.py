import sys
import boto3
import datetime
import yaml

def backup_ec2():
    self.name = sys.argv[0]
    self.id = sys.argv[1]
    self.region = sys.argv[2]
    
    connect_to_aws()
    self.ec2_client = boto3.client('ec2', region_name=this.region)
    create_image()

def connect_to_aws(self):
  #with open /provenir/.passcode file:
    grab key
    grab secret
  #close file
  #connect to aws
  
def create_image(self):
  now = datetime.datetime.now()
  description = "Jenkins2 instance backup occurred " + now.strftime("%Y-%m-%d")
  self.ec2_client.create_image(Name=self.name,\
                              InstanceId=self.id,\
                              Description=description,\
                              NoReboot=True)

if __name__ == "__main__":
  backup_ec2()
