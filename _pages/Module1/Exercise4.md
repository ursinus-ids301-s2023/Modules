---
layout: exercise_python
permalink: "Module1/Exercise4"
title: "IDS 301: Module 1: For Loops And Arrays"
excerpt: "IDS 301: Module 1: For Loops Arrays"
canvasasmtid: "171118"
canvaspoints: "1"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video4"
  points: 1.5
  instructions: "<p>Fill in the method <code>get_min_element</code> that returns the smallest element in an array.  We can start off assuming the minimum element is the first element in the array, and then we loop through all of them and check to see if any of them are smaller.  (NOTE: We're assuming here that the array has at least one element).</p>"
  goals:
    - To write methods in python
    - Write for loops in python that work with arrays
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("0.3.8.14.1.")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("64.79.23.34.80.")
      feedback: "Try again.  It looks like you're always returning the first element of the array.  Be sure to check all elements.  You will have to use an if statement in the loop to check if each element you see is less than the smallest element you've seen so far." 
 
files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
        def get_minimum_element(arr):
          assert(len(arr) > 0) # Assume the array has at least one element
          res = arr[0] # Assume the smallest element is the first element until proven otherwise
          ## TODO: Fill this in
          return res


  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        print(get_minimum_element([64,  0, 93, 84, 90, 80, 38, 81, 43, 87]), end=".")
        print(get_minimum_element([79, 46,  3, 14, 10, 94,  4, 89, 26, 86]), end=".")
        print(get_minimum_element([23, 59, 49, 27, 84, 29,  8,  8, 43, 10]), end=".")
        print(get_minimum_element([34, 63, 74, 93, 75, 30, 14, 68, 65, 89]), end=".")
        print(get_minimum_element([80, 15, 66, 80, 13,  1, 30, 46, 52, 72]), end=".")

---
