variable "ec2name" {
    description = "this will tag and give the name of the ec2 here"
    default = "EC2NameHere"
}

variable "ec2type" {
    description = "machine type that will be used.  for instance t2.micro"
    default = "t2.micro"
}

variable "ec2subnet" {
    description = "the subnet that will be used from your desired vpc to create this ec2"
    default = "subnet-123456"
}

variable "ec2service" {
    description = "the service this ec2 is being used for"
    default = "servicenamehere"
}

variable "ec2department" {
    description = "the department this ec2 belongs to"
    default = "departmentnamehere"
}

variable "ec2ami" {
    description = "the ami value that will be used, for instance ami-07ba77e2ad0ff38b8"
    default = "ami-07ba77e2ad0ff38b8"
}