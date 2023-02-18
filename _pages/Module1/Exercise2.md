---
layout: exercise_python
permalink: "Module1/Exercise2"
title: "IDS 301: Module 1: Python Compound If Statements"
excerpt: "IDS 301: Module 1: Python Compound If Statements"
canvasasmtid: "171116"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  next: "./Video3"
  points: 1.5
  instructions: "<p>Fill in the method to determine whether someone needs assistance at an event.  Someone needs assistance if at least one of these things is true: their age is > 70, or they are sick.</p>"
  goals:
    - To write methods in python
    - To write if statements with compound boolean statements in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("False.True.True.True.False.True.")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("False.False.False.False.False.False.")
      feedback: "Try again.  It looks like you're not checking to see if age is > 7 <code>or</code> if <code>is_sick == True</code>." 
 
files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
        def needs_assistance(age, is_sick):
          """
          Determine if someone needs assistance

          Parameters
          ----------
          age: int
            Age in years
          is_sick: boolean
            True if sick, False if not sick
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
        print(needs_assistance(50, False), end=".")
        print(needs_assistance(71, False), end=".")
        print(needs_assistance(20, True), end=".")
        print(needs_assistance(80, True), end=".")
        print(needs_assistance(10, False), end=".")
        print(needs_assistance(100, False), end=".")

---
