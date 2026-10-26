#set text(font: ("Noto Sans", "Liberation Sans", "DejaVu Sans"))
#set heading(numbering: "1.")
#show link: underline

= A good use of AI... Custom Lessons!

AI's are getting good enough that they can make bespoke courses for learning new skills. This is an example of that use.

To do this, you'll need an AI that has access to your computer (i.e. not just using the chat interface in a web browser). It will need to read and modify files on your computer.

Some examples of this are:

- Claude (from Anthropic)
- ChatGPT with the Code Interpreter plugin (from OpenAI)

Most of these require paid subscriptions.

Most also have VS Code plugins, so you can do everything from there.

== Setting up a course

To make an effective course, you need to be very specific about what you want to learn, and how you want to learn it. You should also be clear about your current skill level, and what you want to achieve.

This is an example of a course specification that I gave to Claude Opus 5.5 in 'plan' mode:

```
I want to learn python for scientific computing, particularly data processing, visualisation and analysis. I have some basic python experience, but need things explaining clearly in plain english - I am not a computer scientist. I want you to make an interactive course for me, starting with the basics and building up to more complex exercises, motivated by real-world examples with Earth Sciences datasets. You should create a lesson to communicate the concepts, and then exercises for me to practice them. At the end of each lesson, you should check what I have done, and provide feedback. You should then ask what lesson I would like to do next, with two or three suggested options. My progress should be saved in local files, so that I can pick up where I left off. You should begin by asking basic questions about what skills I would like to learn, and use my answers to shape the lesson plan.
```

From here, Claude asked a number of questions about topics and skills, and created a course outline for me to approve. It then created the first lesson, and I was able to work through it, with Claude providing feedback on my work.