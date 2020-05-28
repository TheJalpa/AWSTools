from python_terraform import *

# In this case we are setting our current directory where the terraform lives to execute it.
# If you had a separate folder, you would need to point it there instead.  For instance
# if your directory was "tfplan" you would make your directory './tfplan'
tf = Terraform('./')

# Here we are going to do a very basic apply.
# This will simply include telling it to execute the terraform in this directory.
# We remove input so there's no prompt of "Are you sure you want to apply?"
# Lastly we are skipping input and the plan, this will just do a terraform apply.
try:
    print ('Executing Terraform Plan')
    return_code, stdout, stderr = tf.apply(input=False, skip_plan=True, capture_output=False)
    print ('Terraform Successful!')
except:
    # If for some reason we don't successfully execute terraform we'll return an exit 1.
    print ('Was unable to apply your terraform plan')
    exit(1)