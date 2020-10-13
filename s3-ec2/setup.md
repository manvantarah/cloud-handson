# Creating Bucket to upload and download it from ec2 instance(Ubuntu)
##  Configure IAM roles for EC2 instance before, in 'config group' before creating instance!
##  Install pip
  $ sudo apt install python-pip
##  Install boto3 package
  $ brew install boto3
##  Create Bucket from ec2 by using terminal terminal
  $ sudo aws s3://Bucket-Name
##  view the created Buckets from terminal 
  $ sudo aws s3 ls

