provider "aws" {
  region = "us-west-2"
}

#you can change the name from "ec2_creation" to whatever
#is most applicable for you.
resource "aws_instance" "ec2_creation" {
  ami           = var.ec2ami
  instance_type = var.ec2type

  subnet_id = var.ec2subnet
  tags = {
    Name = var.ec2name
    service = var.ec2service
    department = var.ec2department
  }
}