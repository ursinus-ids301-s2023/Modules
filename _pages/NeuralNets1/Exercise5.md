---
layout: exercise_pyodide
permalink: "NeuralNets1/Exercise5"
title: "IDS 301: Neural Nets 1: Dataset Indexing"
excerpt: "IDS 301: Neural Nets 1: Dataset Indexing"
canvasasmtid: "174478"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video4"
  next: "./Video5"
  points: 1.5
  instructions: "<p>Overload the <code>__len__</code> and <code>__getitem__</code> operators in the <code>Squares</code> class below so that the length is <code>self.N</code> and the item at index <code>i</code> is the ith perfect square.  So, when indexing an object of this type, you should see the sequence 1, 4, 9, 16, 25, ...</p>"
  packages: "numpy"
  goals:
    - To overload the __len__ and __getitem__ operators in python classes
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    
  correctcheck: |
    pyodide.globals.out == ".1.4.9.16.25.36.49.64.81.100."
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.out == "."
      feedback: "Try again.  It looks like you might not be returning the correct length.  Try returning <code>self.N</code>" 
    - incorrectcheck: |
        pyodide.globals.out == ".0.1.4.9.16.25.36.49.64.81." 
      feedback: "Try again.  You're very close!  Just be sure that the element at index 0 is 1, not 0." 

files:

  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 400
    code: | 
        import numpy as np

        class Squares:
            def __init__(self, N):
                self.N = N
            
            def __getitem__(self, idx):
                ret = 0
                ## TODO: Fill this in
                return ret
                
            def __len__(self):
                return 0 ## TODO: This is a dummy value



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        N = 10
        s = Squares(10)
        out = "."
        for i in range(len(s)):
            out = out + "{}.".format(s[i])

        
        
---
