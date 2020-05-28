# AWSTools
Miscellaneous AWS Tools that can be used for various use cases

### Categories
- Python
- Terraform

### Python Tools
- EC2 Handler: This tool is used to audit new ec2 instances launched, and will use a lambda to discern if security group rules meet guidelines.  The Lambda will turn an instance off to protect a machine from being thrown into public realms that aren't desirable.  Example: Someone makes an ec2 with ssh open to the world.  The lambda will be invoked by a cloudwatch rule, describe the instance, look at the volume id, compare time stamps, and if a new machine is seen then it will check security group.  If rule == Desired ruleset, turn off machine, else leave it alone.
- pythonterraform: This is an example usage setup for utilizing python-terraform, the library that acts as a wrapper for terraform.  It's very powerful and easy to use.  In this case we will be using it as an example to execute it in 3 ways.  #1 is without vars or arguments, just execute a plan.  #2 is to use and pass arguments.  Lastly is to utilize vars by importing vars from a python file we define.  Let's say you have a vars file that is some 1500 lines long, devops sets it up, and a dev only needs to change 3.  You can then pass those 3 into the pyvars file, specify them, pass them into python-terraform and overwrite them as it executes, making it simple to change them.  On top of this it is very powerful for creating CI/CD tools.

### Terraform
- ec2creation: This is a very quick and easy terraform plan that's been var'd out for you.  Fill out the vars, execute terraform, and spin up an EC2.