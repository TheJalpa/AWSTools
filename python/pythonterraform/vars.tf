variable "awspolicyname" {
    description = "name of the policy you are creating.  this should be well named."
    default = "awspolicynamehere"
}

variable "ec2subnet" {
    default = "subnet-12345678"
    }

variable "ec2service" {
    default = "servicenamehere"
}

variable "ec2department" {
    default = "departmenthere"
}

variable "ec2name" {
    default = "ec2testname"
}

variable "ec2type" {
    default = "t2.micro"
}

variable "ec2ami" {
    default = "ami-07ba77e2ad0ff38b8"
}