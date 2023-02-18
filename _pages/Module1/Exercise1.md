---
layout: exercise_python
permalink: "Module1/Exercise1"
title: "IDS 301: Module 1: Python If Statements"
excerpt: "IDS 301: Module 1: Python If Statements"
canvasasmtid: "171115"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 1.5
  instructions: "<p>Fill in the method to determine whether a number ends in a 0 when expressed in our ordinary number system.  For example, 1200 ends in a 0, but 101 does not.</p>"
  goals:
    - To write methods in python
    - To write basic if statements in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("True.False.True.True.False.")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("False.False.False.False.False.")
      feedback: "Try again.  It looks like you're not checking to see if the number is divisible by 10.  Try using the <code>%</code> operator!" 
 
files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
        def ends_in_zeros(x):
          """
          Determine whether a number ends in 0

          Parameters
          ----------
          x: int
            A Number
          
          Returns
          -------
          True if x ends in a 0, False otherwise
          """
          result = False
          ## TODO: Fill this in
          return result


  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        print(ends_in_zeros(10), end=".")
        print(ends_in_zeros(101), end=".")
        print(ends_in_zeros(15000), end=".")
        print(ends_in_zeros(1200), end=".")
        print(ends_in_zeros(33), end=".")

---
