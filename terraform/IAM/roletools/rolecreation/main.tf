#This can easily be leveraged elsewhere in other terraform
#plans.  For instance if you needed to create something that needed to assume
#a role you could then reference aws_iam_role.rolenamehere.name or id 
#which would then specify and attach the role created here.

resource "aws_iam_role" "rolenamehere" {
  name = var.awsrolename

  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SomeSidCreationName",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:StopInstances",
                "ec2:DescribeSecurityGroups"
            ],
            "Resource": "*"
        }
    ]
}
EOF

  tags = {
    service = var.servicename
    department = var.departmentname
  }
}