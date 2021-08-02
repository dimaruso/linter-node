# it-val-linter    
Code Quality Checker Application  
Includes pep-8 compliance and type consistency tests. If the tests fail, displays comments on the improvement in the stdout.  

## Usage with a terminal
### install guide  
`pip install -r requrements.txt`  
### example usage:  
`pytest --dir="C:\other_dir\project_dir"`  

## Usage with a docker
### install guide  
`bash ./Scripts/setup.sh`
### uninstall guide  
`bash ./Scripts/uninstall.sh`  
### example usage:  
`bash ./Scripts/run.sh "C:\other_dir\project_dir"`  
```text
Note: On Windows, you may need to configure directory permissions in the docker desktop application to use volume.
```
