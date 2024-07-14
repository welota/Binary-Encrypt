# How does this work?

## Understaning what does "**not**" mean.
Not is an logic operator normally used for negating an object, for example, imagine we have a class, we can check if it **does not** exist, by using: `if not class:`.

Well, that is in the case that if we are checking an object, but, if it is a logical operator like true or false? well, thats easy! there is rule name "*Rule of negating*", and
"*Rule of double negating*", basically the rule of negating is inverting a true value, or a 1, so, `not True` returns false, because the opposite of true is false, so the opposite of 1 is 0
(*in binary*); and the "Rule of double negating" its basically negate a negation, so, `not false` returns true, because the same as up there.

Didn't understand? I have a gramatically example so you can understand.
Imagine you say a friend "I want to program", negating it would be like "I don't want to program", thats equal to `not True`, for double negating is like: "Its a lie that i dont want to program".
So it means that you want to program, thats equal to `not False`. By the way, you can triple negate, or more! for example: "Don't believe that is a lie that i dont want to program", that means that
you want to program.

Anyway, for an easy comprehension, if a negation is even, it is false, if it's odd, its true.

## Understaning how the *binary encryptor* works.
Its easy! it just extracts the binary part of the text, then it negates all binary code and then, it converts to UniCode again.

- To obtain the binary part in a text, you transform firstly, the text to ascii, and then that ascii convert to binary, not difficult.
- To obtain the text part of a binary, you transform that binary into ascii, then use a function to read that ascii to make it UniCode.

### fun fact:
Every binary use the method up there to translate text to binary and viceversa.

I hope you like this and understood my explanation, i put some effort in this.
