resource "aws_iam_policy" "policynamehere" {
  name        = var.awspolicyname
  path        = "/"
  description = "Description of your policy goes here"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:Describe*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}