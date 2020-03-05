# Notes for Preparation

## Practical Coding

Almost the entirety of this part of the course is designed to get the students
writing code, interacting with their own code, and asking questions. The goal is
to *engage the students* and then answer questions as they come up.

To that end, there isn't a lot of explicit theory (there's a lot of implied
theory). It's very hands-on and it's very mechanical. The teacher needs to be
familiar with the theory, and there will be plenty of opportunity to talk about
pieces of theory when they come up, but the emphasis should be on *doing.*

## Three Metrics

One thing to note here is that we alternate between three things here: adding
*features* to the game (new actions), making the game more usable (improving the
command line experience), and making the *code* more usable (with classes,
functions, and layout).

Different students will be more attracted to each of those, and that's okay! But
all three are important, and you should be ready to explain why it's important
to have readable code, a usable interface, *and* a lot of fun stuff for the
player to do.

## Testing

Also, at each step, reinforce that the student should *test* their code! Make
sure they run through each of the things they've added, and try to get them to
think about what other actions it may affect and test that as well.

We'll get to automated testing later, but the idea of always testing should be
ingrained.

# Version One

See `_01.py` for an example.

Version one should be a super simple script. It should have a `__main__` clause
and `main()` function, it should provide a command line, and it should accept
two kinds of commands: "quit" which ends the script, and anything else, which it
simply prints out.

This is the `hello world` of interactive scripts!

I recommend writing it out on the whiteboard and having the students copy it,
then going through it line by line and explaining each point (how the shebang
works, order of operations, etc.).

# Version Two

See `_02.py` for an example.

We're going to add some error handling. First, have the students `<ctrl>-D` and
`<ctrl>-C` and see what happens to Version One. Then explain that these are
exceptions, and that we're going to add some code to handle those exceptions
more gracefully!

The new version wraps the request code in a `try..except` block.

I recommend handling one change at a time on the whiteboard, letting the
students try to modify the correct place, and then helping them if needed.

As two optional changes you can make at this point, to help reinforce functions,
you can have them break out the task management as its own function; and the
"goodbye" action as its own function.

# Version Three

See `_03.py` for an example.

We going to do a few things in this version, to produce something that feels a
bit more like a real game. First, break out the task functionality into its own
function, if you have not already done so.

Then add a global variable, `LOCATION`. We're going to let the player travel
between locations!

Now build an `if..elif` block for various locations. Students should add one
location at a time (I recommend a 'tower', 'village', and 'forest'), allowing
each one to change the `LOCATION` and print out a useful message.

Now build a 'help' task, and add an `else` that gives a useful error message.

Let the students know that global variables are rarely a good idea in the
longterm, and that we'll eventually be deleting these -- but as a shortcut,
they're a good way to only have to learn one thing at a time.

# Version Four

See `_04.py` for an example.

Now we're going to make things more complicated!

Add a global `SKILL` for your wizard, and a task to 'study' while in the tower.
Studying should only be possible in the tower, and it should increase `SKILL`.

Remember to update the help action.

Some students may begin to get creative at this point: one of my students provided
an informative error message if studying happened anywhere but the tower;
another declared that there were limits to skill and set an upper cap (and gave
an error message when trying to study past that cap); and another change 'skill'
to 'cleanliness' and had the action be to 'tidy' the tower. Let them! They need
to make the game their own, and these impulses are an excellent first start.

# Version Five

See `_05.py` for an example.

Even more complications!

* Add a global `GOLD` and `LIBRARY`.
* Change the `study` action to require a sufficient `LIBRARY`. 
* Add a `shop` action in the village to improve the `LIBRARY`, but it requires
  `GOLD`.
* And add a `work` action in the village to increase `GOLD`, but it requires
  `SKILL` to make much money.

Don't forget to update the help action!

Again, students will start adding their own flourishes, and encourage that.

# Version Six

See `_06.py` for an example.

Discuss modules at a high level: what they are and why python uses them.

Discuss the `readline` module, and then add it to the script. The teacher should
be sufficiently familiar with `readline` to handle questions, but the basic
documentation for the python3 standard library is probably sufficient.

The goal here is to have tab-completion and up-arrow history work!

# Version Seven

See `_07.py` for an example.

Now we're going to build the beginnings of a class. Because so much centers
around our wizard, we'll make a Wizard class.

To start with, this will just be a data class, storing state. We'll make the
class hold the state of each global variable, then replace each place it calls
the global, and then delete the global.

Make an empty class, and use it to create a wizard object in `main()`. Pass the
wizard object into your task function. Then, for each global variable in turn:

* Add a class attribute that matches the global variable. For example,
  `LOCATION` becomes `self.location` within the `Wizard()` class.
* In the task function, replace each usage of the global variable with the
  object attribute. So everywhere the code uses `LOCATION`, use `wiz.location`
  instead.
* Once it has been replaced everywhere, delete the declarations of the global
  variable.

Once you have all of the globals moved into object attributes, explain that this
is a data class (it only holds data) and explain that we're now going to make it
a full-blown class by adding a useful method.

Add a `wiz.status()` method, which prints out a useful message about the
wizard's current state. And then add an action the wizard can take which uses
the status method.

# Version Eight

See `_08.py` for an example.

This will be a continuation of Version Seven, above. There are multiple ways to
do this, but the end effect should be to move each individual task into the
Wizard class, and simplify the task function.

Once all of the tasks are in the object, this is an excellent time to start
*adding* new kinds of actions. These new actions should be written entirely by
the students, rather than copied from the whiteboard. You can help with syntax,
and you can offer gentle guidance on ways to achieve things in the abstract, but
the students should create 3-6 different actions entirely on their own.

Not all students will have a clear idea of what kinds of actions they *want* to
create, and you can spur their creativity with a few examples:

* The wizard can `gather` ingredients in the forest, `brew` them into potions in
  the tower, and `sell` them in the village. This will require some new state to
  be tracked, such as total ingredients and total potions available.
* Maybe every action so far (`study`, `work`, and even `shop`) increase the
  wizard's stress! When stress reaches a certain level, the wizard can no longer
  perform any of those actions anymore. Stress can be reduced by `relax` in the
  forest.
* There may be a new location, the carnival, which the wizard can travel to.
  While there, the wizard can `show off`... but that requires a different kind
  of skill than village work, and the wizard must `practice` to improve it.

# Version Nine

See `_09.py` for an example.

Create a save file, and make sure the game can save and load from previous
gameplay. At this point, it's basically a real game.

We do this first version of saving the "low level" and manual way, to ensure we
understand the basics.

# Version Ten

See `_10.py` for an example.

Make the save file process use the builtin module configparser. We do it this
way because we don't want to manage the low level and manual way from now on.

# Version Eleven

See `_11.py` and `test_wizard.py` for an example.

Make the game more testable, and then write a little bit of testing!
