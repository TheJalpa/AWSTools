from python_terraform import *
import argparse

# We are going to setup an argument on whether we want to apply terraform, or destroy it
# You can use this for various types of argument applications from passing variables
# To telling terraform how to handle workspaces, or whatever works for your use case.
parser = argparse.ArgumentParser()
parser.add_argument("--tfstate", required=True, type=str)
args = parser.parse_args()
state = args.tfstate

# In this case we are setting our current directory where the terraform lives to execute it.
# If you had a separate folder, you would need to point it there instead.  For instance
# if your directory was "tfplan" you would make your directory './tfplan'
tf = Terraform('./')

if state == 'apply':
# Here we are going to do a very basic apply.
# This will simply include telling it to execute the terraform in this directory.
# We remove input so there's no prompt of "Are you sure you want to apply?"
# Lastly we are skipping input and the plan, this will just do a terraform apply.
    try:
        print ('Executing Terraform Plan')
        return_code, stdout, stderr = tf.apply(input=False, skip_plan=True, capture_output=False)
        print ('Terraform Successful!')
        exit(0)
    except:
        # If for some reason we don't successfully execute terraform we'll return an exit 1.
        print ('Was unable to apply your terraform plan')
        exit(1)
elif state == 'destroy':
    try:
        print ('Destroying Terraform objects')
        return_code, stdout, stderr = tf.destroy(input=False, capture_output=False)
        print ('Terraform Destroy Successful!')
        exit(0)
    except:
        # If for some reason we don't successfully execute terraform we'll return an exit 1.
        print ('Was unable to destroy terraform resources')
        exit(1)
else:
    print ('No valid arguments were found, exiting')
    exit(1)