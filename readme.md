# UD LUG Hacktoberfest 2018

[![Build Status](https://travis-ci.org/crclark96/lug_hacktoberfest18.svg?branch=master)](https://travis-ci.org/crclark96/lug_hacktoberfest18)

## How to contribute

This repository has two important files that should be changed in order to
complete the roll-call. `contributors.md` and `contributors.json` list all
of the people attending our event.

The reason we have two files is to force contributors to use an actual coding
environment, instead of the web editor built into github.

First thing to do is click the big old fork button in the top right of the
repository page. Then clone the repository to your local machine:

```
git clone https://github.com/your-username/lug_hacktoberfest18.git
```

Create a branch:

```
git checkout -b branch-name
```

Branches are easy ways to have multiple versions of working code, or to have
multiple people work on the same code without stepping on each other's toes.
Once your branch looks complete, you can `merge` a branch into another branch
to absorb all of the work.

But before we can do that we have to make actual changes. Edit the two files
and then add them to the staging area like so:

```
git add contributors.md contributors.json
```

The staging area is a place to put code we want to review before adding it to
the project. Think of it as an intermediary between unfinished and finished
code.

Next we'll commit the code, which turns it into "permanent" code. This is code
that we're fairly confident about and want to keep. Make sure you include a
commit message that tells other people what this change does.

```
git commit -m "Commit message"
```

Finally, we'll push the code to our github repository. This just updates the
commit history on github.com to match the commit history on our computer.

```
git push -u origin branch-name
```

The `-u` flag tells git which branch on github corresponds to this branch on
our machine. In the future we can just use `git push` to have the same effect.

Now the code is up online, and we can send a request to the owner of this
repository to merge our code into the official project. This is the most
important part. Click ```New Pull Request``` on the repository webpage and
write a little description about why this change should be accepted.

You can check on the status of your pull request and see if the original author
has made any comments or wants any changes. I've set up a fun little script
that validates the contents of the two files match each other. Often times
open source projects will have similar scripts to run tests and make sure no
new changes break any existing functionality. Your pull request will display
the status of the test, so make sure you run the tests locally to avoid
contributing any broken code.

Congrats on submitting your a pull request! Now check out some cool open source
projects and contribute real code to help real people.