Behave
--
Assignment for submitting Behave scripts in SE 3150.

*Contents* - there are two projects:

**isitchristmas**

**peppers-ghost**

isitchristmas demonstrates how to use built in steps. It has a default environment.py and a steps file that contains the required inclusion to use the built in steps.

peppers-ghost uses both built in steps AND custom steps.

Note that the file structure and positions of the files is very important. These files are organized correctly in the following tree structure:

```text
.
├── isitchristmas
│   └── features
│       ├── environment.py
│       ├── is_it_christmas.feature
│       └── steps
│           └── builtin_steps.py
└── peppers-ghost
    └── features
        ├── environment.py
        ├── peppers-ghost.feature
        └── steps
            └── peppers-steps.py
```

Activate conda env **conda activate behave-env
To run the scripts, cd into the project directory and type **python -m behave**
