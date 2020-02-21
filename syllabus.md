# Python 3.6+ Extra Derpy

## Schedule

### 00: Environment (1 hour)

Most of this will be at the command line. This is some short-term pain that will
lead to long-term "impress future employers." Expect to spend about an hour
working on this -- unfortunately, becoming a programmer often involves setting
up a code-friendly environment! Fortunately, I can at least save you the
research time to figure out what that even means.

* Install `Komodo Edit` or editor of choice (such as Visual Studio Code)
* Install `iTerm2` for terminal usage

  * Download the latest stable release from https://iterm2.com/downloads/
  * Unzip the file
  * Move `iTerm2.app` to your Applications folder

* Install `homebrew` for MacOS (`iTerm`)

  * Open iterm!
  * Run the homebrew install script

    $ curl --fail --silent --show-error \
      --location https://raw.githubusercontent.com/Homebrew/install/master/install \
      --output brewinstall.rb
    $ /usr/bin/ruby -e ./brewinstall.rb

* Install `python3.6+` with `brew` (`iTerm`)

    $ brew install python3

* Install `virtualenv` with `pip3` (`iTerm`)

    $ pip install --upgrade virtualenv

* Set up some `bash` shortcuts for `virtualenv` (`Komodo` in `~/.bash_profile`)

      venvmk() {  # creates a python3 .venv virtualenv
          [[ "${1:-}" =~ -{0,2}h(elp)? ]] \
            && echo "venvmk NAME_OF_VENV" \
            && exit 0
          mkdir -p "${HOME}/.venv/" >/dev/null 2>&1
          pushd "${HOME}/.venv/" >/dev/null 2>&1
              virtualenv --python python3 $@
          popd >/dev/null 2>&1
      }
      venvls() {  # lists all of your .venv virtualenvs
          ls -1 -p "${HOME}/.venv/" | grep '/$' | tr -d '/'
      }
      venv() {  # switches into a .venv virtualenv
          local -r name="${1:-}"
          [[ -z "$name" ]] \
            && echo "Must provide a virtualenv name" \
            && exit 1
          [[ -d "${HOME}/${name}" ]] \
            || echo "${name} is not available as a virtualenv." \
            && exit 1
          source "${HOME}/${name}/bin/activate"
      }
      venvrepair() {  # repairs a python3 .venv virtualenv
          local -r name="${1:-}"
          [[ -z "$name" ]] \
            && echo "Must provide a virtualenv name" \
            && exit 1
          [[ -d "${HOME}/${name}" ]] \
            || echo "${name} is not available as a virtualenv." \
            && exit 1
          pushd "${HOME}/.venv/" >/dev/null 2>&1
              find "${HOME}/.venv/${name}/" -type l -delete
              virtualenv --python python3 "$name"
          popd >/dev/null 2>&1
      }

  * And then reload the profile: (`iTerm`)

    $ source ~/.bash_profile

* Set up a `CS101` `virtualenv` for installed python modules (`iTerm`)

    $ venvmk CS101

* Set up a `CS101` `git` for code (`iTerm`)

    $ mkdir -p ~/git/CS101
    $ cd ~/git/CS101
    $ git init
    $ touch README.md
    $ git add .
    $ git commit -m "Initial commit."

* Set your text editor to default to `~/git/CS101` for now
* In your browser, make a Python bookmark folder and bookmark:

  * https://www.reddit.com/r/learnpython/
  * https://stackoverflow.com/questions/tagged/python-3.x
  * https://docs.python.org/3/

StackOverflow is a good place for curated, pre-existing questions. The
`learnpython` subreddit it a good place to just swing by and ask a beginner
question. And the official docs are a good place to look stuff up.

### 01: Interpretive Dance (½ hour or more)

We'll open the interpreter and do some basic things. This is just to introduce
you to this tool and play a little in a forgiving environment. In the future,
you can use the interpreter to reason about and test out small bits of Python
code before fitting them together.

    $ source ~/.venv/CS101/bin/activate
    (CS101) $ python
    Python 3.7.4 (default, Sep  7 2019, 18:31:37)
    [Clang 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> while True:
    ...     print("Annette, you rock!")
    ...
    Annette, you rock!
    Annette, you rock!
    Annette, you rock!
    Annette, you rock!
    ^C
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    KeyboardInterrupt

* `dir()`
* `help()`
* make a function with a docstring and call `help()`
* some basic math, printing, and method calls

### 02: A Basic Script Framework (½ hour or more)

We will put together a basic script framework you can use to write working
scripts at the command line. Copy and past the following, and then we will go
through each line and discuss what it does.

    #!/usr/bin/env python3

    def main():
        print("Annette, you rock!")

    if __name__ == '__main__':
        main()

Now save the file to `basic.py` and then run:

    $ chmod +x basic.py
    $ ./basic.py
    Annette, you rock!
    $ git add basic.py
    $ git commit --message "A script framework for future work."

Then add a few items:

* `import sys` and `sys.argv`

    import sys
    def main():
        for item in sys.argv:
            print(item)

* `input()` and `print()` with a `while` loop

    def main():
        while True:
            msg = input("What should I say? ")
            print(msg)

* `open("filename.txt")`

    import sys
    def main():
        filename = sys.argv[0]
        f = open(filename)
        for line in f:
            print(line)

* f-string

    import sys
    def main():
        total = 0
        for item in sys.argv:
            try:
                total = total + int(item)
            except:
                print(f"Oops! {item} is not a number!")
        print(f"The total of the integers is {total}.")

### 03: 

## Schedule

* Week 1: overview, introduction, creating a script
* Week 2: variables, input and output, data types, numbers, strings
* Week 3: making the program do some math for us, formatting, IF
* Week 4: booleans, loops, string operations
* Week 5: functions, parameters, return
* Week 6: variable scope, input validation
* Week 7: modules
* Week 8: files, lists, tuples
* Week 9: records, command line
* Week 10: creating modules, reusable code, exception handling
* Week 11: OOP, arcane python
