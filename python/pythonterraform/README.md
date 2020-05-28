### What is Python Terraform?
Python terraform is a python library that is essentially a wrapper for terraform.
It allows you to integrate terraform and python together to be able to create easier
scripts for automation with terraform.

If you are heavy in use on Python at your place of work, or your project, it's a fantastic solution.

### Using Python-Terraform with no args, no vars

We will use the example of pyter-bas.py for our basic example.
In this example we will use python terraform to simply do a terraform plan and apply.

### Using Python-Terraform with args/workspaces

We will use the example of pyter-arg.py for our args example.
This will allow us to do things such as specify a workspace.
If you're trying to execute different environments (say from dev to prod)
this allows us to call in arguments for that, so we can either set that workspace
or perhaps we can even do something like only do a terraform plan and give us the output.

### Using Python-Terraform with vars and a vars file

In this example, on pyter-w-vars.py we will include how to load variables to overwrite existing vars.
This is useful in the case where perhaps you want devs to edit or change vars in a project, or perhaps
limit vars that can be changed in a project, without having to edit the terraform itself.

For example, if a variable named "bobsec2name" had a default value of "bob" we could pass it a
vars file that we pull in and perhaps name it "robert" instead, now the ec2 name is "robert" instead of "bob".

### Example usage of each:

In executing pyter-bas.py
* python3 pyter-bas.py

In executing pyter-arg.py
* python3 pyter-arg.py --tfstate apply
* python3 pyter-arg.py --tfstate destroy

In executing pyter-w-vars.py
* python3 pyter-w-vars.py --tfstate apply
* python3 pyter-w-vars.py --tfstate destroy

(ensuring that the vars being passed are renamed under pyvars.py as they will overwrite any vars set in vars.tf)