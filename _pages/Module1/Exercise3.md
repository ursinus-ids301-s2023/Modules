---
layout: exercise_python
permalink: "Module1/Exercise3"
title: "IDS 301: Module 1: For Loops"
excerpt: "IDS 301: Module 1: For Loops"
canvasasmtid: "171117"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video3"
  next: "./Video4"
  points: 1.5
  instructions: "<p>Fill in a method to compute the first <b>N</b> terms of the harmonic series 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/N.  For example, if N = 4, then the sum is 1 + 1/2 + 1/3 + 1/4</p>"
  goals:
    - To write methods in python
    - Write for loops in python with accumulators
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("1.000_1.500_1.833_2.083_2.283_2.450_2.593_2.718_2.829_")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("0.000_0.000_0.000_0.000_0.000_0.000_0.000_0.000_0.000_")
      feedback: "Try again.  It looks like you're not adding anything to result in the loop." 
 
files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
        def get_harmonic_series(N):
          """
          Compute the harmonic series sum 1 + 1/2 + ... + 1/N

          If N = 1, the result should be 1
          If N = 2, the result should be 1 + 1/2
          If N = 3, the result should be 1 + 1/3 + 1/3
          etc

          Parameters
          ----------
          N: int
            Last term in harmonic series
          """
          result = 0
          ## TODO: Fill this in
          return result


  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        for N in range(1, 10):
          print("{:.3f}".format(get_harmonic_series(N)), end="_")

---
